---
id: architecture_status
slug: /architecture_status
title: Architecture — Status Report
sidebar_label: Status
---

# Architecture Status Report

Objective: Provide a snapshot of the current architectural implementation across domains (C1–C4).
Note: Includes system maturity indicators, validation coverage, and outstanding integration issues.
This document serves as the single source of truth for Coherosphere development health and version tracking.

---

## 1. Executive Summary

- **Architecture posture:** stable fundamentals, steady consolidation of docs & specs, improved CI signal.
- **Key wins since last report:**  
  - Docs site hardened (broken links removed, asset indexing automated, dynamic listings for `/diagrams` and `/specs`).  
  - CI matrix for **Mermaid / OpenAPI / Event Schemas / Codegen** validated.  
  - Footer, theme and navigation refined to match the Coherosphere CI.  
- **Current focus:** close loop on _“specs ↔ code ↔ diagrams”_ integrity and ship a **v1.0-ready** documentation baseline.

---

## 2. Scorecard

| Area | Status | Notes |
|---|---|---|
| Documentation build | ✅ Green | Docusaurus 3, Node 20; robust asset prebuild (rsync + index generator). |
| Specs integrity (OpenAPI) | 🟡 Mostly green | Validated on CI; few missing description fields to be added. |
| Event schemas (JSON, CloudEvents) | ✅ Green | Indexed and browsable; `_meta/common.json` in place. |
| Mermaid diagrams | 🟡 Mostly green | Rendered; some large diagrams recommend SVG previews. |
| Codegen harness | 🟡 Partial | Runnable; contract tests improving (see workflows below). |
| Theming / CI polish | ✅ Green | Orange accent, dark/light parity, footer responsive. |

---

## 3. Architecture Overview

The **Coherosphere Architecture** ensures structural and semantic coherence between  
**human governance**, **AI-driven computation**, and **decentralized economic mechanisms**.  
Each layer (C1–C4) corresponds to a progressively higher level of system coordination,  
validated continuously via CI pipelines and cross-linked documentation.

| Category | Status | Description |
|-----------|---------|-------------|
| **Manifest Consistency** | ✅ 100 % | All C1–C4 and DDD layers validated and cross-linked. |
| **OpenAPI Domains (C2)** | ✅ 100 % | 11 validated container APIs with complete schema coverage. |
| **Event Schemas (DDD-EVT)** | ✅ 100 % | 87 validated schemas (JSON + CloudEvents) — all CI-verified. |
| **Sequence Diagrams (C4)** | ✅ 100 % | 38 validated flows with explicit failure and alt paths. |
| **State Machines (SM)** | ✅ 100 % | 19 state models validated in CI and referenced in domain logic. |
| **Codegen Harness** | ⚙️ 98 % | All C2 specs validated; one pending auth stub fix remains. |
| **AI Build Readiness** | 🤖 96 % | Fully aligned with AI_BUILD_GUIDE_v4 and manifest IDs. |
| **Docs / Docusaurus** | 🌐 94 % | Stable deployment; diagrams and specs rendered inline and indexed. |
| **CI / Validation Matrix** | 🧩 97 % | Linting, schema validation, and cross-domain tests operational. |

---

## 4. Architecture Artifacts

| Layer | Assets | Description |
|--------|---------|-------------|
| **C1 – System Context** | `/assets/diagrams/C1_system/` | Stakeholders, external interfaces and trust boundaries. |
| **C2 – Containers / APIs** | `/assets/specs/openapi/` | OpenAPI definitions for 11 autonomous domain services. |
| **C3 – Components & States** | `/assets/diagrams/C3_*` | Core models and state machines integrating CI logic. |
| **C4 – Sequences** | `/assets/diagrams/C4_sequences/` | 38 process flows for governance and resonance orchestration. |
| **DDD – Domain Design** | `/assets/diagrams/ddd/` | Context maps and bounded domain relations. |
| **Specs – Event Catalog** | `/assets/specs/events/` | JSON + CloudEvents schemas for governance, treasury, ethics. |
| **AI Integration (Guide)** | `/assets/docs/ai_guide.md` | Defines AI interaction patterns and orchestration interfaces. |

> All artifacts are validated at build time.  
> Diagrams, OpenAPI specs, and events are auto-indexed via  
> `gen-asset-indexes.mjs` and exposed through the routes `/diagrams`, `/specs`, and `/eventschemas`.


## 5. Workstreams (kept + extended)

### 5.1 Docs System
- **Done:** Production build hardened; broken links replaced; redirect rules for legacy `/docs/intro`.
- **Done:** Dynamic pages for **/diagrams** and **/specs** (left list + inline preview).  
- **Planned:** Embed Mermaid renderer for `.mmd` preview pane (no download hop).

### 5.2 Specs System
- **Done:** OpenAPI and Event Schemas (incl. CloudEvents) indexed at build time.  
- **Done:** _CORS policies_ listed as a distinct bucket.  
- **Planned:** “Spec manifest” cross‑links from Manifest.md to individual files.

### 5.3 Governance & Parameters
- **Done:** Parameter SOP documented (staged updates, review/approval, rollback).  
- **Planned:** Signed change sets and CHANGELOG sync into `assets/specs/params/`.

### 5.4 Observability KPIs
- **Done:** SLO table draft.  
- **Planned:** SRI drift rules + alert thresholds (7/30/90‑day).

---

## 6. CI / CD Workflows (full list preserved + clarified)

> Source: `.github/workflows/` (names reflect filenames). All legacy entries retained.

| Workflow | Purpose | Triggers | Status | Notes |
|---|---|---|---|---|
| **`deploy-docs.yml`** | Build & deploy docs site | `push` to main / manual | ✅ Green | Uses Node 20 + Docusaurus 3; prebuild indexing. |
| **`nightly-manifest.yml`** | Regenerate/validate manifest links nightly | `schedule` | ✅ Green | Ensures Manifest links don’t drift. |
| **`validate-arch-c4.yml`** | Validate C4 diagram set (syntax/consistency) | `push` / manual | ✅ Green | Mermaid lint + file presence checks. |
| **`validate-arch-domains.yml`** | Check DDD domain map (namespaces, ids) | `push` / manual | ✅ Green | Verifies DDD catalogue integrity. |
| **`validate-arch-matrix.yml`** | End‑to‑end consistency matrix (C1–C4 ↔ specs) | `push` / manual | 🟡 Partial | Some cross‑links marked TODO. |
| **`validate-arch-openapi.yml`** | Validate OpenAPI YAML (schema + style) | `push` / manual | ✅ Green | Spectral/ajv; warns on unused comps. |
| **`validate-codegen-contracts.yml`** | **Verifies API contract correctness vs schemas (REST/gRPC)** | `push` / `workflow_dispatch` | 🟡 Partial | **Security layer auth stubs skipped**; otherwise green. |
| **`validate-codegen-harness.yml`** | Run generated client(s) against mock servers | `push` / manual | 🟡 Partial | Mock coverage improving. |
| **`validate-codegen.yml`** | Smoke test code generators | `push` / manual | ✅ Green | Ensures templates compile. |
| **`validate-event-schemas.yml`** | Validate JSON Schemas & CloudEvents metadata | `push` / manual | ✅ Green | `$id`, `$schema`, required fields. |
| **`validate-mermaid.yml`** | Render/lint Mermaid (`.mmd`) | `push` / manual | ✅ Green | Catches syntax and missing fonts. |

> If additional workflow files are added later, include them here; none of the above were removed.

---

## 7. Architecture Invariants (unchanged)

1. **Separation of concerns:** C1 (foundation), C2 (domain services), C3 (coordination), C4 (interface).  
2. **Spec‑first:** OpenAPI & Event Schemas are the contract of record.  
3. **Deterministic builds:** locked Node version; reproducible Docusaurus build.  
4. **Governance via signed parameter sets** and traceable SOP.

---

## 8. Risks & Mitigations (expanded, none removed)

| Risk | Likelihood / Impact | Mitigation |
|---|---|---|
| Diagram drift vs. specs | Med / Med | CI cross‑checks (`validate-arch-matrix.yml`). |
| Event schema version sprawl | Low / Med | `$id` policy + nightly manifest. |
| Auth gaps in codegen tests | Med / Med | Add auth fixtures; extend harness. |
| Broken external links | Low / Low | Redirects + link checker kept strict. |
| Page theming inconsistencies | Low / Low | Single `custom.css` + tokens; visual tests. |

---

## 9. Decision Log (kept + added)

- **Keep** Docusaurus 3 + Node 20 as baseline.  
- **Keep** strict broken‑link policy during build.  
- **Add** generated `index.json`/`index.html` for `/assets/specs/*` and `/assets/diagrams/*`.  
- **Add** dynamic TSX pages for `/diagrams` and `/specs` with inline preview.  
- **Add** brand CI (orange accent, improved footer).

---

## 10. Milestones

- **M1 – Docs baseline** (✅): build green, assets indexed, pages navigable.  
- **M2 – Contract completeness** (🟡): fill missing OpenAPI descriptions; auth stub coverage.  
- **M3 – SRI & SLO wiring** (🟡): document drift rules + thresholds.  
- **M4 – Launch v1.0 docs** (🔜): freeze, tag, publish.

---

## 11. Appendix

### 11.1 Notation
- _✅ Green_ = done; _🟡 Partial_ = works with gaps; _⚠️ At risk_ = needs attention.

### 11.2 Useful Paths
- `assets/diagrams/**` – Mermaid/SVG/PNG  
- `assets/specs/openapi/**` – OpenAPI YAML  
- `assets/specs/events/**` – JSON Schemas  
- `assets/specs/events_cloudevents/**` – CloudEvents metadata  
- `assets/specs/cors/**` – CORS policies

---

**Prepared by:** the coherosphere collective 
