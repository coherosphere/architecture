# Coherosphere — AI Build Guide (v4.0)

This document defines the machine-readable framework required to fully build, validate, and deploy the *Coherosphere* architecture through automated systems or AI agents.  
It ensures deterministic generation of all architectural artifacts, APIs, diagrams, and documentation.

---

## 1. Overview

| Level | Purpose | Source | Artifacts |
|--------|----------|----------|------------|
| **C1 – System Context** | External actors, zones, trust boundaries | `assets/diagrams/C1_system/` | Mermaid diagrams |
| **C2 – Containers** | 12 core services and interfaces | `assets/diagrams/C2_containers/` | Service diagrams + API Surface |
| **C3 – Components / States** | Internal logic and state transitions | `assets/diagrams/C3_components/`, `assets/diagrams/C3_states/` | Component and state diagrams |
| **C4 – Sequences** | End-to-end system interactions | `assets/diagrams/C4_sequences/` | ~34 sequence diagrams |
| **DDD – Domain Design** | Context map, subdomains, contracts | `assets/diagrams/DDD/` | Context, subdomain, and contract views |
| **Specs** | APIs, Events, SLOs, Governance | `assets/specs/` | OpenAPI & JSON Schema |
| **Infra Config** | CORS, DNS, CI validation rules | `assets/config/` | Policies and workflows |
| **Docs** | Docusaurus documentation | `coherosphere/docs` | Markdown + auto-imported architecture files |

---

## 2. Canonical Domains

All architectural, API, and documentation assets must use these domains:

```
https://api.coherosphere.io
https://staging.api.coherosphere.io
https://app.coherosphere.com
https://coherosphere.com
https://docs.coherosphere.io
https://schemas.coherosphere.io
https://chat.coherosphere.io
https://data.coherosphere.io
https://ai.coherosphere.io
http://localhost:3000
http://localhost:5173
```

**Rules:**
- All `servers.url` fields in OpenAPI specs must resolve to `https://api.coherosphere.io` (prod) or `https://staging.api.coherosphere.io` (stage).
- CORS configuration is defined in `assets/config/cors/cors-policy.json`.
- Browser isolation policies (**COEP**, **CORP**, **COOP**) must be set for both app and docs environments.

---

## 3. API Validation

**Workflow:** `.github/workflows/validate-api-domain.yml`

Steps:
1. Extract all URLs from `assets/specs/openapi/**/*.yaml`
2. Validate against the canonical domain whitelist
3. Check OpenAPI syntax (v3.1) and JSON Schema structure
4. Run [Spectral](https://github.com/stoplightio/spectral) linting rules:
   - Required: `info.version`, `info.title`, `servers`, `tags`
   - No external domains allowed
   - `x-api-version` must be defined

---

## 4. Event Schemas (CloudEvents 1.0)

**Path:** `assets/specs/events/`  
**Format:** JSON Schema Draft 2020-12

Each schema must include:
- `$id` = `https://schemas.coherosphere.io/events/<domain>/<version>.json`
- Fields: `type`, `source`, `time`, `data`
- Example payloads under `examples`
- `x-schema-version` and `description` required

**Validation Command:**
```bash
ajv validate -s schema.json -d example.json --spec=draft2020
```

---

## 5. Mermaid Validation

All `.mmd` diagrams (C1–C4, DDD, SM) must render without syntax errors.

**Check command:**
```bash
mmdc -i <input.mmd> -o <output.svg> --check
```

Requirements:
- Valid Mermaid syntax only  
- All subgraphs properly closed  
- SVG or PNG artifacts must be produced during CI builds

---

## 6. DDD Consistency

Bounded Contexts must align with their corresponding C2 containers.  
C4 sequences must reference their originating DDD events.

**Relationships:**  
`Context Map → C2 Container → Event Schema → C4 Sequence`

Validation:
- Matching event `type` across DDD and schema definitions  
- All subdomains labeled as Core / Supporting / Generic

---

## 7. Versioning

- OpenAPI: `info.version` (semver)  
- Events: `$id` suffix `/v1`, `/v1.1`, etc.  
- C4 Sequences: title includes version (`C4-01 — Flow Name (v1.0)`)

Changes to specs or schemas trigger automatic doc version updates.

---

## 8. Continuous Integration (CI)

| Workflow | Purpose |
|-----------|----------|
| `validate-api-domain.yml` | Validates domain consistency |
| `validate-event-schemas.yml` | Checks JSON Schema syntax and compliance |
| `validate-mermaid.yml` | Ensures Mermaid diagrams compile |
| `deploy-docs.yml` | Builds and deploys Docusaurus to GitHub Pages |
| `spectral-lint.yml` | OpenAPI linting and governance checks |
| `sbom-generate.yml` | Generates SBOM (CycloneDX) for transparency |

---

## 9. Documentation (Docusaurus)

**Repo:** [`coherosphere/docs`](https://github.com/coherosphere/docs)  
**Deployed at:** `https://docs.coherosphere.io`

**CI pipeline:**
1. Clone `coherosphere/architecture`
2. Copy:
   - `assets/diagrams` → `static/diagrams`
   - `assets/specs/openapi` → `static/openapi`
   - `assets/docs` → `docs/architecture`
3. Run `npm run build`
4. Deploy via GitHub Pages (`gh-pages` branch, CNAME: `docs.coherosphere.io`)

---

## 10. Security & Governance Checks

- Validate CORS, COEP, and CORP headers in CI  
- Verify DNS configuration via `assets/config/dns/dns-records.json`  
- Generate **SBOM (CycloneDX)** from all OpenAPI + event specs  
- Enforce audit trail — each change to a policy or schema must include a commit hash reference

---

## 11. Completeness Criteria

A build is **valid** only if:
- All 12 C2 containers exist  
- ≥30 C4 sequences are syntactically valid  
- All OpenAPI specs contain `servers.url` and `version`  
- All event schemas validate under `ajv`  
- All Mermaid diagrams compile  
- Docusaurus documentation builds successfully

---

## 12. AI Build Execution Order

A full AI or CI-based system build follows this deterministic order:

1. Parse all C1–C4 and DDD diagrams  
2. Validate OpenAPI, event, and governance schemas  
3. Generate service code skeletons (per C2 container)  
4. Apply infrastructure policies (CORS, DNS, CI)  
5. Compile documentation via Docusaurus  
6. Deploy API, App, and Docs environments

---

## 13. Licensing & Transparency

- License: **Creative Commons Attribution 4.0 (CC BY 4.0)**  
- All generated artifacts are open for reuse with attribution  
- All modifications must pass CI validation before merge

---

## 14. Ownership & Responsibilities

| Area | Maintainer |
|-------|-------------|
| C2–C3 Architecture | Architecture Team |
| OpenAPI + Events | API Team |
| C4 Sequences | Governance & Treasury |
| CORS / DNS / CI | DevOps |
| Docusaurus Documentation | Docs Team |

---

**Version:** 4.0  
**Date:** October 2025  
**Maintainer:** Coherosphere Collective  
**License:** CC BY 4.0
