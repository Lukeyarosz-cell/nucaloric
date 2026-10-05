import pathlib,json,xml.etree.ElementTree as E,zipfile,shutil
R=pathlib.Path(__file__).resolve().parents[1];O=R/'output';T=json.loads((R/'source/timeline.json').read_text())
root=E.Element('fcpxml',version='1.10');res=E.SubElement(root,'resources')
E.SubElement(res,'format',id='r1',name='FFVideoFormat1080p60',frameDuration='1/60s',width='1920',height='1080',colorSpace='1-1-1 (Rec. 709)')
for id,name,video in [('r2','NUCALORIC-motion-reel-silent.mp4',True),('r3','soundtrack-16s.wav',False)]:
 attrs=dict(id=id,name=name,start='0s',duration='16s')
 if video:attrs.update(hasVideo='1',hasAudio='0',format='r1',videoSources='1')
 else:attrs.update(hasAudio='1',audioSources='1',audioChannels='2',audioRate='48000')
 a=E.SubElement(res,'asset',**attrs);E.SubElement(a,'media-rep',kind='original-media',src=(O/name).as_uri())
lib=E.SubElement(root,'library');event=E.SubElement(lib,'event',name='NUCALORIC motion reel');project=E.SubElement(event,'project',name='NUCALORIC / 16 seconds / 60fps')
seq=E.SubElement(project,'sequence',format='r1',duration='16s',tcStart='0s',tcFormat='NDF',audioLayout='stereo',audioRate='48k');sp=E.SubElement(seq,'spine')
clip=E.SubElement(sp,'asset-clip',ref='r2',name='Motion reel picture',offset='0s',start='0s',duration='16s',format='r1')
E.SubElement(clip,'asset-clip',ref='r3',name='User supplied soundtrack',lane='-1',offset='0s',start='0s',duration='16s',audioRole='music')
marks=[(s['start'],s['name']) for s in T['scenes']]+[(b['time'],f"Beat {b['index']+1}") for b in T['beats'] if 0<=b['time']<16]
for t,name in sorted(marks):E.SubElement(clip,'marker',start=f'{round(t*60)}/60s',duration='1/60s',value=name)
E.indent(root);E.ElementTree(root).write(O/'NUCALORIC-Resolve-60fps.fcpxml',encoding='utf-8',xml_declaration=True)
(R/'source/requirements.txt').write_text('Pillow\nnumpy\nscipy\nmoderngl\nglcontext\ncairosvg\n')
(R/'README.md').write_text('''NUCALORIC — 16-second motion reel

1920×1080 / 60fps / exactly 960 frames / exactly 16 seconds.

The soundtrack is tiktokdownload.online_1791156644577.mp3, using its 14.03–30.03 second excerpt. The edit is based on the roughly 132 BPM pulse and detected transient hits. No voiceover, generated speech, extra music, or added sound effects are included. Only 4ms opening and 80ms ending audio fades were applied.

Motion structure:
0.00–1.82  viewfinder HUD and beat-driven kinetic words
1.82–3.63  morphing geometric grid
3.63–5.45  rotating 3D-projected particle sphere
5.45–7.28  GPU ray-marched glossy liquid forms
7.28–10.92 floating dashboard, cursor movement and click
10.92–12.73 diagonal stripe shutters and kinetic words
12.73–14.55 halftone wipes
14.55–16.00 original NUCALORIC SVG logo reveal

Brand colours: #080809, #e7b5c4, #f4f1ec.

Watch output/NUCALORIC-motion-reel-16s-60fps.mp4.
The silent MP4 and soundtrack-16s.wav are aligned from time zero.
Import output/NUCALORIC-Resolve-60fps.fcpxml into Resolve and relink those two files to the output folder if needed. The interchange timeline contains separate picture and music tracks plus scene and beat markers. The picture is rendered, not a native layered Fusion composition. A DNxHR master is saved separately in the original workspace output folder (not included in this ZIP). Use it as the picture source if your editor cannot decode H.264.

Editable motion source is in source/render.py, with 3D geometry, environment reflections and materials in source/glossy.frag and source/gpu.py. The particle sphere uses genuine 3D coordinates. timeline.json contains audio offset, detected beat positions and frame-rounded scene timings. Manrope is included under the OFL licence; the final brand mark is the site's original SVG.

The two supplied reference videos informed pacing, camera zooms, floating interface treatment and glossy 3D motion. No reference footage, logos or watermarks are reused.

Rebuild with Python, FFmpeg and an EGL-capable OpenGL driver:
python -m venv .venv
.venv/bin/pip install -r source/requirements.txt
.venv/bin/python source/render.py --stills
.venv/bin/python source/render.py
.venv/bin/python source/package.py
''')
D=pathlib.Path('/home/luke/Downloads')
shutil.copy2(O/'NUCALORIC-motion-reel-16s-60fps.mp4',D/'NUCALORIC-motion-reel-16s-60fps.mp4')
with zipfile.ZipFile(D/'NUCALORIC-motion-reel-edit-package.zip','w',zipfile.ZIP_DEFLATED) as z:
 z.write(R/'README.md','NUCALORIC-motion-reel/README.md')
 for folder in ['source','output']:
  for p in sorted((R/folder).iterdir()):
   if p.is_file() and p.suffix not in ['.log','.mov'] and not p.name.endswith('-test.jpg'):
    z.write(p,'NUCALORIC-motion-reel/'+str(p.relative_to(R)))
 p=R/'reference'/T['audio_file'];z.write(p,'NUCALORIC-motion-reel/reference/'+p.name)
print('Editing package complete',flush=True)
