# Data and persistence
`coinData` in app.js contains NUZERO, VORTEX, PARALLAX, PINKNODE, and MIRAGE, including prices, changes, liquidity, holders, launch score, venue, dates, allocations, lock/vesting, and X metrics. These values are fixtures.

`nucWatchlist` contains JSON coin keys and defaults to nuzero, vortex, and pinknode. `nucWallet` stores a wallet provider label. `nucTransition` is a sessionStorage navigation marker.

Watchlist parsing catches invalid JSON but does not validate arrays or known keys. Unexpected stored values may break rendering. An empty dashboard watchlist substitutes NUZERO, which can misrepresent an empty list.

Launch name/ticker changes update review outputs through textContent. Several dropdowns and selection cards are not fully reflected in the final review. `data-ai-apply="rewards"` has no corresponding rewards update branch, although its button is marked applied. These are source findings; runtime regression tests remain necessary.

## Refresh update
The launch review now includes supply, vesting, LP lock, rewards, distribution, Mind, and thesis. Rewards Apply updates the real form control. `nucLaunchDraft` stores a versioned local blueprint and active stage. See [[Experience Direction]].
