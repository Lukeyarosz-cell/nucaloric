# Backpack

Reviewed: 2026-10-05 · Category: Wallets · [[Integration Index]] · [[Implementation Roadmap]]

## Official access path

Use the wallet provider integration and user connection/signing consent. Source: [official documentation](https://docs.backpack.app/).

## NUCALORIC implementation

An additional wallet option for project creators.

Website connector: **not connected**. The current UI and saved browser preferences do not establish production access. GitHub repository upload access, where applicable, is a separate workstation capability.

Acceptance gate: Provider availability, rejection, disconnect, and devnet transaction signing pass.

Dependencies: solana.

## Outage attribution

Wallet availability is device/session specific. Measure detection, authorization, and signing in the actual client; no authoritative global outage feed has been configured.

## Official references

- [https://docs.backpack.app/](https://docs.backpack.app/)
