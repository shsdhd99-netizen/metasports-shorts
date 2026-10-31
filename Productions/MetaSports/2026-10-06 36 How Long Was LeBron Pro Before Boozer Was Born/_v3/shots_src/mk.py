import sys
from PIL import Image, ImageDraw, ImageFont
P=sys.argv[1]
W,H=1080,1920
NAVY=(16,32,64); WHITE=(255,255,255); ORG=(255,122,40); GREY=(160,176,200)
def F(sz): return ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", sz)
def ctr(d,y,t,f,fill):
    w=d.textlength(t,font=f); d.text(((W-w)/2,y),t,font=f,fill=fill)
def card(name,top,big,l1,l2,src,bs=250):
    im=Image.new("RGB",(W,H),NAVY); d=ImageDraw.Draw(im)
    ctr(d,230,top,F(54),GREY); ctr(d,380+(250-bs)//2,big,F(bs),ORG); ctr(d,730,l1,F(70),WHITE); ctr(d,830,l2,F(52),GREY)
    ctr(d,1560,src,F(38),GREY); im.save(P+"\\shots_src\\"+name+".png")
card("c_75","CARLOS BOOZER, 2003-04 CAVALIERS","75","STARTS","beside rookie LeBron","Basketball-Reference")
card("c_34","LAST FINALS GAME TO BIRTH","34","DAYS","June 14 to July 18, 2007","Basketball-Reference, Cameron Boozer's birth date")
card("c_24","LEBRON JAMES","YEAR 24","","the oldest player in the league","Hoops Rumors, Oct 4 2026",bs=190)


