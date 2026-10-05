from pathlib import Path
import math,re,html
root=Path(__file__).resolve().parents[1]
svg=(root/'source/nucaloric-wordmark.svg').read_text();inner=svg[svg.find('>')+1:svg.rfind('</svg>')];vb=re.search('viewBox="([^"]+)"',svg).group(1)
concepts={'make':['MAKE','SOMETHING','REAL.'],'mind':['A MIND.','A PURPOSE.','A PROJECT.'],'together':['START SMALL.','BUILD','TOGETHER.']}
for fmt,w,h in [('landscape',1920,1080),('portrait',1080,1920),('square',1080,1080)]:
 for name,lines in concepts.items():
  pad=w*.075;top=h*.24;fs=w*(.125 if h>w else .09);lh=fs*1.08
  elements=[f'<rect width="{w}" height="{h}" fill="#080809"/>']
  gap=26 if h>w else 30
  for y in range(int(h*.42),int(h-pad),gap):
   for x in range(int(pad),int(w-pad),gap):
    nx=x/w;ny=y/h;crest=.71+.065*math.sin(nx*7-1.2*.55)+.02*math.sin(nx*17+1.2*.3);strength=max(0,(ny-crest+.15)/.35);band=math.exp(-((ny-crest)/.1)**2);s=min(1,strength*.6+band*.5);color='#e7b5c4' if ((x//gap)*17+(y//gap)*31)%53<5 else '#f4f1ec'
    elements.append(f'<circle cx="{x}" cy="{y}" r="{.7+s*5:.2f}" fill="{color}" opacity="{.1+s*.78:.3f}"/>')
  elements.append(f'<text x="{pad}" y="{pad+20*w/1080}" font-family="Arial,sans-serif" font-size="{w*.013}" fill="#e7b5c4" letter-spacing="1.5">NUCALORIC / A PLACE FOR WHAT COMES NEXT</text>')
  for i,line in enumerate(lines): elements.append(f'<text x="{pad}" y="{top+i*lh}" font-family="Arial,sans-serif" font-weight="600" font-size="{fs}" letter-spacing="{-fs*.04}" fill="{("#e7b5c4" if i==2 else "#f4f1ec")}">{line}</text>')
  copy={'make':'Utilize Solana, for real.','mind':'Give your ideas something useful to do.','together':'Your work. Your people. Your next chapter.'}[name]
  elements.append(f'<text x="{pad}" y="{top+lh*3+.055*h}" font-family="Arial,sans-serif" font-size="{w*.018}" fill="#f4f1ec">{copy}</text>')
  lw=w*(.51 if h>w else .30);logoh=lw/(5440/900)
  elements.append(f'<rect x="0" y="{h-pad-logoh-25*w/1080}" width="{w}" height="{pad+logoh+25*w/1080}" fill="#080809"/>')
  elements.append(f'<svg x="{pad}" y="{h-pad-logoh}" width="{lw}" height="{logoh}" viewBox="{vb}">{inner}</svg>')
  elements.append(f'<text x="{w-pad-w*.31}" y="{h-pad}" font-family="Arial,sans-serif" font-size="{w*.013}" fill="#f4f1ec">IDEA → TOOLSET → PROJECT</text>')
  (root/f'stills/{name}-{fmt}.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="NUCALORIC {name} ad">'+''.join(elements)+'</svg>')
print('Created 9 editable SVG advertisements.')
