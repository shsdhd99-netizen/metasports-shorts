import sys
from PIL import Image, ImageDraw, ImageFont
P=sys.argv[1]
W,H=1080,1920
NAVY=(16,32,64); WHITE=(255,255,255); ORG=(255,122,40); GREY=(160,176,200)
def F(sz): return ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", sz)
def ctr(d,y,t,f,fill):
    w=d.textlength(t,font=f); d.text(((W-w)/2,y),t,font=f,fill=fill)
def base():
    im=Image.new("RGB",(W,H),NAVY); return im,ImageDraw.Draw(im)
# keep every number above y=1040: the captions sit at about 55-65% of the height
im,d=base()
ctr(d,200,"CAREER FIELD GOAL %",F(56),GREY)
ctr(d,330,"LeBron",F(78),WHITE); ctr(d,420,"50.7%",F(230),ORG)
ctr(d,700,"Kobe",F(78),WHITE); ctr(d,790,"44.7%",F(230),GREY)
ctr(d,1560,"Regular season - Basketball-Reference",F(38),GREY)
im.save(P+r"\shots_src\c_fg.png")
def att(path,both):
    im,d=base()
    ctr(d,200,"MOST SHOTS TAKEN, ALL TIME",F(56),GREY)
    ctr(d,330,"LeBron",F(78),WHITE); ctr(d,420,"31,502",F(230),ORG)
    if both:
        ctr(d,700,"Kareem",F(78),WHITE); ctr(d,790,"28,307",F(230),GREY)
    ctr(d,1560,"Regular season - Basketball-Reference",F(38),GREY)
    im.save(path)
att(P+r"\shots_src\c_att1.png",False); att(P+r"\shots_src\c_att2.png",True)


