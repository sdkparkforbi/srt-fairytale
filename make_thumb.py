# -*- coding: utf-8 -*-
"""그림책 썸네일(1200x630) — 곰돌이와 위험 도깨비."""
from PIL import Image, ImageDraw, ImageFont

W,H=1200,630
img=Image.new("RGB",(W,H),"#FFF7EA")
d=ImageDraw.Draw(img)
top=(255,230,194); bot=(252,222,212)
for y in range(H):
    t=y/H
    d.line([(0,y),(W,y)],fill=(int(top[0]+(bot[0]-top[0])*t),int(top[1]+(bot[1]-top[1])*t),int(top[2]+(bot[2]-top[2])*t)))
d.rounded_rectangle([34,34,W-34,H-34],radius=40,outline="#F0DFC0",width=4)

malgunbd="C:/Windows/Fonts/malgunbd.ttf"; malgun="C:/Windows/Fonts/malgun.ttf"
def F(p,s): return ImageFont.truetype(p,s)

# sun
d.ellipse([980,70,1110,200],fill="#F2B441")

# ground
d.ellipse([90,470,640,560],fill="#EADCC2")

# bear (left)
bx,by=300,360
d.ellipse([bx-78,by+5,bx+78,by+115],fill="#A9866B")
d.ellipse([bx-62,by-58,bx+62,by+46],fill="#A9866B")
d.ellipse([bx-66,by-92,bx-30,by-56],fill="#A9866B"); d.ellipse([bx+30,by-92,bx+66,by-56],fill="#A9866B")
d.ellipse([bx-58,by-86,bx-36,by-64],fill="#caa985"); d.ellipse([bx+36,by-86,bx+58,by-64],fill="#caa985")
d.ellipse([bx-30,by-22,bx-14,by-6],fill="#33384D"); d.ellipse([bx+14,by-22,bx+30,by-6],fill="#33384D")
d.ellipse([bx-12,by+2,bx+12,by+20],fill="#6b4f3a")
d.arc([bx-20,by+12,bx+20,by+40],start=10,end=170,fill="#5b4030",width=5)

# goblin (peeking, upper right of bear)
gx,gy=470,250
d.ellipse([gx-40,gy-34,gx+40,gy+34],fill="#9B6A9E")
d.polygon([(gx-34,gy-14),(gx-58,gy-36),(gx-46,gy-8)],fill="#7d5380")
d.polygon([(gx+34,gy-14),(gx+58,gy-36),(gx+46,gy-8)],fill="#7d5380")
d.ellipse([gx-18,gy-8,gx-2,gy+8],fill="#fff"); d.ellipse([gx+2,gy-8,gx+18,gy+8],fill="#fff")
d.ellipse([gx-14,gy-5,gx-6,gy+3],fill="#33384D"); d.ellipse([gx+6,gy-5,gx+14,gy+3],fill="#33384D")
d.arc([gx-14,gy+8,gx+14,gy+24],start=10,end=170,fill="#3c2540",width=4)
d.text((gx,gy+52),"위험 도깨비",font=F(malgunbd,22),fill="#6c4570",anchor="mm")

# title (right)
tx=600
d.rounded_rectangle([tx,90,tx+340,142],radius=26,fill="#fff",outline="#E8775A",width=3)
d.text((tx+170,116),"아주 쉬운 그림책",font=F(malgunbd,26),fill="#cf5a3e",anchor="mm")
d.text((tx,170),"곰돌이 은행과",font=F(malgunbd,76),fill="#43392f")
d.text((tx,258),"위험 도깨비",font=F(malgunbd,76),fill="#E8775A")
d.text((tx,372),"~ SRT(중요위험이전) 마법 이야기 ~",font=F(malgun,30),fill="#2E8B8B")
d.text((tx,430),"위험 도깨비만 기사님에게 맡기면",font=F(malgun,26),fill="#8a7252")
d.text((tx,466),"묶였던 비상금이 스르르 풀려요!",font=F(malgun,26),fill="#8a7252")
d.text((tx,520),"우리 12개 은행 합치면 약 23조원이 풀립니다",font=F(malgunbd,24),fill="#cf5a3e")

img.save("assets/thumbnail.png","PNG")
print("saved assets/thumbnail.png",img.size)
