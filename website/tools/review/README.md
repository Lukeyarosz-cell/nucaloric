# Browser verification

Serve the website on port 8080. Install Playwright in a local Node environment; these scripts use `/usr/bin/brave`. Run `node responsive.cjs` and `node interactions.cjs`.

Override `REVIEW_BASE_URL`, `REVIEW_OUTPUT`, or `PLAYWRIGHT_MODULE` when needed. Screenshots and JSON results default to `website/docs/review-results`. The tests use an isolated browser profile; they do not change the founder’s browser state.

## Service status and roadmap

Run `node tools/status/server.cjs` and then `node tools/review/operations.cjs` with the same Playwright environment setup. This verifies both pages, external versus internal failure attribution, missing/stale/offline evidence, search/filter behavior, roadmap access stages, X Pay handoff, and mobile layout. Backend classification checks: `node --test tools/status/monitor.test.cjs`.

## Dark creative workspace review

`creative-workspace.cjs` checks moving/static dot fields, pause and resume across pages, reduced-motion handling, project chapter navigation, real draft detail counts, preservation of open provider evidence, and layout at 1440, 390 and 320 pixels.

The local Brave 154 headless renderer intermittently crashed during repeated navigation. Complete review uses the Chromium build paired with Playwright; desktop Brave settings were not changed. [Playwright browser guidance](https://playwright.dev/docs/browsers) explains the version pairing.

```bash
node /tmp/nucaloric-refresh/node_modules/playwright/cli.js install chromium
REVIEW_BROWSER=bundled PLAYWRIGHT_MODULE=/tmp/nucaloric-refresh/node_modules/playwright node tools/review/creative-workspace.cjs
```

All review runners accept `REVIEW_BROWSER=bundled` or a browser executable path. Default remains `/usr/bin/brave`. Evidence for this revision: `Evidence/Dark Creative Rebuild/` in the Obsidian vault.

## Scrolling video walkthrough

`record-walkthrough.cjs` records all 13 pages in an isolated Playwright Chromium profile, with normal animations at 1440 × 900. It scrolls every page to its footer and checks for browser errors. `assemble-walkthrough.py` combines the raw WebM clips into an H.264 MP4 with 13 named chapters, a coverage report, an Obsidian note, and a browser player. Requires Playwright's installed Chromium, FFmpeg, FFprobe, and Python 3.

```bash
PLAYWRIGHT_MODULE=/tmp/nucaloric-refresh/node_modules/playwright REVIEW_OUTPUT=/home/luke/Projects/nucaloric-walkthrough/2026-10-05 node tools/review/record-walkthrough.cjs
python tools/review/assemble-walkthrough.py /home/luke/Projects/nucaloric-walkthrough/2026-10-05
```

The lower-left page labels exist only in the recording. Browser preferences, wallet state, and private project drafts are not used. Delivery files are archived in the vault under `Evidence/Website Walkthrough/`; raw clips remain in the local walkthrough directory.

## Modular workspace and coin desk

`modular-workbench.cjs` verifies retained workspace preferences, the original homepage wave, coin identity and budget updates, artwork upload, draft reload, portable export/import, invalid imports, legacy draft migration, blocked storage, native scroll depth, reduced motion and primary pages at 1440/390/320 pixels. Evidence: `Evidence/Modular Reference Refit/` in the vault.

## Targeted page refinement

`targeted-refinement.cjs` checks Studio’s actual project identity, Launch’s supply/venue portrait, and the restored Explore console against live network data. It checks twelve-card pagination, compact view at 1440/390/320px, accessible source dates and empty search. It requires the current catalog to contain more than 24 observed listings; deterministic market and failure handling are covered by `working-features.cjs` and `flowmap-launchpads.cjs`.

## Branding and own hardware

`branding-hardware.cjs` verifies managed checkout versus own-machine planning, persistence, exports, URL validation, directory filters, branded service identities, the machine bridge boundary, and full X Pay labels/layout across 13 pages at 1440/390/320px. Uses a configured Paymenter fixture without performing checkout.
