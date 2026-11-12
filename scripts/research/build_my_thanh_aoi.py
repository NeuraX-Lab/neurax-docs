"""Build factual GIS maps, GeoJSON/KML and QA from cached public imagery.

Windows Python 3.12 + Pillow. No network, AI image generation or GIS install.
Coordinates were digitised as a research AOI, not a cadastral boundary.
"""
import csv
import hashlib
import json
import math
from collections import Counter
from pathlib import Path
from xml.etree.ElementTree import Element, SubElement, ElementTree, register_namespace

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[2]
CASE = ROOT / "nasa-space-apps-2026/planning/cases/my-thanh-cai-lay"
DATA = ROOT / "nasa-space-apps-2026/sources/data-audits/my-thanh-cai-lay-2026-11-12"
INPUT = DATA / "imagery"
MAPS = CASE / "maps"
# A west, B north, C east, D south. Geometry is reversed to counterclockwise.
POINTS = [(106.018467, 10.476940), (106.021400, 10.479360),
          (106.024627, 10.477233), (106.021693, 10.474813)]
RING = [POINTS[i] for i in [0, 3, 2, 1, 0]]
CENTER = [sum(x for x, y in POINTS) / 4, sum(y for x, y in POINTS) / 4]
NAVY = "#16243d"
TEAL = "#087f8c"
YELLOW = "#ffe34d"


def read(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write(path, doc):
    path.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def font(size, bold=False):
    return ImageFont.truetype("C:/Windows/Fonts/" + ("arialbd.ttf" if bold else "arial.ttf"), size)


def inside(point, ring):
    x, y = point; result = False
    for a, b in zip(ring, ring[1:]):
        if (a[1] > y) != (b[1] > y) and x < (b[0] - a[0]) * (y - a[1]) / (b[1] - a[1]) + a[0]:
            result = not result
    return result


def project(point, extent, width, height):
    x, y = point
    return ((x - extent[0]) / (extent[2] - extent[0]) * width,
            (extent[3] - y) / (extent[3] - extent[1]) * height)


def draw_aoi(im, extent, labels=True, width=5):
    im = im.convert("RGB"); draw = ImageDraw.Draw(im)
    pts = [project(pt, extent, im.width, im.height) for pt in RING]
    draw.line(pts, fill="black", width=width + 4, joint="curve")
    draw.line(pts, fill=YELLOW, width=width, joint="curve")
    cx, cy = project(CENTER, extent, im.width, im.height)
    draw.ellipse((cx-6, cy-6, cx+6, cy+6), fill="white", outline="black", width=2)
    if labels:
        for name, point in zip("ABCD", POINTS):
            x, y = project(point, extent, im.width, im.height)
            draw.ellipse((x-18, y-18, x+18, y+18), fill=NAVY, outline=YELLOW, width=3)
            draw.text((x, y), name, font=font(20, True), fill="white", anchor="mm")
    return im


def map_page(image_name, metadata_name, output_name, title, caption):
    meta = read(INPUT / metadata_name)
    e = meta["extent"]; assert e["spatialReference"]["wkid"] == 4326
    extent = [e["xmin"], e["ymin"], e["xmax"], e["ymax"]]
    raw = Image.open(INPUT / image_name)
    assert raw.size == (meta["width"], meta["height"])
    map_width = 1320
    map_height = round(raw.height * map_width / raw.width)
    map_image = draw_aoi(raw.resize((map_width, map_height), Image.Resampling.LANCZOS), extent)
    page = Image.new("RGB", (1740, map_height + 260), "#f4f6fa")
    d = ImageDraw.Draw(page)
    d.rectangle((0, 0, page.width, 125), fill=NAVY)
    d.text((36, 24), "NEURAX  /  AGROTWIN", fill=YELLOW, font=font(22, True))
    d.text((36, 61), title, fill="white", font=font(30, True))
    page.paste(map_image, (24, 145))
    sx = 1370; y = 154
    for line, size, bold in [
        ("AOI-MT-01", 26, True), ("Mẫu thủ công chưa duyệt", 20, True),
        ("Xã Mỹ Thành, Đồng Tháp", 19, False), ("Cụm nông nghiệp Cai Lậy", 19, False),
        ("Diện tích xấp xỉ: 17,1 ha", 20, True), ("WGS84 / EPSG:4326", 19, False),
        ("Tâm vùng:", 20, True), (f"{CENTER[1]:.6f} N", 22, False), (f"{CENTER[0]:.6f} E", 22, False),
        ("Ảnh nền: 07/08/2025*", 19, True), ("Viền vàng: ranh mẫu tự chọn", 18, False),
        ("Không phải ranh địa chính", 18, False), ("Không phải thửa thí nghiệm cũ", 18, False),
        ("Không dùng như ranh ruộng", 18, False), ("AOI chính: ranh xã có nguồn", 18, False),
    ]:
        d.text((sx, y), line, font=font(size, bold), fill=NAVY); y += 37 if bold else 30
    y += 15
    for name, (lon, lat) in zip("ABCD", POINTS):
        d.text((sx, y), f"{name}  {lat:.6f} N", font=font(18, True), fill=TEAL)
        d.text((sx+25, y+25), f"{lon:.6f} E", font=font(18), fill=NAVY); y += 65
    # North and scale are georeferenced to the returned EPSG:4326 extent.
    md = ImageDraw.Draw(page); x0, y0 = 100, 145 + map_height - 65
    metres_per_pixel_x = 6371008.8 * math.cos(math.radians(CENTER[1])) * math.radians(extent[2] - extent[0]) / map_width
    bar_m = 200 if "close" in image_name else 500
    bar_px = bar_m / metres_per_pixel_x
    md.rectangle((x0-12, y0-25, x0+bar_px+20, y0+30), fill="white")
    md.line((x0, y0, x0+bar_px, y0), fill=NAVY, width=6)
    md.text((x0, y0+6), f"{bar_m} m (xấp xỉ)", font=font(16), fill=NAVY)
    nx, ny = 24+map_width-45, 185
    md.line((nx, ny+65, nx, ny+10), fill=YELLOW, width=5)
    md.polygon([(nx,ny),(nx-10,ny+20),(nx+10,ny+20)], fill=YELLOW)
    md.text((nx,ny-15), "N", font=font(19,True), fill="white", anchor="mm")
    footer = 145 + map_height + 18
    for line in [caption, "Source: Esri, Vantor, Earthstar Geographics, and the GIS User Community.",
                 "*Ngày nguồn từ citation layer giao AOI. Ranh do NeuraX chọn; tọa độ không là độ chính xác đo đạc."]:
        md.text((30, footer), line, font=font(17), fill=NAVY); footer += 26
    page.save(MAPS / output_name)


def main():
    MAPS.mkdir(parents=True, exist_ok=True)
    boundaries = read(INPUT / "my-thanh-boundary.geojson")
    polygons = boundaries["features"][0]["geometry"]["coordinates"]
    def in_commune(pt):
        return any(inside(pt, poly[0]) and not any(inside(pt, h) for h in poly[1:]) for poly in polygons)
    for a, b in zip(RING, RING[1:]):
        assert all(in_commune((a[0]+(b[0]-a[0])*i/20, a[1]+(b[1]-a[1])*i/20)) for i in range(21))
    assert inside(CENTER, RING)
    # Approximate local equal-distance area; explicitly not a cadastral measurement.
    r = 6371008.8
    xy = [(r*math.cos(math.radians(CENTER[1]))*math.radians(x),r*math.radians(y)) for x,y in RING]
    area_ha = abs(sum(a[0]*b[1]-b[0]*a[1] for a,b in zip(xy,xy[1:]))) / 2 / 10000
    feature = {"type":"Feature", "id":"AOI-MT-01", "properties":{
        "name":"NeuraX Mỹ Thành / Cai Lậy remote-analysis AOI", "status":"illustrative_sample_not_validated_field",
        "selection_date":"2026-11-12", "area_ha_approx":round(area_ha,2),
        "boundary_role":"analyst_digitised_research_area_not_cadastral_or_historical_trial_plot",
        "current_commune":"Mỹ Thành, Đồng Tháp", "commune_code_reference":"28456",
        "field_survey_required_for_agreed_prototype_scope":False, "farm_advice_validated":False,
        "center_lon":CENTER[0], "center_lat":CENTER[1], "coordinates_precision_is_not_accuracy":True,
        "methods":"high-resolution imagery inspection; recent S2/SCL; reference commune containment"},
        "geometry":{"type":"Polygon", "coordinates":[RING]}}
    write(CASE / "illustrative-aoi.geojson", {"type":"FeatureCollection", "features":[feature]})
    with (CASE / "illustrative-coordinates.csv").open("w",encoding="utf-8",newline="") as f:
        w=csv.writer(f);w.writerow(["point","latitude_deg","longitude_deg","crs"])
        for name,(lon,lat) in list(zip("ABCD",POINTS))+[("CENTER",CENTER)]:
            w.writerow([name,f"{lat:.8f}",f"{lon:.8f}","EPSG:4326"])
    ns="http://www.opengis.net/kml/2.2";register_namespace("",ns)
    kml=Element(f"{{{ns}}}kml");doc=SubElement(kml,"Document")
    style=SubElement(doc,"Style",id="aoi");ls=SubElement(style,"LineStyle");SubElement(ls,"color").text="ff4de3ff";SubElement(ls,"width").text="4"
    ps=SubElement(style,"PolyStyle");SubElement(ps,"fill").text="0"
    pm=SubElement(doc,"Placemark");SubElement(pm,"name").text="AOI-MT-01 - research boundary, not cadastral"
    SubElement(pm,"styleUrl").text="#aoi";poly=SubElement(pm,"Polygon");outer=SubElement(poly,"outerBoundaryIs");lr=SubElement(outer,"LinearRing")
    SubElement(lr,"coordinates").text=" ".join(f"{x},{y},0" for x,y in RING)
    pm=SubElement(doc,"Placemark");SubElement(pm,"name").text="AOI-MT-01 center";pt=SubElement(pm,"Point");SubElement(pt,"coordinates").text=f"{CENTER[0]},{CENTER[1]},0"
    ElementTree(kml).write(CASE/"illustrative-aoi.kml",encoding="utf-8",xml_declaration=True)

    map_page("my-thanh-detail.png","my-thanh-detail-export.json","my-thanh-aoi-overview.png",
             "MỸ THÀNH - MẪU THỦ CÔNG CHƯA DUYỆT", "Ranh mẫu tự chọn, không bám ranh thửa đã xác minh; chỉ giữ để audit.")
    map_page("my-thanh-close.png","my-thanh-close-export.json","my-thanh-aoi-detail.png",
             "MẪU CŨ - CHƯA XÁC MINH RANH RUỘNG", "Ranh phân tích vẽ trên ảnh thực; không xác nhận chủ đất, cây cụ thể hoặc lịch luân canh tại thửa.")

    qa=[];scene_doc=read(INPUT/"pc-scenes.json")
    comparison=Image.new("RGB",(1660,930),"#f4f6fa");cd=ImageDraw.Draw(comparison)
    cd.rectangle((0,0,1660,110),fill=NAVY)
    cd.text((28,22),"NEURAX  /  AOI-MT-01",font=font(22,True),fill=YELLOW)
    cd.text((28,58),"SENTINEL-2 - HAI THỜI ĐIỂM CÙNG VÙNG",font=font(28,True),fill="white")
    for idx,date in enumerate(["2026-03-25","2026-11-05"]):
        render=read(INPUT/f"render-{date}.json");scene=next(f for f in scene_doc["features"] if f["id"]==render["id"])
        scl=Image.open(INPUT/f"scl-{date}.tif")
        assert scl.mode in ("L","LA")
        sx,sy,_=scl.tag_v2[33550];tie=scl.tag_v2[33922]
        ext=[tie[3],tie[4]-sy*scl.height,tie[3]+sx*scl.width,tie[4]]
        geo=scl.tag_v2[34735];keys={geo[i]:geo[i+3] for i in range(4,len(geo),4)};assert keys[2048]==4326
        counts=Counter();nodata=0
        for y in range(scl.height):
            for x in range(scl.width):
                ll=(tie[3]+(x+.5)*sx,tie[4]-(y+.5)*sy)
                if not inside(ll,RING):continue
                value=scl.getpixel((x,y));value,alpha=value if isinstance(value,tuple) else (value,255)
                if not alpha or value==0:nodata+=1
                else:counts[value]+=1
        total=sum(counts.values())+nodata;assert total>0
        cloud=sum(counts.get(c,0) for c in [8,9,10]);shadow=counts.get(3,0)
        qa.append({"scene_id":scene["id"],"datetime_utc":scene["properties"]["datetime"],
                   "tile_cloud_percent":scene["properties"].get("eo:cloud_cover"),"processing_baseline":scene["properties"].get("s2:processing_baseline"),
                   "SCL_pixel_centers_inside_AOI":total,"class_counts":dict(counts),"nodata":nodata,
                   "cloud_flag_percent_AOI_sample":round(cloud/total*100,2),"cloud_shadow_percent_AOI_sample":round(shadow/total*100,2),
                   "method":"pixel-center mask on categorical nearest-reprojected ~20m SCL; diagnostic not ground truth"})
        rgb=Image.open(INPUT/f"sentinel-{date}.png").convert("RGB")
        im=draw_aoi(rgb.resize((780,650),Image.Resampling.NEAREST),ext,labels=False,width=4)
        xx=30+idx*820;comparison.paste(im,(xx,175))
        cd.text((xx,129),date+" | Sentinel-2 L2A",font=font(25,True),fill=NAVY)
        cd.text((xx,837),f"SCL mây trong AOI: {qa[-1]['cloud_flag_percent_AOI_sample']}% | bóng mây: {qa[-1]['cloud_shadow_percent_AOI_sample']}%",font=font(19),fill=NAVY)
    cd.text((30,881),"Contains modified Copernicus Sentinel data (2026), via Microsoft Planetary Computer. RGB gốc 10m; SCL 20m.",font=font(18),fill=NAVY)
    cd.text((30,906),"Viền vàng là AOI nghiên cứu. RGB đã dựng màu; không phải reflectance/NDVI hoặc bằng chứng cây trồng cụ thể.",font=font(17),fill=NAVY)
    comparison.save(MAPS/"my-thanh-sentinel2-comparison.png")
    citation=read(INPUT/"aoi-imagery-citation.json")
    assert all(f["attributes"]["SRC_DATE"]==20250807 for f in citation["features"])
    files=[{"file":p.relative_to(DATA).as_posix(),"bytes":p.stat().st_size,"sha256":hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(INPUT.iterdir()) if p.is_file()]
    write(CASE/"illustrative-aoi-manifest.json",{
        "aoi_id":"AOI-MT-01","status":"illustrative_sample_not_validated_field","review_date":"2026-11-12",
        "center_lon_lat":CENTER,"area_ha_approx":round(area_ha,2),"area_method":"local spherical equirectangular approximation, not cadastral measurement",
        "boundary_source_role":"third-party WGS84 commune reference, not official survey boundary",
        "boundary_source_commit":(INPUT/"boundary-source-commit.txt").read_text().strip(),
        "boundary_source_url":"https://github.com/ThangLeQuoc/vietnamese-provinces-database/blob/master/json/geojson/82_dong_thap/wards/28456_my_thanh.geojson",
        "boundary_method":"manually digitised analytical polygon; all vertices and 21 samples per edge inside reference commune",
        "esri_imagery_citation_attributes":[f["attributes"] for f in citation["features"]],
        "esri_attribution":read(INPUT/"esri-world-imagery-service.json")["copyrightText"],
        "sentinel_scene_quality":qa,"imagery_inputs":files,
        "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "field_survey_in_scope":False,"historical_trial_plot_identified":False,"specific_crop_or_current_rotation_verified":False,
        "decision_scope":"Manual sample retained for audit only; independently sourced commune boundary is primary AOI",
        "soil_weather_summary_path":"../../../sources/data-audits/my-thanh-cai-lay-2026-11-12/summary.json"})
    print(json.dumps({"AOI":"AOI-MT-01","area_ha_approx":round(area_ha,2),"center_lon_lat":CENTER,"SCL_QA":qa},ensure_ascii=False))


if __name__=="__main__":
    main()
