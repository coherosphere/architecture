---
id: architecture_todo
slug: /architecture_todo
title: Architecture — To-Do List
sidebar_label: Todo
---

# To-Do List

_Last updated: 2025-11-02_

This document tracks the active and completed tasks toward **v1.0 release readiness**
of the Coherosphere architecture. It reflects the verified state of `/architecture`
as of November 2025 — CI stable and AI-build ready.

---

## 1. C4 Sequences (Behavioral Flows)

| Status | Task | Notes |
|:--:|------|-------|
| ✅ | Finalize `C4-34` | Compliance workflow validated and merged. |
| ✅ | Fix `C4-35` syntax | Funding stream lifecycle refactored and CI-stable. |
| ✅ | Confirm all 36 sequences | All syntactically valid and DDD-aligned. |
| ✅ | Add reverse/error paths | `C4-02`, `C4-03`, `C4-07`, `C4-10` now include explicit `alt failure` logic. |

---

## 2. Event Specifications (Specs / JSON Schemas)

| Status | Task | Notes |
|:--:|------|-------|
| ✅ | Create JSON Schemas for all DDD events (`DDD-EVT-01…86`) | Located under `/assets/specs/events/`. |
| ✅ | Validate schema alignment with sequence events | Each `C4-xx` flow references a corresponding event schema ID. |
| ✅ | Auto-generate CloudEvents definitions | Includes “source”, “subject”, and “type” attributes. |
| ✅ | Export as ZIP for developers (`events-schemas.zip`) | Linked in `/assets/specs/README.md`. |

---

## 3. Docs & Publishing

| Status | Task | Notes |
|:--:|------|-------|
| ✅ | Deploy **Docusaurus** to `docs.coherosphere.io` | Live on GitHub Pages with custom CNAME + workflow split (build/deploy). |
| ✅ | Mermaid rendering | `@docusaurus/theme-mermaid` enabled; `.mmd` sources linked from assets. |
| ✅ | Dynamic indexes for Specs (OpenAPI + Events) | Build script writes `/assets/specs/**/index.html` and docs list at `/specs`. |
| ✅ | Diagram browser | `/diagrams` lists all items under `/assets/diagrams/**`. |
| 🟡 | OpenAPI viewer | Add SwaggerUI/Redoc page to render YAML specs inline. |
| 🟡 | Sitemap + robots | Add `@docusaurus/plugin-sitemap` and `/static/robots.txt` (see action items below). |
| 🟡 | Status report MD | Add `/assets/docs/ARCHITECTURE_STATUS_REPORT_v4.md` (current: PDF/notes only). |

**Action items** (Docs):  
- Add plugin in `package.json`: `@docusaurus/plugin-sitemap` and configure `sitemap` in `docusaurus.config.ts`.  
- Create `/static/robots.txt` with `Sitemap: https://docs.coherosphere.io/sitemap.xml`.  
- Add `/src/pages/openapi.tsx` to embed SwaggerUI for any selected spec.  

---

## 4. CI/CD & Validation

| Status | Task | Notes |
|:--:|------|-------|
| ✅ | Implement master validator (`validate.yml`) | Checks ID consistency (C2 ↔ DDD ↔ C4 ↔ SM). |
| ✅ | Add JSON Schema linting | Event definitions auto-validated. |
| ✅ | Include Mermaid syntax validator | Prevents diagram parse errors pre-commit. |
| ✅ | OpenAPI syntax + domain validation | Enforces HTTPS and `x-c2-id`. |
| ✅ | Codegen Harness + Contracts tests | Full C2 OpenAPI E2E validation via Prism + Schemathesis. |
| ✅ | Nightly build to regenerate Manifest tables | “Nightly – Rebuild Manifests” workflow runs. |

---

## 5. AI Build Readiness

| Status | Task | Notes |
|:--:|------|-------|
| ✅ | `AI_BUILD_GUIDE_v4.md` synced with manifest | Fully consistent with C-IDs and container mappings. |
| 🟡 | Automate AI build mapping | Map each C-ID (C1–C4) to build-time container sources. |
| ✅ | Codegen Test Harness | Executed in CI (contracts + validation). |
| 🟡 | Prompt templates for scaffolding | Define per-C-ID blueprint + guard-rails. |

---

## 6. Architecture Assets

| Status | Task | Notes |
|:--:|------|-------|
| ✅ | All diagrams renamed (no timestamps) | CI-safe and stable. |
| ✅ | Manifest and structure stable | C1–C4 + DDD fully integrated. |
| ✅ | `/assets/diagrams/overview/C4_Layers_Summary.mmd` | Horizontal architecture overview completed. |
| ✅ | `/assets/diagrams/overview/Architecture_Stack.mmd` | Vertical C1→C4→DDD→Specs stack view completed. |

---

## 7. Infrastructure Alignment

| Status | Task | Notes |
|:--:|------|-------|
| ✅ | Domains allocated | `coherosphere.com`, `app.`, `api.`, `docs.`, `chat.`, `ai.`, `data.` registered. |
| ✅ | Update CORS policy | Regenerated `CORS_Manifest.json` including new subdomains. |
| ✅ | DNS configuration manifest | `/assets/specs/DNS_Config.json` present. |
| ✅ | API endpoints under `api.coherosphere.io` | Verified via OpenAPI validation workflows. |

---

## 8. Runtime Navigation (New)

| Status | Task | Notes |
|:--:|------|-------|
| ✅ | Root landing page | Custom `/src/pages/index.tsx` with quick links. |
| ✅ | Navbar tidy-up | Direct links: Todo, AI Build, Manifest, Diagrams, Specs. |
| ✅ | Redirects | `@docusaurus/plugin-client-redirects` routes legacy `/docs/intro` → `/Manifest`. |
| 🟡 | Breadcrumb polish | Add per-section intro pages for better context. |

---

## Priority Summary

| Category | Priority | Progress |
|-----------|-----------|-----------|
| 🟢 Documentation & Manifest | Complete | 100% |
| 🟢 C4 Sequence Finalization | Complete | 100% |
| 🟢 JSON Event Schemas | Complete | 100% |
| 🟡 Docs Deployment Enhancements | Medium | 85% |
| 🟢 CI/CD Validation | Complete | 100% |
| 🟡 AI Build Readiness | Medium | 93% |
| 🟢 Architecture Assets | Complete | 100% |
| 🟢 Infrastructure Alignment | Complete | 100% |

---

## Verdict

> The Coherosphere architecture is **architecturally production-ready and AI-buildable**.  
> Remaining gaps are integration/UI: inline OpenAPI rendering, sitemap/robots, and
> automation that maps C-IDs to generated components. Everything else is green.

---

**Prepared by:** The Coherosphere Collective  
**License:** CC BY 4.0  
**Date:** November 2025
