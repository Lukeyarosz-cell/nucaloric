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
