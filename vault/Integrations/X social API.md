# X social API

Reviewed: 2026-10-05 · Category: Community · [[Integration Index]] · [[Implementation Roadmap]]

## Official access path

Approved developer app and an access plan; OAuth mode and scopes depend on the endpoint. Source: [official documentation](https://docs.x.com/fundamentals/authentication/overview).

## NUCALORIC implementation

User-authorized community publishing and project updates.

Website connector: **not connected**. The current UI and saved browser preferences do not establish production access. GitHub repository upload access, where applicable, is a separate workstation capability.

Acceptance gate: PKCE/user authorization, required scopes, revocation, quotas, and explicit publish consent work.

Dependencies: Foundation, project ownership, and backend deployment.

## Outage attribution

No verified machine-readable provider feed is configured. The page reports unknown and links to the official docs. Do not infer health from a marketing website or invent a status hostname.

## Official references

- [https://docs.x.com/fundamentals/authentication/overview](https://docs.x.com/fundamentals/authentication/overview)

## Installed tools

Official TypeScript XDK `@xdevplatform/xdk` is installed in the isolated `tools/integrations` workspace. It is for the social API; installation does not grant merchant or account access. [Official tools](https://docs.x.com/tools-and-libraries).
