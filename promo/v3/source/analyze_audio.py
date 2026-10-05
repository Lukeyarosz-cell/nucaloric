import wave,pathlib,json,numpy as np,subprocess
from scipy.signal import stft,find_peaks,butter,sosfilt
from PIL import Image,ImageDraw
R=pathlib.Path(__file__).resolve().parents[1]
if not (R/'reference/user-audio.wav').exists():
 audio=R/'reference/tiktokdownload.online_1791156644577.mp3'
 subprocess.run(['ffmpeg','-v','error','-y','-i',str(audio),'-ar','48000','-ac','2',str(R/'reference/user-audio.wav')],check=True)
with wave.open(str(R/'reference/user-audio.wav'),'rb') as f:
 sr=f.getframerate();x=np.frombuffer(f.readframes(f.getnframes()),dtype='<i2').reshape(-1,2)/32768
mono=x.mean(axis=1);low=sosfilt(butter(3,[35,190],btype='bandpass',fs=sr,output='sos'),mono)
hop=480; n=len(mono)//hop;energy=np.sqrt(np.mean(low[:n*hop].reshape(n,hop)**2,axis=1));wide=np.sqrt(np.mean(mono[:n*hop].reshape(n,hop)**2,axis=1))
flux=np.maximum(0,energy-np.roll(energy,3))+np.maximum(0,wide-np.roll(wide,2))*.18
peaks,props=find_peaks(flux,distance=18,prominence=max(.002,float(np.percentile(flux,80))*.6))
rank=sorted(zip(peaks/100,props['prominences']),key=lambda z:z[1],reverse=True)
print('Strongest hits:',[(round(t,2),round(float(a),3)) for t,a in rank[:25]])
# Select a full sixteen seconds; bias toward the first musical phrase when energy is comparable.
candidates=[]
for offset in [0]+[round(t,2) for t,a in rank[:50] if t<len(mono)/sr-16]:
 idx=int(offset*100);seg=wide[idx:idx+1600]; hits=sum(a for t,a in rank if offset<=t<offset+16)
 candidates.append((float(np.mean(seg))*.5+hits*.02-.00006*offset,offset))
print('Best windows:',sorted(candidates,reverse=True)[:10])
im=Image.new('RGB',(1600,450),'#080809');dr=ImageDraw.Draw(im)
for i in range(1600):
 a=wide[int(i*n/1600)];dr.line((i,240-a*550,i,240+a*550),fill='#e7b5c4')
for t,a in rank[:100]:
 xx=t/(len(mono)/sr)*1600;dr.line((xx,50,xx,80),fill='#f4f1ec')
for sec in range(0,int(len(mono)/sr)+1,5):dr.text((sec/(len(mono)/sr)*1600,400),str(sec),fill='white')
im.save(R/'reference/audio-waveform.jpg')
(R/'source/audio-analysis.json').write_text(json.dumps({'sample_rate':sr,'duration':len(mono)/sr,'hits':sorted([{'time':float(t),'strength':float(a)} for t,a in rank],key=lambda z:z['time']),'best_windows':[{'offset':b,'score':a} for a,b in sorted(candidates,reverse=True)[:10]]},indent=2))
