# Browser verification

Serve the website on port 8080. Install Playwright in a local Node environment; these scripts use `/usr/bin/brave`. Run `node responsive.cjs` and `node interactions.cjs`.

Override `REVIEW_BASE_URL`, `REVIEW_OUTPUT`, or `PLAYWRIGHT_MODULE` when needed. Screenshots and JSON results default to `website/docs/review-results`. The tests use an isolated browser profile; they do not change the founder’s browser state.

## Service status and roadmap

Run `node tools/status/server.cjs` and then `node tools/review/operations.cjs` with the same Playwright environment setup. This verifies both pages, external versus internal failure attribution, missing/stale/offline evidence, search/filter behavior, roadmap access stages, X Pay handoff, and mobile layout. Backend classification checks: `node --test tools/status/monitor.test.cjs`.
