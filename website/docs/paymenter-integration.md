# Paymenter and project workspaces

## Current implementation

The static site now includes `hosting.html`, `hosting.js`, and `hosting-config.js`. Hosting is linked from global navigation, command search, the homepage, and the dashboard. Users can select a workload/compute profile, enter a project and optional mint/repository, save a local draft, export JSON, and download a quoted Bash setup script. The mint is a reference; it does not prove ownership or authorize a wallet. The browser neither provisions compute nor executes commands.

`hosting-config.js` is a public configuration file. It intentionally has no server credentials, prices, or product URLs by default. Checkout is disabled until a real product has been configured. This is a Paymenter checkout handoff, not a deployed Paymenter installation or an API billing integration.

## Connect the existing billing portal

Install/configure Paymenter separately with a payment gateway and a server extension matching the provider. Paymenter manages billing; its server extension manages provisioning. Obtain the actual public checkout URL for each product from that installation rather than guessing a route.

Set `paymenterUrl` to the HTTPS billing portal. Set the CPU/GPU product's `checkoutUrl`, an accurate `priceLabel`, and `reviewedFor` to supported workload keys (`web`, `dev`, `model`). Links must use the same origin as the portal. Prices/specifications/availability at Paymenter checkout are authoritative. Only list model workloads after verifying actual RAM/VRAM, hardware access, drivers, and provider permissions. A model can run on suitable CPU compute, but not every CPU/GPU product can support every model.

The current handoff does not send the saved project/mint/repository to Paymenter. Users choose the configured product there. An API integration is required to associate billing services and workspaces automatically.

## Backend required for a live workplace

Add authenticated accounts and persistent project membership. Verify wallet ownership with signed challenges when linking a mint. Store a server-side binding of account/project to Paymenter customer, order, and service identifiers. Keep API credentials exclusively on the server.

Track actual Paymenter/service states from the deployed version: awaiting payment, provisioning, ready, suspended, cancelled, failed. Treat a paid invoice and a successfully provisioned service as separate facts. Only authenticated owners/members may access that service. Use idempotent lifecycle updates and reconciliation with the provider; never infer provisioning from a checkout redirect.

Remote shell access requires an isolated provisioned environment per project and an authenticated terminal gateway. Authorize membership on each connection, issue short-lived service-scoped sessions, and proxy terminal transport on the server. Do not expose a host shell, management API keys, SSH private keys, or arbitrary execution routes in this static application. Suspension/cancellation must revoke sessions. Provider panel console access is a possible first release; verify its exact capabilities, since a server console is not necessarily a general-purpose development shell.

Web workloads need domain/HTTPS configuration and a persistent process manager. Model endpoints need actual hardware sizing and authenticated access from the app. Workloads run on hosted compute, with Solana used for on-chain project behavior; they do not execute inside a token.

## Official references

- [Paymenter server configuration](https://paymenter.org/docs/guides/servers/)
- [Payment gateways](https://paymenter.org/docs/guides/gateways/)
- [API reference](https://paymenter.org/api/), requires Paymenter v1.2.0 or higher
- [Server extension lifecycle](https://paymenter.org/development/extensions/server)

## Verification

Nine browser checks cover unconfigured checkout, required fields, draft restoration, input validation, shell quoting, both downloads, configured checkout, and unsupported/mismatched products. Ten pages are checked at desktop/mobile widths for JavaScript errors, overflow, and Hosting navigation. Generated Bash is syntax checked without executing it.
