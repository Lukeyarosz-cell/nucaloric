# Project workspace redesign — October 4, 2026

The latest site direction favors useful controls and readable information over looping decorative objects. The approved promo reel remains the motion reference; individual effects are optional website treatments.

- Homepage: replaced the glossy idea/experiment/project loop with a project starter. Website, development and model selections preselect the hosting planner.
- Registry: preserved the top hero and all 49 capabilities; rebuilt the catalog with eight category filters, compact navigation, search, status filters and dark ink/pink cards. Category links and keyboard details work.
- Rewards: replaced the broken reward object with readable progress, next steps and a sample referral card. Example daily check-ins persist locally and show the correct remaining XP; these are not real redeemable rewards.
- Account: opens a clear workspace dashboard with the saved project plan, an initially empty watchlist, deployment/model/tool shortcuts and a disabled CLI preview.
- CLI: caution tape reads “UNLOCK CLI FUNCTIONS WITH PAYMENTER”. A configured billing portal can be linked, but only authenticated provisioning and a terminal backend can grant live access. Local browser flags do not unlock commands.
- Navigation: stripe entrance lasts 560 ms before changing pages, then a slower exit. Reduced-motion users navigate without the delay.

Source: `/home/luke/Projects/nucaloric-site`. New shared behavior lives in `workspace.js`; the existing planner, catalog and watchlist remain integrated.

## Design decisions

Use typography, spacing and grouped actions to explain a user's next step. Use ink surfaces, pale pink accents and restrained borders consistently below the Registry hero. Keep decorative motion in supporting areas; avoid continuous glossy objects beside practical project information. Keep payment and provisioning status honest rather than implying a saved plan is a purchased server.

## Evidence

Browser checks cover desktop and mobile across all ten pages, catalog filtering, keyboard access, saved plans, rewards persistence, Paymenter gating and transition timing. Screenshots and results are stored in `Evidence/Project Workspace Redesign`.
