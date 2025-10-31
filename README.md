# coherosphere — Architecture Repository

This repository is the **single source of truth** for the *Coherosphere* system architecture —  
a model-driven, open specification using the **C4 model** (Context → Containers → Components → Code)  
and extended with **Domain-Driven Design (DDD)**, **State Machines (SM)**, and **OpenAPI specs**.

---

## Structure

| Level | Folder | Focus | Content |
|--------|---------|--------|----------|
| **C1 – System Context** | [assets/diagrams/C1_system/](assets/diagrams/C1_system) | External actors, trust zones, boundaries | System, Stakeholders, Trust Boundaries |
| **C2 – Containers** | [assets/diagrams/C2_containers/](assets/diagrams/C2_containers) | Core services, data flow, deployment | 12 core containers (C2-01…C2-12) |
| **C3 – Components & States** | [assets/diagrams/C3_states/](assets/diagrams/C3_states) | Internal logic, state machines, data models | 16 state machines (SM-01.01…SM-10.02) |
| **C4 – Sequences** | [assets/diagrams/C4_sequences/](assets/diagrams/C4_sequences) | Behavioral flows across containers | 30+ end-to-end flows (C4-01…C4-34) |
| **DDD – Domain-Driven Design** | [assets/diagrams/DDD/](assets/diagrams/DDD) | Strategic & Tactical domain design | Subdomains, Team Alignments, Contracts, Aggregates |
| **OpenAPI Specs** | [assets/specs/openapi/](assets/specs/openapi) | Public & inter-service APIs | C2-01…C2-11 REST/gRPC/GraphQL definitions |
| **Docs** | [assets/docs/](assets/docs) | Explanations & design notes | API Surface, Domain Model, Governance Rules |

All diagrams are authored in **Mermaid**, render directly on GitHub,  
and map 1:1 to code-level artifacts.

---

## Core Model

- **C1** — Context: actors, systems, and trust boundaries  
- **C2** — Containers: services (Resonance, PoC, Governance, Treasury, Identity…)  
- **C3** — Components: internal logic and state machines (ERDs, behaviors)  
- **C4** — Code-level sequences and interactions  
- **SM-xx.xx** — State Machines per container  
- **DDD** — Domain-Driven Design, strategic & tactical domain models  
- **OpenAPI** — Live interface specs (`assets/specs/openapi`)  
- **ERD** — Domain-centric aggregate design  

---

## Domain-Driven Design (DDD)

The DDD layer complements the C4 model by connecting **strategic intent**  
(core vs. supporting domains) with **tactical implementation** (aggregates, entities, policies).

### Strategic Design

| Diagram | Description | Path |
|----------|--------------|------|
| 🧩 **Subdomain Map** | Core / Supporting / Generic subdomains | [`assets/diagrams/DDD/Strategic/Subdomains.mmd`](assets/diagrams/DDD/Strategic/Subdomains.mmd) |
| 🧩 **Team ↔ Context Alignment** | Conway’s Law & Team Topologies mapping | [`assets/diagrams/DDD/Strategic/Teams-Contexts.mmd`](assets/diagrams/DDD/Strategic/Teams-Contexts.mmd) |
| 🧩 **Contract Types Overview** | Relationships between bounded contexts (Shared Kernel, ACL, etc.) | [`assets/diagrams/DDD/Strategic/Contracts.mmd`](assets/diagrams/DDD/Strategic/Contracts.mmd) |

### Tactical Design

| Diagram | Description | Example Path |
|----------|--------------|---------------|
| 🧱 **Aggregates** | Aggregate roots, invariants, and entities per BC | `assets/diagrams/DDD/Tactical/Governance/Aggregates.mmd` |
| 🧱 **Entities & Value Objects** | Detailed entity relationships and value objects | `assets/diagrams/DDD/Tactical/PoC/Entities-VOs.mmd` |
| 📜 **Policies & Rules** | Domain policies, thresholds, and constraints | `assets/docs/DDD/Tactical/Governance/Policies.md` |
| 🔁 **Event Storming** | Commands, events, and policies across the domain | `assets/diagrams/DDD/Behavior/Governance/EventStorming.mmd` |
| 🔄 **Sagas / Process Managers** | Long-running processes (e.g. Funding Round, Appeal Flow) | `assets/diagrams/DDD/Behavior/Treasury/Saga-FundingRound.mmd` |

Together, these diagrams and docs describe **how Coherosphere’s subdomains collaborate**  
through clear contracts, shared language, and governed evolution.

---

## Design Principles

> **Technology that serves life. Governance that learns.  
> Money that remembers truth.**

The Coherosphere architecture follows these principles:

- **Clarity over complexity** — one abstraction per level  
- **Resonant modularity** — autonomy at the edge, coherence in the whole  
- **Transparency** — inspectable APIs, rules, and decisions  
- **Evolvability** — parameters and states evolve through governance  
- **Open specification** — licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

---

## Developer Guide

### 🔍 View Diagrams
GitHub renders `.mmd` diagrams automatically.  
For local preview:
```bash
brew install mermaid-cli
mmdc -i assets/diagrams/C3_states/C3-StateMachineOverview.mmd -o state-overview.svg

## Connect

- Website: [coherosphere.com](https://coherosphere.com)  
- GitHub: [github.com/coherosphere](https://github.com/coherosphere)  
- Nostr: [npub…](https://nostr.band/npub1kc9weag9hjf0p0xz5naamts48rdkzymucvrd9ws8ns7n4x3qq5gsljlnck)

---

**Technology that serves life. Governance that learns. Money that remembers truth.**  
*— The coherosphere collective, 2025*
