# Design system

## Approved motion direction — October 4, 2026

The founder approved the 16-second, 1080p/60fps reel as the desired motion style. See [[Motion Style Guide]] for palette, typography, choreography, technical methods and embedded evidence, and [[Future Site Motion]] for proposed website adaptations. Its strongest additions are kinetic words, morphing grids, a perspective particle sphere, glossy pink forms, floating interface demonstrations and brief stripe/halftone reveals. Preserve the original SVG wordmark. Manrope is the reel font; existing website typography remains the baseline until a site-specific change is made.

## Existing website direction
The user's accepted direction developed toward dark surfaces, restrained cream/light sections, pale pink, condensed display typography, a NuCore-derived wordmark, custom token icons, editorial hierarchy, and dot-matrix animations. The archive explicitly rejects unnecessary gradients and a gimmicky geometric telemetry block.

The SVG wordmark preserves custom brand forms. Other condensed text depends on the CSS font stack; do not assume the original NuCore font file is bundled.

## CSS variables (source order; later definitions may override)
- `--ink`: `#050505`
- `--ink-soft`: `#0b0b0d`
- `--panel`: `#101012`
- `--panel-2`: `#151518`
- `--paper`: `#f4f1ec`
- `--paper-2`: `#e9e5de`
- `--white`: `#fffdfa`
- `--pink`: `#e7b5c4`
- `--pink-2`: `#d79aaf`
- `--pink-3`: `#f0cbd5`
- `--grey`: `#989493`
- `--grey-2`: `#666365`
- `--line`: `#29292d`
- `--line-light`: `#cbc6be`
- `--sans`: `Inter,ui-sans-serif,-apple-system,BlinkMacSystemFont,"Segoe UI",Arial,sans-serif`
- `--mono`: `"SFMono-Regular",Consolas,"Liberation Mono",monospace`
- `--cond`: `"Arial Narrow","Roboto Condensed","Aptos Narrow",Impact,sans-serif`
- `--paper-3`: `#f7f2eb`
- `--paper-4`: `#ede7df`
- `--ink-2`: `#121214`
- `--accent-soft`: `#efc2cf}
body{background:var(--ink-soft)}
.display,.registry-title-row h1,.registry-group-head h2,.coin-summary h1,.page-hero h1,.home-system-head h2,.partner-top h2,.registry-editorial-copy h2,.hero-metric b,.coin-id b,.coin-score,.history-head,.reward-card h3,.integration-card h3,.launch-form h3,.control-panel h3,.receipt-box b,.social-stat b,.group-health b,.registry-stats b,.score-panel .score,.capability-strip-stats b,.registry-mini-stat b,.runtime-head,.console-stat b,.terminal-stat b{font-family:var(--cond)}
.nav-tab,.xpay-btn,.wallet-btn,.btn,.ghost-btn,.kicker,.page-meta,.filter-chip,.filter-search,.detail-head,.system-head,.history-row b,.cap-card-body h3,.cap-card-foot b,.service-row,.runtime-capabilities span,.runtime-capabilities b,.launch-step b,.stack-card b,.registry-filter button,#registrySearch,.registry-category-links a,.queue-row b,.queue-row em,.terminal-label,.terminal-foot b,.console-head,.console-stat span,.console-stat em{font-family:var(--cond)`
- `--surface-0`: `#070708`
- `--surface-1`: `#0e0e10`
- `--surface-2`: `#151518`
- `--surface-3`: `#1b191d`
- `--surface-4`: `#242127`
- `--cream`: `#f2ede7`
- `--cream-dim`: `#c9c1bd`
- `--pink-soft`: `#edc3cf`
- `--pink-deep`: `#b8788d`
- `--hairline`: `#302c33`
- `--hairline-soft`: `#262329`
- `--token-bg`: `#0b0b0d`
- `--surface-3`: `#1e1b21`
- `--surface-4`: `#242028`
- `--cream-2`: `#ddd5cf`
- `--pink-bright`: `#efb9ca`
- `--pink-deep`: `#9c687a`
- `--warn`: `#c48770`

## Review priorities
Text contrast, motion preferences, keyboard navigation, focus management, mobile controls, and partner asset reliability. See [[Audit Findings]].

## Reel-inspired website motion — October 4, 2026

The founder requested applying the approved style to the website. Implemented a homepage kinetic introduction and glossy visual, a hosting walkthrough, Registry particle sphere, logo entrance and shorter stripe transitions. See [[Approved Site Motion]] for screenshots, source locations, lifecycle behavior and verification. [[Future Site Motion]] distinguishes completed adaptations from remaining experiments.

## Latest site revision

See [[Project Workspace Redesign]]. The homepage glossy loop has been replaced by an interactive project starter, and stripe navigation has been slowed. Earlier descriptions of those two effects describe the prior implementation. The approved promo reel remains unchanged.

## October 5 creative refresh

[[Creative Refresh]] supersedes the stripe-transition and rotating-sculpture website directions above. Use black, paper, and pale pink; neutral supporting grays; editorial Registry rows; slow visibility-managed dot topography; and a black curtain with white chapter copy.

## Latest dark workspace direction / October 5

[[Dark Creative Rebuild]] supersedes the cream Registry and Studio surfaces. Use ink surfaces, cream type, pale pink accents, bold local Manrope headlines, and visibility-managed dot motion for Status, Studio, Registry and the matching roadmap.

## Flow map and depth / October 5

[[Flow Map and Launchpad Discovery]] adds native scroll depth on dot artwork and reading progress. Keep content stable, respect reduced motion and the motion pause control, and retain the ink/cream/pale-pink palette.

## Modular reference direction / October 5

[[Modular Reference Refit]] — historical refit based on the supplied Home_X image: floating dark modules, square halftone, matrix headings, a personalized workspace, modular coin planning and native scroll depth. This supersedes the previous flat page treatment and eight-step launch interface.

## Targeted refinements / October 5

[[Targeted Page Refinement]] is the current direction. Restore the familiar homepage, Registry and Explore structures; keep Hosting and Rewards intact; refine Studio’s project sheet and Launch’s identity preview. Refresh the accepted design with dot motion rather than replacing each page.

## Branding and developer infrastructure / October 5

[[Branding and Own Hardware]] adds local provider marks, full X Pay labels, a 25-service developer directory, and a saved own-hardware planning path alongside Paymenter. Retain existing page structures. Pairing and execution remain future work.
