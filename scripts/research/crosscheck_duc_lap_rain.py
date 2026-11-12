"""Event-only ERA5 comparison. Model disagreement is not ground validation."""
from pathlib import Path
import argparse,csv,datetime as dt,hashlib,json,urllib.parse,urllib.request
ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/'nasa-space-apps-2026/sources/data-audits/duc-lap-2026-11-12'
OUT=BASE/'event-crosscheck'
QUERY={'latitude':'10.91123','longitude':'106.44351','start_date':'2020-06-12','end_date':'2020-06-17','daily':'precipitation_sum','timezone':'UTC','models':'era5'}
URL='https://archive-api.open-meteo.com/v1/archive?'+urllib.parse.urlencode(QUERY)

def save(name,obj):
    (OUT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--refresh',action='store_true');args=parser.parse_args()
    OUT.mkdir(parents=True,exist_ok=True);raw=OUT/'era5_open_meteo_raw.json'
    if not raw.exists() or args.refresh:
        with urllib.request.urlopen(URL,timeout=45) as response:
            payload=response.read();status=response.status
        document=json.loads(payload);assert 'daily' in document,document
        raw.write_bytes(payload)
        save('retrieval.json',{'url':URL,'query':QUERY,'retrieved_at_utc':dt.datetime.now(dt.timezone.utc).isoformat(),'http_status':status,'provider_docs':'https://open-meteo.com/en/docs/historical-weather-api'})
    doc=json.loads(raw.read_bytes());nasa_path=BASE/'power_daily_2015_2025.json';nasa=json.loads(nasa_path.read_bytes())
    assert doc['utc_offset_seconds']==0 and nasa['header']['time_standard']=='UTC'
    assert doc['daily_units']['precipitation_sum']=='mm'
    assert nasa['parameters']['PRECTOTCORR']['units']=='mm/day'
    dates=doc['daily']['time'];values=doc['daily']['precipitation_sum']
    assert len(dates)==6 and len(set(dates))==6 and len(values)==6
    rows=[]
    for date,value in zip(dates,values):
        assert isinstance(value,(int,float)) and value>=0
        nv=nasa['properties']['parameter']['PRECTOTCORR'][date.replace('-','')]
        rows.append({'date_utc':date,'nasa_power_precip_mm_over_one_day':nv,'era5_via_open_meteo_precip_mm':value,'difference_mm':round(nv-value,3)})
    with (OUT/'comparison.csv').open('w',encoding='utf-8',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    event=next(r for r in rows if r['date_utc']=='2020-06-14')
    summary={'event':event,'six_day_totals_mm':{'NASA_POWER':round(sum(r['nasa_power_precip_mm_over_one_day'] for r in rows),3),'ERA5_via_Open_Meteo':round(sum(r['era5_via_open_meteo_precip_mm'] for r in rows),3)},'requested_lon_lat':[106.44351,10.91123],'era5_returned_lon_lat':[doc['longitude'],doc['latitude']],'power_returned_geometry':nasa['geometry'],'source_grid_degrees':{'POWER_met_lat_lon':[0.5,0.625],'ERA5_lat_lon':[0.25,0.25]},'models':['NASA POWER header MERRA2/POWER','Explicit models=era5 via Open-Meteo; not best_match'],'status':'warn_model_disagreement_unresolved','conclusion':'Different reanalysis products and grid supports disagree. No station truth; neither corrected nor deleted NASA values. Do not use isolated event to optimize crop calendar.','raw_sha256':hashlib.sha256(raw.read_bytes()).hexdigest(),'nasa_raw_sha256':hashlib.sha256(nasa_path.read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'attribution':['NASA Langley Research Center POWER Project','ECMWF/Copernicus ERA5, distributed by Open-Meteo'],'provider_docs':['https://power.larc.nasa.gov/docs/tutorials/service-data-request/api/','https://open-meteo.com/en/docs/historical-weather-api'],'time_check':'Daily windows requested UTC; mm/day integrated over one day compared with mm daily sum. Different spatial support remains.'}
    save('summary.json',summary)
    print(json.dumps(summary,ensure_ascii=False))

if __name__=='__main__':main()
