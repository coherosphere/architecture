# Coherosphere — Unified CORS Policy (v1.2.0)

This repository file is the **single source of truth** for all CORS settings across gateways and edges.

## File
- `assets/config/cors/cors-policy.json`

## Environments
- **api** → `api.coherosphere.io` (production origins only)
- **api_staging** → `staging.api.coherosphere.io` (production + localhost)

### Allowed Origins (production)
- app.coherosphere.com, coherosphere.com
- docs.coherosphere.io, schemas.coherosphere.io, status.coherosphere.io
- governance.coherosphere.io, dev.coherosphere.io
- events.coherosphere.io, metric.coherosphere.io, audit.coherosphere.io
- chat.coherosphere.io, data.coherosphere.io, ai.coherosphere.io

### Extras (staging only)
- http://localhost:3000
- http://localhost:5173

## Methods / Headers
- Methods: GET, POST, PUT, PATCH, DELETE, OPTIONS
- Allowed Headers: Authorization, Content-Type, Accept, X-Request-Id, X-Idempotency-Key, X-Client-Version, If-None-Match
- Exposed Headers: ETag, X-Request-Id, X-RateLimit-Remaining, X-RateLimit-Reset
- Credentials: true
- Max-Age: 86400 seconds

## Usage
- **NGINX** (render from JSON → nginx include via your deployment tooling)
- **Express** (load JSON and apply per-request whitelist)
- **Cloudflare Worker** (read JSON and set headers conditionally by Origin)

> Maintain this **one JSON** and generate environment-specific configs during deployment.