# NUCALORIC — Creative project platform

Interactive front-end concept for an AI-assisted Solana launch platform.

Base platform features:
- Global command palette and direct Account dashboard
- Persistent watchlist with localStorage
- Explore quick-view drawer, sorting, compact mode and compare tray
- Multi-step launch builder with explainable AI recommendations
- Project workspace dashboard with saved plans and a Paymenter CLI gate
- Tabbed coin terminal with holders, launch, mind, treasury, rewards, social and history
- Animated launch maps and functional dot-matrix data surfaces
- Simplified navigation and stronger interaction hierarchy

Serve this directory over HTTP and open `index.html`. Partner logos are stored locally.

Project hosting: `hosting.html` provides saved workspace plans and setup script downloads. `hosting-config.js` connects real Paymenter product checkout links when configured. Purchases, provisioning, and live terminal access require a deployed billing portal and hosting backend; see [integration notes](docs/paymenter-integration.md).

Latest redesign: the homepage has an interactive project starter, Registry has a dark searchable catalog, Rewards has readable example progress, and Account opens a clearer workspace dashboard. Page transitions have a slower stripe reveal and respect reduced motion. See [redesign notes](docs/PROJECT_WORKSPACE_REDESIGN.md).

Creative refresh (October 5): monochrome chapter transitions, neutral three-color surfaces, purposeful dot motion, an editorial Registry with a capability shortlist, and `studio.html` for locally saved/exportable project briefs. See [refresh notes](docs/CREATIVE_REFRESH.md) and [launchpad research](docs/LAUNCHPAD_RESEARCH.md).
