"""Date arithmetic and historical weather exposure for two research candidates.

Dates and 14-day field turnaround are assumptions. Source durations are regional
examples, not verified farm durations. This script cannot approve a rotation.
"""
import csv
import datetime as dt
import hashlib
import json
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "nasa-space-apps-2026/sources/data-audits/duc-lap-2026-11-12"
OUT = BASE / "rotation-window-screen"
CASES = [("DL-A-MAIZE", "CP888", 110, "D8"), ("DL-B-PEANUT", "GV10", 95, "D7")]


def main():
    raw = BASE / "power_daily_2015_2025.json"
    doc = json.loads(raw.read_bytes())
    assert doc["header"]["time_standard"] == "UTC"
    p = doc["properties"]["parameter"]
    rows = []
    for candidate, variety, duration, source in CASES:
        for day in [1, 15]:
            for year in range(2015, 2026):
                start = dt.date(year, 1, day)
                dates = [start + dt.timedelta(days=i) for i in range(duration)]
                last = dates[-1]
                rice = dt.date(year, 5, 15)
                # All days strictly after last crop day and before next sowing.
                available = (rice - last).days - 1
                keys = [d.strftime("%Y%m%d") for d in dates]
                rain = [p["PRECTOTCORR"][k] for k in keys]
                temp = [p["T2M"][k] for k in keys]
                assert all(v >= 0 for v in rain)
                assert all(v != doc["header"]["fill_value"] for v in temp)
                rows.append({"candidate": candidate, "variety_example": variety,
                             "duration_source_id": source, "reference_year": year,
                             "assumed_start_utc": start.isoformat(), "inclusive_crop_end_utc": last.isoformat(),
                             "duration_days": duration, "assumed_rice_sowing": rice.isoformat(),
                             "available_between_crops_days": available, "assumed_turnaround_days": 14,
                             "calendar_slack_days": available - 14,
                             "calendar_only_status": "fits_assumptions" if available >= 14 else "conflict_under_assumptions",
                             "rain_total_mm": round(sum(rain), 3),
                             "tmean_c": round(statistics.mean(temp), 3),
                             "farm_eligibility": "needs_review"})
    OUT.mkdir(parents=True, exist_ok=True)
    with (OUT / "windows.csv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    groups = []
    for candidate, variety, duration, source in CASES:
        for day in [1, 15]:
            subset = [r for r in rows if r["candidate"] == candidate and r["assumed_start_utc"].endswith(f"01-{day:02}")]
            assert len(subset) == 11
            groups.append({"candidate": candidate, "assumed_sowing_month_day": f"01-{day:02}",
                           "duration_days": duration, "years": len(subset),
                           "rain_mm_median": statistics.median(r["rain_total_mm"] for r in subset),
                           "rain_mm_min": min(r["rain_total_mm"] for r in subset),
                           "rain_mm_max": max(r["rain_total_mm"] for r in subset),
                           "mean_tmean_c": round(statistics.mean(r["tmean_c"] for r in subset), 3),
                           "calendar_slack_days_min": min(r["calendar_slack_days"] for r in subset),
                           "calendar_slack_days_max": max(r["calendar_slack_days"] for r in subset),
                           "calendar_conflict_years_under_assumptions": sum(r["calendar_slack_days"] < 0 for r in subset)})
    summary = {"artifact_kind": "research_window_screen_not_crop_model_or_recommendation",
               "baseline": None, "overall_status": "needs_local_soil_water_calendar_review",
               "assumptions": {"starts": ["January 1", "January 15"], "rice_sowing": "May 15",
                               "turnaround_days": 14, "these_are_farm_records": False},
               "duration_evidence": {"D8": "CP888 102-110 days in southern regional trials; upper bound used, not universal maximum",
                                     "D7": "GV10 95 days in Duc Hoa Thuong DX2011-2012 trial; transfer needs review"},
               "raw_sha256": hashlib.sha256(raw.read_bytes()).hexdigest(),
               "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               "groups": groups,
               "limits": ["Different window lengths cannot rank irrigation demand using rain totals",
                          "No ET, Kc, rooting depth, soil storage, irrigation volume or yield model",
                          "Meteorological grid at historical place; not verified selected hamlet or farm",
                          "POWER overall QA WARN persists; flagged June14 2020 outside these declared windows",
                          "No current ENSO or future-season forecast; no farmer sowing/harvest records",
                          "Maturity duration may not equal field release; field drying and clearing require verification",
                          "Rice variety/duration and full annual feasibility remain unverified"],
               "allowed_use": "Discuss calendar sensitivity and questions about irrigation; never score farm eligibility"}
    (OUT / "summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(groups, ensure_ascii=False))


if __name__ == "__main__":
    main()
