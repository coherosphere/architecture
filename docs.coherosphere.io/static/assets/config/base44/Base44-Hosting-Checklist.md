# Coherosphere — Base44 Hosting Checklist (app.coherosphere.com)

**Scope:** Frontend (C2-12 UI) on Base44. API: https://api.coherosphere.io, Docs: https://docs.coherosphere.io.

## 1) DNS & TLS
- [ ] CNAME `app.coherosphere.com` → Base44 target
- [ ] TLS enabled (HSTS recommended)
- [ ] IPv6 if available

## 2) Environment / Config
- [ ] `PUBLIC_URL=https://app.coherosphere.com`
- [ ] `API_BASE_URL=https://api.coherosphere.io`
- [ ] `DOCS_URL=https://docs.coherosphere.io`
- [ ] `AUTH_ISSUER=https://api.coherosphere.io/auth`
- [ ] `AUTH_AUDIENCE=coherosphere`
- [ ] `SRI_FEED=https://data.coherosphere.io/sri/latest.json` (optional)

## 3) CORS & Cookies
- Allowlist origins: `https://app.coherosphere.com`, `https://docs.coherosphere.io`
- Cookies: `SameSite=Lax` (or `None; Secure` if cross-site)

## 4) Auth
- Redirect URIs:
  - `https://app.coherosphere.com/auth/callback`
  - `https://app.coherosphere.com/silent-renew` (if SPA)
- Post-logout redirect: `https://app.coherosphere.com/`

## 5) Realtime
- WebSocket/SSE passthrough for live dashboards (fallback: long-poll)

## 6) Performance
- CDN immutable caching for `/assets/**`
- No-store for authenticated requests
- Brotli + HTTP/2 (or 3)

## 7) Security Headers (baseline)
- See `CSP-Template.txt`
- Referrer-Policy: `strict-origin-when-cross-origin`
- Permissions-Policy: minimal
- X-Content-Type-Options: `nosniff`

## 8) Observability
- OpenTelemetry JS; propagate `traceparent` to API
- Smoke endpoints: `/healthz`, `/version.json`

## 9) CI/CD
- Contracts gate: OpenAPI + JSON Schema validation
- Block deploy on failure
