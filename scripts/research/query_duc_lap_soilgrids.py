"""Audit a SoilGrids WCS access probe; NOT a farm soil survey or suitability model.

Native Windows, Python 3.12 + Pillow. Cached replay by default; --refresh downloads
small WCS subsets. No installation or credentials required in the bundled runtime.
"""
import argparse
import csv
import hashlib
import io
import json
import math
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import urlopen
import xml.etree.ElementTree as ET

from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
DEST = ROOT / "nasa-space-apps-2026/sources/data-audits/duc-lap-2026-11-12/soilgrids-context"
BBOX = [106.42, 10.89, 106.47, 10.94]
POINT = [106.44351, 10.91123]
PROPERTIES = {"phh2o": "pH_H2O", "sand": "percent_mass", "clay": "percent_mass"}
DEPTHS = ["0-5cm", "5-15cm"]
STATS = ["mean", "Q0.05", "Q0.95"]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def request_url(prop, request, extra=()):
    return "https://maps.isric.org/mapserv?" + urlencode([
        ("map", f"/map/{prop}.map"), ("SERVICE", "WCS"),
        ("VERSION", "2.0.1"), ("REQUEST", request), *extra,
    ])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--refresh", action="store_true")
    args = parser.parse_args()
    DEST.mkdir(parents=True, exist_ok=True)
    manifest_path = DEST / "retrieval.json"
    old = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else None
    records = []

    def obtain(name, url):
        path = DEST / name
        if args.refresh:
            with urlopen(url, timeout=40) as response:
                data = response.read()
                record = {"file": name, "request_url": url, "bytes": len(data),
                          "sha256": sha(data), "content_type": response.headers.get("Content-Type"),
                          "retrieved_at_utc": datetime.now(timezone.utc).isoformat()}
            path.write_bytes(data)
        else:
            if old is None or not path.exists():
                raise SystemExit("Cached input missing; download explicitly with --refresh")
            data = path.read_bytes()
            record = next(r for r in old["files"] if r["file"] == name)
            assert record["request_url"] == url and record["sha256"] == sha(data), name
        records.append(record)
        return data

    for prop in PROPERTIES:
        data = obtain(f"{prop}-capabilities.xml", request_url(prop, "GetCapabilities"))
        tree = ET.fromstring(data)
        identifiers = {el.text for el in tree.iter() if el.tag.endswith("}CoverageId")}
        assert all(f"{prop}_{depth}_{stat}" in identifiers for depth in DEPTHS for stat in STATS)
    description = obtain("phh2o-describe.xml", request_url("phh2o", "DescribeCoverage", [
        ("COVERAGEID", "phh2o_0-5cm_mean")]))
    tree = ET.fromstring(description)
    offsets = [el.text.strip() for el in tree.iter() if el.tag.endswith("}offsetVector")]
    assert "250.000000 0" in offsets and "0 -250.000000" in offsets

    rows = []
    geometries = []
    for prop, unit in PROPERTIES.items():
        for depth in DEPTHS:
            for stat in STATS:
                coverage = f"{prop}_{depth}_{stat}"
                url = request_url(prop, "GetCoverage", [
                    ("COVERAGEID", coverage), ("FORMAT", "image/tiff"),
                    ("SUBSET", f"X({BBOX[0]},{BBOX[2]})"),
                    ("SUBSET", f"Y({BBOX[1]},{BBOX[3]})"),
                    ("SUBSETTINGCRS", "http://www.opengis.net/def/crs/EPSG/0/4326"),
                    ("OUTPUTCRS", "http://www.opengis.net/def/crs/EPSG/0/4326"),
                ])
                data = obtain(coverage + ".tif", url)
                assert data[:4] in (b"II*\x00", b"MM\x00*"), coverage
                im = Image.open(io.BytesIO(data))
                assert im.mode in ("I", "I;16", "I;16S")
                scale, tie, keys = im.tag_v2[33550], im.tag_v2[33922], im.tag_v2[34735]
                geo_keys = {keys[i]: keys[i + 3] for i in range(4, len(keys), 4)}
                assert geo_keys[2048] == 4326 and geo_keys[1025] == 1
                assert all(abs(a - b) < 1e-8 for a, b in zip(tie[:3], (0, 0, 0)))
                assert scale[0] > 0 and scale[1] > 0
                extent = [tie[3], tie[4] - scale[1] * im.height,
                          tie[3] + scale[0] * im.width, tie[4]]
                assert all(abs(a - b) < 1e-8 for a, b in zip(extent, BBOX))
                geometry = {"width": im.width, "height": im.height, "pixel_scale_deg": list(scale[:2]),
                            "upper_left_lon_lat": list(tie[3:5]), "crs": "EPSG:4326"}
                geometries.append(geometry)
                col = math.floor((POINT[0] - tie[3]) / scale[0])
                row = math.floor((tie[4] - POINT[1]) / scale[1])
                raw = im.getpixel((col, row))
                # WCS does not identify all nil values; zero cannot mean pH=0 here.
                valid = (0 < raw <= (140 if prop == "phh2o" else 1000))
                rows.append({"property": prop, "depth": depth, "statistic": stat,
                             "reference_col": col, "reference_row": row, "raw_value": raw,
                             "converted_value": raw / 10 if valid else None, "unit": unit,
                             "status": "model_proxy_not_field_measurement" if valid else "unknown_nonpositive_or_out_of_range",
                             "zero_cells_excluded_from_interpretation": list(im.get_flattened_data()).count(0)})
                print(coverage, raw, flush=True)
    assert all(g == geometries[0] for g in geometries)
    for prop in PROPERTIES:
        for depth in DEPTHS:
            group = {r["statistic"]: r["converted_value"] for r in rows if r["property"] == prop and r["depth"] == depth}
            assert all(v is not None for v in group.values())
            assert group["Q0.05"] <= group["Q0.95"]
    with (DEST / "reference-values.csv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    write_json(DEST / "summary.json", {
        "artifact_kind": "modelled_soil_access_probe_not_parcel_or_hamlet_assessment",
        "script_sha256": sha(Path(__file__).read_bytes()),
        "status": "warn_spatial_transfer_not_validated", "provider": "ISRIC SoilGrids WCS",
        "license": "CC-BY-4.0", "native_grid": {"crs": "EPSG:152160", "resolution_m": 250},
        "requested_envelope_lon_lat": BBOX, "envelope_role": "analyst_selected_access_probe_not_farm_or_commune_boundary",
        "reference_point_lon_lat": POINT, "point_role": "GeoNames_historical_place_not_farm",
        "returned_grid": geometries[0], "reprojection_resampling_algorithm": "not_explicitly_set_or_verified",
        "unit_authority": "ISRIC layers documentation; WCS generic uom W.m-2.Sr-1 is not soil units",
        "conversion": "all three requested properties divide raw integer by 10",
        "uncertainty": "Q0.05/Q0.95 are model prediction bounds, not measured minima/maxima or local confidence validation",
        "zero_policy": "no valid pH/texture interpretation of zero; zero cells excluded, no regional aggregate computed",
        "rows": rows, "farm_eligibility_or_ranking_allowed": False,
        "limitations": ["No current cropland mask or verified parcel/AOI intersection", "No salinity, drainage, irrigation or root-zone profile",
                        "No local soil samples or calibration", "Depths stop at 15cm; cannot infer full root-zone water storage"],
    })
    if args.refresh:
        write_json(manifest_path, {"schema_version": 1, "files": records})
    print("Saved soil context probe: 18 coverages; farm ranking remains disallowed")


if __name__ == "__main__":
    main()
