# Interaction map
| Surface | Behavior | State |
|---|---|---|
| Global search | Ctrl/Cmd+K opens command palette; result buttons navigate | DOM |
| Account drawer | Wallet label, dashboard links, watchlist | localStorage + DOM |
| Wallet modal | Stores chosen provider; displays demo address | nucWallet |
| Explore | Tag/search filtering, sort, compact view | DOM |
| Quick view | Coin metrics, watch and compare actions | DOM + watchlist |
| Compare | Up to selected sample coins, fixture metrics | memory |
| Coin tabs | Activates one detail panel | DOM |
| Launch wizard | Eight stages, score heuristic, creator/liquidity Apply | memory/inputs |
| Optimizer | Range controls recompute outputs | inputs |
| Rewards | Changes labels and XP presentation | memory/DOM |
| Registry | Status/search filters and detail drawer | DOM |
| Navigation | Timed transition with sessionStorage arrival marker | nucTransition |

There are no transaction submissions or API-backed health updates. Several animations run continuously; review canvas lifetime and reduced motion before production.
