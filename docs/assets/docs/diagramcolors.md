# 🎨 Coherosphere Diagram Color System (Mermaid CI)

This document defines the **visual language** used across all Coherosphere architecture diagrams  
(C1–C4 levels) rendered in Mermaid.  
Colors are **semantic**, not decorative — each hue communicates a specific type of responsibility, behavior, or systemic role.

---

## 🧩 Color Semantics Overview

| Category | Mermaid Class | Color | Meaning | Typical Components |
|-----------|----------------|--------|----------|--------------------|
| 🟧 **Core Logic / Compute** | `:::compute` | `#ff8b00` | Central algorithmic or resonance logic. Responsible for calculating systemic impact, coherence, or alignment. | Resonance Engine, KPI Aggregator, SRI Engine, CP Calculator |
| 🟨 **Control / API / Validation** | `:::control` | `#fde68a` | Manages flow, orchestrates logic, or validates inputs. Often the gateway layer of a service. | API Controller, Schema Guard, Parameter Versioning |
| 🟦 **Storage / Persistence** | `:::store` | `#0ea5e9` | Stores state, metrics, or historical data for traceability. | Ledger, Database, Snapshot Store, Graph Store |
| 🟪 **User Interface / Presentation** | `:::ui` | `#8b5cf6` | Human-facing surfaces for interaction or transparency. | Resonance Board UI, Developer Portal |
| 🟩 **Event / Publishing** | `:::event` | `#22c55e` | Emits events, metrics, or signals to the ecosystem. | Event Publisher, Feed Service, Federation Client |
| 🟥 **Security / Risk / Guard** | `:::risk` | `#ef4444` | Protects integrity, prevents abuse, or ensures compliance. | Security Layer, Sybil Guard, Compliance Checks |
| 🟫 **Worker / Batch / Job** | `:::worker` | `#fb923c` | Performs background or scheduled processing (decay, sync, recompute). | Recompute Worker, Snapshotter, Sync Agent |
| ⚪ **External System / Integration** | `:::ext` | `#e5e7eb` | External entities interacting with the system. | Bitcoin Layer, External DAO, AI Agent, Oracles |
| ⚫ **Container Boundary** | `:::container` | `#111827` | Visual boundary grouping all components of a service. | C2 or C3 subgraph header |

---

## 🧠 Reading a Diagram

Color in Coherosphere diagrams isn’t arbitrary — it’s **functional**.  
It lets you instantly recognize *what kind of thing* a node represents:

- 🟨 **Controls** guard or route flows.  
- 🟧 **Computes** generate resonance, value, or insight.  
- 🟦 **Stores** persist systemic memory.  
- 🟩 **Events** propagate influence outward.  
- 🟥 **Risk nodes** protect coherence.  
- 🟫 **Workers** maintain temporal processes.  
- 🟪 **UI** visualizes coherence to humans.  
- ⚪ **External** nodes connect to the wider world.

> **Mnemonic:**  
> **Yellow steers, Orange computes, Blue stores, Green emits, Red guards, Brown works, Purple shows, Gray connects.**

---

## 🌈 Mermaid Theme Snippet

You can reuse this theme block across all Coherosphere Mermaid diagrams:

```mermaid
%% --- Coherosphere CI Theme ---
classDef container fill:#111827,stroke:#111827,color:#ffffff,font-weight:bold;
classDef compute fill:#ff8b00,stroke:#333333,color:#ffffff;
classDef control fill:#fde68a,stroke:#b45309,color:#1f2937;
classDef store fill:#0ea5e9,stroke:#075985,color:#ffffff;
classDef event fill:#22c55e,stroke:#065f46,color:#083344;
classDef worker fill:#fb923c,stroke:#7c2d12,color:#1f2937;
classDef ui fill:#8b5cf6,stroke:#4c1d95,color:#ffffff;
classDef risk fill:#ef4444,stroke:#7f1d1d,color:#ffffff;
classDef ext fill:#e5e7eb,stroke:#9ca3af,color:#111827;
linkStyle default stroke:#334155,stroke-width:2px;