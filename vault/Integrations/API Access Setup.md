# API Access Setup

Review date: 2026-10-05. Tool installation and provider authorization are separate. No new provider account, merchant approval, wallet authorization, or production Paymenter portal was created in this update.

Installed in `tools/integrations/`: official `@solana/web3.js` 1.99.0, `@meteora-ag/dynamic-bonding-curve-sdk` 1.5.13, and `@xdevplatform/xdk` 0.6.6. Sources: [Solana RPC documentation](https://solana.com/docs/rpc), [Meteora SDK](https://github.com/MeteoraAg/dynamic-bonding-curve-sdk/blob/main/README.md), [X official tools](https://docs.x.com/tools-and-libraries). The package lock records exact resolved versions. This workspace is isolated from the website and status server. Installation lifecycle scripts were disabled. SDK imports pass and Solana devnet `getHealth` returned `ok`; no transaction was signed or submitted.

## Read-only commands

```bash
cd tools/integrations
npm ci --ignore-scripts
node access-check.cjs sdk
node access-check.cjs solana
# With account credentials supplied privately through environment:
node access-check.cjs x
node access-check.cjs paymenter
```

The X probe uses the official SDK's username lookup for XDevelopers; endpoint reads may consume the account's API allowance. The Paymenter probe performs an authenticated GET of the admin services endpoint and logs only HTTP status, never account/service data. Missing credentials produce a not-configured message rather than a success claim. The Solana probe uses devnet unless `SOLANA_RPC_URL` is explicitly provided. These commands do not update the website's connector status: a successful read-only workstation probe is not an integrated product workflow.

Supply credentials through protected server process environment, not HTML, browser storage, committed files, or vault notes. Templates are in `tools/integrations/.env.example` and `tools/status/.env.example`; they contain placeholders only. The scripts do not automatically read `.env` files.

## Access register

| Service | Next access step | Current product state |
| --- | --- | --- |
| Solana / Helius | Provision production RPC; choose commitment and quota handling | Devnet read-only tool checked; website not connected |
| Meteora | Review SDK/program configuration and transaction requirements | SDK imports; launch path planned |
| Jupiter / Birdeye | Confirm developer key, API family, and quota | Documentation recorded; no product connector |
| Raydium | Review official program/SDK and choose an explicit alternative route | Research only |
| Phantom / Solflare / Backpack | Implement real wallet adapters and consent flow | UI hooks only |
| Paymenter | Provide deployed portal URL, v1.2.0+ compatibility and scoped server token | Checkout handoff remains unconfigured |
| OpenAI / Claude / Gemini / Grok | Provision provider/project access and server-side usage budgets | Gateway planned |
| X social | Create/select app in [X developer console](https://developer.x.com), confirm plan and scopes | Official XDK installed; account access unconfirmed |
| X Money | Obtain official merchant eligibility/API docs from X | Conditional; access unconfirmed |
| GitHub | Existing CLI access uploads this private archive; product OAuth/app access is separate | Archive authorized; website connector not implemented |

Per-provider official references, dependencies, and acceptance gates are in `data/services.json` and the vault's `Integrations/` folder. Paymenter references: [API](https://paymenter.org/api/), [server extensions](https://paymenter.org/docs/guides/servers/), [payment gateways](https://paymenter.org/docs/guides/gateways/). Confirm current Birdeye endpoint details in its developer portal; several deep documentation pages were unavailable during review.

## Dependency review gate

`npm audit fix --ignore-scripts` was run; the installed lock still reports 13 findings (7 moderate, 6 high), including unresolved transitive advisories for bigint-buffer, stream-json, toml, and uuid. The audit report says no fix is available within the current dependency tree. Import checks are not a security clearance. Resolve/review the SDK tree before using it to process untrusted inputs or production transactions. The Node status server and browser site load none of these packages.

[[Integration Index]] · [[Service Monitoring]]
