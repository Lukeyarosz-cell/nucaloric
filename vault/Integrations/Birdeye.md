# Birdeye

Reviewed: 2026-10-05 · Category: Market data · [[Integration Index]] · [[Implementation Roadmap]]

## Official access path

Confirm endpoint access and API-key requirements with the developer portal. Source: [official documentation](https://docs.birdeye.so/).

## NUCALORIC implementation

Token market data and freshness checks for discovery.

Website connector: **not connected**. The current UI and saved browser preferences do not establish production access. GitHub repository upload access, where applicable, is a separate workstation capability.

Acceptance gate: Authorized reads, timestamp validation, rate limits, and unavailable-data UI work.

Dependencies: solana.

## Outage attribution

No verified machine-readable provider feed is configured. The page reports unknown and links to the official docs. Do not infer health from a marketing website or invent a status hostname.

## Official references

- [https://docs.birdeye.so/](https://docs.birdeye.so/)

Review limitation: several deep documentation URLs failed to load. Confirm current endpoint names and headers from the portal before implementing; no Birdeye API call was made.
