"""Prepend clear supersession notices, preserving original PDFs in an archive.

This labels historical artifacts; it does not pretend their content was revised.
Call PDF skill authoring marker before running. Idempotent from archived originals.
"""
from io import BytesIO
from pathlib import Path
import hashlib
import json
from pypdf import PdfReader, PdfWriter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'output/pdf'
FILES=['NeuraX-AgroTwin-Preliminary-Proposal.pdf','NeuraX-AgroTwin-Team-Decision-Proposal.pdf','NeuraX-AgroTwin-Technical-Paper-An.pdf']
ARCHIVE=OUT/'archive/pre-current-state-label-2026-11-12'

def main():
    for n,f in [('A','arial.ttf'),('B','arialbd.ttf')]:pdfmetrics.registerFont(TTFont(n,'C:/Windows/Fonts/'+f))
    pdfmetrics.registerFontFamily('A',normal='A',bold='B',italic='A',boldItalic='B')
    st=ParagraphStyle('body',fontName='A',fontSize=11,leading=17,textColor=colors.HexColor('#23364f'),spaceAfter=15)
    title=ParagraphStyle('title',parent=st,fontName='B',fontSize=25,leading=32,textColor=colors.HexColor('#192a43'),spaceAfter=23)
    ARCHIVE.mkdir(parents=True,exist_ok=True);records=[]
    for name in FILES:
        p=OUT/name;original=ARCHIVE/name
        if not original.exists():original.write_bytes(p.read_bytes())
        raw=original.read_bytes();reader=PdfReader(BytesIO(raw))
        buffer=BytesIO();doc=SimpleDocTemplate(buffer,leftMargin=49,rightMargin=49,topMargin=60,bottomMargin=50)
        parts=[Paragraph('NEURAX / AGROTWIN',st),Spacer(1,20),Paragraph('SNAPSHOT THAM KHẢO<br/>Đã có bản hiện hành thay thế',title),
            Paragraph('<b>Thông báo trạng thái ngày 12/11/2026.</b> Các trang tiếp theo giữ nội dung lịch sử để truy vết. Chưa sửa lại toàn bộ nội dung bên trong; không dùng chúng để chốt địa bàn, phân công hoặc quyền bắt đầu project trước giờ G.',st),
            Paragraph('<b>Case hiện hành: Mỹ Thành.</b> R0 lúa-lúa-lúa, R1 lúa-bắp non-lúa, R2 lúa-đậu xanh-lúa là phương án tham khảo; chưa là hiện trạng block hoặc khuyến cáo đã kiểm. Đức Lập/bắp hạt/đậu phộng trong snapshot không phải lựa chọn hiện tại.',st),
            Paragraph('<b>Phân công hiện hành:</b> Hưng workflow/scope Data -&gt; AI; Việt technical AI/Data Analysis. Hai người cùng core, features, pipeline, kiến trúc, output demo; cùng UI/UX và backend support. Bích Data/review nguồn-feature; Hiếu backend remote gián đoạn; An demo ESP/sensor; Quang Luật thống kê/đánh giá/QA từng block.',st),
            Paragraph('<b>Đọc thay thế:</b> NeuraX-AgroTwin-Site-and-Demo-Dossier-Bich.pdf (bản 1.3), hoặc planning/START-HERE.md trong repo neurax-docs. Có bảng đất-nước-cây-mùa và vai trò mới nhất. Hồ sơ nghiên cứu không tự xác nhận thiết bị, mô hình hoặc điều kiện ruộng thực.',st),
            Paragraph('<b>Trước T0:</b> nghiên cứu và chuẩn bị theo phạm vi BTC cho phép; triển khai submission sau giờ mở hackathon. Remote eligibility/deadline local cần xác nhận. Hardware paper cũ chỉ tham khảo nguyên lý, chưa chốt pinout/inventory hay hiệu chuẩn probe thực tế.',st)]
        doc.build(parts);notice=PdfReader(buffer);assert len(notice.pages)==1
        writer=PdfWriter();writer.append(notice);writer.append(reader)
        writer.add_metadata({'/Title':name.removesuffix('.pdf')+' - SUPERSEDED SNAPSHOT',
            '/Subject':'Historical content with supersession notice; current roles/case in START-HERE and Bich dossier v1.3',
            '/Keywords':'superseded_snapshot; original_sha256='+hashlib.sha256(raw).hexdigest(),'/Author':'NeuraX'})
        with p.open('wb') as f:writer.write(f)
        result=PdfReader(p);assert len(result.pages)==len(reader.pages)+1
        records.append({'file':name,'original_archive':original.relative_to(ROOT).as_posix(),
            'original_sha256':hashlib.sha256(raw).hexdigest(),'output_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
            'original_pages':len(reader.pages),'output_pages':len(result.pages),'scope':'one notice page added, original content unchanged'})
    (OUT/'snapshot-label-manifest.json').write_text(json.dumps({'date':'2026-11-12','files':records},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps([{'file':r['file'],'pages':r['output_pages']} for r in records]))

if __name__=='__main__':main()
