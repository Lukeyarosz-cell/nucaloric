# Jupiter

Reviewed: 2026-10-05 · Category: Liquidity · [[Integration Index]] · [[Implementation Roadmap]]

## Official access path

Create a developer-platform key and confirm the API family, plan, and quotas. Source: [official documentation](https://developers.jup.ag/docs/get-started).

## NUCALORIC implementation

Price discovery and a reviewed swap-routing integration.

Website connector: **not connected**. The current UI and saved browser preferences do not establish production access. GitHub repository upload access, where applicable, is a separate workstation capability.

Acceptance gate: Quotes are fresh, token mints verified, slippage bounded, and signed execution confirmed on chain.

Dependencies: solana, helius.

## Outage attribution

Provider report: [https://status.jup.ag](https://status.jup.ag). The monitor selects these relevant components: Swap API V2, Ultra API, Swap API, Token API V2, Price API V3. A provider report does not prove that our connector works. A failed fetch means unavailable evidence, not a provider outage.

## Official references

- [https://developers.jup.ag/docs/get-started](https://developers.jup.ag/docs/get-started)
- [https://developers.jup.ag/changelog/developer-platform](https://developers.jup.ag/changelog/developer-platform)
