"""Small public-data snapshots for the fixed My Thanh AOI. Cached by default.

Windows Python 3.12, Pillow. --refresh explicitly fetches POWER and small WCS
subsets; imagery was acquired separately via documented export/render URLs.
"""
import argparse
import csv
import datetime as dt
import hashlib
import io
import json
import math
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import urlopen

from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "nasa-space-apps-2026/sources/data-audits/my-thanh-cai-lay-2026-11-12"
POINT = [106.02154675, 10.4770865]
BBOX = [106.017, 10.461833333333331, 106.039, 10.480166666666669]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def write(path, doc):
    path.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--refresh", action="store_true")
    args = ap.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    soil_dir = OUT / "soilgrids"
    soil_dir.mkdir(exist_ok=True)
    jobs = [(OUT / "power_daily_2015_2025.json",
             "https://power.larc.nasa.gov/api/temporal/daily/point?" + urlencode({
                 "parameters": "T2M,T2M_MAX,T2M_MIN,PRECTOTCORR", "community": "AG",
                 "longitude": POINT[0], "latitude": POINT[1], "start": "20150101", "end": "20251231",
                 "format": "JSON", "time-standard": "UTC"}))]
    specs = []
    for prop, depths in [("phh2o", ["0-5cm", "5-15cm", "15-30cm"]), ("sand", ["0-5cm"]), ("clay", ["0-5cm"])]:
        for depth in depths:
            for stat in ["mean", "Q0.05", "Q0.95"]:
                cid = f"{prop}_{depth}_{stat}"
                url = "https://maps.isric.org/mapserv?" + urlencode([
                    ("map", f"/map/{prop}.map"), ("SERVICE", "WCS"), ("VERSION", "2.0.1"),
                    ("REQUEST", "GetCoverage"), ("COVERAGEID", cid), ("FORMAT", "image/tiff"),
                    ("SUBSET", f"X({BBOX[0]},{BBOX[2]})"), ("SUBSET", f"Y({BBOX[1]},{BBOX[3]})"),
                    ("SUBSETTINGCRS", "http://www.opengis.net/def/crs/EPSG/0/4326"),
                    ("OUTPUTCRS", "http://www.opengis.net/def/crs/EPSG/0/4326"),
                ])
                jobs.append((soil_dir / (cid + ".tif"), url))
                specs.append((prop, depth, stat, soil_dir / (cid + ".tif")))
    records_path = OUT / "retrieval.json"
    if args.refresh:
        def fetch(job):
            path, url = job
            with urlopen(url, timeout=45) as response:
                data = response.read()
                record = {"file": path.relative_to(OUT).as_posix(), "url": url,
                          "retrieved_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
                          "http_status": response.status, "content_type": response.headers.get("Content-Type"),
                          "bytes": len(data), "sha256": sha(data)}
            path.write_bytes(data)
            return record
        with ThreadPoolExecutor(max_workers=2) as pool:
            records = list(pool.map(fetch, jobs))
        write(records_path, {"files": records})
    else:
        records = json.loads(records_path.read_text(encoding="utf-8"))["files"]
        for path, url in jobs:
            record = next(r for r in records if r["file"] == path.relative_to(OUT).as_posix())
            assert record["url"] == url and record["sha256"] == sha(path.read_bytes()), path.name

    raw = OUT / "power_daily_2015_2025.json"
    seen_duplicates = []
    def unique(pairs):
        doc = {}
        for k, v in pairs:
            if k in doc:
                seen_duplicates.append(k)
            doc[k] = v
        return doc
    weather = json.loads(raw.read_bytes(), object_pairs_hook=unique)
    assert not seen_duplicates
    p = weather["properties"]["parameter"]
    names = ["T2M", "T2M_MAX", "T2M_MIN", "PRECTOTCORR"]
    dates = [dt.date(2015, 1, 1) + dt.timedelta(days=i) for i in range(4018)]
    assert dates[-1] == dt.date(2025, 12, 31) and weather["header"]["time_standard"] == "UTC"
    keys = {date.strftime("%Y%m%d") for date in dates}
    assert all(set(p[name]) == keys for name in names)
    assert all(weather["parameters"][n]["units"] == ("mm/day" if n == "PRECTOTCORR" else "C") for n in names)
    rows, flags = [], []
    for date in dates:
        key = date.strftime("%Y%m%d")
        v = {name: p[name][key] for name in names}
        assert all(math.isfinite(x) and x != weather["header"]["fill_value"] for x in v.values())
        assert v["T2M_MIN"] <= v["T2M"] <= v["T2M_MAX"] and v["PRECTOTCORR"] >= 0
        if v["PRECTOTCORR"] > 200:
            flags.append({"date": date.isoformat(), "rain_mm": v["PRECTOTCORR"]})
        rows.append({"date_utc": date.isoformat(), **v})
    with (OUT / "daily.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)

    soil_rows = []
    for prop, depth, stat, path in specs:
        im = Image.open(io.BytesIO(path.read_bytes()))
        scale, tie, keys = im.tag_v2[33550], im.tag_v2[33922], im.tag_v2[34735]
        geo_keys = {keys[i]: keys[i + 3] for i in range(4, len(keys), 4)}
        assert geo_keys[2048] == 4326 and geo_keys[1025] == 1
        assert abs(tie[3] - BBOX[0]) < 1e-8 and abs(tie[4] - BBOX[3]) < 1e-8
        assert abs(tie[3] + scale[0] * im.width - BBOX[2]) < 1e-8
        assert abs(tie[4] - scale[1] * im.height - BBOX[1]) < 1e-8
        col = math.floor((POINT[0] - tie[3]) / scale[0]); row = math.floor((tie[4] - POINT[1]) / scale[1])
        value = im.getpixel((col, row))
        valid = 0 < value <= (140 if prop == "phh2o" else 1000)
        soil_rows.append({"property": prop, "depth": depth, "statistic": stat, "raw_integer": value,
                          "converted_value": value / 10 if valid else None,
                          "unit": "pH_H2O" if prop == "phh2o" else "percent_mass", "valid_model_value": valid,
                          "returned_grid_size": list(im.size), "pixel_scale_deg": list(scale[:2])})
    for prop, depth in {(r["property"], r["depth"]) for r in soil_rows}:
        g = {r["statistic"]: r["converted_value"] for r in soil_rows if r["property"] == prop and r["depth"] == depth}
        assert all(x is not None for x in g.values()) and g["Q0.05"] <= g["Q0.95"]
    prior = json.loads((ROOT / "nasa-space-apps-2026/sources/data-audits/long-khanh-cai-lay-2026-11-12/power_daily_2015_2025.json").read_bytes())
    write(OUT / "summary.json", {
        "artifact_kind": "fixed_AOI_remote_data_not_measured_farm_soil_or_crop_model", "review_date": "2026-11-12",
        "sample_point_lon_lat": POINT, "sample_role": "point_within_commune_not_field_or_whole_commune_soil_average", "aoi_geometry_path": "../../../planning/cases/my-thanh-cai-lay/aoi.geojson",
        "power": {"header": weather["header"], "units": weather["parameters"], "days": len(rows), "values": len(rows) * 4,
                  "technical_checks": "pass", "quality": "warn" if flags else "technical_pass_not_field_validated",
                  "extreme_rain_review_threshold_mm": 200, "flags_not_proven_errors": flags,
                  "raw_sha256": sha(raw.read_bytes()), "same_parameter_arrays_as_long_khanh_probe": p == prior["properties"]["parameter"],
                  "spatial_support_degrees": [0.5, 0.625]},
        "soilgrids": {"native_support_m": 250, "native_crs": "EPSG:152160", "output_crs": "EPSG:4326",
                      "query_center_not_whole_AOI_soil_average": True, "resampling_algorithm_not_verified": True,
                      "conversion_authority": "https://docs.isric.org/globaldata/soilgrids/SoilGrids_faqs_01.html",
                      "all_requested_properties_divide_raw_by": 10, "zero_not_interpreted_as_valid_soil_value": True,
                      "values": soil_rows, "local_samples": None},
        "script_sha256": sha(Path(__file__).read_bytes()),
        "limits": ["No farmer or field survey required for the agreed remote-data hackathon scope",
                   "No claim of agronomic suitability or measured irrigation/yield/soil benefit",
                   "No current baseline rotation inferred from two satellite dates",
                   "Published Long Khanh/Cai Lay experiments are reference evidence, not same-site observations"],
    })
    print(json.dumps({"days": len(rows), "rain_review_flags": flags, "soil_coverages": len(soil_rows)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
