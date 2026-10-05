# GitHub

Reviewed: 2026-10-05 · Category: Developer tools · [[Integration Index]] · [[Implementation Roadmap]]

## Official access path

GitHub CLI is already authorized for this project archive; an in-product integration needs its own authorization. Source: [official documentation](https://docs.github.com/en/rest/quickstart).

## NUCALORIC implementation

Source archive today; planned repository evidence and developer workflow connections.

Website connector: **not connected**. The current UI and saved browser preferences do not establish production access. GitHub repository upload access, where applicable, is a separate workstation capability.

Acceptance gate: App/user scopes, project ownership, private repository access, and webhook signature checks are implemented.

Dependencies: Foundation, project ownership, and backend deployment.

## Outage attribution

Provider report: [https://www.githubstatus.com](https://www.githubstatus.com). The monitor selects these relevant components: Git Operations, API Requests, Webhooks. A provider report does not prove that our connector works. A failed fetch means unavailable evidence, not a provider outage.

## Official references

- [https://docs.github.com/en/rest/quickstart](https://docs.github.com/en/rest/quickstart)
