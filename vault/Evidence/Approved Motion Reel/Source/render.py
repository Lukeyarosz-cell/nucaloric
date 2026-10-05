from PIL import Image,ImageDraw,ImageFont,ImageFilter
import numpy as np, math,json,pathlib,functools,subprocess,sys,io
import cairosvg
from gpu import Glossy
ROOT=pathlib.Path(__file__).resolve().parents[1];OUT=ROOT/'output';OUT.mkdir(exist_ok=True)
TL=json.loads((ROOT/'source/timeline.json').read_text());SC=TL['scenes'];W,H,FPS,D=1920,1080,60,16
INK='#080809';PAPER='#f4f1ec';PINK='#e7b5c4';GRAY='#999295';P=TL['beat_period']
F=ROOT/'source/Manrope.ttf'
def clamp(x):return min(1,max(0,x))
def ease(x):x=clamp(x);return 1-(1-x)**4
def smooth(x):x=clamp(x);return x*x*(3-2*x)
def spring(x):x=clamp(x);return 1-math.exp(-8*x)*math.cos(11*x) if x<1 else 1
@functools.lru_cache(150)
def font(size,weight=800):
 f=ImageFont.truetype(str(F),int(size));f.set_variation_by_axes([weight]);return f
@functools.lru_cache(1024)
def typelayer(txt,size,col,weight=800):
 f=font(size,weight);b=f.getbbox(txt);im=Image.new('RGBA',(int(f.getlength(txt))+14,b[3]-b[1]+14))
 ImageDraw.Draw(im).text((7,7-b[1]),txt,font=f,fill=col);return im

def paste(im,lay,x,y,angle=0,scale=1,opacity=1,center=False):
 if scale!=1:lay=lay.resize((max(1,int(lay.width*scale)),max(1,int(lay.height*scale))),Image.Resampling.BICUBIC)
 if angle:lay=lay.rotate(angle,Image.Resampling.BICUBIC,expand=True)
 if opacity<1:
  lay=lay.copy();lay.putalpha(lay.getchannel('A').point(lambda a:int(a*clamp(opacity))))
 if center:x-=lay.width/2;y-=lay.height/2
 im.paste(lay,(int(x),int(y)),lay)

def text(im,txt,x,y,size=80,col=INK,weight=800,center=False,q=1,angle=0,scale=1):
 e=ease(q)
 if e<=0:return
 paste(im,typelayer(txt,size,col,weight),x,y+(1-e)*65,angle=angle,scale=scale,opacity=e,center=center)

def circ(dr,x,y,r,col,outline=None,width=1):
 if r>0:dr.ellipse((int(x-r),int(y-r),int(x+r),int(y+r)),fill=col,outline=outline,width=width)

def pill(im,label,x,y,col=PINK,fg=INK,size=22):
 f=font(size,700);w=int(f.getlength(label))+40;h=size+29
 ImageDraw.Draw(im).rounded_rectangle((x,y,x+w,y+h),radius=h//2,fill=col)
 text(im,label,x+16,y+13,size,fg,700)
 return w

def arrow(dr,x,y,l=55,col=INK,width=5):
 dr.line((x,y,x+l,y),fill=col,width=width);dr.line((x+l-18,y-18,x+l,y,x+l-18,y+18),fill=col,width=width)

def roundcard(w,h,col=PAPER):
 a=Image.new('RGBA',(w+48,h+48));dr=ImageDraw.Draw(a);dr.rounded_rectangle((20,30,w+20,h+30),radius=27,fill=(0,0,0,70));a=a.filter(ImageFilter.GaussianBlur(8))
 ImageDraw.Draw(a).rounded_rectangle((12,9,w+12,h+9),radius=26,fill=col)
 return a

# The supplied SVG is the final logo, rasterized at full output resolution.
svg=(ROOT/'source/nucaloric-wordmark.svg').read_text()
def logo(color):
 data=cairosvg.svg2png(bytestring=svg.replace('currentColor',color).encode(),output_width=1400,output_height=232)
 return Image.open(io.BytesIO(data)).convert('RGBA')
LOGO=logo(INK);SMALL_LOGO=logo(PAPER).resize((170,28),Image.Resampling.LANCZOS)
# Precomputed Fibonacci particles: genuine 3D projection, not a flat disc.
N=2100;j=np.arange(N);yy=1-2*(j+.5)/N;rr=np.sqrt(1-yy*yy);theta=j*2.39996322973
PARTS=np.stack([rr*np.cos(theta),yy,rr*np.sin(theta)],axis=1)
RAND=np.random.default_rng(21);RANDS=RAND.random(N)
GL=None

def beatpulse(t):
 times=np.array([b['time'] for b in TL['beats']]);u=t-times
 return float(np.max(np.where(u>=0,np.exp(-np.maximum(u,0)*14),0)))

def hud(im,t,dark=True,amount=1):
 if amount<=0:return
 a=Image.new('RGBA',(W,H));dr=ImageDraw.Draw(a);col=PAPER if dark else INK;fade=round(150*amount)
 rgb=tuple(int(col[k:k+2],16) for k in (1,3,5))+(fade,)
 # Fine viewfinder corners and tracking marks.
 for x,y,sx,sy in [(48,45,1,1),(W-48,45,-1,1),(48,H-45,1,-1),(W-48,H-45,-1,-1)]:
  dr.line((x+sx*62,y,x,y,x,y+sy*62),fill=rgb,width=2)
 for x in [W//2]:dr.line((x-10,45,x+10,45),fill=rgb,width=1)
 circ(dr,83,79,4,PINK if dark else INK)
 text(a,'REC',97,67,19,col,600)
 text(a,'NUCALORIC / MOTION REEL',1440,68,19,col,600)
 text(a,'REAL UTILITY',75,980,19,col,600)
 frame=int(t*FPS);tc=f'00:00:{frame//FPS:02}:{frame%FPS:02}'
 text(a,tc,1680,980,20,col,600)
 a.putalpha(a.getchannel('A').point(lambda z:int(z*.72*amount)));im.paste(a,(0,0),a)

# Shape contours interpolate continuously among circle, square and four-lobed cross.
def shape_points(cx,cy,r,kind,morph,rotation):
 a=np.linspace(0,2*np.pi,100,endpoint=False)+rotation
 def radius(which):
  if which==0:return np.full_like(a,r*.85)
  if which==1:return r*.77/(np.abs(np.cos(a))**7+np.abs(np.sin(a))**7)**(1/7)
  if which==2:return r*(.63+.26*np.cos(a*4))
  return r*(.65+.22*np.sin(a*3))
 rad=radius(kind%4)*(1-morph)+radius((kind+1)%4)*morph
 return list(zip(cx+rad*np.cos(a),cy+rad*np.sin(a)))

def dashboard(local,global_t):
 # A floating dashboard, then a cursor click opens a live-looking command workspace.
 click=9.55-SC[4]['start'];active=local>=click
 a=roundcard(1400,740,INK);dr=ImageDraw.Draw(a)
 dr.rounded_rectangle((12,9,1412,80),radius=26,fill='#242025')
 for k in range(3):circ(dr,47+k*25,44,6,[PINK,PAPER,GRAY][k])
 text(a,'nucaloric / project workspace',155,33,22,PAPER,600)
 dr.line((255,81,255,722),fill='#393137',width=2)
 for k,lab in enumerate(['OVERVIEW','WORKSPACE','APIs','TERMINAL']):
  y=153+k*74
  if k==(3 if active else 0):dr.rounded_rectangle((37,y-13,226,y+36),radius=10,fill=PINK)
  text(a,lab,51,y,21,INK if k==(3 if active else 0) else GRAY,700)
 text(a,'YOUR PROJECT',42,637,19,PAPER,700)
 text(a,'Build something real.',300,125,55,PAPER)
 text(a,'A workspace for your next useful idea.',306,204,25,GRAY,500)
 for k,(lab,sub) in enumerate([('HOSTING','Run your project.'),('APIs','Connect capabilities.'),('SCRIPTS','Make it your own.')]):
  x=305+k*345;dr.rounded_rectangle((x,284,x+320,459),radius=18,fill=PINK if k==0 else '#242025')
  fg=INK if k==0 else PAPER;text(a,lab,x+23,314,31,fg)
  text(a,sub,x+23,372,22,fg,500)
  if k==0:pill(a,'OPEN WORKSPACE',x+22,410,INK,PAPER,16)
 dr.rounded_rectangle((306,486,1327,686),radius=19,fill='#141215',outline='#41333b',width=2)
 if active:
  lines=['$ npm run build','project ready','Your next idea starts here.']
  for k,line in enumerate(lines):
   count=int(clamp((local-click-.04-k*.14)/.3)*len(line))
   text(a,line[:count],335,512+k*49,25,PINK if k==0 else PAPER,600)
 else:
  text(a,'YOUR IDEA. YOUR WORKSPACE.',338,517,32,PAPER)
  text(a,'Hosting, APIs, scripts, and more.',338,575,25,GRAY,500)
  pill(a,'MAKE SOMETHING USEFUL',340,627,'#32252c',PINK,18)
 # Cursor crosses the interface on a bezier path and visibly clicks the CTA.
 u=smooth((local-.7)/1.35);sx,sy=1240,635;tx,ty=471,435
 cx=sx+(tx-sx)*u;cy=sy+(ty-sy)*u-135*math.sin(u*math.pi)
 if local<click+.55:
  cursor=Image.new('RGBA',(55,75));cd=ImageDraw.Draw(cursor)
  cd.polygon([(4,3),(4,54),(17,42),(28,66),(40,60),(28,37),(48,35)],fill=PAPER,outline=INK,width=3)
  paste(a,cursor,cx,cy)
  if local>=click:
   q=clamp((local-click)/.55);dr.ellipse((cx-80*q,cy-80*q,cx+80*q,cy+80*q),outline=PINK,width=max(1,int(5*(1-q))))
 return a

# Each segment is anchored to four or eight beats in the actual replacement audio.
def scene(i,t,global_t):
 pulse=beatpulse(global_t)
 if i==0:
  b=min(3,int(t/P));bg=[INK,PINK,INK,INK][b];fg=[PAPER,INK,PINK,PAPER][b]
  im=Image.new('RGB',(W,H),bg);dr=ImageDraw.Draw(im)
  u=t-b*P;q=ease(u/.18)
  if b<3:
   word=['BUILD','SOMETHING','REAL.'][b];size=[210,168,242][b]
   # Elastic scale, rotation, and a trailing echo provide kinetic motion on each word.
   z=.74+.26*spring(u/.28);angle=(-6 if b%2 else 5)*(1-q)
   for trail in [2,1]:paste(im,typelayer(word,size,fg),960-trail*(1-q)*40,520+trail*(1-q)*12,center=True,angle=angle,scale=z,opacity=(1-q)*.2)
   text(im,word,960,520,size,fg,center=True,angle=angle,scale=z)
   circ(dr,1640,290,25+16*pulse,fg);dr.line((230,820,230+1460*q,820),fill=fg,width=3)
  else:
   text(im,'BUILD SOMETHING',960,395,112,PAPER,center=True,q=u/.16)
   text(im,'REAL.',960,610,218,PINK,center=True,q=(u-.08)/.18)
  return im,True if bg==INK else False
 if i==1:
  im=Image.new('RGB',(W,H),PINK);dr=ImageDraw.Draw(im)
  cycle=t/P;step=int(cycle);m=smooth((cycle-step)*1.5)
  for row in range(3):
   for col in range(5):
    cx=320+col*320;cy=260+row*275;r=107+10*pulse
    pts=shape_points(cx,cy,r,(row+col+step)%4,m,t*.28*(1 if col%2 else -1))
    dr.polygon(pts,fill=INK if (row+col)%3 else PAPER)
  # The final beat pulls all shapes toward the centre and the sphere takes over.
  text(im,'BEYOND TOKEN PARAMETERS.',960,925,34,INK,700,center=True,q=(t-.15)/.4)
  return im,False
 if i==2:
  im=Image.new('RGB',(W,H),INK);dr=ImageDraw.Draw(im);glow=Image.new('RGBA',(W,H));gd=ImageDraw.Draw(glow)
  angle=t*.95;c,s=math.cos(angle),math.sin(angle);xx=PARTS[:,0]*c+PARTS[:,2]*s;zz=-PARTS[:,0]*s+PARTS[:,2]*c;yy=PARTS[:,1]
  tilt=.2*math.sin(t);y2=yy*math.cos(tilt)-zz*math.sin(tilt);z2=yy*math.sin(tilt)+zz*math.cos(tilt)
  radius=(335+25*pulse)*(1+.055*t);persp=3.1/(3.1-z2*.38);px=1240+xx*radius*persp;py=540+y2*radius*persp
  for k in np.argsort(z2):
   size=1.0+(z2[k]+1)*1.1;bright=clamp((z2[k]+1)/2);rgb=(int(110+121*bright),int(73+108*bright),int(89+107*bright))
   circ(dr,px[k],py[k],size,rgb)
   if z2[k]>.6 and RANDS[k]>.82:circ(gd,px[k],py[k],size*2,(231,181,196,100))
  glow=glow.filter(ImageFilter.GaussianBlur(4));im.paste(glow,(0,0),glow)
  for k,word in enumerate(['IDEAS','INTO','UTILITY.']):text(im,word,135,305+k*140,109,PINK if k==2 else PAPER,q=(t-k*.12)/.32)
  text(im,'MORE WAYS TO UTILIZE SOLANA.',140,816,23,GRAY,600,q=(t-.5)/.3)
  return im,True
 if i==3:
  global GL
  if GL is None:GL=Glossy(W,H)
  im=GL.render(t+.35,pulse)
  # Glossy liquid form carries the screen, with type anchored in negative space.
  text(im,'MAKE IT',160,305,92,PAPER,q=t/.3)
  text(im,'USEFUL.',160,425,108,PINK,q=(t-.12)/.3)
  pill(im,'REAL PROJECTS. REAL POSSIBILITIES.',158,700,'#2d1c27',PINK,19)
  # A miniature glossy satellite adds depth as the large form moves in orbit.
  return im,True
 if i==4:
  im=Image.new('RGB',(W,H),PAPER);dr=ImageDraw.Draw(im)
  # Large soft branded light behind the interface, as in the supplied references.
  light=Image.new('RGBA',(W,H));ld=ImageDraw.Draw(light);circ(ld,1530,645,330,(231,181,196,190));light=light.filter(ImageFilter.GaussianBlur(90));im.paste(light,(0,0),light)
  a=dashboard(t,global_t)
  q=spring(t/.8);zoom=1+smooth((t-2.45)/.5)*.22
  angle=-4*(1-ease(t/1.5));paste(im,a,960,540+(1-q)*950,angle=angle,scale=zoom,center=True)
  text(im,'HOST. CONNECT. RUN.',960,914,30,INK,center=True,q=(t-.5)/.4)
  return im,False
 if i==5:
  im=Image.new('RGB',(W,H),PINK);dr=ImageDraw.Draw(im)
  # Moving diagonal shutters expose words exactly on the quarter-note hits.
  b=min(3,int(t/P));u=t-b*P;word=['BUILD.','SELL.','GROW.','CREATE.'][b]
  shift=180*ease(u/.35)
  for k in range(-8,24):
   x=k*160+shift;dr.polygon([(x-260,0),(x-190,0),(x+350,H),(x+280,H)],fill=INK)
  cover=Image.new('RGBA',(W,H));cd=ImageDraw.Draw(cover);cd.rounded_rectangle((390,360,1530,700),radius=170,fill=PAPER if b%2==0 else INK)
  text(cover,word,960,530,156,INK if b%2==0 else PINK,center=True,scale=.8+.2*spring(u/.26))
  im.paste(cover,(0,0),cover)
  return im,False
 if i==6:
  im=Image.new('RGB',(W,H),INK);dr=ImageDraw.Draw(im)
  # A moving halftone field grows from tiny points to overlapping discs.
  phase=t/(SC[6]['duration']);beat=int(t/P);spacing=45
  for y in range(-30,H+spacing,spacing):
   for x in range(-30,W+spacing,spacing):
    wave=.5+.5*math.sin(x*.007+y*.008-t*5);r=(4+15*wave)*(1+.35*pulse)
    circ(dr,x+(20*math.sin(t*2)),y,r,PINK if beat%2 else PAPER)
  a=roundcard(1060,270,INK);text(a,'FOR REAL.',550,139,138,PINK,center=True)
  paste(im,a,960,540,center=True,angle=2*math.sin(t*3))
  return im,True
 # Actual brand mark finishes the reel, revealed from travelling strips.
 im=Image.new('RGB',(W,H),PAPER);dr=ImageDraw.Draw(im)
 duration=SC[7]['duration'];u=ease(t/.4)
 # Pink seed contracts into the branded logo reveal.
 if t<.38:circ(dr,960,510,820*(1-u),PINK)
 mask=Image.new('L',LOGO.size,0);md=ImageDraw.Draw(mask)
 for k in range(14):
  q=ease((t-k*.008)/.31);x=k*100;md.rectangle((x,0,x+100,int(LOGO.height*q)),fill=255)
 lay=LOGO.copy();lay.putalpha(Image.fromarray(np.minimum(np.array(lay.getchannel('A')),np.array(mask)).astype('uint8')))
 paste(im,lay,960,470,center=True,scale=.98+.02*smooth(t/.7))
 text(im,'UTILIZE SOLANA. FOR REAL.',960,683,42,INK,700,center=True,q=(t-.22)/.35)
 dr.line((640,780,640+640*ease((t-.4)/.5),780),fill=PINK,width=5)
 return im,False

# Both reference videos are inspiration only; no watermark or footage is reused.
def frame_at(now):
 i=max(k for k,s in enumerate(SC) if now>=s['start']);local=now-SC[i]['start'];im,dark=scene(i,local,now)
 if i in [5,6,7] and local<.25:
  prev,_=scene(i-1,SC[i-1]['duration']-.25+local,now-.25);q=ease(local/.25);mask=Image.new('L',(W,H),0);md=ImageDraw.Draw(mask)
  if i==5:
   for k in range(-9,26):
    x=k*160;ww=165*q;md.polygon([(x-260,0),(x-260+ww,0),(x+350+ww,H),(x+350,H)],fill=255)
  else:
   for y in range(-30,H+45,45):
    for x in range(-30,W+45,45):circ(md,x,y,35*q,255)
  im=Image.composite(im,prev,mask)
 if i>0 and local<.18 and i not in [5,6,7]:
  prev,_=scene(i-1,SC[i-1]['duration']-.18+local,now-.18);q=ease(local/.18)
  if i%2:
   # Venetian strip wipe: alternating directions create a quick shutter transition.
   mask=Image.new('L',(W,H),0);md=ImageDraw.Draw(mask)
   for k in range(12):
    x=k*160;h=int(H*clamp(q*1.2-(k%3)*.07));md.rectangle((x,0 if k%2==0 else H-h,x+160,h if k%2==0 else H),fill=255)
   im=Image.composite(im,prev,mask)
  else:
   mask=Image.new('L',(W,H),0);md=ImageDraw.Draw(mask);r=math.hypot(W,H)*q;circ(md,960,540,r,255);im=Image.composite(im,prev,mask)
 # Global HUD with a quiet fade-out for the logo lockup.
 hud(im,now,dark,amount=1-smooth((now-SC[-1]['start'])/.45) if i==7 else 1)
 return im

if '--stills' in sys.argv:
 for i,s in enumerate(SC):frame_at(s['start']+min(s['duration']*.62,1.2)).save(OUT/f'scene-{i+1:02}.jpg',quality=95)
 montage=Image.new('RGB',(1280,1440))
 for i in range(8):montage.paste(Image.open(OUT/f'scene-{i+1:02}.jpg').resize((640,360)),((i%2)*640,(i//2)*360))
 montage.save(OUT/'storyboard.jpg',quality=94);print('Stills complete');exit()
# Preserve the replacement music, taking a sixteen-second phrase from its drop.
audio=ROOT/'reference'/TL['audio_file']
if not audio.exists():audio=pathlib.Path('/home/luke/Downloads')/TL['audio_file']
subprocess.run(['ffmpeg','-v','error','-y','-ss',str(TL['audio_offset']),'-i',str(audio),'-t','16','-af','afade=t=in:d=0.004,afade=t=out:st=15.92:d=0.08','-ar','48000','-ac','2',str(OUT/'soundtrack-16s.wav')],check=True)
cmd=['ffmpeg','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r','60','-i','-','-i',str(OUT/'soundtrack-16s.wav'),'-c:v','libx264','-preset','fast','-crf','16','-pix_fmt','yuv420p','-c:a','aac','-b:a','320k','-movflags','+faststart','-t','16',str(OUT/'NUCALORIC-motion-reel-16s-60fps.mp4')]
p=subprocess.Popen(cmd,stdin=subprocess.PIPE,stderr=open(OUT/'render.log','w'))
for n in range(960):
 now=n/FPS;im=frame_at(now);p.stdin.write(im.tobytes())
 if n%120==0:print(f'Rendered {now:.0f}/16 seconds',flush=True)
p.stdin.close();assert p.wait()==0
subprocess.run(['ffmpeg','-v','error','-y','-i',str(OUT/'NUCALORIC-motion-reel-16s-60fps.mp4'),'-an','-c:v','copy',str(OUT/'NUCALORIC-motion-reel-silent.mp4')],check=True)
print('Render complete',flush=True)
