# Meteora

Reviewed: 2026-10-05 · Category: Liquidity · [[Integration Index]] · [[Implementation Roadmap]]

## Official access path

Official SDKs are public; chain operations require RPC capacity, a wallet, and transaction fees. Source: [official documentation](https://docs.meteora.ag/get-started).

## NUCALORIC implementation

Dynamic Bonding Curve launch configuration and a planned liquidity migration path.

Website connector: **not connected**. The current UI and saved browser preferences do not establish production access. GitHub repository upload access, where applicable, is a separate workstation capability.

Acceptance gate: Devnet create/swap/migrate tests pass with validated parameters and explicit signing; fee and migration behavior are documented.

Dependencies: solana, phantom, helius.

## Outage attribution

No verified machine-readable provider feed is configured. The page reports unknown and links to the official docs. Do not infer health from a marketing website or invent a status hostname.

## Official references

- [https://docs.meteora.ag/get-started](https://docs.meteora.ag/get-started)
- [https://github.com/MeteoraAg/dynamic-bonding-curve-sdk/blob/main/README.md](https://github.com/MeteoraAg/dynamic-bonding-curve-sdk/blob/main/README.md)

## Installed SDK / dependency gate

`@meteora-ag/dynamic-bonding-curve-sdk` 1.5.13 and `@solana/web3.js` 1.99.0 are installed only in the isolated developer tooling directory. Import checks pass. No launch, swap, or signing operation was submitted. The locked dependency tree has unresolved npm audit advisories; review/resolve them before processing transaction input in production. The website monitor has no npm dependencies.
