# Checklist — So an AI can build Coherosphere correctly (v3)

**Scope:** End‑to‑end guardrails so an autonomous agent can generate code, configs, and docs for the Coherosphere stack without ambiguity.

---

## 0) Canonical domains & environments
- Landing: `https://coherosphere.com`
- **App (UI):** `https://app.coherosphere.com` (Base44 hosting)
- **API:** `https://api.coherosphere.io`
- **Docs:** `https://docs.coherosphere.io`
- **Schemas (JSON Schema):** `https://schemas.coherosphere.io`
- Environments: `production`, `staging` (`https://staging.api.coherosphere.io`), `local`
- All OpenAPI `servers.url` MUST include the production URL exactly: `https://api.coherosphere.io`

## 1) Repositories (single source of truth)
- **coherosphere/architecture** — C1–C4, DDD, SM, OpenAPI, Event Schemas, CI governance
- **coherosphere/api** — Service implementations (contract‑first; generated from OpenAPI)
- **coherosphere/app** — Member UI (C2‑12), built for Base44; consumes OpenAPI + Event feeds

## 2) Repository structure (architecture repo)
```
assets/
  diagrams/
    C1_system/            # Stakeholders, Trust Boundaries, System Context
    C2_containers/        # 12 containers + dataflow + deployment
    C3_components/        # per container component diagrams
    C3_states/            # state machines (SM-xx.yy)
    C4_sequences/         # end-to-end flows (C4-01..C4-34)
    DDD/                  # Context Map, Subdomains, Contracts, Team Topologies
  specs/
    openapi/              # C2-0X_*.yaml (OpenAPI 3.1)
    events/               # JSON Schemas (2020-12) + _meta
  docs/                   # API Surface, ERD/Domain Model, SLOs, Parameter Governance
scripts/                  # CI helper scripts (validators, generators)
.github/workflows/        # CI (domain checks, schema validation, lint, build)
```

## 3) Naming & IDs (mandatory)
- **Containers:** `C2-0X` (e.g., `C2-01 Resonance Service`)
- **Components:** `C3-0X.yy` (e.g., `C3-01.04 Resonance Engine`)
- **Sequences:** `C4-XX` (e.g., `C4-03 Quadratic Funding`)
- **State Machines:** `SM-0X.yy` and reference **C2-ID** + entity name (e.g., `SM-02.01 CONTRIBUTION`)
- Diagrams must include the IDs **in the node labels**.
- OpenAPI files: `C2-0X_<service>_v1.yaml` (3.1.0)
- Events: `<domain>/<EventName>.v<major>.json` with `$id=https://schemas.coherosphere.io/events/<domain>/<EventName>.v<major>.json`

## 4) API contracts (OpenAPI, contract‑first)
- Version: OpenAPI 3.1.0 (JSON Schema 2020‑12 compatible)
- **Servers:** MUST include
  - `https://api.coherosphere.io` (production)
  - `https://staging.api.coherosphere.io` (staging)
  - `http://localhost:8080` (local)
- CI: **API Domain Validation** workflow must fail on any missing or wrong prod URL
- Response envelopes: standard problem+json for errors; pagination = cursor‑based
- Auth: OAuth2/OIDC (PKCE for public clients), JWT (aud=`coherosphere`, iss=`https://api.coherosphere.io/auth`)
- Rate Limits: define per‑route defaults + 429 error model
- Idempotency: POST with `Idempotency-Key`
- Versioning: URI stable; breaking changes → new `v2` file; minor changes via `x-minor-version`

## 5) Event contracts (JSON Schema)
- Draft: **2020‑12**
- `$id` base: `https://schemas.coherosphere.io/events/...`
- Common fragments: `assets/specs/events/_meta/common.json` (`$defs`: `ID`, `ULID`, `Money`, `Did`)
- Each event schema MUST have: `type: object`, non‑empty `required[]`, and semantic field names
- Domains: `poc`, `ethics`, `resonance`, `metrics`, `gov`, `treasury`, `hubs`, `security`
- CI: **Validate Event Schemas** workflow must fail on `$id`/`$schema` mismatch or missing `required`

## 6) DDD & model artifacts
- Context Map with relationships (Customer‑Supplier, ACL, Conformist, Shared Kernel)
- Subdomains: **Core** (Resonance, PoC, Governance), **Supporting** (Treasury, Identity, Metrics), **Generic** (Security, API Gateway)
- Contract types: Commands, Queries, Events (documented; Events are machine‑readable)
- ERD: Core aggregates (Contribution, Member, Project, Proposal, Round, Stream, KPI, Attestation)
- Team/Context alignment: Team Topologies (Stream‑aligned, Platform, Enabling) mapped to BCs

## 7) State machines (SM) — minimum set
- PoC: CONTRIBUTION lifecycle, LEDGER_ENTRY decay/recompute
- Governance: PROPOSAL, APPEAL
- Treasury: QF_ROUND, PAYOUT_STREAM
- Identity: DID/ATTESTATION, REPUTATION_SCORE
- Hubs: HUB_SYNC_FRAME, PROJECT
- Metrics: KPI_SNAPSHOT
- Ethics: ETHICS_EVAL
- Security: INCIDENT, TRANSPARENCY_REPORT
- Each SM references `C2-ID`, entity name, and key triggers/events

## 8) Sequences (C4) — minimum set (30+)
- C4‑01 Contribution → PoC → Resonance → Metrics
- C4‑02 Governance (Proposal → Vote → Execution → Audit)
- C4‑03 Quadratic Funding Round (Setup → Matching → Payout)
- C4‑04 Member Onboarding → Identity Verification → Reputation
- … (full list maintained in `assets/diagrams/C4_sequences/` + CSV index)

## 9) Security & compliance (musts)
- TLS everywhere; HSTS on `app.coherosphere.com`
- CORS allowlist: `https://app.coherosphere.com`, `https://docs.coherosphere.io`
- Cookies: `SameSite=Lax` or `None; Secure`; domain `.coherosphere.com` when needed
- Secrets via GitHub Environments/Secrets; no secrets in repo
- Audit: immutable transparency bundles; SIEM ingestion; incident runbook
- Privacy: data minimization; PII isolation in Identity; access logs retained per policy

## 10) Non‑functional requirements
- SLOs: Availability, p95 latency, error budget (document in `assets/docs/SLOs.md`)
- Throughput targets per key route; burst rate limits
- Observability: OpenTelemetry traces; `traceparent` from app → api; logs structured JSON
- Data retention windows & backup policy; recovery objectives (RPO/RTO)
- Performance budgets for UI (LCP/TBT/CLS) and API (p95 latency envelopes)

## 11) App (Base44) — invariants
- `PUBLIC_URL=https://app.coherosphere.com`
- `API_BASE_URL=https://api.coherosphere.io`
- OIDC redirects: `/auth/callback`, optional `/silent-renew`
- Realtime: WS/SSE passthrough; fallback long‑poll
- Security headers (CSP baseline provided); static assets hashed & cached immutably

## 12) CI/CD (minimum workflows in architecture repo)
- `validate-api-domain.yml` — OpenAPI servers URL gate
- `validate-event-schemas.yml` — JSON Schema 2020‑12 gate
- (optional) Spectral lint for OpenAPI, Mermaid render smoke test
- Status badges in README

## 13) Code generation & scaffolding
- Generate server stubs/clients from OpenAPI (api repo) — language: TypeScript (tRPC optional), or Go/Java per service
- SDK semantics align with OpenAPI and C4 sequences (error models, pagination, retries)
- Event producers/consumers typed from JSON Schemas (e.g., TypeBox/Zod generation)

## 14) Governance parameters & versioning
- Registry for λ, α, q, θ (MetaGov) with history and change policy
- Changes flow: Proposal → Vote → DecisionRecorded → PolicyChanged event
- Version pins in services; feature flags with default fallbacks

## 15) Definition of Done (per artifact)
- Has ID (C2/C3/C4/SM) and correct filename
- Validates in CI (schema, domains, lint)
- Linked in README or index CSV
- Has minimal examples (request/response or event payload)

---

**One‑liner sanity check:**  
If a fresh agent starts from this repo, it can:  
(1) resolve canonical domains, (2) generate API & event contracts, (3) scaffold services & UI,  
(4) pass CI gates, and (5) deploy the app against the production API URL.

