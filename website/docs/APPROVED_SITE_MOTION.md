# Approved motion applied to the website

Implemented October 4, 2026 from the founder-approved 16-second reel.

The homepage keeps its custom wordmark and existing entry actions. Its project introduction now uses staggered real DOM words, “Build something real,” alongside a glossy pink visual. The original SVG receives a short entrance reveal. The artwork is an eight-second seamless, silent 960×720 loop (approximately 183KB), with a still poster, explicit play/pause control, and visibility-aware playback.

The Hosting hero now includes a workspace walkthrough: project plan, tools, and illustrative command preview. It plays once on entry, with a decorative cursor, click ripple and typed commands. Step buttons support keyboard selection and keep the selected state across scrolling. Replay restarts the sequence. This is a walkthrough; live checkout and provisioning still depend on the existing Paymenter integration.

Registry's main sculpture is now a perspective particle sphere with 900 points, depth sorting and slow rotation. It uses the existing shared dot renderer and visibility/reduced-motion handling. Individual tool cards remain steady.

Shared navigation now uses a stripe entrance of 180ms, followed by a 240ms destination reveal. Same-page hash links remain immediate. Reduced-motion navigation skips the animation delay. Arrival handling is included on every page, including Hosting and Dashboard. Navigation prefetches the destination document when a same-origin link is activated.

The homepage wave now honors reduced motion and stops its animation clock when offscreen or the document is hidden. The new word entrances and walkthrough have static readable states; the decorative video is paused by default with reduced motion and can be started explicitly.

## Files

- index.html: project introduction, wordmark entrance, silent visual and controls.
- hosting.html: interactive illustrative walkthrough.
- app.js: shared sphere renderer, shorter navigation and homepage wave lifecycle.
- motion.js: entrances, video visibility/playback, walkthrough steps and responsive cursor aiming.
- styles.css: scoped Manrope motion typography, cards, transitions and static fallbacks.
- All HTML pages: load the motion module and support the transition arrival state.
- assets/motion: local video, poster and Manrope font/OFL licence.
- tools/motion: editable GPU shader and asset generator. Rebuild with Python dependencies from requirements.txt, an EGL-capable OpenGL driver, and FFmpeg.

Previous site files are preserved at /home/luke/Projects/nucaloric-backups/before-approved-site-motion-2026-10-04.

## Validation

20 new motion/browser checks passed: DOM text, visible-only silent playback, pause persistence, offscreen behavior, short navigation, automatic walkthrough, keyboard selection, selection persistence, replay, sphere animation, reduced-motion still states/navigation, desktop/mobile fit and no-JavaScript messaging. No uncaught page errors occurred. Nine hosting regression checks passed, including plans, input validation, downloads and configured checkout behavior. Ten pages passed desktop and mobile smoke checks. Registry regression results and screenshots are preserved in the Obsidian vault under Evidence/Approved Site Motion.

The changes are available in the local preview. No external deployment was part of this update.
