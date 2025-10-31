# Coherosphere — Architecture Repository

This repository is the **single source of truth** for the *Coherosphere* system architecture —  
a fully model-driven, open specification built around the **C4 model**  
and extended with **Domain-Driven Design (DDD)**, **State Machines**, and **OpenAPI specs**.

---

## Structure

| Level | Folder | Focus | Content |
|--------|---------|--------|----------|
| **C1 – System Context** | [`docs//assets/diagrams/C1_system/`](assets/diagrams/C1_system) | External actors, trust zones, boundaries | System, Stakeholders, Trust Boundaries |
| **C2 – Containers** | [`docs//assets/diagrams/C2_containers/`](assets/diagrams/C2_containers) | Core services, data flow, deployment | 12 core containers (C2-01…C2-12) |
| **C3 – Components & States** | [`docs//assets/diagrams/C3_states/`](assets/diagrams/C3_states) | Internal logic, state machines, data models | 16 state machines (SM-01.01…SM-10.02) |
| **C4 – Sequences** | [`docs//assets/diagrams/C4_sequences/`](assets/diagrams/C4_sequences) | Behavioral flows across containers | 30+ end-to-end flows (C4-01…C4-34) |
| **OpenAPI Specs** | [`docs//assets/specs/openapi/`](assets/specs/openapi) | Public & inter-service APIs | C2-01…C2-11 REST/gRPC/GraphQL definitions |
| **Docs** | [`docs//assets/docs/`](assets/docs) | Explanations & design notes | API Surface, Domain Model, Governance Rules |

All diagrams are written in **Mermaid**, render directly on GitHub,  
and map 1:1 to code-level artifacts.

---

## Core Model

- **C1** – Context: actors, systems, and trust boundaries  
- **C2** – Containers: services (Resonance, PoC, Governance, Treasury, Identity…)  
- **C3** – Components: internal logic and data models (ERDs, State Machines)  
- **C4** – Code-Level Behavior: sequences, flows, and API interactions  
- **SM-xx.xx** – Behavioral State Machines per container  
- **OpenAPI** – Live interface definitions (versioned)  
- **ERD / DDD** – Domain-centric data and aggregate design  

---

## Design Principles

> **Technology that serves life. Governance that learns.  
> Money that remembers truth.**

The Coherosphere architecture follows these guiding principles:

- **Clarity over complexity** – each level reveals exactly one layer of abstraction  
- **Resonant modularity** – autonomy at the edge, coherence in the whole  
- **Transparency** – every API, rule, and decision is inspectable  
- **Evolvability** – state machines and parameters evolve via governance proposals  
- **Open Specification** – licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

---

## Developer Setup

### View diagrams
GitHub renders all `.mmd` diagrams automatically.  
For local previews:
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
