# Phantom

Reviewed: 2026-10-05 · Category: Wallets · [[Integration Index]] · [[Implementation Roadmap]]

## Official access path

A compatible wallet and explicit user connection/signing consent. Source: [official documentation](https://docs.phantom.com/solana/integrating-phantom).

## NUCALORIC implementation

Wallet connection and user-approved Solana transaction signing.

Website connector: **not connected**. The current UI and saved browser preferences do not establish production access. GitHub repository upload access, where applicable, is a separate workstation capability.

Acceptance gate: Real connect, rejection, disconnect, network mismatch, and signing flows pass on devnet.

Dependencies: solana.

## Outage attribution

Wallet availability is device/session specific. Measure detection, authorization, and signing in the actual client; no authoritative global outage feed has been configured.

## Official references

- [https://docs.phantom.com/solana/integrating-phantom](https://docs.phantom.com/solana/integrating-phantom)
