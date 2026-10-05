# Branding and own hardware — October 5, 2026

The founder requested recognizable provider logos, the full X Pay label, more developer services and a future own-server option alongside Paymenter. This extends the accepted page layouts in [[Targeted Page Refinement]].

## Website

Local recognizable marks accompany provider identities in the service directory, status rows and overview, roadmap connections and selected static labels. X Pay keeps the real X mark plus the complete label at desktop and phone sizes. It remains a conditional roadmap link, not a working payment service. Paymenter uses its official brand symbol; existing marks and new Simple Icons assets retain their original sources in `assets/partners/sources.json`. No invented vendor logos or hotlinked runtime logo dependencies.

The homepage retains its restored composition; GitHub, Cloudflare and Paymenter join its existing brand tiles. The ecosystem page now has a searchable, category-filtered 25-service directory. The status and roadmap catalogs share the same records. Eight additions: Cloudflare, Docker, Tailscale, Raspberry Pi, Supabase, Vercel, Netlify and PostgreSQL. GitHub was already present and is more prominent.

## Hosting paths

The existing Hosting design now offers Paymenter workspace or Your own hardware. The own-hardware path records Linux PC/server (x86_64) or Raspberry Pi (ARM64), Cloudflare Tunnel/Access, Tailscale or an existing private network, and an optional HTTPS app address. It saves and restores in the current browser and exports a JSON plan and local Linux setup script. It disables Paymenter checkout for this path. Existing managed product validation remains unchanged.

This is working planning UI. Device pairing, remote shell execution, agent installation and deployments are not enabled. No server login, password or API credential is requested. App addresses reject embedded credentials and query parameters. Local plans remain `nucHostingPlan` version 1 with additive fields; earlier Paymenter plans still restore by default. Machine enrollment is explicitly false.

## Planned implementation

Build an outbound authenticated machine bridge with owner-approved enrollment, short-lived pairing codes, machine identity, revocation, heartbeat and workload limits. Validate architecture, container compatibility, storage and backups. Keep credentials on the machine/backend; do not place tokens in the browser draft. Gate browser terminals by project ownership and a healthy authenticated connection. A PC/Raspberry Pi heartbeat must be separate from vendor service status. Paymenter remains the managed billing/provisioning path; own hardware is an alternative. The status board now separately lists the unconfigured Own-hardware bridge.

Stage 3 of the existing animated roadmap covers both paths. See [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/), [Tailscale](https://tailscale.com/docs/how-to/quickstart), [Docker Engine](https://docs.docker.com/engine/install/) and [Raspberry Pi remote access](https://www.raspberrypi.com/documentation/computers/remote-access.html).

## Provider visibility

Ten official feeds are configured; actual coverage is reported after each collection. Four new cloud/network providers plus Cloudflare add component scope. Cloudflare's feed may be unavailable directly in the browser because of CORS; the Node collector can read it. Unreadable or unconfigured provider evidence stays Unknown, while all authenticated product connections remain Not connected. Hardware and self-managed PostgreSQL/Docker do not get fabricated vendor uptime.

## Verification

Browser tests cover both hosting paths, configured checkout separation, local reload, JSON/script export, invalid URLs, service search/category filtering, branded identities and full X Pay labels. All 13 pages fit 1440, 390 and 320px. Existing project/market/status/roadmap tests continue to pass; status fixture counts now follow the shared catalog. Evidence: `Evidence/Branding and Own Hardware/`. Backend classification tests: 18 passed.

Live site: https://lukeyarosz-cell.github.io/nucaloric-site/
Source: `/home/luke/Projects/nucaloric-site`
