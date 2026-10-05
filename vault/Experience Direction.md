# Experience direction and launch / registry refresh
Reviewed and implemented October 4, 2026.

## What the project appears to value
This is an interpretation of repeated user feedback, not a formal company mission statement: distinctive NuCore-derived identity, restrained black/cream/pink styling, readable information, deliberate motion, user appeal, integrated product journeys, and transparency about capabilities and limits. The archive's evolution favors useful interfaces over decorative telemetry.

## What changed
The Launch Studio replaces the oversized hero and cramped three-column builder with a compact branded introduction, two-column workspace, clearly separated form content, and a model summary below. It adds browser-local draft persistence, required identity and supply checks, actionable rewards allocation, complete review of supply/vesting/lock/distribution/Mind/thesis, and downloadable JSON blueprints. The launch map is an optional expandable section.

Registry replaces two competing hero sections with one introduction and an animated dot constellation linking all eight capability groups. Tool names use readable text; group titles retain custom lettering. Cards have keyboard activation and hover feedback. Search has result counts, a no-results state, reset, and descriptive labels. The atlas pauses when hidden, offscreen, or reduced motion is requested. Displayed health/activity metrics are explicitly examples.

Shared CSS now hides an empty compare tray, which was previously visible on mobile. Changes are local; no GitHub upload or hosting deployment was performed. Original source files are backed up in `/home/luke/Projects/nucaloric-backups/before-launch-registry-refresh`.

## Recommended next additions, in order
1. A concise homepage product explanation beneath the wordmark, strengthening the existing Explore a coin and Build a coin actions. Add a real walkthrough of the sample experience so visitors understand Mind, receipts, and capabilities before navigating deeper.
2. Launch starter templates with transparent assumptions, short field explanations, and a summary of required funding and network costs once a real execution model is defined. Do not fabricate transaction cost estimates.
3. A useful activity layer: dated launch receipts, linked evidence, source/timestamp labels, watchlist notifications, and explicit pending/unavailable states. Begin with correctly labeled demo content, then integrate actual data sources.
4. Consistent keyboard navigation, focus trapping/return, reduced motion, accessible labels, and stable local partner assets across every page. Preserve visual identity while using ordinary text for explanations and inputs.
5. A formal company purpose / values note. Validate the interpretation above with the founder before turning it into public claims.

## Validation
Ten browser workflow checks passed. Launch and Registry had no JavaScript errors or document overflow at 1440 and 390 pixels. All nine pages passed JavaScript-error smoke checks. Partner requests were blocked during automated testing for repeatability; external logo reliability is not established by these tests. Desktop and mobile screenshots and the test runner are preserved under `Evidence/Launch Registry Refresh`.

## Prototype boundary
The optimizer is a local heuristic, draft storage is per browser, and exported blueprints do not submit transactions. Wallet signing, service health, market data, X activity, and settlement remain production integration work.
