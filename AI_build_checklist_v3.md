# Coherosphere — AI Build Checklist (v4.0)

Purpose:  
Defines the complete dependency and build graph required for an AI or automated pipeline to reconstruct the full Coherosphere system from specification to deployable artifacts.

---

## 1. System Overview

| Layer | Scope | Source of Truth | Output |
|--------|--------|------------------|---------|
| C1 – System Context | Actors, trust zones, external systems | `assets/diagrams/C1_system/` | Mermaid diagrams (`*.mmd`) |
| C2 – Containers | 12 core services (Resonance → UI) | `assets/diagrams/C2_containers/` | Container diagrams + API surface |
| C3 – Components / States | Internal logic per container | `assets/diagrams/C3_components/`, `assets/diagrams/C3_states/` | Component + State Machine diagrams |
| C4 – Sequences | Inter-service flows | `assets/diagrams/C4_sequences/` | End-to-end sequence diagrams |
| DDD – Domain Design | Context maps, subdomains, contracts | `assets/diagrams/DDD/` | Strategic + Tactical DDD diagrams |
| Specs | API, Events, SLOs, Parameters | `assets/specs/` | YAML / JSON schemas |
| Infra Config | CORS, DNS, CI Rules | `assets/config/` | JSON policies, Terraform, Workflow YAMLs |
| Docs | Architecture explanations | `assets/docs/` | Markdown documentation |

---

## 2. Repository Map

| Repository | Purpose | Deployment |
|-------------|----------|-------------|
| `coherosphere/architecture` | System specification and design (C1–C4 + DDD) | Source of Truth (static) |
| `coherosphere/api` | API implementation, adapters, and gRPC/GraphQL gateway | `api.coherosphere.io` |
| `coherosphere/app` | Frontend / member interface, governance UI | `app.coherosphere.com` |
| `coherosphere/docs` (planned) | Public documentation and SDKs | `docs.coherosphere.io` |

---

## 3. Required Assets per Build Step

### 3.1 Architectural Diagrams
- All `.mmd` files under `assets/diagrams/**`
- Must be validated via `mmdc` (Mermaid CLI)
- Naming conventions:
  - `C1_*` → Context
  - `C2_*` → Containers
  - `C3_*` → Components or State Machines
  - `C4_*` → Sequences
  - `DDD_*` → Domain / Team / Contract structure

### 3.2 Specifications
- API Specs: `assets/specs/openapi/`
  - REST, gRPC, GraphQL Federation
  - Must resolve under `https://api.coherosphere.io`
- Event Schemas: `assets/specs/events/`
  - CloudEvents 1.0-compliant
  - Includes JSON Schema validation
- Parameters, SLOs, Governance Policies: `assets/specs/governance/`

### 3.3 Infrastructure Configurations
- CORS: `assets/config/cors/cors-policy.json`
- DNS: `assets/config/dns/`
  - Includes `dns-records.json`, `terraform/main.tf`, `bind/*.zone.tpl`
- CI Workflows: `.github/workflows/`
  - `validate-api-domain.yml`
  - `validate-event-schemas.yml`
- Validation scripts: `scripts/validate_*.py`

---

## 4. Build Sequence (AI Pipeline)

| Step | Task | Input | Output |
|------|------|--------|---------|
| 1 | Parse architectural diagrams | `/assets/diagrams` | Extract structure and dependencies |
| 2 | Validate OpenAPI + Event Schemas | `/assets/specs/openapi`, `/assets/specs/events` | Validated spec bundle |
| 3 | Resolve service definitions | C2 Containers → C3 Components | Code scaffolds per service |
| 4 | Generate infra configs | `/assets/config/cors`, `/assets/config/dns` | Deployment-ready configurations |
| 5 | Link governance parameters | `/assets/specs/governance` | Parameter version files |
| 6 | Integrate CI/CD validation | `.github/workflows`, `/scripts` | Automated checks for build compliance |
| 7 | Export documentation | `/assets/docs`, `/README.md` | Generated Docusaurus or Markdown site |

---

## 5. Deployment Targets

| Domain | Purpose | Managed By |
|---------|----------|-------------|
| `coherosphere.com` | Landing Page | Base44 |
| `app.coherosphere.com` | Main Application | Base44 |
| `api.coherosphere.io` | API Gateway | Cloud / Container |
| `docs.coherosphere.io` | Documentation | GitHub Pages |
| `schemas.coherosphere.io` | JSON Schemas / API Specs | CDN / S3 |
| `governance.coherosphere.io` | DAO Interface | App Microfrontend |
| `status.coherosphere.io` | Uptime / Status | UptimeRobot |
| `chat.coherosphere.io` | AI Copilot Interface | OpenAI / Custom |
| `data.coherosphere.io` | Data Lake | Parquet / Athena |
| `ai.coherosphere.io` | ML / Semantic Layer | Vector DB + RAG |

---

## 6. Validation Rules

- All URLs in OpenAPI specs must resolve under `https://api.coherosphere.io`
- All CORS origins must match entries in `cors-policy.json`
- All DNS records must be declared in `dns-records.json`
- Each C3 component must reference its C2 parent ID
- Each C4 sequence must include valid participating containers
- Each SM (State Machine) must include defined events and transitions
- Each spec and config must have version headers (`version: "x.y.z"`)

---

## 7. Output Packages

| Bundle | Purpose | Location |
|---------|----------|-----------|
| `coherosphere_openapi_bundle.zip` | All validated OpenAPI specs | `/assets/specs/openapi/` |
| `coherosphere_event_schemas.zip` | All validated CloudEvents schemas | `/assets/specs/events/` |
| `coherosphere_cors_policy.zip` | Unified CORS config | `/assets/config/cors/` |
| `coherosphere_dns_config.zip` | Machine-readable DNS config | `/assets/config/dns/` |
| `coherosphere_ci_workflows.zip` | CI validation workflows | `/.github/workflows/` |

---

## 8. Change Control

- All modifications must include:
  - `version` bump in corresponding JSON/YAML
  - Updated diagram (`.mmd`) and regenerated image if applicable
  - Commit message format:  
    ```
    <type>(scope): <summary>
    e.g., spec(api): update PoC service schema to v1.4
    ```
- Every merged PR triggers:
  - Schema validation
  - CORS origin verification
  - DNS consistency check
  - Mermaid diagram syntax validation

---

## 9. Completion Criteria

The system is **AI-build-ready** when:
1. All C1–C4, DDD, and SM diagrams parse successfully.
2. All OpenAPI / Event / CORS / DNS specs validate without error.
3. All containers and components have unique IDs and traceable lineage.
4. CI pipeline passes: schema, syntax, and domain checks.
5. The architecture repo alone is sufficient for an AI to generate:
   - service code structure,
   - deployment configuration,
   - documentation,
   - and system-wide interrelations.

---

**Version:** 4.0  
**Maintained by:** Coherosphere Collective  
**License:** CC BY 4.0  
