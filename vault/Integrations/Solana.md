# Solana

Reviewed: 2026-10-05 · Category: Chain · [[Integration Index]] · [[Implementation Roadmap]]

## Official access path

Public RPC can be read without an account; production RPC capacity must be provisioned. Source: [official documentation](https://solana.com/docs/rpc).

## NUCALORIC implementation

Read chain state, simulate transactions, and confirm user-signed transactions.

Website connector: **not connected**. The current UI and saved browser preferences do not establish production access. GitHub repository upload access, where applicable, is a separate workstation capability.

Acceptance gate: A devnet transaction is simulated, approved in a real wallet, submitted, and confirmed; commitment, retries, and RPC limits are handled.

Dependencies: Foundation, project ownership, and backend deployment.

## Outage attribution

Provider report: [https://status.solana.com](https://status.solana.com). The monitor selects these relevant components: Mainnet Beta - Cluster, Mainnet Beta - RPC Nodes, US RPC Nodes, EU RPC Nodes, Asia RPC Nodes. A provider report does not prove that our connector works. A failed fetch means unavailable evidence, not a provider outage.

## Official references

- [https://solana.com/docs/rpc](https://solana.com/docs/rpc)
