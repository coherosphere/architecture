---
id: manifest
slug: /manifest
title: Canonical Domain Manifest
sidebar_label: Manifest
description: Canonical reference for C1–C4, DDD, Events, and Specs mapping within the Coherosphere architecture.
---

# Architecture Manifest

The **Coherosphere Manifest** defines the canonical linkage between:
- **C1–C4 architecture layers** (System → Container → Component → Sequence)
- **DDD domains** and their bounded contexts
- **Specification assets** (`/assets/specs/*`)
- **Governance entities** and **AI build readiness mappings**

---

## Structure Overview

| Layer | Focus | Assets | Description |
|-------|--------|---------|-------------|
| **C1** | System Context | `/assets/diagrams/C1_system/` | Defines boundaries, stakeholders, and trust zones. |
| **C2** | Container View | `/assets/diagrams/C2_containers/` | Functional surface: APIs, dataflow, deployment. |
| **C3** | Components & States | `/assets/diagrams/C3_*` | State machines, domain models, and data persistence. |
| **C4** | Sequences | `/assets/diagrams/C4_sequences/` | Behavioral flows between containers and events. |
| **DDD** | Domain Design | `/assets/diagrams/ddd/` | Subdomains, contexts, and team ownership maps. |
| **Specs** | JSON + OpenAPI | `/assets/specs/*` | Machine-readable definitions for APIs and events. |

---

## Cross-Layer Consistency

| Reference | Linked Element | Description |
|------------|----------------|-------------|
| `C4-xx` | ↔ `DDD-EVT-xx` | Each behavioral sequence must emit at least one DDD event. |
| `C2-xx` | ↔ `OpenAPI` | Every container exposes a validated OpenAPI domain. |
| `SM-xx` | ↔ `C4-xx` | State transitions correspond to observable event flows. |
| `Manifest` | ↔ `AI_BUILD_GUIDE_v4` | Mapping of architecture identifiers to AI build scaffolding. |

---

## Validation & CI

- **Validated via CI workflows** (`validate-arch-openapi.yml`, `validate-mermaid.yml`, `validate-codegen-contracts.yml`)
- **Automatic schema validation** for events and OpenAPI specs
- **Mermaid syntax verification** for diagrams
- **AI Build harness mapping** verified through `codegen_harness_validate.sh`

---

## License & Attribution

- **License:** Creative Commons Attribution (CC BY 4.0)  
- **Source:** [`coherosphere/architecture`](https://github.com/coherosphere/architecture)  
- **Maintainer:** The Coherosphere Collective  
- **Last updated:** November 2025