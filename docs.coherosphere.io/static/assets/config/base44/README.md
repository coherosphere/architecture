# Base44 Integration — Coherosphere

This skeleton wires **app.coherosphere.com** (Base44 hosting) to **api.coherosphere.io** and **docs.coherosphere.io**.

## Folders
- `assets/config/base44/` — hosting checklist, CSP template (infra-facing)
- `app/.env.example` — environment variables for Base44
- `app/config/App-Config.json` — runtime config consumed by the frontend
- `.github/workflows/deploy-base44.yml` — CI: build, deploy, health checks

## Required GitHub secrets
- `BASE44_TOKEN` — deploy token for Base44
- (optional) `SENTRY_DSN`, etc.

After unzip, commit and push to `main`. The workflow deploys on changes to `app/**` or `assets/config/base44/**`.
