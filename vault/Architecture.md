# Architecture
`index.html`, `explorer.html`, `coin.html`, `launchpad.html`, `optimizer.html`, `rewards.html`, `ecosystem.html`, `registry.html`, and `dashboard.html` are separate documents.

`app.js` uses native DOM queries and listeners. It initializes shared navigation transitions, toasts, wallet modal interactions, canvas drawings, coin fixtures, filters, optimization outputs, registry filters, command search, drawers, compare, dashboard rendering, and the launch wizard.

`styles.css` contains successive design iterations and responsive overrides. Later rules can override earlier versions; review computed styles before changing a component.

`assets/nucaloric-wordmark.svg` supplies the custom brand lettering. Five token identities live in `assets/tokens/`. Partner logos use external URLs.

No bundler or compilation is required. Serve the directory over HTTP. No server routes, secrets, dependencies manifest, on-chain programs, or database schema were found.

## Change boundaries
Shared JavaScript and CSS affect every page. HTML fixtures and shared coinData must remain consistent. Keep the downloaded ZIP as the original baseline. Use [[GitHub Setup]] for version control.
