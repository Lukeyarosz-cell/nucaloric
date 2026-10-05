import pathlib,json,xml.etree.ElementTree as ET,zipfile,shutil
ROOT=pathlib.Path(__file__).resolve().parents[1];OUT=ROOT/'output';TL=json.loads((ROOT/'source/timeline.json').read_text());FPS=30;frames=round(TL['duration']*FPS)
def rat(t):return f'{round(t*FPS)}/{FPS}s'
def timecode(t):
 n=round(t*1000);h=n//3600000;m=n//60000%60;s=n//1000%60;ms=n%1000
 return f'{h:02}:{m:02}:{s:02},{ms:03}'
srt=[]
for i,s in enumerate(TL['scenes']):
 words=json.loads((OUT/f'words-{i+1:02}.json').read_text());a=s['voice_start']+words[0]['offset'];b=s['voice_start']+words[-1]['offset']+words[-1]['duration']
 srt.append(f"{i+1}\n{timecode(a)} --> {timecode(b)}\n{s['text'].replace('New Caloric','NUCALORIC')}\n")
(OUT/'NUCALORIC-captions.srt').write_text('\n'.join(srt))
root=ET.Element('fcpxml',version='1.10');res=ET.SubElement(root,'resources')
ET.SubElement(res,'format',id='r1',name='FFVideoFormat1080p30',frameDuration='1/30s',width='1920',height='1080',colorSpace='1-1-1 (Rec. 709)')
for id,name,vid in [('r2','NUCALORIC-promo-v2-silent.mp4',True),('r3','voiceover.wav',False),('r4','swoosh-effects.wav',False)]:
 attrs={'id':id,'name':name,'start':'0s','duration':f'{frames}/30s'}
 if vid:attrs.update(hasVideo='1',hasAudio='0',format='r1',videoSources='1')
 else:attrs.update(hasAudio='1',audioSources='1',audioChannels='2',audioRate='48000')
 asset=ET.SubElement(res,'asset',**attrs);ET.SubElement(asset,'media-rep',kind='original-media',src=(OUT/name).as_uri())
lib=ET.SubElement(root,'library');event=ET.SubElement(lib,'event',name='NUCALORIC v2');proj=ET.SubElement(event,'project',name='NUCALORIC • Voice + Swooshes • No Music')
seq=ET.SubElement(proj,'sequence',format='r1',duration=f'{frames}/30s',tcStart='0s',tcFormat='NDF',audioLayout='stereo',audioRate='48k')
sp=ET.SubElement(seq,'spine');clip=ET.SubElement(sp,'asset-clip',ref='r2',name='Motion picture',offset='0s',start='0s',duration=f'{frames}/30s',format='r1')
for ref,name,lane,role in [('r3','Voiceover','-1','dialogue'),('r4','Swoosh effects','-2','effects')]:
 ac=ET.SubElement(clip,'asset-clip',ref=ref,name=name,lane=lane,offset='0s',start='0s',duration=f'{frames}/30s',audioRole=role)
 if ref=='r4':
  volume=ET.SubElement(ac,'adjust-volume',amount='-6dB')
for s in TL['scenes']:ET.SubElement(clip,'marker',start=rat(s['start']),duration='1/30s',value=f"Scene {s['index']+1}",note=s['text'])
ET.indent(root);ET.ElementTree(root).write(OUT/'NUCALORIC-Resolve-timeline.fcpxml',encoding='utf-8',xml_declaration=True)
(ROOT/'source/requirements.txt').write_text('Pillow\nnumpy\nscipy\nedge-tts\n')
(ROOT/'README.md').write_text(f'''NUCALORIC — motion promo v2

1920×1080 / 30 fps / {TL['duration']:.2f} seconds.

Watch output/NUCALORIC-promo-v2.mp4. It contains a synthetic American male voiceover and isolated stereo swooshes. There is NO background music.

For editing:
- NUCALORIC-promo-v2-silent.mp4: picture only.
- voiceover.wav: complete voice track, aligned from time zero.
- swoosh-effects.wav: complete effects track, aligned from time zero.
- voice-and-effects.wav: the finished mix with effects ducked under narration.
- NUCALORIC-Resolve-timeline.fcpxml: timeline interchange file with picture, voice and effects on separate tracks. Import into Resolve via File > Import > Timeline, and relink the three media files to this output folder if required. The animated picture is rendered; this is not a native layered Fusion project.
- NUCALORIC-captions.srt: optional captions, not burned into picture.
- storyboard.jpg: eight-scene visual overview.

To add music, use the silent picture plus either the final mix or the two individual audio stems. All stems start at time zero.

Animation source is in source/render.py. Narration source and timing are in source/narration.py and timeline.json. Manrope font is included with its OFL license.

Rebuild using Python 3 and FFmpeg:
python -m venv .venv
.venv/bin/pip install -r source/requirements.txt
.venv/bin/python source/narration.py en-US-GuyNeural
.venv/bin/python source/render.py
.venv/bin/python source/package.py

Narration is synthesized using edge-tts (https://github.com/rany2/edge-tts). Change the voice argument to regenerate it. NUCALORIC is spelled “New Caloric” in the spoken script to guide pronunciation. Sound effects are original filtered-noise sweeps generated in render.py; no music samples are used.
''')
# A portable package: all linked media are together and editable source is included.
DEST=pathlib.Path('/home/luke/Downloads');DEST.mkdir(exist_ok=True)
shutil.copy2(OUT/'NUCALORIC-promo-v2.mp4',DEST/'NUCALORIC-promo-v2.mp4')
with zipfile.ZipFile(DEST/'NUCALORIC-promo-v2-edit-package.zip','w',zipfile.ZIP_DEFLATED) as z:
 z.write(ROOT/'README.md','NUCALORIC-v2/README.md')
 for folder in ['source','output']:
  for p in sorted((ROOT/folder).iterdir()):
   if p.is_file() and p.suffix not in ['.mp3','.log'] and not p.name.startswith('voice-0'):
    z.write(p,'NUCALORIC-v2/'+str(p.relative_to(ROOT)))
print('Packaged',flush=True)
