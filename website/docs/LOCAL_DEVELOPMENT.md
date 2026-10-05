# Local development

The website has no frontend build step. For the live service-status API use Node.js 22+:

```bash
cd /home/luke/Projects/nucaloric-site
node tools/status/server.cjs
```

Open http://127.0.0.1:8080/. This PC currently runs the same server through the user service `nucaloric-preview.service`; do not start a second process on that port. Use `systemctl --user restart nucaloric-preview.service` after backend edits.

A plain Python/VS Code static preview can still render the site, but its status page explicitly falls back to the dated snapshot and cannot verify current server health. See [SERVICE_MONITORING.md](SERVICE_MONITORING.md) and [API_ACCESS.md](API_ACCESS.md).

```bash
node --check app.js
node --test tools/status/monitor.test.cjs
```

Browser review scripts live under `tools/review/`; see that README for Playwright setup. Evidence for the service update is stored in the Obsidian vault under `Evidence/Service Integrations/`. Brave, VS Code and Obsidian were opened on the PC for review.
