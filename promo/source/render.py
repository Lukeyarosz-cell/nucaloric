from PIL import Image, ImageDraw, ImageFont
import numpy as np, math, subprocess, wave, pathlib, json
ROOT=pathlib.Path(__file__).resolve().parents[1]; OUT=ROOT/'output'; OUT.mkdir(exist_ok=True)
W,H,FPS=1920,1080,24
scenes=[(6,['Everything on Solana','starts with something','you made.'],'01 / THE IDEA'),(5,['Get your project plan.','Experiment with tooling.','Open what’s possible.'],'02 / BUILD'),(6,['Expand the capabilities','of the Solana chain.'],'03 / NUCALORIC'),(5,['More than just','token parameters.'],'04 / REAL UTILITY'),(7,['HOSTING. APIs.','SCRIPTS. AND MORE.'],'05 / YOUR WORKSPACE'),(5,['Sell what you make.'],'06 / CREATE VALUE'),(5,['Grow your projects.','Grow your community.'],'07 / KEEP BUILDING'),(6,['NUCALORIC','Utilize Solana.','For real.'],'08 / START SOMETHING')]
D=sum(s[0] for s in scenes); pink=(231,181,196); white=(244,241,236)
fontpath=str(ROOT/'source/Manrope.ttf'); fonts={s:ImageFont.truetype(fontpath,s) for s in [24,30,36,76,92,112]}
starts=np.cumsum([0]+[x[0] for x in scenes]).tolist()
# Original stereo synth score, transition swells, clicks and low impacts.
SR=48000; t=np.arange(D*SR)/SR; snd=np.zeros(len(t))
for k in range(int(D*2)):
 start=k*.5; mask=(t>=start)&(t<start+.42); u=t[mask]-start
 freq=[110,138.59,164.81,123.47][(k//8)%4]
 snd[mask]+=.12*np.sin(2*np.pi*freq*u)*np.exp(-u*9)
 if k%2==0:snd[mask]+=.16*np.sin(2*np.pi*(48*u+32*(1-np.exp(-u*18))/18))*np.exp(-u*16)
rng=np.random.default_rng(42)
for b in starts[:-1]:
 mask=(t>=b)&(t<b+.8); u=t[mask]-b
 snd[mask]+=.12*rng.normal(size=len(u))*np.exp(-u*12)+.18*np.sin(2*np.pi*65*u)*np.exp(-u*6)
 if b>0:
  mask=(t>=b-.65)&(t<b);u=(t[mask]-(b-.65))/.65
  snd[mask]+=.075*rng.normal(size=len(u))*u**3
snd*=np.minimum(t/1.2,1)*np.minimum((D-t)/2,1);snd=np.tanh(snd)*.85
stereo=np.stack([snd,np.roll(snd,240)*.96],axis=1)
with wave.open(str(OUT/'original-score.wav'),'wb') as f:
 f.setnchannels(2);f.setsampwidth(2);f.setframerate(SR);f.writeframes((stereo*32767).astype('<i2').tobytes())
cmd=['ffmpeg','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-','-i',str(OUT/'original-score.wav'),'-c:v','libx264','-preset','fast','-crf','18','-pix_fmt','yuv420p','-c:a','aac','-b:a','256k','-movflags','+faststart',str(OUT/'NUCALORIC-promo.mp4')]
p=subprocess.Popen(cmd,stdin=subprocess.PIPE,stderr=open(OUT/'render.log','w'))
for frame in range(D*FPS):
 now=frame/FPS;i=max(j for j,b in enumerate(starts[:-1]) if b<=now);dur,lines,label=scenes[i];local=now-starts[i]
 light=i in [1,3,6];bg=white if light else (5,5,5);fg=(5,5,5) if light else white
 im=Image.new('RGB',(W,H),bg);dr=ImageDraw.Draw(im)
 for x in range(70,W,60):
  for y in range(70,H,60):
   r=1.2+1.3*(.5+.5*math.sin(x*.009+y*.011-now*1.7));dr.ellipse((x-r,y-r,x+r,y+r),fill=(210,204,199) if light else (29,27,30))
 dr.text((90,60),'NUCALORIC',font=fonts[30],fill=fg);dr.text((90,985),label,font=fonts[24],fill=(150,99,119) if light else pink)
 dr.line((90,945,1830,945),fill=(190,178,178) if light else (50,44,48),width=2)
 dr.line((90,945,90+1740*now/D,945),fill=pink,width=5)
 # Animated orbit of pink particles links each scene.
 cx,cy=1530,490
 for k in range(110):
  a=k*2.399+now*.35;rad=125+90*math.sin(k*.27+now*.7);x=cx+math.cos(a)*rad;y=cy+math.sin(a)*rad;r=3+(k%4)
  dr.ellipse((x-r,y-r,x+r,y+r),fill=pink if not light else (177,112,137))
 size=112 if i==7 else 92 if max(map(len,lines))<25 else 76
 y0=365-(len(lines)-2)*40
 for k,line in enumerate(lines):
  q=min(1,max(0,(local-.14*k)/.7));ease=1-(1-q)**3
  if q>0:
   color=pink if (k==len(lines)-1 or i==4) and not light else fg
   # Fade and rise each line.
   color=tuple(int(bg[z]+(color[z]-bg[z])*q) for z in range(3))
   dr.text((90,y0+k*(size+24)+int((1-ease)*60)),line,font=fonts[size],fill=color)
 if i==4:dr.text((95,760),'CLI WORKSPACES  /  WEBSITES  /  MODEL WORKLOADS',font=fonts[24],fill=pink)
 if i==7:dr.text((95,820),'BUILD SOMETHING THAT MATTERS.',font=fonts[24],fill=pink)
 fade=min(1,local/.2,(dur-local)/.25)
 if fade<1:im=Image.blend(Image.new('RGB',(W,H),(5,5,5)),im,max(0,fade))
 if frame in [60,starts[4]*FPS+60,starts[7]*FPS+72]:im.save(OUT/f'preview-{i+1}.jpg')
 p.stdin.write(im.tobytes())
 if frame%(FPS*5)==0:print(f'Rendered {now:.0f}/{D}s',flush=True)
p.stdin.close();code=p.wait();assert code==0
# Standard EDL import for a Resolve timeline with a pre-rendered master.
(OUT/'NUCALORIC.edl').write_text('TITLE: NUCALORIC PROMO\nFCM: NON-DROP FRAME\n\n001  AX       V     C        00:00:00:00 00:00:45:00 01:00:00:00 01:00:45:00\n* FROM CLIP NAME: NUCALORIC-promo.mp4\n')
(ROOT/'README.md').write_text('NUCALORIC motion promo\n======================\n\n45 seconds, 1920×1080, 24fps. Original synthesized music and effects; no voiceover.\n\noutput/NUCALORIC-promo.mp4 is the finished video. output/original-score.wav is the separate score. source/render.py regenerates all animation and sound. Manrope is bundled with its OFL license.\n\nDaVinci Resolve: import the MP4 into a 24fps timeline, or import output/NUCALORIC.edl and link the MP4. This is a rendered clip with an EDL, not a native layered Resolve project. The editable animation lives in source/render.py.\n\nHosting and tooling scenes communicate the product direction; live paid provisioning is not connected in the website yet.\n')
print('Complete',flush=True)
