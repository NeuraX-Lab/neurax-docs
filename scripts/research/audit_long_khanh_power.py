"""Cached NASA weather probe for the Long Khanh/Cai Lay historical case.

Standard library only. Point is a locality, not the published experimental field.
Download URL is in manifest.json; this script never calls the network.
"""
import csv
import datetime as dt
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "nasa-space-apps-2026/sources/data-audits/long-khanh-cai-lay-2026-11-12"
PARAMS = ["T2M", "T2M_MAX", "T2M_MIN", "PRECTOTCORR"]
URL = "https://power.larc.nasa.gov/api/temporal/daily/point?parameters=T2M,T2M_MAX,T2M_MIN,PRECTOTCORR&community=AG&longitude=106.11667&latitude=10.38333&start=20150101&end=20251231&format=JSON&time-standard=UTC"


def main():
    raw = OUT / "power_daily_2015_2025.json"
    duplicate_keys = []
    def pairs_hook(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                duplicate_keys.append(key)
            result[key] = value
        return result
    doc = json.loads(raw.read_bytes(), object_pairs_hook=pairs_hook)
    assert not duplicate_keys
    p = doc["properties"]["parameter"]
    assert doc["header"]["time_standard"] == "UTC"
    assert all(doc["parameters"][name]["units"] == ("mm/day" if name == "PRECTOTCORR" else "C") for name in PARAMS)
    dates = [dt.date(2015, 1, 1) + dt.timedelta(days=i) for i in range(4018)]
    assert dates[-1] == dt.date(2025, 12, 31)
    keys = {date.strftime("%Y%m%d") for date in dates}
    assert all(set(p[name]) == keys for name in PARAMS)
    rows = []
    flags = []
    for date in dates:
        key = date.strftime("%Y%m%d")
        values = {name: p[name][key] for name in PARAMS}
        assert all(math.isfinite(v) and v != doc["header"]["fill_value"] for v in values.values())
        assert values["T2M_MIN"] <= values["T2M"] <= values["T2M_MAX"]
        assert values["PRECTOTCORR"] >= 0
        if values["PRECTOTCORR"] > 200:
            flags.append({"date": date.isoformat(), "rain_mm": values["PRECTOTCORR"],
                          "meaning": "exploratory review threshold, not proven error"})
        rows.append({"date_utc": date.isoformat(), **values})
    with (OUT / "daily.csv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    manifest = {
        "artifact_kind": "historical_locality_weather_probe_not_experiment_replication",
        "review_date": "2026-11-12", "request_url": URL,
        "raw_file": raw.name, "raw_sha256": hashlib.sha256(raw.read_bytes()).hexdigest(),
        "raw_bytes": raw.stat().st_size, "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "header": doc["header"], "parameters": doc["parameters"],
        "requested_point_lon_lat": [106.11667, 10.38333],
        "point_source": "https://mapcarta.com/15497128 (GeoNames 1575725)",
        "point_role": "locality_reference_not_verified_farm_or_experimental_plot",
        "returned_geometry": doc["geometry"], "time_standard": "UTC",
        "native_meteorology_support_deg": {"latitude": 0.5, "longitude": 0.625},
        "resolution_source": "https://power.larc.nasa.gov/docs/tutorials/service-data-request/api/",
        "technical_checks": "pass", "days": len(rows), "values": len(rows) * len(PARAMS),
        "extreme_rain_review_threshold_mm_per_day": 200, "extreme_rain_flags": flags,
        "overall_quality": "warn" if flags else "technical_pass_not_locally_validated",
        "limitations": ["Climate period2015-2025 differs from historical field experiments",
                        "No local station/irrigation/field weather validation", "No soil or crop water model",
                        "Published treatment summaries are not raw independent training samples",
                        "No measured or predicted yield/water saving/soil change assigned to this grid"],
    }
    (OUT / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: manifest[k] for k in ["days", "values", "raw_sha256", "technical_checks", "overall_quality", "extreme_rain_flags"]}))


if __name__ == "__main__":
    main()
