# DEX Screener

Purpose: read-only Solana pool discovery and market observations for Explore and pool details.

Official API documentation: https://docs.dexscreener.com/api/reference

Implemented routes: `/latest/dex/search?q=…`, `/token-pairs/v1/solana/{mint}`, `/latest/dex/pairs/solana/{pool}`; the pair route also refreshes saved pool addresses. Calls were verified in a browser from the public website origin without an API key. Server-style requests can receive provider anti-bot rejections; the production frontend uses normal browser fetch.

The documented search/pair routes have a 300 requests/minute limit. NUCALORIC makes calls on page load or explicit search/refresh, with no price polling. A failed or rate-limited request displays unavailable data. No trading or transaction submission is implemented.

This runtime market integration supplements the 17-service deployment/status register. There is no verified official DEX Screener status feed configured, and market access is not evidence of token safety. See [[Working Features]].
