"""Trace a visible cultivation block, not a homogeneous soil or cadastral parcel.

Native Windows/Python 3.12/Pillow; cached imagery and soil rasters only.
Pixel vertices are analyst annotations reviewed against the source image.
"""
import csv
import hashlib
import json
import math
from pathlib import Path
from xml.etree.ElementTree import Element, SubElement, ElementTree, register_namespace
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parents[2]
CASE=ROOT/'nasa-space-apps-2026/planning/cases/my-thanh-cai-lay'
DATA=ROOT/'nasa-space-apps-2026/sources/data-audits/my-thanh-cai-lay-2026-11-12'
PIXELS=[(699,54),(913,130),(850,299),(844,316),(626,241),(638,211),(660,155),(680,101)]

def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,obj):p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def font(n,b=False):return ImageFont.truetype('C:/Windows/Fonts/'+('arialbd.ttf' if b else 'arial.ttf'),n)
def inside(pt,ring):
    x,y=pt;ok=False
    for (a,b),(c,d) in zip(ring,ring[1:]):
        if (b>y)!=(d>y) and x<(c-a)*(y-b)/(d-b)+a:ok=not ok
    return ok

def main():
    src=DATA/'imagery/my-thanh-close.png';raw=Image.open(src).convert('RGB')
    meta=read(DATA/'imagery/my-thanh-close-export.json');e=meta['extent']
    assert raw.size==(meta['width'],meta['height']) and e['spatialReference']['wkid']==4326
    def geo(x,y):return [e['xmin']+x/raw.width*(e['xmax']-e['xmin']),e['ymax']-y/raw.height*(e['ymax']-e['ymin'])]
    coords=[geo(x,y) for x,y in PIXELS];coords.append(coords[0])
    a2=sum(a*d-c*b for (a,b),(c,d) in zip(PIXELS,PIXELS[1:]+PIXELS[:1]))
    cx=sum((a+c)*(a*d-c*b) for (a,b),(c,d) in zip(PIXELS,PIXELS[1:]+PIXELS[:1]))/(3*a2)
    cy=sum((b+d)*(a*d-c*b) for (a,b),(c,d) in zip(PIXELS,PIXELS[1:]+PIXELS[:1]))/(3*a2)
    center=geo(cx,cy)
    if a2>0:coords=list(reversed(coords)) # geo latitude flips pixel y; RFC7946 outer ring CCW
    sx=math.radians((e['xmax']-e['xmin'])/raw.width)*6371008.8*math.cos(math.radians(center[1]))
    sy=math.radians((e['ymax']-e['ymin'])/raw.height)*6371008.8
    area=abs(a2)/2*sx*sy/10000
    commune=read(CASE/'aoi.geojson')['features'][0]['geometry']['coordinates']
    for a,b in zip(coords,coords[1:]):
        for i in range(21):
            q=[a[k]+(b[k]-a[k])*i/20 for k in range(2)]
            assert any(inside(q,poly[0]) and not any(inside(q,h) for h in poly[1:]) for poly in commune)
    props={'id':'MT-BLOCK-01','status':'analyst_digitised_visible_cultivation_block_not_verified_farm',
           'area_ha_approx':round(area,3),'center_lon_lat':center,'crs':'EPSG:4326',
           'homogeneous_soil_verified':False,'current_crop_verified':False,'rotation_verified':False,
           'may_contain_multiple_subplots':True,'legal_boundary':False,'source_image_date_metadata':'2025-08-07',
           'date_scope':'source citation footprint; not current 2026 field survey',
           'edge_interpretation':'visible outer cultivation edges next to tree strips and bunds; no land title or farm ownership inferred'}
    write(CASE/'study-block.geojson',{'type':'FeatureCollection','features':[{'type':'Feature','properties':props,'geometry':{'type':'Polygon','coordinates':[coords]}}]})
    with (CASE/'study-block-coordinates.csv').open('w',encoding='utf-8',newline='') as f:
        w=csv.writer(f);w.writerow(['point','source_pixel_x','source_pixel_y','longitude','latitude','role'])
        for i,(x,y) in enumerate(PIXELS):w.writerow([chr(65+i),x,y,*geo(x,y),'visible_edge_vertex_approximate'])
        w.writerow(['centroid',cx,cy,*center,'analysis_point_not_soil_sample'])
    ns='http://www.opengis.net/kml/2.2';register_namespace('',ns)
    k=Element(f'{{{ns}}}kml');doc=SubElement(k,'Document');pm=SubElement(doc,'Placemark')
    SubElement(pm,'name').text='MT-BLOCK-01 - visible cultivation block, not verified parcel'
    style=SubElement(pm,'Style');ls=SubElement(style,'LineStyle');SubElement(ls,'color').text='ff4de3ff';SubElement(ls,'width').text='3'
    ps=SubElement(style,'PolyStyle');SubElement(ps,'fill').text='0'
    pg=SubElement(pm,'Polygon');bd=SubElement(pg,'outerBoundaryIs');lr=SubElement(bd,'LinearRing');SubElement(lr,'coordinates').text=' '.join(f'{x},{y},0' for x,y in coords)
    ElementTree(k).write(CASE/'study-block.kml',encoding='utf-8',xml_declaration=True)
    soil=[]
    for p in sorted((DATA/'soilgrids').glob('*.tif')):
        im=Image.open(p);sc=im.tag_v2[33550];tie=im.tag_v2[33922];keys=im.tag_v2[34735]
        geo_keys={keys[i]:keys[i+3] for i in range(4,len(keys),4)}
        assert geo_keys[2048]==4326 and geo_keys[1025]==1
        col=math.floor((center[0]-tie[3])/sc[0]);row=math.floor((tie[4]-center[1])/sc[1])
        assert 0<=col<im.width and 0<=row<im.height
        v=im.getpixel((col,row));prop,depth,stat=p.stem.split('_',2)
        valid=0<v<=(140 if prop=='phh2o' else 1000)
        soil.append({'property':prop,'depth':depth,'statistic':stat,'raw_integer':v,'value':v/10 if valid else None,
                     'unit':'pH_H2O' if prop=='phh2o' else 'percent_mass','returned_grid_col_row':[col,row],
                     'source_file':p.relative_to(DATA).as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
    write(CASE/'study-block-soil-model.json',{'point_lon_lat':center,'scope':'model cell at block centroid, not sampled soil or block average',
        'native_support_m':250,'resampling_algorithm_not_verified':True,'values':soil,'EC_or_local_samples_available':False})
    with (CASE/'study-block-soil-model.csv').open('w',encoding='utf-8',newline='') as f:
        fields=['property','depth','statistic','raw_integer','value','unit','source_file','sha256']
        w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(soil)
    annotated=raw.copy();d=ImageDraw.Draw(annotated);d.line(PIXELS+[PIXELS[0]],fill='#ffe34d',width=2)
    def map_page(detail):
        box=(580,20,950,355) if detail else (0,0,1500,1120)
        im=annotated.crop(box);iw=1100;ih=round(im.height*iw/im.width);im=im.resize((iw,ih),Image.Resampling.LANCZOS)
        page=Image.new('RGB',(1540,ih+205),'#f4f6fa');dr=ImageDraw.Draw(page)
        dr.rectangle((0,0,1540,105),fill='#192a43');dr.text((22,15),'NEURAX / AGROTWIN',font=font(22,True),fill='#40b89e')
        dr.text((22,50),'MT-BLOCK-01 / KHỐI CANH TÁC SỐ HÓA THEO ẢNH',font=font(26,True),fill='white')
        page.paste(im,(20,125));y=145
        lines=['VIỀN VÀNG MẢNH','Bám cạnh canh tác nhìn thấy.','Không dùng hình thoi 17 ha.',f'Diện tích xấp xỉ: {area:.2f} ha','Có thể có nhiều ô nhỏ.','','CHƯA XÁC MINH','Ranh thửa / chủ đất','Đất đồng nhất / EC','Cây cụ thể / lịch luân canh','','TÂM PHÂN TÍCH',f'{center[1]:.7f} N',f'{center[0]:.7f} E','Không phải điểm lấy mẫu đất.','','Ảnh nguồn theo metadata:','07/08/2025; chưa là hiện trạng','được kiểm tại ruộng năm 2026.']
        for s in lines:
            dr.text((1140,y),s,font=font(20,s in ['VIỀN VÀNG MẢNH','CHƯA XÁC MINH','TÂM PHÂN TÍCH']),fill='#192a43');y+=33
        dr.text((22,ih+145),'Ảnh: Esri, Vantor, Earthstar Geographics, and the GIS User Community. EPSG:4326; ranh do NeuraX số hóa.',font=font(17),fill='#23364f')
        dr.text((22,ih+174),'Đường vẽ không che tô mặt ruộng. Phóng ảnh không tăng độ chính xác; chưa có kiểm chứng ranh độc lập.',font=font(17),fill='#23364f')
        page.save(CASE/'maps'/('my-thanh-study-block-detail.png' if detail else 'my-thanh-study-block-context.png'))
    map_page(False);map_page(True)
    write(CASE/'study-block-manifest.json',{'review_date':'2026-11-12','properties':props,'source_pixel_vertices':PIXELS,
        'source_image_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'georeferencing_export':str((DATA/'imagery/my-thanh-close-export.json').relative_to(ROOT)).replace('\\','/'),
        'inside_source_commune_check':'all vertices and 21 samples per edge pass point-in-polygon',
        'accuracy':'not independently measured; source citation nominal accuracy is not an error bound for this trace',
        'area_method':'local spherical equirectangular approximation, not cadastral area',
        'weather_role':'existing POWER point is nearby regional context, not this block centroid; no new weather observation',
        'soil_role':'centroid resampled from cached coverage separately; do not copy old point values as measured block properties',
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()})
    print(json.dumps({'block_id':'MT-BLOCK-01','area_ha_approx':round(area,3),'center_lon_lat':center,'soil_model_cells':len(soil),'scope':'visible cultivation block only'}))

if __name__=='__main__':main()
