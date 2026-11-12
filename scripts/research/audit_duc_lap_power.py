"""Small, standard-library-only public NASA data audit, not a crop model."""
from pathlib import Path
import argparse,calendar,csv,datetime as dt,hashlib,json,math,statistics,urllib.parse,urllib.request

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'nasa-space-apps-2026/sources/data-audits/duc-lap-2026-11-12'
PARAMS=['T2M','T2M_MAX','T2M_MIN','PRECTOTCORR']
QUERY={'parameters':','.join(PARAMS),'community':'AG','longitude':'106.44351','latitude':'10.91123','start':'20150101','end':'20251231','format':'JSON','time-standard':'UTC'}
URL='https://power.larc.nasa.gov/api/temporal/daily/point?'+urllib.parse.urlencode(QUERY)
RAW='power_daily_2015_2025.json'

def unique_object(pairs):
    out={}
    for key,value in pairs:
        if key in out:raise ValueError('Duplicate JSON key: '+key)
        out[key]=value
    return out

def dump(name,obj):
    (OUT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def write_csv(name,rows):
    with (OUT/name).open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--refresh',action='store_true',help='Explicitly redownload the public API response');args=ap.parse_args()
    OUT.mkdir(parents=True,exist_ok=True)
    raw=OUT/RAW
    if not raw.exists() or args.refresh:
        req=urllib.request.Request(URL,headers={'User-Agent':'NeuraX-Public-Data-Audit/0.1'})
        with urllib.request.urlopen(req,timeout=60) as response:
            payload=response.read();status=response.status;content_type=response.headers.get('Content-Type')
        doc=json.loads(payload)
        assert 'properties' in doc,doc.get('messages',doc)
        raw.write_bytes(payload)
        dump('retrieval.json',{'retrieved_at_utc':dt.datetime.now(dt.timezone.utc).isoformat(),'request_url':URL,'http_status':status,'content_type':content_type,'bytes':len(payload)})
    doc=json.loads(raw.read_bytes(),object_pairs_hook=unique_object);header=doc['header'];params=doc['properties']['parameter'];metadata=doc['parameters'];fill=header['fill_value']
    assert header['time_standard']=='UTC',header
    assert all(p in params for p in PARAMS),params.keys()
    assert metadata['PRECTOTCORR']['units']=='mm/day',metadata['PRECTOTCORR']
    assert all(metadata[p]['units']=='C' for p in PARAMS[:3]),metadata
    first=dt.date(2015,1,1);last=dt.date(2025,12,31)
    dates=[first+dt.timedelta(days=i) for i in range((last-first).days+1)]
    expected={d.strftime('%Y%m%d') for d in dates}
    key_issues={p:{'missing_keys':sorted(expected-set(params[p])),'extra_keys':sorted(set(params[p])-expected)} for p in PARAMS}
    rows=[];missing={p:0 for p in PARAMS};physical=[]
    for d in dates:
        key=d.strftime('%Y%m%d');row={'date':d.isoformat()}
        for p in PARAMS:
            value=params[p].get(key)
            invalid=value is None or value==fill or not isinstance(value,(int,float)) or not math.isfinite(value)
            row[p]=None if invalid else value
            missing[p]+=int(invalid)
        if all(row[p] is not None for p in PARAMS):
            if not -90<=row['T2M_MIN']<=row['T2M']<=row['T2M_MAX']<=65:physical.append({'date':key,'issue':'temperature_order_or_broad_bound'})
            if row['PRECTOTCORR']<0:physical.append({'date':key,'issue':'negative_rain'})
        rows.append(row)
    review_flags=[{'date':r['date'],'parameter':'PRECTOTCORR','value':r['PRECTOTCORR'],'reason':'Above exploratory 200 mm/day review threshold; not proof of error and not automatically removed'} for r in rows if r['PRECTOTCORR'] is not None and r['PRECTOTCORR']>200]
    qa={'expected_days':len(dates),'parameter_count':len(PARAMS),'fill_value':fill,'missing_values':missing,'key_issues':key_issues,'physical_flags':physical,'review_flags':review_flags,'status':'warn' if review_flags else 'pass_internal_only','duplicate_json_keys':'none','time_standard':'UTC','date_range':[first.isoformat(),last.isoformat()]}
    dump('qa.json',qa)
    assert not any(missing.values()) and not physical and all(not v['missing_keys'] and not v['extra_keys'] for v in key_issues.values()),'Data QA failed; see qa.json, no complete aggregation assumed'
    write_csv('daily.csv',rows)
    months=[]
    for year in range(2015,2026):
        for month in range(1,13):
            group=[r for r in rows if r['date'].startswith(f'{year}-{month:02d}')]
            assert len(group)==calendar.monthrange(year,month)[1]
            months.append({'year':year,'month':month,'days':len(group),'rain_total_mm':round(sum(r['PRECTOTCORR'] for r in group),3),'tmean_c':round(statistics.mean(r['T2M'] for r in group),3),'mean_daily_tmax_c':round(statistics.mean(r['T2M_MAX'] for r in group),3),'mean_daily_tmin_c':round(statistics.mean(r['T2M_MIN'] for r in group),3),'days_tmax_ge35c':sum(r['T2M_MAX']>=35 for r in group),'days_rain_lt1mm':sum(r['PRECTOTCORR']<1 for r in group)})
    write_csv('monthly.csv',months)
    clim=[]
    for month in range(1,13):
        group=[r for r in months if r['month']==month]
        clim.append({'month':month,'years':len(group),'mean_monthly_rain_mm':round(statistics.mean(r['rain_total_mm'] for r in group),3),'median_monthly_rain_mm':round(statistics.median(r['rain_total_mm'] for r in group),3),'min_monthly_rain_mm':min(r['rain_total_mm'] for r in group),'max_monthly_rain_mm':max(r['rain_total_mm'] for r in group),'mean_tmean_c':round(statistics.mean(r['tmean_c'] for r in group),3),'mean_days_tmax_ge35c':round(statistics.mean(r['days_tmax_ge35c'] for r in group),3)})
    write_csv('monthly_reference_2015_2025.csv',clim)
    annual=[]
    for y in range(2015,2026):
        group=[r for r in rows if r['date'].startswith(str(y))]
        annual.append({'year':y,'rain_total_mm':round(sum(r['PRECTOTCORR'] for r in group),3),'tmean_c':round(statistics.mean(r['T2M'] for r in group),3),'days_tmax_ge35c':sum(r['T2M_MAX']>=35 for r in group)})
    write_csv('annual.csv',annual)
    # Independent aggregation path: sum monthly values vs raw daily totals.
    annual_delta=max(abs(a['rain_total_mm']-sum(m['rain_total_mm'] for m in months if m['year']==a['year'])) for a in annual)
    assert annual_delta<0.02,annual_delta
    summary={'period':'2015-2025','years':11,'days':len(rows),'daily_values':len(rows)*len(PARAMS),'mean_annual_rain_mm':round(statistics.mean(r['rain_total_mm'] for r in annual),3),'minimum_rain_year':min(annual,key=lambda x:x['rain_total_mm']),'maximum_rain_year':max(annual,key=lambda x:x['rain_total_mm']),'driest_reference_month':min(clim,key=lambda x:x['mean_monthly_rain_mm']),'wettest_reference_month':max(clim,key=lambda x:x['mean_monthly_rain_mm']),'hottest_reference_month':max(clim,key=lambda x:x['mean_tmean_c']),'max_monthly_daily_rain_sum_delta_mm':round(annual_delta,6),'interpretation':'Historical gridded reference only; not official 30-year normal, field rain gauge, ENSO attribution or crop recommendation.'}
    flagged_dates={r['date'] for r in review_flags}
    stress_clim=[]
    for month in range(1,13):
        # Explicit missing contribution stress test, NOT corrected rainfall or final climatology.
        total=sum(r['PRECTOTCORR'] for r in rows if int(r['date'][5:7])==month and r['date'] not in flagged_dates)
        stress_clim.append({'month':month,'mean_rain_contribution_excluding_flagged_days_mm':round(total/11,3)})
    summary['review_flags']=review_flags
    summary['quality_status']=qa['status']
    summary['median_wettest_month']=max(clim,key=lambda x:x['median_monthly_rain_mm'])
    summary['sensitivity_excluding_flagged_day_contributions']={'description':'Arithmetic influence check only; leaves an incomplete period. Not imputation, correction or validated rain estimate. Raw and reported reference remain unchanged.','flagged_days':sorted(flagged_dates),'mean_annual_rain_contribution_mm':round(sum(r['PRECTOTCORR'] for r in rows if r['date'] not in flagged_dates)/11,3),'maximum_month':max(stress_clim,key=lambda x:x['mean_rain_contribution_excluding_flagged_days_mm'])}
    dump('summary.json',summary)
    dump('data_dictionary.json',{'provider_parameters':metadata,'derived':{'rain_total_mm':'Sum of complete daily PRECTOTCORR (mm/day) over one-day intervals; total mm','tmean_c':'Arithmetic mean daily T2M; no field validation','days_tmax_ge35c':'Diagnostic >=35 C threshold only, not a validated crop damage rule','days_rain_lt1mm':'Diagnostic <1 mm/day threshold only; not root-zone drought','monthly_reference':'Mean/median/min/max of 11 yearly month totals; not 30-year climate normal'}})
    dump('manifest.json',{'audit_date_local':'2026-11-12','case_id':'duc-lap-ha-place-reference-v1','point_role':'Approximate historical place reference from GeoNames; not surveyed farm, not verified parcel centroid','point_source':'https://www.geonames.org/search.html?q=Xa+Duc+Lap+Ha&country=VN','requested_lon_lat':[106.44351,10.91123],'coordinate_reference':'Longitude/latitude degrees; geodetic place reference, not a cadastral survey','returned_geometry':doc.get('geometry'),'query':QUERY,'retrieval':json.loads((OUT/'retrieval.json').read_text(encoding='utf-8')),'source_header':header,'source_parameter_metadata':metadata,'messages':doc.get('messages'),'resolution_source':'https://power.larc.nasa.gov/docs/tutorials/service-data-request/api/','meteorology_source_grid_deg_lat_lon':[0.5,0.625],'crs_note':'Point GeoJSON geographic coordinates; no reprojection/resampling in this audit','use_restriction':'NASA POWER open data; credit provider/source; no rights inferred for third-party soil documents','raw_sha256':hashlib.sha256(raw.read_bytes()).hexdigest(),'raw_bytes':raw.stat().st_size,'analysis_script':'scripts/research/audit_duc_lap_power.py','script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'qa_result':qa['status'],'passed_checks':['completeness','units','duplicate keys','temperature ordering','nonnegative rain','monthly vs daily sums'],'limitations':['Exploratory extreme-rain review flag unresolved; independent cross-check pending','No parcel soil, irrigation, crop sequence or farm observation validated','Not an agronomic suitability or yield model','No current-season forecast or ENSO causal analysis','Requested and returned point precision does not improve source grid resolution']})
    print(json.dumps({'qa':qa['status'],'header':header,'summary':summary,'raw_bytes':raw.stat().st_size},ensure_ascii=False))

if __name__=='__main__':main()
