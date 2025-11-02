---
id: ai_guide
slug: /ai_guide
title: AI Build Guide
---


# AI Build Guide

Objective: Document the Coherosphere AI build process — from prompt design to integration testing.
Note: Covers AI-assisted generation, model governance, and validation routines for architectural artifacts.
This guide ensures that AI participation in build workflows is transparent, reproducible, and auditable.e.

---

## 1. Build Philosophy

The Coherosphere build system aligns with three guiding principles:

| Principle | Description |
|------------|--------------|
| **Declarative Architecture** | Every service (C1–C4) defines its contract via OpenAPI + JSON Schemas. |
| **Continuous Validation** | Each commit triggers a full contract and codegen validation. |
| **Self-Documenting System** | Docs, diagrams, and manifests are generated automatically at build time. |

---

## 2. Build Flow Overview

    A[Commit / PR] --> B[CI Trigger]
    B --> C[Run Validation Workflows]
    C --> D[Generate SDKs + Mock Servers]
    D --> E[Static Docs Build (Docusaurus)]
    E --> F[Publish Docs + Specs to GitHub Pages]
    F --> G[Sync Registry + SBOM]


---

## 3. C-ID Mapping

Each **C-layer** (C1–C4) component is explicitly mapped to its specification and container:

| C-ID | Description | Source Path | Output |
|------|--------------|--------------|---------|
| **C1** | Foundation Layer | `/assets/specs/core/` | Base schemas |
| **C2** | Domain Layer | `/assets/specs/openapi/C2-*` | Domain APIs |
| **C3** | Coordination Layer | `/assets/specs/events/` | Event Schemas |
| **C4** | Interface Layer | `/assets/specs/interfaces/` | Gateway + SDKs |

Mappings are verified in the workflow `validate-codegen-harness.yml` using a shared manifest file.

---

## 4. Parameter Governance Integration

Each build performs consistency checks against the **parameter registry** defined in `/assets/specs/params/`:

- Validate JSON schema integrity (`λ, α, θ, quorum, threshold`).
- Ensure registry signature is valid (Ed25519, M-of-N governance keys).
- Check referenced Proposal-ID exists in Governance domain.

---

## 5. Dynamic Asset Generation

Build scripts generate static indexes to make architecture assets discoverable in Docs:

| Directory | Content | Generated Index |
|------------|----------|------------------|
| `/assets/diagrams/` | C4 + System diagrams | `/diagrams/index.html` |
| `/assets/specs/openapi/` | OpenAPI specifications | `/specs/index.html` |
| `/assets/specs/events/` | JSON + CloudEvent Schemas | `/eventschemas/index.html` |

Generation handled by [`scripts/gen-asset-indexes.mjs`](https://github.com/coherosphere/architecture/blob/main/docs.coherosphere.io/scripts/gen-asset-indexes.mjs).

---

## 6. CI Workflows Summary

| Workflow | Purpose | Output |
|-----------|----------|---------|
| **validate-openapi.yml** | Validate all OpenAPI specs with Redocly | `.harness_out_contracts/` |
| **validate-codegen.yml** | Generate SDKs, run Prism harness, validate schema | `.harness_out/sdk_*` |
| **validate-mermaid.yml** | Lint and render all Mermaid diagrams | `build/diagrams/` |
| **validate-params.yml** | Verify registry signatures + parameter schema | `/assets/specs/params/` |
| **build-docs.yml** | Build Docusaurus static site and deploy to GitHub Pages | `docs.coherosphere.io` |
| **nightly-manifest.yml** | Regenerate architecture manifest and validation reports | `/assets/docs/` |

---

## 7. Deployment Process

1. **Build artifacts** are created locally under `/build/`.
2. Docs site built via Docusaurus v3.9 and deployed to `docs.coherosphere.io`.
3. Generated assets synced under `/static/assets` in CI.
4. Pages deployed using GitHub Actions → `actions/deploy-pages@v4`.

---

## 8. SBOM and Integrity Verification

- **SBOM (Software Bill of Materials)** auto-generated at build time using `cyclonedx-npm`.
- **Integrity hashes (SHA256)** verified for all critical assets under `/assets/specs/`.
- Results stored in `.sbom/` for transparency and reproducibility.

---

## 9. Version History

| Version | Date | Highlights |
|----------|------|-------------|
| **v4.0** | 2025-08 | Initial AI build pipeline integration |
| **v4.1** | 2025-09 | Added SBOM and schema validation |
| **v4.2** | 2025-10 | Codegen + test harness integration |
| **v4.3** | 2025-11 | Added C-ID mapping, governance validation, and dynamic asset indexing |

---

**Prepared by:** the coherosphere collective 
