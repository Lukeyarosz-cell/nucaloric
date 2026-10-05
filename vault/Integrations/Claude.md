# Claude

Reviewed: 2026-10-05 · Category: AI · [[Integration Index]] · [[Implementation Roadmap]]

## Official access path

Provision Anthropic API access and keep credentials on the backend. Source: [official documentation](https://platform.claude.com/docs/en/api/overview).

## NUCALORIC implementation

A planned Claude model gateway.

Website connector: **not connected**. The current UI and saved browser preferences do not establish production access. GitHub repository upload access, where applicable, is a separate workstation capability.

Acceptance gate: Authenticated requests, quota handling, streaming interruption, and tenant metering pass.

Dependencies: paymenter.

## Outage attribution

Provider report: [https://status.claude.com](https://status.claude.com). The monitor selects these relevant components: Claude API (api.anthropic.com). A provider report does not prove that our connector works. A failed fetch means unavailable evidence, not a provider outage.

## Official references

- [https://platform.claude.com/docs/en/api/overview](https://platform.claude.com/docs/en/api/overview)
