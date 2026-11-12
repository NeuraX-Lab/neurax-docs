"""Document/data integrity audit, not product or agronomic validation.

Native Windows bundled Python, pypdf, Pillow. No network or product execution.
"""
import csv
import datetime as dt
import hashlib
import json
import math
import posixpath
import re
from pathlib import Path
from zipfile import ZipFile
from xml.etree import ElementTree
from PIL import Image
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[2]
CASE=ROOT/'nasa-space-apps-2026/planning/cases/my-thanh-cai-lay'
DATA=ROOT/'nasa-space-apps-2026/sources/data-audits/my-thanh-cai-lay-2026-11-12'
OUT=CASE/'consistency-audit.json'

def read(p):return json.loads(p.read_bytes())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def local_links(s):
    for t in re.findall(r'!?\[[^\]]*\]\(([^\n]+?)\)',s):
        if not t.startswith(('http:','https:','mailto:','#','plugin:','app:')):yield t.strip('<>').split('#')[0]
def clean(r):
    out=[]
    for p in r:
        if not out or out[-1]!=p:out.append(p)
    return out

def main():
    checks={};warnings=[];missing=[];n=0;mds=list((ROOT/'nasa-space-apps-2026').rglob('*.md'))+list((ROOT/'team').glob('*.md'))+[ROOT/'README.md']
    for p in mds:
        s=p.read_text(encoding='utf-8-sig');assert s.count('```')%2==0,p
        for t in local_links(s):
            n+=1
            if not (p.parent/t).exists():missing.append({'file':p.relative_to(ROOT).as_posix(),'target':t})
    upstream='nasa-space-apps-2026/sources/data-audits/my-thanh-cai-lay-2026-11-12/imagery/boundary-readme.md'
    assert all(x['file']==upstream for x in missing),missing
    checks['markdown']={'files':len(mds),'local_link_occurrences':n,'project_missing_links':0,'imported_upstream_readme_missing_links':missing,'fences':'pass'}
    if missing:warnings.append('Imported vendor README retains links to absent upstream database folders; provenance snapshot left unchanged.')
    retrieval=read(DATA/'retrieval.json')['files'];assert len(retrieval)==16
    for r in retrieval:assert sha(DATA/r['file'])==r['sha256']
    weather=read(DATA/'power_daily_2015_2025.json')['properties']['parameter']
    expected={(dt.date(2015,1,1)+dt.timedelta(days=i)).strftime('%Y%m%d') for i in range(4018)}
    for param,series in weather.items():
        assert set(series)==expected,param
        assert all(math.isfinite(v) and v!=-999 for v in series.values())
    for k in expected:assert weather['T2M_MIN'][k]<=weather['T2M'][k]<=weather['T2M_MAX'][k] and weather['PRECTOTCORR'][k]>=0
    checks['raw_data']={'hashes_verified':len(retrieval),'days_per_variable':4018,'values':sum(map(len,weather.values())),
        'daily_keys_finite_fill_temp_order_precip_sign':'pass','rain_review_flag_mm':weather['PRECTOTCORR']['20200614'],'quality':'WARN, not corrected or field validated'}
    official=read(DATA/'imagery/official-my-thanh-geometry.json')['features'][0]['geometry']['coordinates']
    current=read(CASE/'aoi.geojson')['features'][0]['geometry']['coordinates']
    assert [[clean(r) for r in p] for p in official]==current
    block=read(CASE/'study-block.geojson')['features'][0];ring=block['geometry']['coordinates'][0]
    assert ring[0]==ring[-1] and len(ring)==9 and block['properties']['homogeneous_soil_verified'] is False
    meta=read(DATA/'imagery/my-thanh-close-export.json');e=meta['extent'];manifest=read(CASE/'study-block-manifest.json')
    for (x,y),row in zip(manifest['source_pixel_vertices'],list(csv.DictReader((CASE/'study-block-coordinates.csv').open(encoding='utf-8')))):
        lon=e['xmin']+x/meta['width']*(e['xmax']-e['xmin']);lat=e['ymax']-y/meta['height']*(e['ymax']-e['ymin'])
        assert abs(float(row['longitude'])-lon)<1e-10 and abs(float(row['latitude'])-lat)<1e-10
    for name in ['aoi.kml','study-block.kml']:ElementTree.parse(CASE/name)
    soil=read(CASE/'study-block-soil-model.json');point=soil['point_lon_lat']
    for r in soil['values']:
        p=DATA/r['source_file'];assert sha(p)==r['sha256'];im=Image.open(p);sc=im.tag_v2[33550];tie=im.tag_v2[33922]
        pixel=(math.floor((point[0]-tie[3])/sc[0]),math.floor((tie[4]-point[1])/sc[1]))
        assert im.getpixel(pixel)==r['raw_integer'] and r['value']==r['raw_integer']/10
    checks['geometry_and_soil']={'commune_matches_primary_source':True,'block_pixel_to_coordinate_transform':'pass','kml_parse':'pass','soil_model_values_rechecked':len(soil['values']),'not_checked':'field boundaries, crop identity, uniform soil, suitability, independent positional accuracy'}
    rows=list(csv.DictReader((CASE/'rotation-evidence-review.csv').open(encoding='utf-8-sig')))
    assert len(rows)==12 and len({r['claim_id'] for r in rows})==12
    assert all(not r['reviewer_decision'] and not r['review_date'] for r in rows)
    checks['crop_evidence']={'rows':12,'review_status':'not reviewed; decision/date empty','field_recommendation_ready':False}
    pdf=ROOT/'output/pdf/NeuraX-AgroTwin-Site-and-Demo-Dossier-Bich.pdf';b=read(pdf.with_suffix('.build.json'));assert sha(pdf)==b['output_sha256']
    for r in b['inputs']:assert sha(ROOT/r['path'])==r['sha256'],r['path']
    reader=PdfReader(pdf);txt=' '.join(' '.join(p.extract_text().split()) for p in reader.pages)
    for phrase in ['Hưng và Việt','Data Analysis','Backend','score=null','is_current=null','1.3']:assert phrase in txt,phrase
    assert all('\ufffd' not in p.extract_text() for p in reader.pages)
    checks['current_pdf']={'pages':len(reader.pages),'included_source_hashes':len(b['inputs']),'output_hash':'pass','roles_and_unknown_semantics':'pass','visual_review':'separate rendered-page inspection required'}
    snapshots=read(ROOT/'output/pdf/snapshot-label-manifest.json')['files']
    for r in snapshots:
        p=ROOT/'output/pdf'/r['file'];a=ROOT/r['original_archive'];assert sha(p)==r['output_sha256'] and sha(a)==r['original_sha256']
        old=PdfReader(a);new=PdfReader(p);assert len(new.pages)==len(old.pages)+1
        assert 'SNAPSHOT' in new.pages[0].extract_text() and '1.3' in new.pages[0].extract_text()
        for i,page in enumerate(old.pages):assert page.extract_text()==new.pages[i+1].extract_text()
    checks['snapshot_pdfs']={'files':len(snapshots),'notice_current_version':'1.3','original_pages_text_preserved':True}
    with ZipFile(ROOT/'output/handoff/NeuraX-MyThanh-Bich-Research-Pack-2026-11-12.zip') as z:
        assert z.testzip() is None;zm=json.loads(z.read('manifest.json'));assert zm['version']=='1.3'
        for r in zm['files']:assert hashlib.sha256(z.read(r['path'])).hexdigest()==r['sha256']
        assert z.read(pdf.name)==pdf.read_bytes()
        zl=0
        for name in z.namelist():
            if name.endswith('.md'):
                s=z.read(name).decode('utf-8-sig');assert '<!-- INCLUDE:' not in s
                for t in local_links(s):
                    assert posixpath.normpath(posixpath.join(posixpath.dirname(name),t)) in z.namelist(),(name,t);zl+=1
        checks['zip']={'entries':len(z.namelist()),'internal_local_links_verified':zl,'crc_and_hashes':'pass','pdf_matches_current':True}
    doc={'audit_kind':'documentation and cached-source integrity, not product/field validation','review_date':'2026-11-12',
         'checks':checks,'warnings':warnings,'unresolved':['Official challenge Resources/local agenda/remote eligibility not fully verified',
         'Crop-water-season review and sourced NASA-feature-to-comparison rule incomplete',
         'No end-to-end product execution, trained model validation, farmer test or hardware calibration in this audit'],
         'script_sha256':sha(Path(__file__))}
    OUT.write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'markdown_files':len(mds),'local_links':n,'upstream_snapshot_link_warnings':len(missing),'raw_hashes':16,'soil_model_values':15,'current_pdf_pages':len(reader.pages),'snapshot_pdfs':3,'zip':'pass','integrity_result':'PASS with explicit upstream-link warnings; readiness remains partial'}))

if __name__=='__main__':main()
