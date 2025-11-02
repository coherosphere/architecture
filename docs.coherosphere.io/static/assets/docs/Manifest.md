---
id: manifest
slug: /manifest
title: Canonical Domain Manifest
sidebar_label: Manifest
description: Canonical reference for C1–C4, DDD, Events, and Specs mapping within the Coherosphere architecture.
---

# Architecture Manifest

Objective: Outline the guiding principles, structure, and intent of the Coherosphere architecture.
Note: Describes how the system aligns human, technological, and governance layers for coherent collective intelligence.
Serves as the conceptual anchor and reference frame for all architectural documents.

---

## 1. System Overview

| Layer | Purpose | Core Components |
|-------|----------|-----------------|
| **C1 – Foundation** | Core primitives, identity, base contracts | Identity Service, Registry, Base Schemas |
| **C2 – Domain Services** | Autonomous modular domains | Resonance, Governance, Treasury, Ethics, Metrics |
| **C3 – Coordination Layer** | Cross-domain orchestration and consensus | Scheduler, Meta-Governance, SRI Aggregator |
| **C4 – Interface Layer** | External APIs, UIs, connectors | Gateways, SDKs, External Integration APIs |

---

## 2. Domain Architecture (C2)

| Domain | Description | Linked Spec |
|---------|--------------|--------------|
| **C2-01 Resonance** | Impact × Alignment engine for contribution scoring | `/assets/specs/openapi/C2-01_Resonance.yaml` |
| **C2-02 Proof of Contribution (PoC)** | Verifiable contribution attestations | `/assets/specs/openapi/C2-02_PoC.yaml` |
| **C2-03 Governance** | DAO-based decision governance | `/assets/specs/openapi/C2-03_Governance.yaml` |
| **C2-04 Treasury** | Multi-asset resource management and funding | `/assets/specs/openapi/C2-04_Treasury.yaml` |
| **C2-05 Identity** | Member identity and credentials | `/assets/specs/openapi/C2-05_Identity.yaml` |
| **C2-06 Hubs** | Decentralized coordination of subnets | `/assets/specs/openapi/C2-06_Hubs.yaml` |
| **C2-07 Metrics** | KPI and SRI data collection | `/assets/specs/openapi/C2-07_Metrics.yaml` |
| **C2-08 Ethics** | Normative guardrails and bias detection | `/assets/specs/openapi/C2-08_Ethics.yaml` |
| **C2-09 Knowledge** | Semantic graph of institutional knowledge | `/assets/specs/openapi/C2-09_Knowledge.yaml` |
| **C2-10 Security** | Zero-trust policies and verifiable access | `/assets/specs/openapi/C2-10_Security.yaml` |
| **C2-11 Gateway** | External system entrypoint and API mesh | `/assets/specs/openapi/C2-11_Gateway.yaml` |

---

## 3. Parameter Governance

Governance of system parameters (λ, α, θ, quorum, threshold, rubric) is handled via the **Parameter-Registry Protocol**.

- Parameters stored in `/assets/specs/params/*.json`
- Signed via Ed25519 (multi-sig governance keys)
- Each change emits: `DecisionRecorded` + `PolicyChanged` events
- Fallback: **soft revert** on metric drift > X% / **hard stop** on security incidents

---

## 4. AI Build Automation

The AI build pipeline maps **C-IDs** to their source domains and code generation outputs.

| C-ID | Description | Output Target |
|------|--------------|----------------|
| **C1–C4** | Layer separation and dependency flow | `/assets/diagrams/overview/Architecture_Stack.mmd` |
| **AI_BUILD_GUIDE_v4** | Defines automated build mapping | `/assets/docs/AI_BUILD_GUIDE_v4.md` |
| **CODEGEN_HARNESS** | Auto-validates generated SDKs and mocks | `.github/workflows/validate-codegen-harness.yml` |

---

## 5. Documentation and Index Generation

| Component | Description | Source |
|------------|-------------|---------|
| **Docusaurus Docs** | Serves `/assets/docs` under `docs.coherosphere.io` | `docs.coherosphere.io/` |
| **Dynamic Indexes** | HTML indexes generated for diagrams, OpenAPI specs, and events | `scripts/gen-asset-indexes.mjs` |
| **Diagrams Overview** | Auto-listed via `/diagrams` | `/assets/diagrams/overview/*` |
| **Specs Overview** | Auto-listed via `/specs` | `/assets/specs/openapi/*` |
| **Event Schemas** | Auto-listed via `/eventschemas` | `/assets/specs/events/*` |

---

## 6. Validation & Integrity

- **OpenAPI Specs** validated by `@redocly/cli`
- **Events** validated via Ajv (JSON Schema Draft 2020-12)
- **Diagrams** validated via `validate-mermaid.yml`
- **Codegen Contracts** validated against `/assets/specs/openapi`

---

## 7. Versioning and Evolution

| Version | Date | Major Changes |
|----------|------|----------------|
| **v4.0** | 2025-08 | Integration of DDD + Specs layers |
| **v4.1** | 2025-09 | C4 Diagram automation and OpenAPI validation |
| **v4.2** | 2025-10 | Full Codegen + Harness integration |
| **v4.3** | 2025-11 | Dynamic asset indexing + AI build mapping + Governance parameters |

---

## 8. Governance Model

| Role | Scope | Authority |
|------|--------|------------|
| **Meta-Governance DAO** | Parameter registry, architecture consistency | M-of-N signature approval |
| **Resonance Core** | Validation of contribution signals | Weighted by trust & alignment |
| **Ethics Guard** | Oversight of bias and model norms | Prevents systemic drift |
| **Treasury Ops** | Resource allocation enforcement | Budget consensus |
| **Knowledge Custodian** | Semantic coherence of ontology | Schema evolution control |

---

**Prepared by:** the coherosphere collective 
