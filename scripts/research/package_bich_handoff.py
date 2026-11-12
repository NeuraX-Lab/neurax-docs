"""Package the current research dossier and GIS handoff, excluding superseded AOIs."""
import hashlib
import json
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

ROOT=Path(__file__).resolve().parents[2]
CASE=ROOT/'nasa-space-apps-2026/planning/cases/my-thanh-cai-lay'
OUT=ROOT/'output/handoff/NeuraX-MyThanh-Bich-Research-Pack-2026-11-12.zip'
PDF=ROOT/'output/pdf/NeuraX-AgroTwin-Site-and-Demo-Dossier-Bich.pdf'

README='''NEURAX / AGROTWIN - BÀN GIAO NGHIÊN CỨU CHO BÍCH
12/11/2026 - bản 1.3

1. Mở PDF 13 trang tại thư mục gốc trước (có trang bìa).
   Mục 7-10 có bảng đất-nước-cây-mùa; mục 11 có vai trò sáu người.
   Điền research/rotation-evidence-review.csv (12 hàng), giữ nguyên phần
   evidence đã có, bổ sung nguồn và review vào các cột trống.
2. Mở gis/study-block.kml bằng Google Earth để xem khối canh tác minh họa
   MT-BLOCK-01 (~2 ha), tâm 10.4790981 N, 106.0216210 E.
   CSV tọa độ có cả pixel nguồn; GeoJSON/KML dùng longitude trước latitude.
3. gis/aoi.* là RANH XÃ Mỹ Thành có nguồn (52,3 km² thuộc tính nguồn).
   Không dùng toàn xã làm một ruộng. Hình thoi 17 ha cũ KHÔNG có trong pack.
4. research/ có bản Markdown, bản đồ và JSON/CSV SoilGrids tại tâm block mới.
   Đây là DỰ ĐOÁN MÔ HÌNH, không phải mẫu đất, không có EC hoặc ground truth.
5. research/satellite-source/ giữ ảnh xuất và extent để đối chiếu đường vẽ.
   Viền được số hóa thủ công theo mép canh tác thấy được, có thể chứa nhiều ô;
   chưa là ranh thửa pháp lý, đất đồng nhất hoặc lịch luân canh được xác minh.
   Ngày metadata ảnh nguồn 07/08/2025; chưa kiểm hiện trạng ruộng năm 2026.
6. Demo dùng đất/giá thể có ghi nguồn tại HCM; không cần lấy đất Mỹ Thành.
   Số đo lab không đại diện số đo ngoài đồng. Thiếu hiệu chuẩn VWC thì chỉ
   dùng chỉ số độ ẩm tương đối. Chờ datasheet HTTPSLAB để kiểm tích hợp.

Ảnh: Esri, Vantor, Earthstar Geographics, and the GIS User Community.
Giữ attribution khi chia sẻ ảnh. Không gọi imagery này là dữ liệu NASA
hoặc gộp quyền sử dụng với license SoilGrids. Ranh xã: bản đồ của NXB
Tài nguyên - Môi trường và Bản đồ Việt Nam. SoilGrids: ISRIC, CC-BY-4.0.
Nguồn, giới hạn và link nghiên cứu ở trang 9 PDF. Pack là tài liệu đọc và GIS,
không phải toàn bộ raw NASA/SoilGrids hay môi trường tái lập repo.
Chưa có khảo sát thực địa, đo thiết bị hoặc khuyến cáo sản xuất đã kiểm chứng.
'''

def main():
    files=[(PDF,PDF.name),(CASE/'rotation-evidence-for-bich.md','research/rotation-evidence-for-bich.md'),
           (CASE/'rotation-evidence-review.csv','research/rotation-evidence-review.csv'),
           (ROOT/'nasa-space-apps-2026/planning/my-thanh-team-roles-2026-11-12.md','research/team-roles.md'),
           (ROOT/'team/team-profile.md','research/team-profile-reference.md')]
    for n in ['aoi.geojson','aoi.kml','coordinates.csv','aoi-manifest.json','study-block.geojson','study-block.kml','study-block-coordinates.csv','study-block-manifest.json']:
        files.append((CASE/n,'gis/'+n))
    for n in ['study-block-soil-model.json','study-block-soil-model.csv','review-source-record.json']:
        files.append((CASE/n,'research/'+n))
    for n in ['my-thanh-commune-aoi.png','my-thanh-study-block-detail.png','my-thanh-study-block-context.png']:
        files.append((CASE/'maps'/n,'research/maps/'+n))
    data=ROOT/'nasa-space-apps-2026/sources/data-audits/my-thanh-cai-lay-2026-11-12/imagery'
    for n in ['my-thanh-close.png','my-thanh-close-export.json','aoi-imagery-citation.json','official-my-thanh-geometry.json']:
        files.append((data/n,'research/satellite-source/'+n))
    def expand(p):
        import re
        lines=[]
        for line in p.read_text(encoding='utf-8-sig').splitlines():
            m=re.fullmatch(r'<!-- INCLUDE:(.+) -->',line.strip())
            lines.append(expand((p.parent/m[1]).resolve()) if m else line)
        return '\n'.join(lines)
    content={n:p.read_bytes() for p,n in files}
    content['research/dossier.md']=expand(CASE/'bich-site-and-demo-dossier.md').replace('../../team/team-profile.md','team-profile-reference.md').encode('utf-8')
    content['research/team-roles.md']=content['research/team-roles.md'].decode('utf-8').replace('../../team/team-profile.md','team-profile-reference.md').encode('utf-8')
    # Imported profile links refer to the full repo; make this portable reading pack honest.
    import re
    profile=content['research/team-profile-reference.md'].decode('utf-8-sig')
    def profile_link(m):
        label,target=m.groups()
        if target.startswith(('http://','https://','#')):return m[0]
        if target.endswith('my-thanh-team-roles-2026-11-12.md'):return f'[{label}](team-roles.md)'
        return label+' (tài liệu trong repo, không kèm ZIP)'
    content['research/team-profile-reference.md']=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',profile_link,profile).encode('utf-8')
    manifest={'date':'2026-11-12','version':'1.3','purpose':'reading and GIS handoff; not complete raw-data archive','files':[{'path':n,'sha256':hashlib.sha256(b).hexdigest()} for n,b in content.items()]}
    OUT.parent.mkdir(parents=True,exist_ok=True)
    with ZipFile(OUT,'w',ZIP_DEFLATED) as z:
        z.writestr('START-HERE.txt',README.encode('utf-8-sig'))
        for n,b in content.items():z.writestr(n,b)
        z.writestr('manifest.json',json.dumps(manifest,ensure_ascii=False,indent=2).encode('utf-8'))
    with ZipFile(OUT) as z:
        assert z.testzip() is None
        for row in manifest['files']:assert hashlib.sha256(z.read(row['path'])).hexdigest()==row['sha256']
    print(json.dumps({'file':str(OUT),'entries':len(content)+2,'bytes':OUT.stat().st_size,'hashes_verified':True}))

if __name__=='__main__':main()
