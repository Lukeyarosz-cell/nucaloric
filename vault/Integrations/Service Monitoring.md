# Service Monitoring

Reviewed and implemented locally on 2026-10-05. Canonical register: `data/services.json`. Public pages: `status.html`, `roadmap.html`. Provider sources and access requirements are recorded individually in the Obsidian vault under `Integrations/`.

The status monitor reads five verified public feeds: [Solana](https://status.solana.com), [Jupiter](https://status.jup.ag), [OpenAI](https://status.openai.com), [Claude](https://status.claude.com), and [GitHub](https://www.githubstatus.com). It selects relevant components rather than assigning a provider's consumer-product incident to unrelated APIs. Other providers have unknown status until a verified adapter is configured. Wallet availability belongs to the actual client session. Paymenter's runtime belongs to our self-hosted portal.

## Runtime

Requires Node.js 22+; the website/status server uses only Node's built-in modules. No SDK package is loaded by the server.

```bash
node tools/status/server.cjs
```

Open `http://127.0.0.1:8080/status.html` or `/roadmap.html`. Public API: `GET /api/service-status`; process health: `GET /api/health`. Feed reads have a 10-second timeout, 60-second server cache, and 180-second evidence expiry. The browser refreshes once a minute while visible. Probes come from fixed, version-controlled provider sources; the browser cannot supply arbitrary target URLs. Feed errors yield **unknown**, not provider outage.

The current PC runs `nucaloric-preview.service` as a user service. Manage it with `systemctl --user status|restart nucaloric-preview.service`. Local preview remains bound to loopback. Production deployment requires an HTTPS reverse proxy, a protected backend health aggregate, and independent external checks; setting an environment label alone does not deploy production infrastructure.

## Two distinct signals

- Provider report: availability of selected components from the official public source. Include checked time, evidence, active incidents, and source link.
- NUCALORIC connection: authenticated evidence from our own connector. No health feed means **not connected**; a configured feed that fails means **unknown**. Authentication, quota, backend, and upstream errors remain distinguishable.

Our own section covers the website/monitor process, the collector, project identity/API, workspace provisioning, terminal gateway, and AI gateway. Only the website and collector are currently running here. Do not use wallet/localStorage demo flags or repository-upload access as product-connector health.

## Internal health contract

Configure `NUC_INTERNAL_HEALTH_URL` and optional `NUC_INTERNAL_HEALTH_TOKEN` in protected process environment. URLs must use HTTPS (loopback HTTP is permitted), with no embedded credentials or query token. Only this configured server target is contacted. The endpoint should return:

```json
{
  "services": {
    "paymenter": {
      "status": "degraded",
      "reason": "authentication",
      "checkedAt": "2026-10-05T15:00:00Z"
    },
    "terminal-gateway": {
      "status": "operational",
      "reason": "healthy",
      "checkedAt": "2026-10-05T15:00:00Z"
    }
  }
}
```

The example timestamps are illustrative; observations older than 180 seconds become unknown. Allowed health states: `operational`, `degraded`, `outage`, `maintenance`, `unknown`. Allowed reason codes: `healthy`, `authentication`, `quota`, `timeout`, `backend_error`, `provider_error`, `maintenance`, `unknown`. Missing service IDs are not connected. Internal IDs: `project-api`, `workspace-provisioner`, `terminal-gateway`, `ai-gateway`; provider IDs are in the register. The monitor publishes only allowlisted status/reason/time fields. Never send raw error messages, credentials, prompts, or customer account details into this endpoint.

## Saved observations and downtime

```bash
node tools/status/snapshot.cjs
```

This writes a dated `data/service-status.json`. A plain static host can show it when the live API is unavailable, with an explicit snapshot warning. Expired observations become unknown; snapshot process health is never presented as current. Browser failure to reach our API does not establish a global outage or root cause.

No historical uptime, incident durations, or alert delivery is claimed. To measure actual downtime, add an independently hosted synthetic probe, persist incident transitions, assign an incident owner, and document recovery before presenting uptime percentages. Provider status alone does not verify an on-chain program, a wallet extension, or our launch workflow end to end.

## Roadmap and access

Seven stages cover visibility, identity/wallet/RPC, liquidity, billing/workspaces, AI gateways, X community, and conditional X payments. Stages have dependencies and explicit acceptance gates, not invented dates. X social tools are available; [X Money](https://money.x.com/en) merchant API access has not been established from the official public documentation reviewed. Independent xMoney products are not the X platform.

The isolated Solana/Meteora/X SDK workspace is documented in `API_ACCESS.md`. Its npm audit still contains unresolved dependency advisories; it is not loaded into the website server and must pass dependency review before production transaction handling.

## Verification

```bash
node --test tools/status/monitor.test.cjs
PLAYWRIGHT_MODULE=/tmp/nucaloric-refresh/node_modules/playwright node tools/review/operations.cjs
```

Tests cover outage scope, malformed feeds, incident state, stale and future internal evidence, credential-safe configuration, live/search/filter/roadmap interactions, offline and stale fallback, and mobile overflow. Existing site interaction and responsive checks remain in `tools/review/`.

[[Integration Index]] · [[Implementation Roadmap]] · [[API Access Setup]]

## Verified local review

18 monitor tests, 23 operations UI checks, 18 existing interactions, and 22 existing-page responsive checks passed. The two new pages also passed mobile overflow checks. JavaScript syntax and local links pass. Evidence: `Evidence/Service Integrations/`.

## Current interface

See [[Flow Map and Launchpad Discovery]] for the selectable animated implementation network and expanded status board, component evidence and actual observed check history.
