# Targeted page refinement — October 5, 2026

The founder asked for a more complete version of the familiar website, and rejected the extent of the last modular redesign. This is the latest approved scope, superseding the homepage, Explore, Registry and preview-card direction in [[Modular Reference Refit]].

- Home: restored the complete pre-modular homepage composition and original wordmark/wave. Retained restrained native scroll depth and existing motion.
- Hosting and Rewards: preserved byte-for-byte; no shared styles or scripts were edited for these pages.
- Registry: restored the earlier dark editorial structure, all 49 tools, eight family dot compositions, search, filtering and shortlist. Kept new mosaic artwork as a subtle layer.
- Studio: retained the accepted page and working project library. Replaced the floating PROJECT DESK panel with a square NUCALORIC working sheet that mirrors actual project name, purpose and first milestone.
- Launch: retained the working modular builder. Replaced the LAUNCH PLAN tag/card with a token identity portrait, orbit dots, artwork and live supply/venue. Local save, artwork, modules and JSON portability remain available.
- Explore: restored the familiar Find launches hero, market console, broad cards and Grid/Compact choices. Retained real Solana pool observations, source attribution, watchlists and OTC/PAID discovery. Twelve-card pagination keeps the directory manageable. No example prices, fake AI scores or holder counts were reinstated.

## Implementation

Five HTML pages plus scoped `refinement.css` / `refinement.js`. `live-market.js` now renders the classic card presentation only when the Explore root requests it; the pool detail page retains its current interface. Card canvas instances are unmounted before replacement. Motion follows native scrolling and respects reduced-motion and the shared pause clock.

Production launch execution still requires wallets and configured integrations. Drafts and watchlists remain local to the browser. PAID listing catalog dates remain separate from live pool quotes in the expandable source evidence.

## Verification

Browser evidence is in `Evidence/Targeted Page Refinement/`. Updated existing browser suites cover local saves and backups, artwork and coin-plan portability, source membership, market failures, shortlist interactions, motion and layouts at 1440, 390 and 320 pixels. The targeted review also checks actual project identity, supply/venue, live pagination and compact layout. Hosting and Rewards checksums match the pre-change copies.

Live website: https://lukeyarosz-cell.github.io/nucaloric-site/
Source: `/home/luke/Projects/nucaloric-site`
Prior revision backup: `/home/luke/Projects/nucaloric-backups/before-targeted-refinement-2026-10-05/`
