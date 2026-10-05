# NUCALORIC creative ad assets

Three concepts: **Make something real**, **A mind / a purpose / a project**, and **Start small / build together**.

- `stills/`: nine editable SVGs and nine PNG exports, with each concept in 1920×1080, 1080×1920, and 1080×1080.
- `motion/`: three silent six-second, 30 fps H.264 clips: landscape and portrait Make Something Real, plus square Build Together.
- `source/`: editable canvas motion template, SVG generator, render script, original wordmark, Manrope font, and its OFL license.
- `index.html`: visual contact sheet and playable videos.

Palette: #080809 / #f4f1ec / #e7b5c4. Original wordmark preserved. PNG/SVG stills use Arial; motion uses the included Manrope. No third-party footage or audio is included. Motion clips have no audio so they can be cut to a future soundtrack.

These are creative brand assets, not a finished campaign or a promise of live hosting, payouts, launch guarantees, or investment performance.

## Rebuild

Run `python source/make-stills.py`. Serve this folder on localhost:8081 using `python -m http.server 8081 --bind 127.0.0.1`. Install `playwright` into a local Node environment. Run `node source/render-assets.cjs`; the script uses `/usr/bin/brave` and FFmpeg. To use an existing Playwright installation set `PLAYWRIGHT_MODULE` to its absolute module path.

`source/motion-template.html` exposes `drawAd(time, width, height, concept)`, so wording, dot movement, duration, and layouts can be changed. The current export is 180 frames at 30 fps. Keep the footer free of dots so the original wordmark stays readable.
