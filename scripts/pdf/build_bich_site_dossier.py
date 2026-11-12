"""Research handoff PDF, authored from Markdown; not field or sensor validation."""
import hashlib
import html
import json
import re
from pathlib import Path
from PIL import Image as PILImage
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Image, Flowable
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT=Path(__file__).resolve().parents[2]
CASE=ROOT/'nasa-space-apps-2026/planning/cases/my-thanh-cai-lay'
SRC=CASE/'bich-site-and-demo-dossier.md'
OUT=ROOT/'output/pdf/NeuraX-AgroTwin-Site-and-Demo-Dossier-Bich.pdf'
NAVY=colors.HexColor('#192A43');TEAL=colors.HexColor('#298E7C');INK=colors.HexColor('#23364F')
MUTED=colors.HexColor('#637289');PALE=colors.HexColor('#ECF6F2');LINE=colors.HexColor('#DCE3EB')
W,H=A4;M=43;CW=W-2*M
for n,f in [('A','arial.ttf'),('B','arialbd.ttf'),('I','ariali.ttf')]:
    pdfmetrics.registerFont(TTFont(n,'C:/Windows/Fonts/'+f))
pdfmetrics.registerFontFamily('A',normal='A',bold='B',italic='I',boldItalic='B')
ST={
 'body':ParagraphStyle('body',fontName='A',fontSize=10,leading=14.3,textColor=INK,spaceAfter=8,allowWidows=0,allowOrphans=0),
 'h1':ParagraphStyle('h1',fontName='B',fontSize=18,leading=23,textColor=NAVY,spaceAfter=13,keepWithNext=True),
 'note':ParagraphStyle('note',fontName='A',fontSize=9.3,leading=13.3,textColor=INK,backColor=PALE,borderPadding=8,spaceAfter=13),
 'cell':ParagraphStyle('cell',fontName='A',fontSize=8.4,leading=11.6,textColor=INK),
 'thead':ParagraphStyle('thead',fontName='B',fontSize=8.4,leading=11.6,textColor=colors.white),
 'caption':ParagraphStyle('caption',fontName='I',fontSize=8.3,leading=11.5,textColor=MUTED,spaceAfter=8),
 'ref':ParagraphStyle('ref',fontName='A',fontSize=8.8,leading=12.3,textColor=INK,spaceAfter=8),
 'step':ParagraphStyle('step',fontName='A',fontSize=10,leading=14.3,textColor=INK,leftIndent=14,firstLineIndent=-14,spaceAfter=8),
}

def inline(s):
    s=html.escape(s.replace('\u2011','-').replace('\u2013','-').replace('\u2014','-'))
    s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',lambda m:f'<link href="{m[2]}" color="#298E7C">{m[1]}</link>' if m[2].startswith('http') else m[1],s)
    s=re.sub(r'\*\*([^*]+)\*\*',r'<b>\1</b>',s)
    s=re.sub(r'`([^`]+)`',r'<font color="#375874">\1</font>',s)
    return s

def P(s,kind='body'):return Paragraph(inline(s),ST[kind])

logo_path=ROOT/'output/pdf/assets/neurax-logo-original.png'
logo=PILImage.open(logo_path).convert('RGB');mask=logo.point(lambda v:255 if v<120 else 0).convert('L');logo=logo.crop(mask.getbbox())

def header(c,d):
    c.saveState();c.drawImage(ImageReader(logo),M,H-46,24,25,preserveAspectRatio=True,mask='auto')
    c.setFillColor(NAVY);c.setFont('B',9);c.drawString(M+33,H-28,'NEURAX / AGROTWIN')
    c.setFillColor(MUTED);c.setFont('A',7.8);c.drawString(M+33,H-41,'FIELD SHIFT | HỒ SƠ NGHIÊN CỨU GỬI BÍCH')
    c.drawRightString(W-M,H-29,'1.3 / 12.11.3026');c.setStrokeColor(LINE);c.line(M,H-55,W-M,H-55)
    c.line(M,37,W-M,37);c.setFont('A',7.2);c.drawString(M,23,'Desk research + demo tại bàn; chưa kiểm chứng ruộng thực.');c.drawRightString(W-M,23,str(d.page-1))
    c.restoreState()

class Cover(Flowable):
    """Reuse the existing proposal cover's logo, navy/teal palette and hierarchy."""
    def __init__(self):super().__init__();self.width=CW;self.height=690
    def draw(self):
        c=self.canv;c.saveState();c.setFillColor(NAVY);c.rect(-M-6,-80,W+12,H+100,fill=1,stroke=0)
        c.setFillColor(colors.white);c.roundRect(0,615,56,56,10,fill=1,stroke=0)
        c.drawImage(ImageReader(logo),8,621,40,44,preserveAspectRatio=True,mask='auto')
        c.setFont('B',18);c.drawString(72,648,'NEURAX');c.setFillColor(colors.HexColor('#40B89E'));c.setFont('A',9)
        c.drawString(73,628,'FIELD SHIFT / NASA SPACE APPS 2026')
        c.setFont('B',10);c.drawString(0,548,'HỒ SƠ NGHIÊN CỨU VÀ REVIEW NỘI BỘ')
        c.setFillColor(colors.white);c.setFont('B',44);c.drawString(0,477,'AgroTwin')
        c.setFont('B',24);c.drawString(0,428,'Mỹ Thành');c.drawString(0,393,'Đất - nước - cây - mùa')
        st=ParagraphStyle('covertext',fontName='A',fontSize=13,leading=20,textColor=colors.HexColor('#CAD6E5'))
        p=Paragraph('Ba phương án tham khảo, bằng chứng và phần chưa biết.<br/>Tài liệu để Bích nghiên cứu tiếp, cùng phân công sáu thành viên và phương án demo tại HCM.',st)
        _,ph=p.wrap(CW-20,115);p.drawOn(c,0,342-ph)
        c.setStrokeColor(colors.HexColor('#46627D'));c.line(0,195,CW,195)
        for x,n,t in [(0,'01','R0 / R1 / R2'),(172,'02','Nguồn và giới hạn'),(344,'03','Review và bàn giao')]:
            c.setFillColor(colors.HexColor('#40B89E'));c.setFont('B',20);c.drawString(x,150,n)
            c.setFillColor(colors.white);c.setFont('A',10.5);c.drawString(x,126,t)
        p=Paragraph('Bản 1.3 | 12/11/2026<br/>Chưa là khuyến cáo canh tác hoặc khảo sát thực địa.<br/>Chuẩn bị nghiên cứu trước giờ G; triển khai project theo giờ BTC cho phép.',ParagraphStyle('coverfoot',fontName='A',fontSize=9.2,leading=15,textColor=colors.HexColor('#B5C6D9')))
        _,ph=p.wrap(CW,75);p.drawOn(c,0,24)
        c.restoreState()

class LabFlow(Flowable):
    def __init__(self):super().__init__();self.width=CW;self.height=138
    def draw(self):
        c=self.canv;bw=195
        blocks=[(0,75,'ĐẤT TẠI BÀN HCM','Probe thật / đo lặp','lab telemetry'),(0,18,'DỮ LIỆU VÙNG','NASA + SoilGrids','nguồn / thời gian / QA'),(CW-bw,46,'NÔNG TRẠI MÔ PHỎNG','So sánh R0 / R1 / R2','giả định + khoảng trống')]
        for x,y,a,b,d in blocks:
            c.setFillColor(PALE);c.setStrokeColor(LINE);c.roundRect(x,y,bw,49,6,fill=1,stroke=1)
            for j,(s,bold) in enumerate([(a,True),(b,False),(d,False)]):
                c.setFont('B' if bold else 'A',8 if j==0 else 7.9);c.setFillColor(NAVY if bold else MUTED);c.drawCentredString(x+bw/2,y+34-j*13,s)
        c.setStrokeColor(TEAL);c.setLineWidth(1.3)
        for y,z in [(99,80),(42,59)]:
            c.line(bw,y,CW-bw-8,z);c.line(CW-bw-8,z,CW-bw-14,z+4);c.line(CW-bw-8,z,CW-bw-14,z-4)
        c.setFont('A',7.6);c.setFillColor(TEAL);c.drawCentredString(CW/2,2,'Luồng tích hợp đề xuất; dữ liệu lab và dữ liệu vùng giữ nhãn nguồn riêng.')

def table(lines):
    rows=[[v.strip() for v in l.strip().strip('|').split('|')] for l in lines]
    rows=[r for r in rows if not all(re.fullmatch(r':?-+:?',x) for x in r)]
    n=len(rows[0]);widths={3:[CW*.23,CW*.39,CW*.38],4:[CW*.09,CW*.31,CW*.30,CW*.30],6:[CW*.08,CW*.21,CW*.21,CW*.08,CW*.21,CW*.21]}.get(n,[CW/n]*n)
    t=Table([[P(v,'thead' if i==0 else 'cell') for v in r] for i,r in enumerate(rows)],colWidths=widths,repeatRows=1,hAlign='LEFT')
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),NAVY),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#F1F5F7')]),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),('LINEBELOW',(0,0),(-1,-1),.35,LINE)]))
    return t

def main():
    inputs=[SRC,logo_path]
    def expand(path):
        result=[]
        for line in path.read_text(encoding='utf-8-sig').splitlines():
            m=re.fullmatch(r'<!-- INCLUDE:(.+) -->',line.strip())
            if m:
                child=(path.parent/m[1]).resolve();inputs.append(child);result.extend(expand(child))
            else:result.append(line)
        return result
    lines=expand(SRC);story=[Cover(),PageBreak()];i=0;section=0;source_section=False
    while i<len(lines):
        s=lines[i].strip()
        if not s or s.startswith('# ') or s.startswith('>'):i+=1;continue
        if s.startswith('## '):
            if section:story.append(PageBreak())
            section+=1;source_section=s.startswith('## 12. ');story.append(P(s[3:],'h1'));i+=1;continue
        if s=='<!-- FLOW -->':story.append(LabFlow());i+=1;continue
        if s.startswith('!['):
            m=re.match(r'!\[([^]]*)\]\(([^)]+)\)',s);path=(SRC.parent/m[2]).resolve();inputs.append(path)
            im=PILImage.open(path);w,h=im.size
            maxw=440 if section==2 else CW;maxh=490 if section==2 else 385
            scale=min(maxw/w,maxh/h);pic=Image(str(path),width=w*scale,height=h*scale);pic.hAlign='CENTER'
            story.extend([pic,Spacer(1,7)]);i+=1;continue
        if s.startswith('|'):
            block=[]
            while i<len(lines) and lines[i].strip().startswith('|'):block.append(lines[i]);i+=1
            story.extend([table(block),Spacer(1,10)]);continue
        block=[s];i+=1
        while i<len(lines) and lines[i].strip() and not lines[i].strip().startswith(('## ','|','![','<!--','- ')) and not re.match(r'^\d+\. ',lines[i].strip()):
            block.append(lines[i].strip());i+=1
        text=' '.join(block)
        if text.startswith('- '):text=text[2:]
        story.append(P(text,'ref' if source_section else ('step' if re.match(r'^\d+\. ',text) else 'body')))
    digest=hashlib.sha256(SRC.read_bytes()).hexdigest();OUT.parent.mkdir(parents=True,exist_ok=True)
    doc=SimpleDocTemplate(str(OUT),pagesize=A4,leftMargin=M,rightMargin=M,topMargin=72,bottomMargin=49,
        title='NeuraX AgroTwin - Site and Demo Dossier for Bich',author='NeuraX',
        subject='Research handoff v1.3; R0-R2 soil-water-crop-season evidence; team roles; not field validation',keywords='source_sha256='+digest)
    doc.build(story,onLaterPages=header)
    inputs.extend(CASE/n for n in ['study-block.geojson','study-block-coordinates.csv','study-block-soil-model.json','study-block-manifest.json','aoi-manifest.json','rotation-evidence-review.csv'])
    record={'source_sha256':digest,'output_sha256':hashlib.sha256(OUT.read_bytes()).hexdigest(),
            'inputs':[{'path':p.relative_to(ROOT).as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in inputs],
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'validation':'render and review after build; PDF build is not sensor or agronomic validation'}
    (OUT.parent/'NeuraX-AgroTwin-Site-and-Demo-Dossier-Bich.build.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(OUT)

if __name__=='__main__':main()
