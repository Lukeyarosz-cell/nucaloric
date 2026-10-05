import asyncio, json, pathlib, subprocess, sys, wave
import edge_tts
import numpy as np
ROOT=pathlib.Path(__file__).resolve().parents[1]; OUT=ROOT/'output'; OUT.mkdir(exist_ok=True)
voice=sys.argv[1] if len(sys.argv)>1 else 'en-US-GuyNeural'
texts=[
'Everything on Solana starts with something you made.',
'Get your project plan. Give your idea a direction.',
'Experiment with tooling. Open up what you can build.',
'With New Caloric, expand the capabilities of Solana. Go beyond token parameters.',
'Hosting. APIs. Scripts. Local models. And more room to build.',
'Sell what you make. Turn your work into a product.',
'Grow your projects. And your community.',
'New Caloric. Utilize Solana. For real.'
]
base=[6,5,5,6,8,5,5,5]
async def main():
 scenes=[]; cursor=0; chunks=[]
 for i,txt in enumerate(texts):
  mp=OUT/f'voice-{i+1:02}.mp3';wv=OUT/f'voice-{i+1:02}.wav'
  if not mp.exists() or not (OUT/f'words-{i+1:02}.json').exists() or not (OUT/'voice-name.txt').exists() or (OUT/'voice-name.txt').read_text().strip()!=voice:
   words=[]
   with mp.open('wb') as audio:
    async for part in edge_tts.Communicate(txt,voice,rate='+4%',pitch='-2Hz',boundary='WordBoundary').stream():
     if part['type']=='audio': audio.write(part['data'])
     elif part['type']=='WordBoundary': words.append({'text':part['text'],'offset':part['offset']/10000000,'duration':part['duration']/10000000})
   (OUT/f'words-{i+1:02}.json').write_text(json.dumps(words,indent=2))
  subprocess.run(['ffmpeg','-v','error','-y','-i',str(mp),'-ar','48000','-ac','1',str(wv)],check=True)
  with wave.open(str(wv),'rb') as f: samples=np.frombuffer(f.readframes(f.getnframes()),dtype='<i2').astype(np.float64)/32768
  # Keep enough breathing room after every spoken line.
  dur=max(base[i],round((len(samples)/48000+.85)*30)/30)
  scenes.append({'index':i,'start':cursor,'duration':dur,'voice_start':cursor+.35,'text':txt,'voice_file':mp.name})
  chunks.append((cursor+.35,samples));cursor+=dur
  print(f'Voice {i+1}: {len(samples)/48000:.2f}s, scene {dur:.2f}s',flush=True)
 mix=np.zeros((round(cursor*48000),2))
 for start,data in chunks:
  a=round(start*48000);mix[a:a+len(data),:]+=data[:,None]
 peak=np.max(np.abs(mix));mix*=.78/max(peak,.001)
 with wave.open(str(OUT/'voiceover.wav'),'wb') as f:
  f.setnchannels(2);f.setsampwidth(2);f.setframerate(48000);f.writeframes((mix*32767).astype('<i2').tobytes())
 (OUT/'voice-name.txt').write_text(voice)
 (ROOT/'source/timeline.json').write_text(json.dumps({'fps':30,'duration':cursor,'voice':voice,'scenes':scenes},indent=2))
 (ROOT/'source/voiceover-script.txt').write_text('\n\n'.join(texts)+'\n\nNew Caloric is the narration spelling of NUCALORIC. No music is included.\n')
asyncio.run(main())
