NUCALORIC — motion promo v2

1920×1080 / 30 fps / 50.70 seconds.

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
