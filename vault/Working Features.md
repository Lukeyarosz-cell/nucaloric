# Working features — October 5, 2026

## Available without keys
	
- **Explore:** real Solana pool search by token name, symbol, or mint address, with provider-reported price, 24h change, liquidity and volume. Explore now defaults to primary-listed OTC Desks and PAID coins, with independently requested pool quotes. The dated PAID catalog and separate Pump.fun venue view are explained in [[Flow Map and Launchpad Discovery]]. Sort returned pools, inspect a pool, save up to 20 pools, and refresh a saved watchlist. Account and Dashboard display these saved live pools.
- **Pool details:** real pair-specific observations, token/pool addresses, market cap and FDV when returned, buy/sell counts, creation date, and source/explorer links. Missing metrics display Unavailable. Former example coin URLs direct people back to live Explore.
- **Status:** the public GitHub Pages site can read the five verified official provider feeds directly. Backend status API remains preferred where available. Browser and server collectors share the same component parsing; a feed failure means Unknown, never a fabricated provider outage. Twelve services still have no verified public status feed. Our 17 documented backend connectors remain unconfigured.
- **Project Studio and Dashboard:** multiple saved projects, milestone checklists, project search, recoverable archiving, JSON backup/import across devices, and existing Markdown brief export. Import validates every project before saving and imports new copies without replacing existing projects. Up to 100 projects and 50 milestones per project; backup limit 2 MB.
- The old wallet selector no longer claims a fake wallet connection.

## Storage and limits

Projects and watched pools persist in this browser on this website origin. Projects do not automatically synchronize across devices or between localhost and the public site; export/import a backup to move them. Watchlists are currently local to the browser. Local storage failure is shown rather than reporting a successful save.

Market observations come from DEX Screener, not a NUCALORIC pricing engine. Same-name tokens and manipulated pools can exist; token addresses are shown, and no token safety, holder count, liquidity-lock, allocation or AI score is inferred. Requests are read-only, manually refreshed, time out after 12 seconds, and show unavailable/rate-limit states without example-price fallbacks. A received observation becomes explicitly old after one minute. The watchlist supports at most 20 pools; searches show up to 30 matching provider pools.

No private keys, wallet signatures, payments, deployments of user tokens, paid API plans or credentials were used. Token launches, Paymenter checkout/provisioning, terminal access, AI execution, X posting and payments remain future integration work.

## Source and evidence

`live-market.js`, `projects.js`, `provider-status.js`, `working-features.css`, updated `refresh.js`, `operations.js`, `app.js`, and page markup. The local Node monitor imports the shared provider parser.

Evidence: `Evidence/Working Features/`. Real browser requests were verified separately from deterministic network-failure and data-validation tests. See `working-features.json`, existing workflow/motion/operations reports, and responsive screenshots.

Official API reference: [DEX Screener API](https://docs.dexscreener.com/api/reference). Public pool search, pair and token-pool endpoints require no key in the verified browser calls. Solana, Jupiter, OpenAI, Claude and GitHub status sources remain the verified feeds recorded in [[Service Monitoring]].

Live website: https://lukeyarosz-cell.github.io/nucaloric-site/
