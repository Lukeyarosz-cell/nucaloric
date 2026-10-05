# OpenAI

Reviewed: 2026-10-05 · Category: AI · [[Integration Index]] · [[Implementation Roadmap]]

## Official access path

Create project access and store an API credential on the backend with usage controls. Source: [official documentation](https://developers.openai.com/api/reference/overview).

## NUCALORIC implementation

A planned Responses/Realtime gateway for project assistants.

Website connector: **not connected**. The current UI and saved browser preferences do not establish production access. GitHub repository upload access, where applicable, is a separate workstation capability.

Acceptance gate: Server-side authentication, budgets, streaming errors, cancellation, and tenant boundaries are tested.

Dependencies: paymenter.

## Outage attribution

Provider report: [https://status.openai.com](https://status.openai.com). The monitor selects these relevant components: Responses, Realtime, Chat Completions, Embeddings, Images, Audio. A provider report does not prove that our connector works. A failed fetch means unavailable evidence, not a provider outage.

## Official references

- [https://developers.openai.com/api/reference/overview](https://developers.openai.com/api/reference/overview)
