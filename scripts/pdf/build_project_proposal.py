from pathlib import Path
from agrotwin_visuals import ProjectVisual
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
SRC=ROOT/'nasa-space-apps-2026/planning/project-brief.md'
OUT=ROOT/'output/pdf/NeuraX-AgroTwin-Preliminary-Proposal.pdf'
AS=ROOT/'output/pdf/assets'
for n,f in [('A','arial.ttf'),('B','arialbd.ttf'),('I','ariali.ttf')]:pdfmetrics.registerFont(TTFont(n,str(Path('C:/Windows/Fonts')/f)))
pdfmetrics.registerFontFamily('A',normal='A',bold='B',italic='I',boldItalic='B')
NAVY=colors.HexColor('#192A43');TEAL=colors.HexColor('#40B89E');INK=colors.HexColor('#23364F');MUTED=colors.HexColor('#637289');PALE=colors.HexColor('#ECF6F2');LINE=colors.HexColor('#DCE3EB')
W,H=A4;M=47;CW=W-2*M
logo=PILImage.open(AS/'neurax-logo-original.png').convert('RGB');mask=logo.point(lambda v:255 if v<120 else 0).convert('L');logo=logo.crop(mask.getbbox())
styles={
 'body':ParagraphStyle('body',fontName='A',fontSize=10.2,leading=15.3,textColor=INK,spaceAfter=8.5,splitLongWords=1,allowWidows=0,allowOrphans=0),
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
 can.setFont('A',7.4);can.setFillColor(MUTED);can.drawRightString(W-M,H-29,'PROPOSAL SƠ BỘ 0.4 · NỘI BỘ')
 can.setStrokeColor(LINE);can.line(M,H-38,W-M,H-38);can.line(M,38,W-M,38)
 can.setFont('A',7.4);can.drawString(M,24,'Field Shift | Đề xuất trước triển khai | 12.11.2026');can.drawRightString(W-M,24,str(doc.page))
 can.restoreState()
class Cover(Flowable):
 def __init__(self):Flowable.__init__(self);self.width=CW;self.height=710
 def draw(self):
  c=self.canv;c.saveState();c.setFillColor(NAVY);c.rect(-M,-100,W,H+140,fill=1,stroke=0)
  c.setFillColor(colors.white);c.roundRect(0,620,56,56,10,fill=1,stroke=0);c.drawImage(ImageReader(logo),8,626,40,44,preserveAspectRatio=True,mask='auto')
  c.setFillColor(colors.white);c.setFont('B',18);c.drawString(72,653,'NEURAX');c.setFont('A',9);c.setFillColor(TEAL);c.drawString(73,633,'FIELD SHIFT / NASA SPACE APPS 2026')
  c.setFillColor(TEAL);c.setFont('B',10);c.drawString(0,554,'PROPOSAL SƠ BỘ DỰ ÁN')
  c.setFillColor(colors.white);c.setFont('B',44);c.drawString(0,482,'AgroTwin')
  for i,t in enumerate(['Từ dữ liệu môi trường','đến lựa chọn có thể giải thích.']):
   c.setFont('B',23);c.drawString(0,435-i*33,t)
  p=Paragraph('Case địa phương, farm tương tác, phương pháp, kiến trúc và kế hoạch nâng chất lượng bài thi local / global.',ParagraphStyle('cp',fontName='A',fontSize=14,leading=21,textColor=colors.HexColor('#CAD6E5')))
  _,ph=p.wrap(450,110);p.drawOn(c,0,315-ph)
  c.setStrokeColor(colors.HexColor('#46627D'));c.line(0,190,CW,190)
  for x,n,t in [(0,'01','Giải quyết điều gì'),(172,'02','Bằng chứng nào'),(344,'03','Triển khai ra sao')]:
   c.setFillColor(TEAL);c.setFont('B',20);c.drawString(x,149,n);c.setFont('A',11);c.setFillColor(colors.white);c.drawString(x,124,t)
  p=Paragraph('Bản proposal 0.4 · 12/11/2026<br/>Review nội bộ trước triển khai; chưa là sản phẩm đã kiểm chứng.<br/>Bản nguồn: project-brief.md · Hardware: paper kỹ thuật riêng.',ParagraphStyle('cp2',fontName='A',fontSize=9.3,leading=15,textColor=colors.HexColor('#B5C6D9')))
  _,ph=p.wrap(CW,80);p.drawOn(c,0,25)
  c.restoreState()

class HardwareDiagram(Flowable):
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
   box(0,135,112,65,'Probe tại bàn','Điểm đo thực');box(152,135,112,65,'ESP32 / bridge','H1 + quality');box(305,135,196,65,'Thẻ context + display','Tách khỏi ranking vùng',True)
   arr(112,167,152,167);arr(264,167,305,167);arr(448,83,448,135)
   c.setFont('A',8);c.setFillColor(MUTED);c.drawString(6,h-112,'LUỒNG THIẾT BỊ: quan sát tại điểm và kiểm tích hợp')
  elif self.kind=='topology':
   box(0,13,125,67,'Probe analog','ADC đúng range');box(0,121,125,67,'SHT31 / OLED','I2C nếu lắp')
   box(195,55,125,100,'ESP32','MCU acquisition',True);box(385,55,116,100,'Laptop','Bridge + log + A1')
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


class Diagram(Flowable):
 def __init__(self,kind):
  Flowable.__init__(self);self.kind=kind;self.width=CW
  self.height={'solution':222,'journey':188,'architecture':490,'farm':360,'evidence':270,'roadmap':280,'wireframe':230,'score':245}[kind]
 def draw(self):
  if self.kind in ('architecture','farm','evidence'):
   obj=ProjectVisual(self.kind,CW);obj.canv=self.canv;obj.draw();return
  c=self.canv;h=self.height
  def rect(x,y,w,hh,fill=PALE):
   c.setFillColor(fill);c.roundRect(x,h-y-hh,w,hh,6,fill=1,stroke=0)
  def t(s,x,y,size=9,bold=False,col=INK):
   c.setFillColor(col);c.setFont('B' if bold else 'A',size);c.drawString(x,h-y-size*.85,s)
  def p(s,x,y,w,size=9,bold=False,col=INK):
   st=ParagraphStyle('figp',fontName='B' if bold else 'A',fontSize=size,leading=size*1.3,textColor=col)
   ob=Paragraph(s,st);_,ph=ob.wrap(w,200);ob.drawOn(c,x,h-y-ph)
  def box(x,y,w,hh,title,sub='',dark=False):
   rect(x,y,w,hh,NAVY if dark else PALE);p(title,x+8,y+10,w-16,9,True,colors.white if dark else INK)
   if sub:p(sub,x+8,y+hh-19,w-16,7.5,False,colors.HexColor('#CFDCEB') if dark else MUTED)
  def arr(x1,y1,x2,y2):
   import math
   c.setStrokeColor(TEAL);c.setLineWidth(1.2);c.line(x1,h-y1,x2,h-y2);a=math.atan2(y2-y1,x2-x1)
   for of in [-.5,.5]:c.line(x2,h-y2,x2-5*math.cos(a+of),h-y2+5*math.sin(a+of))
  if self.kind=='solution':
   for x,title,sub in [(0,'NASA climate / EO','Nguồn môi trường'),(178,'K1: cây, đất, mùa','Nguồn domain'),(356,'Ưu tiên người dùng','Weight / constraint')]:box(x,0,145,48,title,sub)
   box(0,78,145,51,'D1 / Q1','Feature + QA');box(178,78,145,51,'Constraint + ranking','Phương pháp baseline',True);box(356,78,145,51,'A1 / Dashboard','Kết quả + evidence')
   arr(72,48,72,78);arr(145,103,178,103);arr(250,48,250,78);arr(415,48,310,78);arr(323,103,356,103)
   box(0,166,145,44,'Node / H1','Đo tại điểm');box(356,166,145,44,'Context riêng','Không tự vào ranking')
   arr(145,188,356,188);arr(428,166,428,129)
  elif self.kind=='journey':
   entries=[(0,0,'1. Context','Vùng + hiện trạng'),(178,0,'2. Dữ liệu','Coverage + nguồn'),(356,0,'3. Ưu tiên','Constraint + weights'),(356,108,'4. So phương án','Eligibility + score'),(178,108,'5. Giải thích','Reason + missing'),(0,108,'6. Review','Điều cần kiểm tiếp')]
   for x,y,a,b in entries:box(x,y,145,60,a,b,x==356 and y==108)
   arr(145,30,178,30);arr(323,30,356,30);arr(428,60,428,108);arr(356,138,323,138);arr(178,138,145,138)
  elif self.kind=='roadmap':
   entries=[(0,0,'P0: framing','Nguồn và unknown'),(178,0,'P1: DATA / K1 / Q1','Đủ điều kiện dùng'),(356,0,'P2: baseline A1','Tính và giải thích'),(0,105,'P3: measurement','Nhánh thiết bị'),(178,105,'P4: integration','UI + packages'),(356,105,'P5: evaluation','QA và backup'),(356,210,'P6: bàn giao','Rehearsal / nộp')]
   for x,y,a,b in entries:box(x,y,145,59,a,b,a.startswith('P4'))
   arr(145,29,178,29);arr(323,29,356,29);arr(405,59,284,105);arr(145,134,178,134);arr(323,134,356,134);arr(428,164,428,210)
   p('Fixture UI và protocol có thể chuẩn bị song song; build theo thời điểm BTC cho phép.',0,210,315,9,col=MUTED)
  elif self.kind=='wireframe':
   rect(0,0,CW,222,colors.HexColor('#F1F5F8'));rect(8,8,CW-16,30,NAVY);t('AGROTWIN / WIREFRAME MINH HỌA',19,17,9,True,colors.white)
   rect(12,48,140,162,colors.white);p('CONTEXT',22,58,120,9,True);p('Vùng / period<br/>Hiện trạng<br/>Nguồn / coverage<br/><br/>Ưu tiên<br/>Trạng thái dữ liệu',22,79,120,9)
   for i,label in enumerate(['Hiện trạng','Phương án B','Phương án C']):
    x=164+i*108;rect(x,48,98,74,PALE);p(label,x+7,57,84,9,True);p('Eligibility<br/>Điểm thành phần',x+7,81,84,8)
   rect(164,132,314,78,colors.white);p('EVIDENCE VÀ GIỚI HẠN',174,143,290,9,True);p('Lý do · Source IDs · Missing inputs<br/>Context node: vị trí / thời gian / quality<br/>Đây là bố cục dự kiến, chưa có dữ liệu thật.',174,164,290,8.5)
  else:
   sets=[([.60,.25,.15],'Ưu tiên nước'),([.20,.60,.20],'Ưu tiên đất')]
   source_text=SRC.read_text(encoding='utf-8')
   rows=re.findall(r'\| SYN-[ABC][^|]*\|\s*([0-9.]+)\s*\|\s*([0-9.]+)\s*\|\s*([0-9.]+)',source_text)
   assert len(rows)==3;data=[[float(v) for v in row] for row in rows]
   parsed_weights=re.findall(r'Weights ([0-9.]+)/([0-9.]+)/([0-9.]+)',source_text)
   assert len(parsed_weights)==2;sets=[([float(v) for v in ws],label) for ws,label in zip(parsed_weights,['Ưu tiên nước','Ưu tiên đất'])]
   palette=[TEAL,colors.HexColor('#A3B87A'),colors.HexColor('#8397CF')]
   for k,(weights,title) in enumerate(sets):
    x=k*260;t(title,x,8,10,True);t('w = '+ ' / '.join(f'{v:.2f}' for v in weights),x,28,8,col=MUTED)
    for i,vals in enumerate(data):
     y=61+i*40;t('ABC'[i],x,y+1,9,True);left=x+18;contrib=[w*v for w,v in zip(weights,vals)]
     for val,color in zip(contrib,palette):
      width=val*172;rect(left,y,width,17,color);left+=width
     t(f'{sum(contrib):.4f}',x+194,y+2,8)
   for i,(label,color) in enumerate(zip(['Water','Soil','Climate'],palette)):
    rect(i*120,205,12,10,color);t(label,18+i*120,204,8)
   t('SYNTHETIC: chỉ số minh họa, không phải dữ liệu cây thật.',0,231,8,col=MUTED)

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
story.extend([toc,Spacer(1,17),P('Cách review: chốt bài toán và giả định, kiểm nguồn/phương pháp, sau đó rà scope, phase, owner và acceptance. Nội dung chưa có artifact giữ trạng thái đề xuất.','quote'),PageBreak()])
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
   if title.startswith(('1. ', '19. ', 'Phụ lục A.')):story.append(PageBreak())
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
  if l.startswith('```mermaid'):
   marker=next((b for b in block if b.strip().startswith('%% figure:')),None)
   assert marker, 'Mermaid diagram missing figure mapping'
   figure=Diagram(marker.split(':',1)[1].strip());figure.keepWithNext=1;story.append(figure);i+=1;continue
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

doc=PaperDoc(str(OUT),pagesize=A4,rightMargin=M-6,leftMargin=M-6,topMargin=57,bottomMargin=52,title='NeuraX AgroTwin - Proposal so bo du an',author='NeuraX',keywords='source_sha256='+hashlib.sha256(SRC.read_bytes()).hexdigest(),subject='Preliminary project proposal for NeuraX, v0.4, 12 November 2026',allowSplitting=1)
doc.multiBuild(story,onFirstPage=headfoot,onLaterPages=headfoot)
print(OUT)
