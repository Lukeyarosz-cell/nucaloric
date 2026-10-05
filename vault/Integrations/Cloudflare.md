# Cloudflare

Reviewed 2026-10-05. Product integration is planned and not connected.

## Role

Planned DNS, protected tunnels, edge delivery and storage options for developer projects.

## Access

Account, domain and an owner-configured Tunnel/Access policy; credentials remain on the machine or backend.

## Implementation gate

Verify domain ownership, access policy, tunnel health and revocation before attaching a project.

## Status and branding

Selected official public status feed: https://www.cloudflarestatus.com

Components: Tunnel, Access, Authoritative DNS, Workers, R2.

The verified JSON feed works in the Node collector. Browser access may fail because the feed does not advertise CORS; that is shown as unknown availability, not an outage.

Local mark: `assets/partners/cloudflare.svg`. Original source recorded in `assets/partners/sources.json`.

Official documentation: [Cloudflare](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

[[Branding and Own Hardware]] · [[Integration Index]]
