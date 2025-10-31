# coherosphere — Architecture Repository

This repository is the **single source of truth** for the *coherosphere* system architecture —  
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
| **OpenAPI Specs** | [assets/specs/openapi/](assets/specs/openapi) | Public & inter-service APIs | C2-01…C2-11 REST/gRPC/GraphQL definitions |
| **Docs** | [assets/docs/](assets/docs) | Explanations & design notes | API Surface, Domain Model, Governance Rules |

All diagrams are authored in **Mermaid**, render directly on GitHub,  
and map 1:1 to code-level artifacts.

---

## Core Model

- **C1** – Context: actors, systems, and trust boundaries  
- **C2** – Containers: services (Resonance, PoC, Governance, Treasury, Identity…)  
- **C3** – Components: internal logic and state machines (ERDs, behaviors)  
- **C4** – Code-level sequences and interactions  
- **SM-xx.xx** – State Machines per container  
- **OpenAPI** – Live interface specs (versioned under `assets/specs/openapi`)  
- **DDD / ERD** – Domain-centric aggregate design  

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
