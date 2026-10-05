"""Join Playwright clips into a chaptered MP4 and a small browser player."""
import json
import pathlib
import subprocess
import sys

output = pathlib.Path(sys.argv[1]).resolve()
coverage = json.loads((output / 'recording-coverage.json').read_text())
assert len(coverage) == 13 and all(p['reachedBottom'] and not p['errors'] for p in coverage)
chapters = []
elapsed = 0
playlist = []
metadata = [';FFMETADATA1', 'title=NUCALORIC — Every page walkthrough', 'artist=NUCALORIC']
for page in coverage:
    clip = output / 'raw' / page['file']
    probe = json.loads(subprocess.check_output([
        'ffprobe', '-v', 'error', '-show_format', '-of', 'json', str(clip)
    ]))
    duration = round(float(probe['format']['duration']) * 1000)
    chapters.append({'page': page['page'], 'title': page['title'], 'start': elapsed / 1000, 'end': (elapsed + duration) / 1000})
    playlist.extend([f"file '{clip}'", f'duration {duration / 1000:.3f}'])
    metadata.extend(['[CHAPTER]', 'TIMEBASE=1/1000', f'START={elapsed}', f'END={elapsed + duration}', f"title={page['title']}"])
    elapsed += duration
(output / 'concat.txt').write_text('\n'.join(playlist) + '\n')
(output / 'chapters.ffmeta').write_text('\n'.join(metadata) + '\n')
(output / 'chapters.json').write_text(json.dumps(chapters, indent=2) + '\n')
video_name = 'NUCALORIC-website-walkthrough-2026-10-05.mp4'
video = output / video_name
subprocess.run([
    'ffmpeg', '-y', '-hide_banner', '-loglevel', 'warning',
    '-f', 'concat', '-safe', '0', '-i', str(output / 'concat.txt'),
    '-i', str(output / 'chapters.ffmeta'), '-map', '0:v:0',
    '-map_metadata', '1', '-map_chapters', '1', '-an',
    '-c:v', 'libx264', '-preset', 'fast', '-crf', '18', '-threads', '4',
    '-pix_fmt', 'yuv420p', '-r', '25', '-movflags', '+faststart', str(video),
], check=True)
probe = json.loads(subprocess.check_output([
    'ffprobe', '-v', 'error', '-show_format', '-show_streams', '-show_chapters', '-of', 'json', str(video)
]))
assert len(probe['chapters']) == 13
assert abs(float(probe['format']['duration']) - elapsed / 1000) < 1
(output / 'video-metadata.json').write_text(json.dumps(probe, indent=2) + '\n')
def timestamp(seconds):
    seconds = int(seconds)
    return f'{seconds // 60:02}:{seconds % 60:02}'
lines = [
    '# Website walkthrough', '',
    f'All 13 website pages, recorded at 1440 × 900 with animations enabled. Duration: {timestamp(elapsed / 1000)}.', '',
    f'![[Evidence/Website Walkthrough/{video_name}]]', '',
    'Each page is scrolled from its hero to its footer. Page labels are recording overlays; they are not part of the website. The MP4 contains named chapters and is silent.', '',
    '| Time | Page |', '| --- | --- |',
]
lines.extend(f"| {timestamp(c['start'])} | {c['title']} |" for c in chapters)
lines.extend(['', 'Source capture and raw clips: `/home/luke/Projects/nucaloric-walkthrough/2026-10-05/`.',
              'Repeatable recording and assembly scripts: `website/tools/review/record-walkthrough.cjs` and `assemble-walkthrough.py`.',
              'Coverage check: all 13 footers reached; no browser runtime errors.', ''])
(output / 'Website Walkthrough.md').write_text('\n'.join(lines))
html = '''<!doctype html>
<html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>NUCALORIC · Website walkthrough</title>
<style>
:root{color-scheme:dark}*{box-sizing:border-box}body{margin:0;background:#080809;color:#f4f1ec;font:16px/1.6 system-ui,sans-serif}main{max-width:1480px;margin:auto;padding:32px 20px}p{color:#b9b6b4}h1{font-size:clamp(28px,5vw,52px);line-height:1.1;margin:8px 0 20px}.eyebrow{color:#e7b5c4;letter-spacing:.18em;font-size:12px}video{display:block;width:100%;background:#080809;border:1px solid #343033;border-radius:10px}a{color:#e7b5c4}#chapters{display:flex;flex-wrap:wrap;gap:8px;margin-top:20px}button{border:1px solid #484046;background:#151214;color:#f4f1ec;border-radius:6px;padding:10px 13px;cursor:pointer}button:hover,button:focus-visible{border-color:#e7b5c4}#loading{color:#e7b5c4}button:disabled{opacity:.5;cursor:wait}footer{margin-top:26px;font-size:13px;color:#b9b6b4}
</style><main>
<div class="eyebrow">NUCALORIC / OCTOBER 5, 2026</div>
<h1>A walk through every page.</h1>
<p>13 pages · __DURATION__ · Animated desktop walkthrough</p>
<video id="video" controls playsinline preload="metadata" poster="poster.jpg"></video>
<p id="loading" role="status">Loading the video…</p>
<a id="download" href="__VIDEO__" download>Download MP4 (__SIZE__ MB)</a>
<div id="chapters" aria-label="Jump to page"></div>
<footer>Captured from the current local website. Page labels are added for the recording.</footer>
</main><script>
const chapters=__CHAPTERS__,video=document.getElementById('video'),status=document.getElementById('loading');
for(const chapter of chapters){const button=document.createElement('button');button.textContent=chapter.title;button.disabled=true;button.addEventListener('click',()=>{video.currentTime=chapter.start;video.play().catch(()=>{});video.scrollIntoView({behavior:'smooth',block:'center'});});document.getElementById('chapters').append(button);}
(async()=>{try{
const response=await fetch('__VIDEO__');
if(!response.ok||response.headers.get('content-type')?.includes('text/html'))throw new Error('Please sign in with your remote desktop password, then reopen this video link.');
const reader=response.body.getReader(),chunks=[];let received=0;
while(true){const {done,value}=await reader.read();if(done)break;chunks.push(value);received+=value.length;status.textContent=`Loading the video… ${Math.min(100,Math.round(received/__BYTES__*100))}%`;}
video.src=URL.createObjectURL(new Blob(chunks,{type:'video/mp4'}));
await new Promise((resolve,reject)=>{video.addEventListener('loadedmetadata',resolve,{once:true});video.addEventListener('error',()=>reject(new Error('This browser could not load the video. Use the MP4 download link.')),{once:true});});
document.querySelectorAll('button').forEach(button=>button.disabled=false);status.textContent='Ready. Press play or choose a page.';
}catch(error){status.textContent=error.message;}})();
</script></html>'''
html = html.replace('__DURATION__', timestamp(elapsed / 1000)).replace('__VIDEO__', video_name)
html = html.replace('__SIZE__', f'{video.stat().st_size / 1000000:.1f}').replace('__BYTES__', str(video.stat().st_size))
html = html.replace('__CHAPTERS__', json.dumps(chapters))
(output / 'index.html').write_text(html)
(output / 'poster.jpg').write_bytes((output / 'stills/index-top.jpg').read_bytes())
print(f'ASSEMBLED {video}: {timestamp(elapsed / 1000)}, {video.stat().st_size / 1000000:.1f} MB, 13 chapters', flush=True)
