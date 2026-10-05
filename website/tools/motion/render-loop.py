import sys,pathlib,subprocess,math
from gpu import Glossy
r=pathlib.Path(__file__).resolve().parents[2]/'assets/motion';g=Glossy(960,720)
p=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s','960x720','-r','30','-i','-','-an','-c:v','libx264','-preset','fast','-crf','23','-pix_fmt','yuv420p','-movflags','+faststart',str(r/'possibilities-loop.mp4')],stdin=subprocess.PIPE)
for frame in range(240):
 t=frame/30;u=.35+1.45*(.5-.5*math.cos(t*2*math.pi/8));im=g.render(u,0)
 if frame==30:im.save(r/'possibilities-poster.jpg',quality=92)
 p.stdin.write(im.tobytes())
p.stdin.close();assert p.wait()==0
print('Eight-second seamless silent loop complete')
