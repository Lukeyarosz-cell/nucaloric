from PIL import Image,ImageDraw,ImageFont,ImageFilter
import numpy as np
from scipy.signal import butter,sosfilt
import math,pathlib,json,wave,subprocess,functools,sys
ROOT=pathlib.Path(__file__).resolve().parents[1];OUT=ROOT/'output';OUT.mkdir(exist_ok=True)
TL=json.loads((ROOT/'source/timeline.json').read_text());SC=TL['scenes'];D=TL['duration'];FPS=30;W,H=1920,1080
INK='#080809';PAPER='#f4f1ec';PINK='#e7b5c4';GRAY='#8b8586';DARK='#201c20'
FONT=ROOT/'source/Manrope.ttf'
def clamp(v):return min(1,max(0,v))
def ease(v):v=clamp(v);return 1-(1-v)**4
def spring(v):v=clamp(v);return 1- math.exp(-8*v)*math.cos(10*v) if v<1 else 1
@functools.lru_cache(256)
def font(size,weight=800):
 f=ImageFont.truetype(str(FONT),max(1,int(size)));f.set_variation_by_axes([weight]);return f
@functools.lru_cache(1024)
def typeimg(text,size,color,weight=800):
 f=font(size,weight);box=f.getbbox(text);im=Image.new('RGBA',(int(f.getlength(text))+12,box[3]-box[1]+12));ImageDraw.Draw(im).text((6,6-box[1]),text,font=f,fill=color);return im

def text(im,txt,x,y,size=100,color=INK,weight=800,progress=1,delay=0,angle=0,scale=1,anchor='left',mode='rise'):
 q=ease(progress-delay)
 if q<=0:return
 lay=typeimg(txt,size,color,weight).copy()
 if scale!=1:lay=lay.resize((max(1,int(lay.width*scale)),max(1,int(lay.height*scale))),Image.Resampling.BICUBIC)
 if angle:lay=lay.rotate(angle,Image.Resampling.BICUBIC,expand=True)
 if mode=='rise':y+=(1-q)*85
 elif mode=='slide':x-=(1-q)*160
 elif mode=='zoom':
  z=.7+.3*q;lay=lay.resize((int(lay.width*z),int(lay.height*z)),Image.Resampling.BICUBIC)
 if q<1:lay.putalpha(lay.getchannel('A').point(lambda a:int(a*q)))
 if anchor=='center':x-=lay.width/2
 im.paste(lay,(int(x),int(y)),lay)

def pill(im,label,x,y,fill=PINK,fg=INK,size=24,pad=23):
 f=font(size,700);w=int(f.getlength(label))+pad*2;h=size+pad
 ImageDraw.Draw(im).rounded_rectangle((int(x),int(y),int(x+w),int(y+h)),radius=h//2,fill=fill)
 text(im,label,x+pad-5,y+(h-size)/2-2,size,fg,700)
 return w

def arrow(dr,x,y,length=80,color=INK,width=8):
 dr.line((x,y,x+length,y),fill=color,width=width);dr.line((x+length-25,y-25,x+length,y,x+length-25,y+25),fill=color,width=width,joint='curve')

def badge(im,i,bg):
 color=INK if bg!=INK else PAPER
 text(im,'NUCALORIC',70,55,23,color,800)
 text(im,f'0{i+1} / BUILD SOMETHING REAL',70,1004,19,color,600)

def card(w,h,fill=PAPER):
 a=Image.new('RGBA',(w+40,h+40));dr=ImageDraw.Draw(a)
 dr.rounded_rectangle((20,28,w+20,h+28),radius=28,fill=(0,0,0,35))
 a=a.filter(ImageFilter.GaussianBlur(6));ImageDraw.Draw(a).rounded_rectangle((12,8,w+12,h+8),radius=26,fill=fill)
 return a

def place(im,lay,x,y,angle=0,scale=1):
 if scale!=1:lay=lay.resize((max(1,int(lay.width*scale)),max(1,int(lay.height*scale))),Image.Resampling.BICUBIC)
 if angle:lay=lay.rotate(angle,Image.Resampling.BICUBIC,expand=True)
 im.paste(lay,(int(x),int(y)),lay)

def circle(dr,cx,cy,r,fill,outline=None,width=1):
 if r>0:dr.ellipse((int(cx-r),int(cy-r),int(cx+r),int(cy+r)),fill=fill,outline=outline,width=width)

# Every scene has its own visual grammar, animated on the narration timeline.
def scene(i,t):
 dur=SC[i]['duration'];bg=[INK,PAPER,INK,PINK,INK,PAPER,PINK,INK][i]
 im=Image.new('RGB',(W,H),bg);dr=ImageDraw.Draw(im)
 if i==0:
  # A seed becomes a creation; bold typography hands off to a paper project card.
  if t<1.5:
   r=80+28*math.sin(t*2);circle(dr,1520,530,r,PINK)
   text(im,'EVERYTHING',100,300,154,PAPER,progress=(t-.15)/.6,mode='slide')
   text(im,'ON SOLANA.',100,475,154,PINK,progress=(t-.5)/.6,mode='slide')
   arrow(dr,1420,760,210,PINK,8)
  else:
   text(im,'STARTS WITH',105,215,100,PAPER,progress=(t-1.5)/.5)
   a=card(1200,405,PINK);text(a,'SOMETHING',70,45,148,INK);text(a,'YOU MADE.',70,208,148,INK)
   q=spring((t-1.9)/.65);place(im,a,140+(1-q)*100,370+(1-q)*780,angle=5-7*q)
   text(im,'YOUR IDEA IS THE START.',1230,825,26,PAPER,700,progress=(t-3.2)/.5)
   q=ease((t-3.2)/.8);dr.line((300,780,300+950*q,740),fill=PAPER,width=11)
 elif i==1:
  text(im,'GET YOUR',90,270,125,INK,progress=(t-.15)/.65,mode='slide')
  text(im,'PROJECT',90,408,125,INK,progress=(t-.35)/.65,mode='slide')
  text(im,'PLAN.',90,546,125,INK,progress=(t-.55)/.65,mode='slide')
  pill(im,'GIVE YOUR IDEA A DIRECTION',95,775,PINK)
  # Plan checklist enters with a spring and checkmarks draw in sequence.
  a=card(660,675,'#ffffff');text(a,'YOUR NEXT BIG THING',65,62,28,INK)
  text(a,'Project plan',65,120,60,INK)
  for k,(title,sub) in enumerate([('01  DEFINE','Find a useful problem.'),('02  EXPERIMENT','Try the tools. Test the idea.'),('03  BUILD','Make something people use.')]):
   y=225+k*130;ImageDraw.Draw(a).line((65,y-15,600,y-15),fill='#ded9d4',width=2)
   text(a,title,65,y,31,INK);text(a,sub,65,y+47,23,GRAY,500)
   q=ease((t-1-k*.65)/.35)
   if q>0:
    dd=ImageDraw.Draw(a);circle(dd,570,y+27,19,PINK);dd.line((559,y+27,567,y+35,583,y+17),fill=INK,width=4)
  q=spring((t-.3)/1);place(im,a,1070,205+(1-q)*900,angle=-5+2*math.sin(t*.6))
  circle(dr,1720,870,46+(5*math.sin(t*2)),INK);arrow(dr,1697,870,45,PAPER,5)
 elif i==2:
  for k,word in enumerate(['MAKE.','BREAK.','BUILD.']):
   text(im,word,90,245+k*153,133,PINK if k==2 else PAPER,progress=(t-.18-k*.28)/.55,mode='slide')
  text(im,'EXPERIMENT WITH TOOLING.',96,795,29,PAPER,700,progress=(t-.8)/.5)
  a=card(900,600,'#171517');ad=ImageDraw.Draw(a);ad.rounded_rectangle((12,8,912,80),radius=24,fill='#292429')
  for k in range(3):circle(ad,55+k*30,44,7,[PINK,PAPER,GRAY][k])
  text(a,'workspace / terminal',180,31,22,PAPER,600)
  commands=[('$ nucaloric init my-project',PINK),('project workspace ready',PAPER),('$ build --with api,hosting,cli',PINK),('tools connected',PAPER),('$ make something useful',PINK)]
  for k,(txt,col) in enumerate(commands):
   amount=int(clamp((t-.7-k*.57)/.55)*len(txt));text(a,txt[:amount],53,127+k*77,29,col,600)
  q=ease((t-.4)/.7);place(im,a,890+(1-q)*1100,250+12*math.sin(t),angle=2)
  pill(im,'IDEA → EXPERIMENT → PROJECT',990,895,PINK)
 elif i==3:
  text(im,'GO BEYOND',95,230,178,INK,progress=(t-.2)/.7,mode='slide')
  text(im,'TOKEN PARAMETERS.',102,440,94,INK,progress=(t-.55)/.7)
  if t<2.6:
   a=card(585,180,INK);text(a,'name / supply / symbol',55,49,30,PAPER,600);text(a,'THAT’S JUST THE START.',55,99,26,PINK)
   q=spring((t-1)/.6);place(im,a,1090,670+(1-q)*450,angle=-4)
  else:
   for k,(lab,icon) in enumerate([('HOSTING','↗'),('APIs','{ }'),('SCRIPTS','>_')]):
    q=spring((t-2.45-k*.16)/.7);a=card(490,210,PAPER)
    
    if k==0: arrow(ImageDraw.Draw(a),55,75,70,INK,6)
    else: text(a,icon,40,38,62,INK)
    text(a,lab,40,127,35,INK)
    place(im,a,105+k*575,675+(1-q)*420,angle=(k-1)*3)
   text(im,'MORE WAYS TO UTILIZE SOLANA.',100,575,29,INK,700,progress=(t-2.6)/.6)
 elif i==4:
  # Four product demonstrations slide horizontally rather than repeating title cards.
  cuts=[0,1.75,3.5,5.0];k=max(j for j,b in enumerate(cuts) if t>=b);u=t-cuts[k]
  titles=['HOSTING.','APIs.','SCRIPTS.','LOCAL MODELS.'];subs=['A place for your project to run.','Connect ideas to capabilities.','Build. Change. Run again.','Bring your own compute.']
  text(im,titles[k],90,235,119 if k<3 else 100,PINK,progress=u/.45,mode='slide')
  text(im,subs[k],98,397,32,PAPER,600,progress=(u-.22)/.5)
  a=card(730,650,PAPER);ad=ImageDraw.Draw(a)
  pill(a,['YOUR WORKSPACE','YOUR CONNECTIONS','YOUR COMMAND LINE','YOUR MODEL'][k],45,40,INK,PAPER,22)
  if k==0:
   for j in range(3):
    yy=130+j*142;ad.rounded_rectangle((45,yy,695,yy+112),radius=17,fill='#e8e3dc');text(a,['WEB / APP','DEVELOPMENT','COMPUTE'][j],75,yy+25,29,INK)
    circle(ad,646,yy+55,10,PINK);text(a,['Deploy your project','Tools for your workflow','Room to experiment'][j],75,yy+68,19,GRAY,600)
  elif k==1:
   for j,(x,y) in enumerate([(120,195),(535,195),(330,440)]):
    ad.line((355,330,x+45,y+45),fill=GRAY,width=4);ad.rounded_rectangle((x,y,x+115,y+95),radius=22,fill=PINK);text(a,['API','APP','SOL'][j],x+15,y+26,30,INK)
   circle(ad,355,330,52,INK);text(a,'{ }',355,301,42,PAPER,anchor='center')
   text(a,'CONNECT. BUILD. EXTEND.',70,570,29,INK)
  elif k==2:
   for j,line in enumerate(['$ git pull','$ npm run build','$ run deploy','ready for the next idea']):
    q=int(clamp((u-.35-j*.25)/.3)*len(line));text(a,line[:q],57,170+j*95,32,INK,600)
  else:
   for row in range(3):
    for col in range(4):
     x=115+col*160;y=195+row*125
     if col<3:ad.line((x,y,x+160,y),fill='#c0a3ac',width=3)
     if row<2:ad.line((x,y,x,y+125),fill='#c0a3ac',width=3)
     circle(ad,x,y,18+5*math.sin(t*4+row+col),PINK)
   text(a,'YOUR IDEAS. YOUR COMPUTE.',53,570,28,INK)
  q=spring(u/.7);place(im,a,1080+(1-q)*900,190+8*math.sin(t),angle=-3+math.sin(t))
  for j,lab in enumerate(['HOSTING','APIs','SCRIPTS','MODELS']):
   pill(im,lab,95+j*205,675,PINK if j==k else DARK,INK if j==k else PAPER,21)
  text(im,'AND MORE ROOM TO BUILD.',98,833,34,PAPER,progress=(t-6.65)/.6)
 elif i==5:
  text(im,'SELL WHAT',90,230,131,INK,progress=(t-.15)/.6,mode='slide')
  text(im,'YOU MAKE.',90,390,131,INK,progress=(t-.4)/.6,mode='slide')
  text(im,'TURN YOUR WORK',98,665,43,INK,700,progress=(t-.8)/.6)
  text(im,'INTO A PRODUCT.',98,725,43,INK,700,progress=(t-1.1)/.6)
  for k,(lab,detail) in enumerate([('YOUR API','A useful connection.'),('YOUR TOOL','A better workflow.'),('YOUR PRODUCT','Something people want.')]):
   a=card(590,355,[INK,PINK,'#ffffff'][k]);fg=PAPER if k==0 else INK
   pill(a,'BUILT BY YOU',48,38,PINK if k==0 else INK,INK if k==0 else PAPER,19)
   text(a,lab,48,140,49,fg);text(a,detail,48,220,25,fg,500)
   q=spring((t-.45-k*.5)/.8);place(im,a,1130-k*37,190+k*145+(1-q)*850,angle=8-k*7)
  if t>3.0:pill(im,'MAKE IT VALUABLE.',1020,870,INK,PAPER,24)
 elif i==6:
  # A small useful project becomes a connected community.
  text(im,'GROW YOUR',90,240,118,INK,progress=(t-.18)/.6,mode='slide')
  text(im,'PROJECTS.',90,380,118,INK,progress=(t-.4)/.6,mode='slide')
  text(im,'AND YOUR',95,610,62,INK,700,progress=(t-1.8)/.6)
  text(im,'COMMUNITY.',95,695,82,INK,progress=(t-2.1)/.6)
  cx,cy=1465,540;nodes=[]
  for j in range(12):
   q=ease((t-.75-j*.15)/.7);a=j*2.399;targ=160+35*(j%4);x=cx+math.cos(a+.08*t)*targ*q;y=cy+math.sin(a+.08*t)*targ*q
   if q>0:
    dr.line((cx,cy,x,y),fill='#b47c8f',width=4);circle(dr,x,y,(22+(j%3)*8)*q,PAPER if j%2 else INK)
  circle(dr,cx,cy,92+6*math.sin(t*1.5),INK);text(im,'YOU',cx,508,44,PAPER,anchor='center')
  if t>3.0:pill(im,'BUILT TOGETHER.',1320,902,PAPER,INK,23)
 elif i==7:
  # Brand lockup assembles, then a confident final statement fills the screen.
  q=ease((t-.12)/.85);circle(dr,960,520,360*q,PINK)
  if t<1.7:
   text(im,'NUCALORIC',960,421,137,INK,progress=(t-.25)/.65,anchor='center',mode='zoom')
  else:
   circle(dr,960,520,360,INK)
   text(im,'NUCALORIC',960,170,58,PINK,progress=(t-1.7)/.45,anchor='center')
   text(im,'UTILIZE SOLANA.',960,385,135,PAPER,progress=(t-1.7)/.6,anchor='center',mode='zoom')
   text(im,'FOR REAL.',960,570,167,PINK,progress=(t-4.0)/.6,anchor='center',mode='zoom')
   text(im,'BUILD SOMETHING THAT MATTERS.',960,853,26,PAPER,700,progress=(t-4.5)/.6,anchor='center')
 badge(im,i,bg)
 return im

# Isolated broadband swishes with stereo travel: no notes, beat or music bed.
SR=48000;N=round(D*SR);sfx=np.zeros((N,2));rng=np.random.default_rng(2718)
events=[]
for s in SC:
 events.append((s['start']+.04,.54,.28))
for idx,beats in {0:[1.5,1.9],1:[1.0,1.65,2.3],2:[.5,1.4,2.1],3:[2.45,2.64,2.82],4:[1.75,3.5,5.0],5:[.45,.95,1.45],6:[1.5,2.2],7:[1.7,4.0]}.items():
 for t in beats:events.append((SC[idx]['start']+t,.34,.16))
for k,(start,length,level) in enumerate(events):
 n=int(length*SR);u=np.linspace(0,1,n);noise=rng.normal(size=n)
 low=sosfilt(butter(2,1800,fs=SR,output='sos'),noise);high=sosfilt(butter(2,[1100,9500],btype='band',fs=SR,output='sos'),noise)
 envelope=np.sin(np.pi*u)**2*(.3+.7*u);sig=(low*(1-u)+high*u)*envelope
 sig/=max(np.max(np.abs(sig)),.001);sig*=level
 pan=u if k%2==0 else 1-u;stereo=np.stack((sig*np.sqrt(1-pan),sig*np.sqrt(pan)),axis=1)
 a=int(start*SR);b=min(a+n,N);sfx[a:b]+=stereo[:b-a]
with wave.open(str(OUT/'swoosh-effects.wav'),'wb') as f:
 f.setnchannels(2);f.setsampwidth(2);f.setframerate(SR);f.writeframes((np.clip(sfx,-.9,.9)*32767).astype('<i2').tobytes())
with wave.open(str(OUT/'voiceover.wav'),'rb') as f:voice=np.frombuffer(f.readframes(f.getnframes()),dtype='<i2').reshape(-1,2)/32768
# Keep effects underneath the spoken words.
activity=np.convolve(np.abs(voice[::480,0]),np.ones(9)/9,mode='same');gain=np.repeat(np.where(activity>.008,.48,1),480)[:N]
mix=voice+sfx*gain[:,None];peak=np.max(np.abs(mix))
if peak>.93:mix*=.93/peak
with wave.open(str(OUT/'voice-and-effects.wav'),'wb') as f:
 f.setnchannels(2);f.setsampwidth(2);f.setframerate(SR);f.writeframes((mix*32767).astype('<i2').tobytes())

if '--stills' in sys.argv:
 for i in range(8):scene(i,[3.9,3.2,3.0,4.0,4.8,3.3,3.8,5.2][i]).save(OUT/f'scene-{i+1:02}.jpg',quality=93)
 exit()
cmd=['ffmpeg','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-','-i',str(OUT/'voice-and-effects.wav'),'-c:v','libx264','-preset','fast','-crf','17','-pix_fmt','yuv420p','-c:a','aac','-b:a','256k','-movflags','+faststart','-shortest',str(OUT/'NUCALORIC-promo-v2.mp4')]
p=subprocess.Popen(cmd,stdin=subprocess.PIPE,stderr=open(OUT/'render.log','w'))
for f in range(round(D*FPS)):
 now=f/FPS;i=max(j for j,s in enumerate(SC) if s['start']<=now);local=now-SC[i]['start'];im=scene(i,local)
 # Alternating circle, diagonal and sliding reveals avoid dissolve title-card pacing.
 if i>0 and local<.58:
  prev=scene(i-1,SC[i-1]['duration']-.58+local);q=ease(local/.58);mask=Image.new('L',(W,H),0);md=ImageDraw.Draw(mask)
  if i%3==0:
   r=math.hypot(W,H)*q;circle(md,1600,300,r,255)
  elif i%3==1:
   x=-H+(W+H)*q;md.polygon([(0,0),(x+H,0),(x,H),(0,H)],fill=255)
  else:
   x=W*q;md.rectangle((0,0,int(x),H),fill=255)
  im=Image.composite(im,prev,mask)
 if f<12:im=Image.blend(Image.new('RGB',(W,H),INK),im,ease(f/12))
 p.stdin.write(im.tobytes())
 if f%(FPS*5)==0:print(f'Rendered {now:.0f}/{D:.1f}s',flush=True)
p.stdin.close();assert p.wait()==0
# Silent version and separate stems let the editor add their own music cleanly.
subprocess.run(['ffmpeg','-v','error','-y','-i',str(OUT/'NUCALORIC-promo-v2.mp4'),'-an','-c:v','copy',str(OUT/'NUCALORIC-promo-v2-silent.mp4')],check=True)
for i in range(8):scene(i,[3.9,3.2,3.0,4.0,4.8,3.3,3.8,5.2][i]).save(OUT/f'scene-{i+1:02}.jpg',quality=93)
print('Complete',flush=True)
