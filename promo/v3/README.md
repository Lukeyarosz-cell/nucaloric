NUCALORIC — 16-second motion reel

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
