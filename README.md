# Coherosphere — Architecture Repository

This repository is the **single source of truth** for the *Coherosphere* system architecture.  
It provides a complete, machine-readable specification of the system using the **C4 model**  
(Context → Containers → Components → Code), extended with **Domain-Driven Design (DDD)**,  
**State Machines (SM)**, and **OpenAPI / Event / Infrastructure specifications**.

---

## 1. Structure

| Level | Folder | Focus | Content |
|--------|---------|--------|----------|
| C1 – System Context | `assets/diagrams/C1_system/` | External actors, trust zones, boundaries | System, Stakeholders, Trust Boundaries |
| C2 – Containers | `assets/diagrams/C2_containers/` | Core services and interconnections | 12 core containers (C2-01 … C2-12) |
| C3 – Components & States | `assets/diagrams/C3_components/`, `assets/diagrams/C3_states/` | Internal service logic and state machines | 16+ component/state machine diagrams |
| C4 – Sequences | `assets/diagrams/C4_sequences/` | Behavioral flows across containers | 30+ end-to-end interaction flows |
| DDD – Domain Design | `assets/diagrams/DDD/` | Context maps, subdomains, contracts | Strategic & tactical DDD diagrams |
| Specs | `assets/specs/` | APIs, Events, SLOs, Governance Parameters | OpenAPI / CloudEvents / JSON Schema |
| Infra Config | `assets/config/` | Infrastructure and security configuration | CORS, DNS, CI Rules |
| Docs | `assets/docs/` | Architectural documentation | Markdown specifications and usage guides |

All diagrams are authored in **Mermaid**, render directly on GitHub,  
and map one-to-one to code-level or service-level artifacts.

---

## 2. Related Repositories

| Repository | Purpose | Deployment Target |
|-------------|----------|--------------------|
| `coherosphere/architecture` | System specification and design | Source of Truth |
| `coherosphere/api` | API layer, OpenAPI / gRPC / GraphQL federation | `api.coherosphere.io` |
| `coherosphere/app` | Frontend / member platform / governance UI | `app.coherosphere.com` |
| `coherosphere/docs` (planned) | Developer documentation and SDKs | `docs.coherosphere.io` |

---

## 3. Core Models and Artifacts

- **C1–C4** – Context, Container, Component, and Sequence models  
- **DDD** – Domain-Driven Design: Context Maps, Subdomains, Team Alignment  
- **SM-xx.xx** – State Machines for all major entities  
- **OpenAPI** – Public and inter-service APIs  
- **Events** – CloudEvents 1.0-compliant event schemas  
- **CORS Policy** – Unified access control policy (`assets/config/cors/cors-policy.json`)  
- **DNS Config** – Machine-readable DNS records and Terraform/BIND templates (`assets/config/dns/`)  
- **CI Rules** – Automated validation workflows for API, Events, and Domains (`.github/workflows/`)  

---

## 4. Design Principles

- **Clarity over complexity** – one abstraction per level  
- **Resonant modularity** – autonomy at the edge, coherence in the whole  
- **Transparency** – inspectable APIs, schemas, and governance parameters  
- **Evolvability** – all parameters and states evolve through governance  
- **Open specification** – everything under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

---

## 5. Validation and CI

Each commit is automatically validated through GitHub Actions:

- Mermaid diagram syntax validation  
- OpenAPI schema validation  
- Event schema validation  
- Domain whitelist enforcement (CORS + DNS consistency)  
- Version compliance checks across specs  

Scripts and workflows are defined in:
- `.github/workflows/`
- `scripts/validate_api_domain.py`
- `scripts/validate_event_schemas.py`

---

## 6. Build and Reproduction

A fully automated or AI-assisted build of the system should follow the dependency order:

1. Parse all C1–C4 and DDD diagrams  
2. Validate API, Event, and Governance specs  
3. Generate service scaffolds per container (C2 → C3)  
4. Apply infrastructure configurations (CORS, DNS, CI Rules)  
5. Export documentation to `docs.coherosphere.io`

All dependencies and tasks are listed in  
[`AI_build_checklist_v4.md`](AI_build_checklist_v4.md).

---

## 7. Deployment Domains

| Domain | Purpose | Host / Platform |
|---------|----------|----------------|
| `coherosphere.com` | Landing page | Base44 |
| `app.coherosphere.com` | Application / Member interface | Base44 |
| `api.coherosphere.io` | Main API gateway | Cloud / Container |
| `docs.coherosphere.io` | Documentation site | GitHub Pages |
| `schemas.coherosphere.io` | Public JSON Schemas | CDN / S3 |
| `governance.coherosphere.io` | DAO and proposal interface | App microfrontend |
| `status.coherosphere.io` | System uptime and metrics | UptimeRobot |
| `chat.coherosphere.io` | AI Copilot | OpenAI / Custom |
| `data.coherosphere.io` | Data lake | Parquet / Athena |
| `ai.coherosphere.io` | ML / Semantic layer | Vector DB + RAG |

---

## 8. License and Attribution

All contents are licensed under **Creative Commons Attribution 4.0 (CC BY 4.0)**.  
You are free to share, adapt, and reuse the material with attribution to the Coherosphere Collective.

---

## 9. Connect

- Website: [coherosphere.com](https://coherosphere.com)  
- GitHub: [github.com/coherosphere](https://github.com/coherosphere)  
- Nostr: [npub…](https://nostr.band/npub1kc9weag9hjf0p0xz5naamts48rdkzymucvrd9ws8ns7n4x3qq5gsljlnck)

---

**Technology that serves life. Governance that learns. Money that remembers truth.**  
*— The Coherosphere Collective, 2025*
