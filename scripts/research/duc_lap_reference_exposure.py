"""Historical exposure for a declared hypothetical 75-day window; not advice."""
from pathlib import Path
import csv,datetime as dt,hashlib,json,statistics
ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/'nasa-space-apps-2026/sources/data-audits/duc-lap-2026-11-12'
OUT=BASE/'reference-exposure'

def main():
    raw=BASE/'power_daily_2015_2025.json';doc=json.loads(raw.read_bytes());p=doc['properties']['parameter']
    assert doc['header']['time_standard']=='UTC'
    OUT.mkdir(parents=True,exist_ok=True)
    rows=[]
    for year in range(2015,2026):
        start=dt.date(year,1,15);dates=[start+dt.timedelta(days=i) for i in range(75)]
        vals=[{k:p[k][d.strftime('%Y%m%d')] for k in ['T2M','T2M_MAX','PRECTOTCORR']} for d in dates]
        assert all(v>=0 for row in vals for k,v in row.items() if k=='PRECTOTCORR')
        assert all(v!=doc['header']['fill_value'] for row in vals for v in row.values())
        rows.append({'reference_year':year,'assumed_start_utc':start.isoformat(),'inclusive_end_utc':dates[-1].isoformat(),'days':len(dates),'rain_total_mm':round(sum(v['PRECTOTCORR'] for v in vals),3),'tmean_c':round(statistics.mean(v['T2M'] for v in vals),3),'days_tmax_ge35c_diagnostic':sum(v['T2M_MAX']>=35 for v in vals)})
    with (OUT/'exposure.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    summary={'case_mode':'reference_sandbox','window_definition':{'sowing_date':'15 January each year, design assumption not farm record','length_days_inclusive':75,'duration_rationale':'Upper end of IAS DH-1 published 70-75 day duration, transfer not reviewed','source':'https://iasvn.org/giong-me-dh-1'},'years':11,'rain_total_mm':{'minimum':min(r['rain_total_mm'] for r in rows),'median':statistics.median(r['rain_total_mm'] for r in rows),'mean':round(statistics.mean(r['rain_total_mm'] for r in rows),3),'maximum':max(r['rain_total_mm'] for r in rows)},'mean_tmean_c':round(statistics.mean(r['tmean_c'] for r in rows),3),'flagged_2020_06_14_in_window':False,'quality':'Complete window coverage; overall POWER audit WARN and crop validity not established','raw_sha256':hashlib.sha256(raw.read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'limits':['Hypothetical sowing window, not observed cropping calendar','Historical grid exposure, not coming-season forecast','No ET/crop coefficient/soil storage/irrigation; cannot compute water deficit or water saving','Tmax >=35 C is a diagnostic count, not a crop damage threshold','Outside flagged event by predeclared season window, not outlier cleaning'],'decision_use':'Makes water availability and sowing calendar explicit review questions; does not select a best crop or certify eligibility'}
    (OUT/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(summary,ensure_ascii=False))

if __name__=='__main__':main()
