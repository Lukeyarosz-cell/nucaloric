# Approved motion style

Approved by the founder on October 4, 2026: “this is amazing, perfect” and “this is exactly what i was looking for.” This refers specifically to the 16-second motion reel below. Use it as the visual reference for future NUCALORIC motion work.

![[Evidence/Approved Motion Reel/NUCALORIC-motion-reel-16s-60fps.mp4]]

![[Evidence/Approved Motion Reel/storyboard.jpg]]

## The direction

Bold, rhythmic motion design with a clear sequence of ideas. Words arrive on hits, shapes continuously transform, the camera carries the viewer into useful interfaces, and the original wordmark closes the piece. Each scene has a distinct visual treatment while the palette and typography connect the whole reel. The motion makes building real projects feel tangible.

The supplied `Download.mp4` and `Download (1).mp4` informed quick zooms, floating interfaces, glossy forms, cursor interactions, and crisp transitions. Their footage, watermarks, and logos were not reused.

## Brand treatment

| Element | Treatment in the approved reel |
| --- | --- |
| Ink | `#080809`; the website's existing primary ink token remains `#050505` |
| Pink | `#e7b5c4` |
| Cream | `#f4f1ec` |
| Typography | Manrope variable font at strong weights, mostly 800; lighter supporting labels |
| Brand identity | Original NuCore-derived SVG wordmark; preserve its custom letterforms |
| Composition | Large readable words, generous space, one dominant idea at a time |
| Surfaces | Flat ink/pink/cream fields, with reflections and localized lighting on glossy forms |

Manrope is the reel's type choice, not a decision to replace the website's existing display font system. The accepted glossy lighting is a treatment for dimensional artwork; retain the established flat UI palette when adapting it to the site.

## Motion vocabulary

| Technique | How it was made | What it communicates |
| --- | --- | --- |
| Viewfinder HUD | Thin corner brackets, recording mark, restrained labels, advancing timecode; fades out for the logo | A composed frame for the reel |
| Kinetic type | New word and colour treatment on each beat; scale overshoot, short rotation, fading motion trails | BUILD → SOMETHING → REAL |
| Morphing shape grid | Contours interpolate among circles, rounded squares, crosses and three-lobed forms, with staggered phase and rotation | Going beyond token parameters |
| Particle sphere | 2,100 Fibonacci-distributed points in 3D, rotated and perspective projected; depth sorting, variable brightness and restrained bloom | Ideas becoming capabilities |
| Glossy 3D blobs | GPU ray marching of smooth merged spheres and a torus; animated deformation, reflective studio strips, pink material and orbiting satellites | Useful creation and possibility |
| Dashboard and cursor | Floating rounded interface, spring entrance, cursor travel, click ripple, typed terminal output and camera push-in | Hosting, APIs and scripts as a project workspace |
| Stripe wipe | Diagonal moving shutters used as a reveal mask, followed by beat-driven words | BUILD / SELL / GROW / CREATE |
| Halftone wipe | A moving dot field and expanding circular reveal masks | FOR REAL, then a transition to the brand |
| Logo reveal | Original SVG exposed in staggered vertical strips; supporting line and pink underline settle beneath it | NUCALORIC. Utilize Solana. For real. |

The HUD is an editorial framing device. It does not establish a new requirement for telemetry decoration throughout the product.

## Timing and sound

The final render is exactly **16 seconds, 1920 × 1080, 60fps, 960 frames**. It uses `tiktokdownload.online_1791156644577.mp3`, taking the **14.03–30.03 second** excerpt around its drop. The measured pulse is approximately **131.965 BPM**, or **0.454666 seconds per beat**. No added voiceover, speech, music or sound effects appear in this version. Only a 4ms opening fade and an 80ms ending fade were applied to the supplied audio.

| Time in reel | Scene |
| --- | --- |
| 0.000–1.817 | HUD and word-by-word kinetic type |
| 1.817–3.633 | Morphing shape grid |
| 3.633–5.450 | Particle sphere |
| 5.450–7.283 | Glossy 3D forms |
| 7.283–10.917 | Dashboard and cursor; click at about 9.55s |
| 10.917–12.733 | Stripe shutters and kinetic words |
| 12.733–14.550 | Halftone field and wipes |
| 14.550–16.000 | SVG logo reveal |

These scene boundaries are rounded to 60fps frames. Large changes follow four- or eight-beat groups, while smaller accents follow individual hits. This musical pacing belongs to the ad; site motion should follow user actions and visibility instead of requiring audio.

## Reusable principles

- Use a strong entrance, a short readable hold, and a purposeful exit.
- Make one effect the focus of each section. Alternate texture, dimensional forms and clean interfaces to maintain hierarchy.
- Give cards mass through a small spring overshoot and camera movement rather than constant wobbling.
- Let particles and shape morphs connect product ideas; give content and controls clear space.
- Finish with a legible brand lockup and a clear promise.

## Evidence and editable sources

The reel, soundtrack excerpt, storyboard, original SVG, font/licence, renderer, 3D shader and frame timing are preserved in `Evidence/Approved Motion Reel` within this vault. Source files are under its `Source` subfolder. The full working project remains at `/home/luke/Projects/nucaloric-promo/v3`.

The implementation uses Python/Pillow, ModernGL/EGL, a GLSL fragment shader and FFmpeg. The editable motion is procedural source; the Resolve interchange timeline contains rendered picture and a separate soundtrack, not layered Fusion effects.

Verification checked complete video decoding, exact frame count and dimensions, and a sample-for-sample match of the soundtrack's unfaded interior to the replacement audio.

See [[Promo Video]] for exports and version history, [[Future Site Motion]] for proposed web adaptations, and [[Design System]] for current website tokens.
