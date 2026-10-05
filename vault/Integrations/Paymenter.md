# Paymenter

Reviewed: 2026-10-05 · Category: Hosting & billing · [[Integration Index]] · [[Implementation Roadmap]]

## Official access path

Deploy your own Paymenter portal; API reference requires v1.2.0+ and a server-side bearer token. Source: [official documentation](https://paymenter.org/api/).

## NUCALORIC implementation

Orders, invoices, and service state for paid developer workspaces.

Website connector: **not connected**. The current UI and saved browser preferences do not establish production access. GitHub repository upload access, where applicable, is a separate workstation capability.

Acceptance gate: Checkout, paid-order reconciliation, provisioning, suspension, and user ownership checks pass before terminal access is enabled.

Dependencies: Foundation, project ownership, and backend deployment.

## Outage attribution

Paymenter is self-hosted. Monitor our deployed portal and its upstream payment/provisioning dependencies separately; there is no global Paymenter runtime status for our installation. No portal URL has been configured.

## Official references

- [https://paymenter.org/api/](https://paymenter.org/api/)
- [https://paymenter.org/docs/guides/servers/](https://paymenter.org/docs/guides/servers/)
- [https://paymenter.org/docs/guides/gateways/](https://paymenter.org/docs/guides/gateways/)
- [https://paymenter.org/development/extensions/server](https://paymenter.org/development/extensions/server)
