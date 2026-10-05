# Dot motion and interaction update
October 4, 2026.

## Requested changes
Replaced Registry's labeled capability map with a flowing dot sculpture. Removed all 49 abbreviation badges from the markup. Added a distinct animated dot signature above the usage footer of every capability card. Added a moving dot background throughout the Launch Studio workspace.

## Motion behavior
Eight pattern families — waves, radial ripples, rotating fields, sweeps, interference, diagonal flows, spirals, and compound pulses — vary by per-card frequency and phase to produce 49 signatures. A shared renderer uses one animation clock, caps updates around 30 frames per second, sizes for device pixel density, pauses offscreen/hidden surfaces, and renders still compositions for reduced motion. Existing site animations remain separate from this new renderer.

## Additional polish
Added a short homepage explanation. Made mobile search visible. Implemented command arrows and Enter, command focus return, drawer focus trapping and restoration, accessible search labels and close controls. Validated watchlist storage and removed the misleading sample coin for empty watchlists. Added deliberate text fallbacks for unavailable external logos. Navigation has a more solid background, controls have visible focus outlines, and capability cards retain readable status and descriptive text.

## Verification
Ten launch/registry regression checks and fourteen new animation/layout/interaction checks passed. Nine pages loaded without JavaScript exceptions. Tested desktop at 1440px and phones at 390px. Checked screenshots, canvas movement, distinct signatures, reduced motion, search navigation, corrupt/empty watchlists, and keyboard drawer activation/focus return. External requests were intentionally blocked in browser tests; fallback UI was exercised but live partner asset availability was not verified.

## Files and limits
Updated `registry.html`, `launchpad.html`, `index.html`, `styles.css`, and `app.js`. Original versions are saved at `/home/luke/Projects/nucaloric-backups/before-dot-motion`. The work is local and the preview is served at http://127.0.0.1:3000/. No production transaction integrations, deployment, or GitHub upload occurred.
