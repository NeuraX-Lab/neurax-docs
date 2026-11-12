"""Vector diagrams for proposed architecture; no empirical measurements."""
import math
from reportlab.platypus import Flowable, Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors

NAVY=colors.HexColor('#192A43')
TEAL=colors.HexColor('#40B89E')
INK=colors.HexColor('#23364F')
PALE=colors.HexColor('#ECF6F2')
MUTED=colors.HexColor('#637289')
LINE=colors.HexColor('#DCE3EB')

class ProjectVisual(Flowable):
    def __init__(self,kind,width,reference_mode=False):
        super().__init__()
        self.kind=kind;self.width=width
        self.reference_mode=reference_mode
        self.height={'architecture':490,'farm':360,'evidence':270}[kind]

    def draw(self):
        c=self.canv;h=self.height;w=self.width
        def para(text,x,y,width,size=9,bold=False,color=INK):
            ob=Paragraph(text,ParagraphStyle('visual',fontName='B' if bold else 'A',fontSize=size,leading=size*1.35,textColor=color))
            _,ph=ob.wrap(width,500);ob.drawOn(c,x,h-y-ph)
        def box(x,y,width,height,title,body='',dark=False):
            c.setFillColor(NAVY if dark else PALE)
            c.roundRect(x,h-y-height,width,height,7,fill=1,stroke=0)
            para(title,x+10,y+9,width-20,9.5,True,colors.white if dark else INK)
            if body:para(body,x+10,y+29,width-20,8,False,colors.HexColor('#D6E3EC') if dark else MUTED)
        def arrow(x1,y1,x2,y2,dashed=False):
            c.setStrokeColor(TEAL);c.setLineWidth(1.4)
            c.setDash(4,3) if dashed else c.setDash()
            c.line(x1,h-y1,x2,h-y2);c.setDash()
            a=math.atan2(y2-y1,x2-x1)
            for of in [-.5,.5]:c.line(x2,h-y2,x2-6*math.cos(a+of),h-y2+6*math.sin(a+of))
        if self.kind=='architecture':
            col=(w-28)/3
            top=[('NASA history','Mưa / nhiệt; grain và thời gian'),('Nguồn địa phương','Đất / cây / mùa; phạm vi áp dụng'),('Ưu tiên và ENSO','Outlook có ngày, horizon')]
            mid=[('D1 + Q1','Feature / QA / manifest'),('K1','Nguồn / rule / unknown'),('Context / scenario','Giả định riêng; ENSO có gate')]
            for i,(title,body) in enumerate(top):box(i*(col+14),0,col,65,title,body)
            for i,(title,body) in enumerate(mid):
                x=i*(col+14);box(x,100,col,65,title,body);arrow(x+col/2,65,x+col/2,100)
            box(140,207,w-280,68,'Eligibility + scoring','Hưng / Việt; sensitivity và lý do',True)
            for i in range(3):arrow(i*(col+14)+col/2,165,w/2,207)
            box(0,317,300,67,'A1 / Farm 2D','Hiếu: lịch mùa vụ / why-not / missing',True)
            box(326,317,w-326,67,'E1 / evidence','Quang Luật: kiểm độc lập')
            arrow(w/2,275,150,317);arrow(w/2,275,410,317)
            box(0,418,223,58,'Thiết bị / H1','An: chờ model; time / unit / quality')
            box(267,418,w-267,58,'Ô thử nghiệm live riêng','Mẫu tại bàn; không thay input vùng')
            arrow(223,447,267,447);arrow(283,418,283,384)
        elif self.kind=='farm':
            c.setFillColor(colors.HexColor('#F1F5F8'));c.roundRect(0,0,w,h,8,fill=1,stroke=0)
            box(9,9,w-18,48,'AGROTWIN / FARM 2D','WIREFRAME ĐỀ XUẤT - không phải kết quả đã chạy',True)
            box(10,70,128,174,'CASE NGHIÊN CỨU','Đức Lập<br/>Thửa đất: chưa chốt<br/><br/>NASA history<br/>Nguồn đất / mùa<br/>ENSO có ngày<br/><br/>Ưu tiên người dùng')
            sx=151;sw=w-sx-12
            para('LỊCH KẾ HOẠCH THEO MÙA',sx,75,sw,9,True)
            labels=['Tham chiếu 3 lúa','2 lúa + bắp','2 lúa + mè'] if self.reference_mode else ['Hiện trạng','Phương án B','Phương án C']
            for i,label in enumerate(labels):
                yy=104+i*43
                para(label,sx,yy,90,8.5,True)
                c.setFillColor(TEAL if i==0 else colors.HexColor('#A3B87A'))
                c.roundRect(sx+94,h-yy-23,sw-95,23,4,fill=1,stroke=0)
                para('Ngày / giống: cần review' if self.reference_mode else 'Chuỗi cây: chờ nguồn và review',sx+101,yy+5,sw-110,7.6)
            para('Thanh màu chỉ minh họa vị trí; chưa là lịch cây đã xác minh.',sx,236,sw,7.5,color=MUTED)
            box(10,268,231,78,'VÌ SAO / KHI NÀO / THIẾU GÌ?','Rule + source + điều kiện đổi ý<br/>Không ép dữ liệu thiếu thành pass')
            box(255,268,w-265,78,'SENSOR LIVE TẠI BÀN','Raw/index + time + quality<br/>Sandbox chỉ khi bật riêng')
        else:
            col=(w-24)/3
            for i,(a,b) in enumerate([('01 / NGUỒN','Input + version + scope'),('02 / PHƯƠNG PHÁP','Feature / rule / missing'),('03 / KẾT QUẢ','Eligibility / score / reason')]):
                x=i*(col+12);box(x,0,col,69,a,b,i==2)
                if i<2:arrow(x+col,34,x+col+12,34)
            box(0,114,232,77,'04 / KIỂM ĐỘC LẬP','Cùng input/version; tính lại rule/score')
            box(266,114,w-266,77,'05 / ĐIỀU KIỆN ĐỔI Ý','Miền đã thử / unknown / bước kiểm tiếp')
            arrow(w-75,69,w-75,114);arrow(266,154,232,154)
            para('Mở được nguồn không đồng nghĩa nguồn đúng cho mọi vùng. Chưa có phép thử thì chưa ghi pass.',0,222,w,9,color=MUTED)
