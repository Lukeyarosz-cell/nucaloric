# Modular reference refit — October 5, 2026

Reference: `/home/luke/Downloads/Home _ X.jpeg` (preserved in `Evidence/Modular Reference Refit/Home_X-reference.jpeg`). The supplied image shows a floating black budget card, dot-matrix heading, square-segment meter and pixel-cut background. The site adapts these ideas with original canvas/CSS artwork; the reference image is not bundled on the public website. Preserve the original SVG wordmark and the ink, cream and pale-pink palette.

## Site structure

All 13 pages now share a workspace strip, local workspace settings, motion control and rounded dark module treatment. Hero scenes add square halftone backgrounds and floating black information cards. Studio, Registry, Status, Explore, Hosting, Dashboard, Rewards, Optimizer and Ecosystem retain their existing tools and controls with a consistent surface treatment. Roadmap nodes become floating modules on a pixel field, with visible selection and real stage details. Existing example-only areas remain prototypes; styling is not evidence of backend availability.

Home is now a personal starting point: Coin desk, Project desk and Market watch. Create/Build/Discover focus and pinned module order persist on this browser. Actual local drafts, active projects, milestones, saved pools and selected tools shape the homepage. The old demo market/activity counters were replaced with capability, status and roadmap modules. Original creator/agent/community kits remain available.

## Personal workspace

`nucWorkspacePrefs` stores a local display name, focus, module spacing and pinned order. This is not an account or cross-device synchronization. Settings use a native accessible dialog; save failures explicitly report that changes apply only to the current page. Pinning preserves focus while moving modules. The page reads local data safely and renders personal text through `textContent`.

## Coin desk

The old eight-step launcher has been replaced by independently editable Identity, Budget and Distribution modules, plus optional Community links and Registry toolset modules. All updates feed live identity and budget previews. Artwork uploads accept PNG/JPEG/WebP up to 2 MB, decode locally, crop to 256 × 256 and store a bounded PNG in the plan. Unsupported images preserve existing artwork.

Budget uses the visitor's planned liquidity and personal cost reserve against their chosen SOL limit. The segmented meter and remaining amount use these entered values. No wallet funds, provider fee quote, safety score or AI optimization result is inferred. Over-limit plans show an explicit warning. Supply allocation and intended venue/vesting describe a plan, not an executed contract.

Drafts autosave to `nucCoinWorkbench`, with explicit save and storage-failure states. JSON download includes the full fields, optional modules and artwork; import validates its format before replacing the current plan. Invalid files leave current work intact. Name/ticker, integer supply, numeric amounts and HTTPS community links are checked before export. Previous `nucLaunchDraft` fields migrate into the desk without deleting the original blueprint. Nothing signs, pays, deploys or creates a token.

## Motion and depth

The square halftone uses the existing shared canvas clock: up to 30fps, pixel ratio capped at 1.5, only visible surfaces, paused when hidden. Hero backgrounds move up to 60 pixels with native scroll; floating cards move in the opposite direction. The homepage adds a sticky three-card story driven by document position. Mobile displays the story cards as a readable stack. Reduced motion freezes pixel art, removes depth shifts and makes the story unstuck. Existing motion controls and the workspace motion button share the pause preference. Interactive fields remain stationary. Roadmap canvas surfaces are unmounted when replaced by filters to avoid retaining old canvases.

## Source and publishing

`modular.css`, `modular.js`, `launch-workbench.js`, shared `refresh.js`, updated `flowmap.js` and 13 HTML pages. Frontend links carry a revision query so a previously visited browser receives the coordinated update. No build framework or new production dependency was added. The temporary HTML transformation helper lives outside the project; the website runs directly from its static files.

Authoring: `/home/luke/Projects/nucaloric-site`. Public checkout: `/home/luke/Projects/nucaloric-public-site`. Private archive: `/home/luke/Projects/nucaloric-github`. Obsidian: `/home/luke/Documents/NUCALORIC`. Backup: `/home/luke/Projects/nucaloric-backups/before-modular-refit-2026-10-05`.

## Verification

45 modular/coin-workflow checks, 40 working-feature checks, 25 motion/workspace checks, 23 service/roadmap checks, 26 source-attribution/flow checks, 18 existing interaction checks and 22 responsive layouts passed, with zero browser runtime errors. The six primary pages also fit at 320px. Review evidence covers persistence, portable plans, artwork, invalid imports, blocked storage, legacy migration, native depth changes, reduced motion, existing project backups and live data failure states. Screenshots and reports are under `Evidence/Modular Reference Refit`.

Related: [[Design System]], [[Flow Map and Launchpad Discovery]], [[Working Features]], [[Live Website]].
