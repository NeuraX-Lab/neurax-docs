"""Primary AOI from the publisher's administrative geometry, not a guessed field.

Cached inputs only; Windows Python3.12 and Pillow. Does not establish crop cover,
soil uniformity, cadastral rights or production suitability of the commune.
"""
import csv
import hashlib
import json
from pathlib import Path
from xml.etree.ElementTree import Element, SubElement, ElementTree, register_namespace
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parents[2]
CASE=ROOT/"nasa-space-apps-2026/planning/cases/my-thanh-cai-lay"
INPUT=ROOT/"nasa-space-apps-2026/sources/data-audits/my-thanh-cai-lay-2026-11-12/imagery"


def read(p):return json.loads(p.read_text(encoding="utf-8-sig"))
def write(p,j):p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
def font(n,b=False):return ImageFont.truetype("C:/Windows/Fonts/"+("arialbd.ttf" if b else "arial.ttf"),n)


def clean(ring):
    out=[]
    for p in ring:
        if not out or p!=out[-1]:out.append(p)
    if out[0]!=out[-1]:out.append(out[0])
    return out


def main():
    original=read(INPUT/"official-my-thanh-geometry.json")
    feature=original["features"][0]
    assert feature["properties"]["a03_ten"]=="Xã Mỹ Thành"
    geometry={"type":"MultiPolygon","coordinates":[[clean(r) for r in poly] for poly in feature["geometry"]["coordinates"]]}
    reference=read(INPUT/"my-thanh-boundary.geojson")["features"][0]["geometry"]
    assert geometry["coordinates"]==[[clean(r) for r in p] for p in reference["coordinates"]]
    points=[v for p in geometry["coordinates"] for r in p for v in r]
    bbox=[min(p[0] for p in points),min(p[1] for p in points),max(p[0] for p in points),max(p[1] for p in points)]
    assert all(105<x<107 and 10<y<11 for x,y in points)
    props={"name":"Mỹ Thành commune / AOI-MT-ADMIN-v1","status":"source_defined_commune_AOI_for_remote_research_not_crop_suitability",
           "source":"https://sapnhap.bando.com.vn","source_object_id":"diaphanhanhchinhcapxa_2025.464",
           "source_area_km2":float(feature["properties"]["a07_dt"]),"aoi_role":"administrative_research_extent_not_a_farm",
           "current_cropland_mask_available":False,"same_soil_or_rotation_everywhere":False,"field_boundary_validated":False}
    write(CASE/"aoi.geojson",{"type":"FeatureCollection","bbox":bbox,"features":[{"type":"Feature","id":"AOI-MT-ADMIN-v1","properties":props,"geometry":geometry}]})
    with (CASE/"coordinates.csv").open("w",encoding="utf-8",newline="") as f:
        w=csv.writer(f);w.writerow(["polygon","ring","vertex","longitude_deg","latitude_deg","crs"])
        for pi,poly in enumerate(geometry["coordinates"]):
            for ri,ring in enumerate(poly):
                for vi,(lon,lat) in enumerate(ring):w.writerow([pi,ri,vi,lon,lat,"EPSG:4326"])
    ns="http://www.opengis.net/kml/2.2";register_namespace("",ns)
    k=Element(f"{{{ns}}}kml");doc=SubElement(k,"Document");style=SubElement(doc,"Style",id="boundary")
    ls=SubElement(style,"LineStyle");SubElement(ls,"color").text="ff4de3ff";SubElement(ls,"width").text="4"
    ps=SubElement(style,"PolyStyle");SubElement(ps,"fill").text="0"
    pm=SubElement(doc,"Placemark");SubElement(pm,"name").text="My Thanh commune - source boundary, not farm";SubElement(pm,"styleUrl").text="#boundary"
    mg=SubElement(pm,"MultiGeometry")
    for poly in geometry["coordinates"]:
        pg=SubElement(mg,"Polygon")
        for i,ring in enumerate(poly):
            boundary=SubElement(pg,"outerBoundaryIs" if i==0 else "innerBoundaryIs");lr=SubElement(boundary,"LinearRing")
            SubElement(lr,"coordinates").text=" ".join(f"{x},{y},0" for x,y in ring)
    ElementTree(k).write(CASE/"aoi.kml",encoding="utf-8",xml_declaration=True)
    meta=read(INPUT/"admin-map-export.json");e=meta["extent"];assert e["spatialReference"]["wkid"]==4326
    raw=Image.open(INPUT/"admin-satellite-raw.png").convert("RGB");assert raw.size==(meta["width"],meta["height"])
    def project(pt):return ((pt[0]-e["xmin"])/(e["xmax"]-e["xmin"])*raw.width,(e["ymax"]-pt[1])/(e["ymax"]-e["ymin"])*raw.height)
    d=ImageDraw.Draw(raw)
    for poly in geometry["coordinates"]:
        for ring in poly:
            pix=[project(pt) for pt in ring];d.line(pix,fill="black",width=8);d.line(pix,fill="#ffe34d",width=4)
    point=project((106.02154675,10.4770865));d.ellipse((point[0]-7,point[1]-7,point[0]+7,point[1]+7),fill="cyan",outline="black",width=2)
    page=Image.new("RGB",(1450,1620),"#f4f6fa");p=ImageDraw.Draw(page);p.rectangle((0,0,1450,115),fill="#16243d")
    p.text((25,18),"NEURAX / AGROTWIN",font=font(22,True),fill="#ffe34d")
    p.text((25,56),"MỸ THÀNH - RANH NGHIÊN CỨU CẤP XÃ CÓ NGUỒN",font=font(27,True),fill="white")
    page.paste(raw,(20,135));y=155
    for line in ["AOI-MT-ADMIN-v1","Xã Mỹ Thành, Đồng Tháp","Diện tích theo nguồn: 52,3 km²","","VIỀN VÀNG","Ranh từ bản đồ NXB","Tài nguyên - Môi trường","và Bản đồ Việt Nam","","Đã đối chiếu geometry","với bản sao tham khảo.","Không phải ranh ruộng.","","CHẤM XANH","Điểm lấy POWER/SoilGrids","10.4770865 N","106.02154675 E","Không là điểm khảo sát.","","Cần mask ruộng / vườn /","nước / dân cư khi phân tích.","Chưa có mask cây hằng năm","được xác minh toàn xã."]:
        p.text((1040,y),line,font=font(20 if len(line)<31 else 18,line in ["AOI-MT-ADMIN-v1","VIỀN VÀNG","CHẤM XANH"]),fill="#16243d");y+=37
    p.text((25,1550),"Ảnh nền: Esri, Vantor, Earthstar Geographics, and the GIS User Community; mosaic, ngày tùy tile.",font=font(17),fill="#16243d")
    p.text((25,1578),"Ranh nguồn bản đồ hành chính không xác nhận điều kiện đất, cây trồng, quyền đất hoặc phù hợp sản xuất.",font=font(17),fill="#16243d")
    page.save(CASE/"maps/my-thanh-commune-aoi.png")
    write(CASE/"aoi-manifest.json",{"aoi_id":"AOI-MT-ADMIN-v1","review_date":"2026-11-12","properties":props,"bbox":bbox,
        "primary_request":{"url":"https://sapnhap.bando.com.vn/pread_json","method":"POST","form":{"id":"diaphanhanhchinhcapxa_2025.464"}},
        "primary_geometry_sha256":hashlib.sha256((INPUT/"official-my-thanh-geometry.json").read_bytes()).hexdigest(),
        "geometry_matches_reference_after_removing_duplicate_vertices":True,
        "reference_independence":"reference is a copy derived from same publisher, not independent field validation",
        "provider_application_geojson_data_projection":"EPSG:4326, verified in public application code",
        "normalization":"removed only consecutive duplicate closing vertex; no invented corners or simplification; rebuilt bbox for selected feature",
        "legacy_manual_polygon":"illustrative-aoi.geojson, not validated field boundary and no longer primary AOI",
        "soil_weather_spatial_scope":"existing point samples; not an observed or aggregate soil census of whole commune",
        "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()})
    print("Built source-defined commune AOI; geometry matches primary and reference after duplicate-vertex normalization")


if __name__=="__main__":main()
