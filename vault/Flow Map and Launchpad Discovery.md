# Flow map and launchpad discovery — October 5, 2026

The public site retains ink surfaces, cream text, pale pink accents and the original dot theme. This update supersedes the list-based roadmap and the general-purpose Explore defaults.

## Roadmap

Seven selectable nodes form three proposed implementation branches. Animated dot paths connect foundation → wallets/chain → launch/liquidity, foundation → billing/workspaces → AI gateways, and foundation → community/X → the conditional payment rail. These are planning sequences, not claims that later integrations are running. A selected node exposes its actual completion gates, official service links, access requirements and dependencies. Keyboard buttons, stage hash links and mobile layout work. Focus highlights a branch without hiding context.

## Status

A compact overview shows all 17 providers alongside our connector readiness. Five readable official feeds expose their selected components above the detailed service board. Compact and detailed layouts, one-click evidence expansion and provider-to-row navigation make more information accessible. Recent check dots persist up to 24 actual observations on this device; they are not historical uptime percentages. Unknown states and unconfigured connectors remain distinct from reported outages. On GitHub Pages, website availability describes this browser's successful page load, not global uptime.

## Explore

OTC Desks: live, read-only primary registry at https://otcdesks.cash/api/coins. PAID means https://usepaid.app/ and https://x.com/UsePaid, superseding the older Ignition comparison. Its live endpoint cannot be read cross-origin from this site, so a dated catalog of actual public token listing links is bundled. At the last catalog refresh there were 12 OTC records and 20 distinct Solana PAID listings.

DEX Screener's `/tokens/v1/solana/{mints}` supplies fresh market observations, batched up to 30 mints per request. Membership is checked by exact base-token mint; one highest-liquidity returned pool per token is displayed. Unindexed primary listings remain visible with market data unavailable. A source listing proves listing membership, not creator identity, launch execution, safety or returns. A trading venue alone does not establish original launchpad provenance.

NEW TECH combines the registries; OTC DESKS and PAID isolate their listings. PUMP.FUN VENUES explicitly uses `pumpfun`/`pumpswap` market-venue evidence only. Name/symbol/mint filtering, sorting, saved pools, watchlist refresh and live pool detail remain available. Listing and pool observation timestamps are separate. Failed market requests remove old prices rather than substituting examples.

Catalog refresh, without keys: run `node tools/status/update-launchpads.cjs` in the authoring directory, then publish the resulting `data/launchpads.json`. The updater reads actual primary listing anchors and writes atomically only after both sources validate. This is a manual publishing command, not an automatic job. The catalog is a bounded discovery sample, not a complete launch history.

## Scroll depth and motion

A small dot rail follows the document's actual reading depth. Dot artwork shifts at most 30 pixels with native scrolling; content and controls stay stable. There is no scroll interception. Traveling graph signals pause with the existing motion control, when outside the viewport, and when the document is hidden. Reduced-motion preferences remove traveling signals and artwork depth shifts. Backgrounds and text keep the approved palette.

## Source and evidence

Authoring: `/home/luke/Projects/nucaloric-site`. Core changes: `flowmap.js`, `depth-motion.js`, `depth-pages.css`, `launchpad-market.js`, `live-market.js`, `operations.js`, `roadmap.html`, `status.html`, `explorer.html`, `data/launchpads.json`. Review scripts cover keyboard/hash selection, mobile geometry, motion controls, depth, status evidence, source attribution, stale registry fallback and quote failures. Evidence is saved under `Evidence/Flow Map and Launchpad Discovery`.

Official references: [OTC documentation](https://otcdesks.cash/docs), [OTC discovery](https://otcdesks.cash/explore), [PAID](https://usepaid.app/), [DEX Screener API](https://docs.dexscreener.com/api/reference).
