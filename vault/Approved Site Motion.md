# Approved reel style on the website

Implemented October 4, 2026. This is the first website adaptation of [[Motion Style Guide]].

## What changed

- Homepage: staggered “Build something real” typography, original wordmark entrance, and a silent glossy pink visual with a poster and play/pause control.
- Hosting: a once-per-view workspace walkthrough with responsive cursor motion, ripple, typed command preview, manually selectable steps and replay.
- Registry: a depth-aware particle sphere inside the existing shared dot renderer.
- Navigation: brief stripe shutters, with an 180ms entrance and 240ms destination reveal.
- Motion behavior: visibility-aware media, static reduced-motion states and homepage wave lifecycle handling. A manually selected walkthrough step persists when scrolling.

The wordmark-centered homepage and existing navigation remain the entry to the product. Motion is concentrated in the project introduction and walkthrough. The workspace animation presents an example rather than an executed purchase or provisioned server.

## Preview

[Homepage](http://127.0.0.1:3000/index.html) · [Hosting](http://127.0.0.1:3000/hosting.html) · [Registry](http://127.0.0.1:3000/registry.html)

![[Evidence/Approved Site Motion/home-desktop.png]]

![[Evidence/Approved Site Motion/hosting-desktop.png]]

![[Evidence/Approved Site Motion/index-mobile.png]]

## Implementation and evidence

Source: `/home/luke/Projects/nucaloric-site`. Implementation details are in `docs/APPROVED_SITE_MOTION.md`. The GPU shader and loop generator are saved in `tools/motion`; the loop has no audio track and is roughly 183KB. The Manrope font is scoped to the new motion sections and saved with its OFL licence.

20 motion checks and nine hosting regression checks passed. Ten pages passed desktop/mobile smoke checks. Registry regression results and screenshots are preserved alongside the motion review in `Evidence/Approved Site Motion`.

The prior site is backed up at `/home/luke/Projects/nucaloric-backups/before-approved-site-motion-2026-10-04`. The change is local; it has not been deployed externally.

Remaining experiments are tracked in [[Future Site Motion]] and [[Roadmap]].

## Latest site revision

See [[Project Workspace Redesign]]. The homepage glossy loop has been replaced by an interactive project starter, and stripe navigation has been slowed. Earlier descriptions of those two effects describe the prior implementation. The approved promo reel remains unchanged.
