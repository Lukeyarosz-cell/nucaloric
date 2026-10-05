# Audit findings
## Evidence and limits
Saved browser audit timestamp: 2026-10-04T19:19:40.441Z. It predates this resumed session and reflects the extracted v12 site. Browser reruns are blocked by this session's sandbox. Node syntax checking succeeds. Current static reference audit found 0 missing local paths.

## Recorded page checks
| Page | Width | JS errors | Page overflow | Broken images |
|---|---:|---:|---|---:|
| index | 1440 | 0 | False | 5 |
| explorer | 1440 | 0 | False | 2 |
| coin | 1440 | 0 | False | 2 |
| launchpad | 1440 | 0 | False | 2 |
| optimizer | 1440 | 0 | False | 2 |
| rewards | 1440 | 0 | False | 2 |
| ecosystem | 1440 | 0 | False | 7 |
| registry | 1440 | 0 | False | 2 |
| dashboard | 1440 | 0 | False | 2 |
| index | 390 | 0 | False | 5 |
| explorer | 390 | 0 | False | 2 |
| coin | 390 | 0 | False | 2 |
| launchpad | 390 | 0 | False | 2 |
| optimizer | 390 | 0 | False | 2 |
| rewards | 390 | 0 | False | 2 |
| ecosystem | 390 | 0 | False | 7 |
| registry | 390 | 0 | False | 2 |
| dashboard | 390 | 0 | False | 2 |

The audit's overflow-element list includes descendants of closed offscreen drawers; these should not be treated as visible page overflow.

## Confirmed source or recorded findings
- External Phantom/Solflare logos failed across pages; homepage/ecosystem have additional failures.
- Every page lacks a meta description in the saved audit.
- Search controls and optimizer sliders lack programmatic labels in the saved audit.
- Homepage has no h1; coin page has two h1 elements.
- Launch rewards recommendation displays Applied without changing a rewards setting.
- Launch review does not fully capture supply, vesting, lock, distribution, or Mind selections.
- Command palette advertises arrow navigation and Enter, but the document key handler implements Ctrl/Cmd+K and Escape; keyboard result navigation needs implementation or verification.
- Watchlist schema is not validated; empty dashboard state falls back to a sample coin.

## Interaction evidence
- Explore search filters coins: recorded failure; requires corrected test and rerun
- Quick View opens: recorded failure; requires corrected test and rerun
- Watchlist persists across reload: recorded failure; requires corrected test and rerun
- Compare modal opens with two coins: recorded failure; requires corrected test and rerun
- Command palette filters and navigates: recorded pass
- Dashboard shows persisted watchlist: recorded pass
- Launch builder traverses eight stages: recorded pass
- Optimizer updates score and outputs: recorded pass
- Registry offline filter: recorded pass
- Registry capability detail opens: recorded failure; requires corrected test and rerun
- Coin query selects Vortex: recorded failure; requires corrected test and rerun
- Coin tabs switch panels: recorded pass
- Wallet choice stores demo wallet: recorded pass

Failures are not all product defects. Watch/compare used stale selectors in the saved output. Coin heading selection matched two elements. Current source binds quick and capability drawers; click targets and overlays need checking. Search visibility may be affected by CSS overriding the hidden attribute; verify before fixing.

## Screenshot limitation
The saved mobile Explore screenshot has large blank areas. The audit runner did not scroll through the page before capture, so IntersectionObserver reveal elements can remain hidden. Scroll every section into view and wait for animations before visual approval; these captures are not complete visual verification.

## Priorities
Fix semantic labels and reliable assets; complete keyboard/focus behavior; validate persisted state; finish launch review semantics; then replace demo integrations. See [[Roadmap]].
