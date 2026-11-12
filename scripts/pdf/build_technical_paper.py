from pathlib import Path
from io import BytesIO
import re,html,hashlib
from PIL import Image as PILImage
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,Table,TableStyle,KeepTogether,Flowable,Image,NextPageTemplate,CondPageBreak
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.lib.styles import ParagraphStyle,getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4

ROOT=Path(__file__).resolve().parents[2]
SRC=ROOT/'nasa-space-apps-2026/planning/hardware-design-paper.md'
OUT=ROOT/'output/pdf/NeuraX-AgroTwin-Technical-Paper-An.pdf'
AS=ROOT/'output/pdf/assets'
for n,f in [('A','arial.ttf'),('B','arialbd.ttf'),('I','ariali.ttf')]:pdfmetrics.registerFont(TTFont(n,str(Path('C:/Windows/Fonts')/f)))
pdfmetrics.registerFontFamily('A',normal='A',bold='B',italic='I',boldItalic='B')
NAVY=colors.HexColor('#192A43');TEAL=colors.HexColor('#40B89E');INK=colors.HexColor('#23364F');MUTED=colors.HexColor('#637289');PALE=colors.HexColor('#ECF6F2');LINE=colors.HexColor('#DCE3EB')
W,H=A4;M=47;CW=W-2*M
logo=PILImage.open(AS/'neurax-logo-original.png').convert('RGB');mask=logo.point(lambda v:255 if v<120 else 0).convert('L');logo=logo.crop(mask.getbbox())
styles={
 'body':ParagraphStyle('body',fontName='A',fontSize=10.3,leading=15.3,textColor=INK,spaceAfter=8.5,splitLongWords=1,allowWidows=0,allowOrphans=0),
 'h1':ParagraphStyle('h1',fontName='B',fontSize=19,leading=24,textColor=NAVY,spaceBefore=2,spaceAfter=16,keepWithNext=1),
 'h2':ParagraphStyle('h2',fontName='B',fontSize=12.2,leading=17,textColor=NAVY,spaceBefore=10,spaceAfter=7,keepWithNext=1),
 'caption':ParagraphStyle('caption',fontName='I',fontSize=9,leading=12.5,textColor=MUTED,spaceAfter=11),
 'quote':ParagraphStyle('quote',fontName='A',fontSize=9,leading=13,textColor=MUTED,backColor=PALE,borderPadding=9,spaceAfter=8),
 'cell':ParagraphStyle('cell',fontName='A',fontSize=8.7,leading=12.2,textColor=INK),
 'thead':ParagraphStyle('thead',fontName='B',fontSize=9,leading=12.5,textColor=colors.white),
 'code':ParagraphStyle('code',fontName='A',fontSize=8.2,leading=11.5,textColor=INK,leftIndent=8,spaceAfter=2),
 'bullet':ParagraphStyle('bullet',fontName='A',fontSize=10,leading=14.5,textColor=INK,leftIndent=12,firstLineIndent=-8,spaceAfter=7),
 'ref':ParagraphStyle('ref',fontName='A',fontSize=9,leading=13.5,textColor=INK,spaceAfter=10,splitLongWords=1),
}
def inline(s,refdef=False):
 s=html.escape(s)
 s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',lambda m:f'<link href="{m.group(2)}" color="#248B79">{m.group(1)}</link>' if m.group(2).startswith('http') else m.group(1),s)
 s=re.sub(r'\*\*([^*]+)\*\*',r'<b>\1</b>',s)
 s=re.sub(r'`([^`]+)`',r'<font color="#375874">\1</font>',s)
 if not refdef:s=re.sub(r'\[(S\d+)\]',r'<link href="#\1" color="#248B79">[\1]</link>',s)
 return s

def P(s,style='body'):return Paragraph(inline(s),styles[style])

def headfoot(can,doc):
 if doc.page==1:return
 can.saveState();can.setFillColor(NAVY);can.setFont('B',8.3);can.drawString(M,H-29,'NEURAX / AGROTWIN')
 can.setFont('A',7.4);can.setFillColor(MUTED);can.drawRightString(W-M,H-29,'HỒ SƠ THIẾT KẾ 0.3 · NỘI BỘ')
 can.setStrokeColor(LINE);can.line(M,H-38,W-M,H-38);can.line(M,38,W-M,38)
 can.setFont('A',7.4);can.drawString(M,24,'Field Shift | Đề xuất trước triển khai | 12.11.2026');can.drawRightString(W-M,24,str(doc.page))
 can.restoreState()
class Cover(Flowable):
 def __init__(self):Flowable.__init__(self);self.width=CW;self.height=710
 def draw(self):
  c=self.canv;c.saveState();c.setFillColor(NAVY);c.rect(-M,-100,W,H+140,fill=1,stroke=0)
  c.setFillColor(colors.white);c.roundRect(0,620,56,56,10,fill=1,stroke=0);c.drawImage(ImageReader(logo),8,626,40,44,preserveAspectRatio=True,mask='auto')
  c.setFillColor(colors.white);c.setFont('B',18);c.drawString(72,653,'NEURAX');c.setFont('A',9);c.setFillColor(TEAL);c.drawString(73,633,'FIELD SHIFT / NASA SPACE APPS 2026')
  c.setFillColor(TEAL);c.setFont('B',10);c.drawString(0,554,'HỒ SƠ PHÂN TÍCH VÀ THIẾT KẾ HỆ THỐNG')
  c.setFillColor(colors.white);c.setFont('B',44);c.drawString(0,482,'AgroTwin')
  for i,t in enumerate(['Từ bài toán luân canh','đến phần cứng có thể kiểm chứng.']):
   c.setFont('B',23);c.drawString(0,435-i*33,t)
  p=Paragraph('Lập luận lựa chọn thiết bị, kiến trúc dữ liệu, hiệu chuẩn, kiểm thử và phương án backup cho An và cả nhóm.',ParagraphStyle('cp',fontName='A',fontSize=14,leading=21,textColor=colors.HexColor('#CAD6E5')))
  _,ph=p.wrap(450,110);p.drawOn(c,0,315-ph)
  c.setStrokeColor(colors.HexColor('#46627D'));c.line(0,190,CW,190)
  for x,n,t in [(0,'01','Vì sao chọn'),(172,'02','Kiểm đúng bằng gì'),(344,'03','Lỗi thì làm sao')]:
   c.setFillColor(TEAL);c.setFont('B',20);c.drawString(x,149,n);c.setFont('A',11);c.setFillColor(colors.white);c.drawString(x,124,t)
  p=Paragraph('Bản thiết kế 0.3 · 12/11/2026<br/>Tài liệu nội bộ trước triển khai. Chưa có kết quả thử nghiệm.<br/>HTTPSLAB: chờ thông số. ESP32: cấu hình tham chiếu dự phòng.',ParagraphStyle('cp2',fontName='A',fontSize=9.3,leading=15,textColor=colors.HexColor('#B5C6D9')))
  _,ph=p.wrap(CW,80);p.drawOn(c,0,25)
  c.restoreState()

class Diagram(Flowable):
 def __init__(self,kind):Flowable.__init__(self);self.kind=kind;self.width=CW;self.height={'architecture':228,'topology':225,'states':195,'backup':220}[kind]
 def draw(self):
  c=self.canv;h=self.height
  def box(x,y,w,hh,title,sub='',dark=False):
   c.setFillColor(NAVY if dark else PALE);c.roundRect(x,h-y-hh,w,hh,7,fill=1,stroke=0)
   st=ParagraphStyle('d',fontName='B',fontSize=9.2,leading=12,textColor=colors.white if dark else INK,alignment=1)
   p=Paragraph(title,st);_,ph=p.wrap(w-12,hh);p.drawOn(c,x+6,h-y-12-ph)
   if sub:
    pp=Paragraph(sub,ParagraphStyle('ds',fontName='A',fontSize=7.5,leading=10,textColor=colors.HexColor('#CAD6E5') if dark else MUTED,alignment=1));_,sh=pp.wrap(w-12,hh);pp.drawOn(c,x+6,h-y-hh+8)
  def arr(x1,y1,x2,y2,color=TEAL):
   import math
   c.setStrokeColor(color);c.setLineWidth(1.4);c.line(x1,h-y1,x2,h-y2);a=math.atan2(y2-y1,x2-x1)
   for off in [-.5,.5]:c.line(x2,h-y2,x2-5*math.cos(a+off),h-y2+5*math.sin(a+off))
  if self.kind=='architecture':
   for x,title,sub in [(0,'NASA + domain','D1 / K1'),(132,'Kiểm chất lượng','Q1'),(264,'Phân tích / rank','Hưng + Việt'),(396,'Dashboard','A1 / E1')]:box(x,14,105,69,title,sub,x==264)
   for x in [105,237,369]:arr(x,48,x+25,48)
   box(0,135,112,65,'Probe tại bàn','Điểm đo thực');box(152,135,112,65,'Node / bridge','H1 + quality');box(305,135,196,65,'Thẻ context + display','Tách khỏi ranking vùng',True)
   arr(112,167,152,167);arr(264,167,305,167);arr(448,83,448,135)
   c.setFont('A',8);c.setFillColor(MUTED);c.drawString(6,h-112,'LUỒNG THIẾT BỊ: quan sát tại điểm và kiểm tích hợp')
  elif self.kind=='topology':
   box(0,13,125,67,'Probe analog','ADC đúng range');box(0,121,125,67,'SHT31 / OLED','I2C nếu lắp')
   box(195,55,125,100,'ESP32 backup','MCU acquisition',True);box(385,55,116,100,'Laptop','Bridge + log + A1')
   arr(125,47,195,86);arr(125,153,195,128);arr(195,128,125,153);arr(320,91,385,91);arr(385,123,320,123)
   c.setFillColor(MUTED);c.setFont('A',7.5);c.drawString(329,h-75,'USB Serial');c.drawString(171,h-207,'Nguồn USB theo board guide; GND chung')
  elif self.kind=='states':
   c.setFillColor(MUTED);c.setFont('B',9);c.drawString(0,h-15,'CHẤT LƯỢNG PHÉP ĐO')
   for x,title,sub in [(0,'unknown','chưa đủ kiểm'),(177,'ok','đủ policy đã chốt'),(354,'invalid','lỗi đã xác định')]:box(x,29,147,58,title,sub,x==177)
   arr(147,58,177,58);arr(324,58,354,58)
   c.setFillColor(MUTED);c.setFont('B',9);c.drawString(0,h-115,'CÁCH GIAO VÀ TUỔI DỮ LIỆU')
   for x,title,sub in [(0,'live','đang nhận'),(177,'stale','quá timeout'),(354,'replay','phát lại có nhãn')]:box(x,130,147,58,title,sub)
  else:
   rows=[('B0','Live: probe + USB; bổ sung nếu ổn'),('B1 / B2','Bỏ phần phụ / quay về USB + snapshot'),('B3','Replay log thật: giữ parser và UI'),('B4','Synthetic: chỉ kiểm contract hardware')]
   for i,(a,b) in enumerate(rows):
    y=i*53;box(0,y,77,42,a,'',i==0);box(95,y,406,42,b,'',False)
    arr(77,y+21,95,y+21)

class PaperDoc(SimpleDocTemplate):
 def afterFlowable(self,f):
  if isinstance(f,Paragraph) and f.style.name=='h1':
   title=f.getPlainText();key='sec-'+hashlib.sha1(title.encode()).hexdigest()[:10]
   self.canv.bookmarkPage(key);self.canv.addOutlineEntry(title,key,level=0,closed=False);self.notify('TOCEntry',(0,title,self.page,key))

def table(lines):
 rows=[]
 for k,line in enumerate(lines):
  cells=[s.strip() for s in line.strip().strip('|').split('|')]
  if k==1 and all(re.match(r'^:?-+:?$',s.replace(' ','')) for s in cells):continue
  rows.append([Paragraph(inline(s),styles['thead' if k==0 else 'cell']) for s in cells])
 n=len(rows[0]);ratios={2:[.30,.70],3:[.24,.34,.42],4:[.14,.25,.27,.34]}.get(n,[1/n]*n)
 t=Table(rows,colWidths=[CW*r for r in ratios],repeatRows=1,hAlign='LEFT')
 t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),NAVY),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#F1F5F7')]),('LINEBELOW',(0,0),(-1,0),.5,NAVY),('LINEBELOW',(0,1),(-1,-1),.4,LINE)]))
 return t

story=[Cover(),PageBreak(),Paragraph('Mục lục',ParagraphStyle('toctitle',parent=styles['h1'],spaceAfter=20))]
toc=TableOfContents();toc.levelStyles=[ParagraphStyle('toc',fontName='A',fontSize=9.2,leading=12,textColor=INK,spaceBefore=1,leftIndent=0,firstLineIndent=0,rightIndent=20)]
story.extend([toc,Spacer(1,17),P('Cách dùng: đọc lập luận trước khi mua hoặc đấu nối; dùng bảng kiểm và backup khi rehearsal. Những ngưỡng chưa pilot không được coi là thông số đã đạt.','quote'),PageBreak()])
lines=SRC.read_text(encoding='utf-8').splitlines();i=0;started=False
while i<len(lines):
 l=lines[i].strip()
 if not l:i+=1;continue
 if l.startswith('# '):i+=1;continue
 if l.startswith('>'):
  # Version/status are covered by the authored cover and abstract.
  i+=1;continue
 if l.startswith('## '):
  title=l[3:]
  if started:
   if title.startswith(('1. ', '18. ', 'Phụ lục A.')):story.append(PageBreak())
   else:story.append(CondPageBreak(150));story.append(Spacer(1,14))
  story.append(P(title,'h1'));started=True;i+=1;continue
 if l.startswith('### '):story.append(P(l[4:],'h2'));i+=1;continue
 if l.startswith('<!-- FIGURE:'):
  kind=l.split(':')[1].split(' ')[0].replace('-->','').strip();figure=Diagram(kind);figure.keepWithNext=1;story.append(figure);i+=1;continue
 if l.startswith('!['):
  m=re.match(r'!\[([^]]*)\]\(([^)]+)\)',l);path=(SRC.parent/m.group(2)).resolve();im=PILImage.open(path).convert('RGBA');bg=PILImage.new('RGBA',im.size,'white');bg.alpha_composite(im);bg=bg.convert('RGB');buf=BytesIO();bg.save(buf,format='PNG');buf.seek(0)
  iw,ih=bg.size;scale=min(270/iw,143/ih);pic=Image(buf,width=iw*scale,height=ih*scale);pic.hAlign='CENTER';pic.keepWithNext=1;story.append(pic);i+=1;continue
 if l.startswith('|'):
  block=[]
  while i<len(lines) and lines[i].strip().startswith('|'):block.append(lines[i]);i+=1
  story.extend([table(block),Spacer(1,11)]);continue
 if l.startswith('```'):
  block=[];i+=1
  while i<len(lines) and not lines[i].startswith('```'):block.append(lines[i]);i+=1
  code=[Paragraph(html.escape(s).replace(' ','&nbsp;'),styles['code']) for s in block]
  t=Table([[code]],colWidths=[CW]);t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),colors.HexColor('#F0F4F7')),('BOX',(0,0),(-1,-1),.5,LINE),('TOPPADDING',(0,0),(-1,-1),10),('BOTTOMPADDING',(0,0),(-1,-1),8)]));story.extend([t,Spacer(1,10)]);i+=1;continue
 if l.startswith('- [S'):
  m=re.match(r'- \[(S\d+)\] (.+?) (https?://\S+)$',l)
  if m:
   key,desc,url=m.groups();text=f'<a name="{key}"/><b>[{key}]</b> {html.escape(desc)}<br/><link href="{url}" color="#248B79">{html.escape(url)}</link>';story.append(Paragraph(text,styles['ref']))
  else:story.append(P(l[2:],'ref'))
  i+=1;continue
 if l.startswith('- '):story.append(Paragraph('• '+inline(l[2:]),styles['bullet']));i+=1;continue
 if l.startswith('**Hình '):story.append(P(l,'caption'));i+=1;continue
 # Join only consecutive lines in a prose block.
 block=[l];i+=1
 while i<len(lines) and lines[i].strip() and not re.match(r'^(#|\||```|!\[|<!--|- )',lines[i].strip()):block.append(lines[i].strip());i+=1
 story.append(P(' '.join(block)))

doc=PaperDoc(str(OUT),pagesize=A4,rightMargin=M-6,leftMargin=M-6,topMargin=57,bottomMargin=52,title='NeuraX AgroTwin - Ho so phan tich va thiet ke he thong demo',author='NeuraX',subject='Technical design paper for An and team, v0.3, 12 November 2026; HTTPSLAB pending',keywords='source_sha256='+hashlib.sha256(SRC.read_bytes()).hexdigest(),allowSplitting=1)
doc.multiBuild(story,onFirstPage=headfoot,onLaterPages=headfoot)
print(OUT)
