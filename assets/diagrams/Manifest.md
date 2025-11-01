# Coherosphere — Diagrams Manifest

This document provides a full index of all architectural diagrams across the **C4 model**  
(Context → Containers → Components → Code) and **DDD strategic design** for the Coherosphere architecture.

Each diagram is stored in Mermaid (`.mmd`) format, with `.svg` for rendering on GitHub and `.png` for previews.

---

## Level C1 — System Context

**Path:** `/assets/diagrams/C1_system/`

| Diagram | Files | Description |
|----------|--------|--------------|
| **C1_System_Context_Diagram** | `.mmd`, `.svg`, `.png` | Shows all external actors, systems, and trust boundaries at the system level. |
| **C1_Stakeholders** | `.mmd`, `.svg`, `.png` | Identifies human, institutional, and AI stakeholders interacting with the system. |
| **C1_Trust_Boundaries** | `.mmd`, `.svg`, `.png` | Defines public, DAO, federated, and secure zones within the Coherosphere. |

---

## Level C2 — Containers

**Path:** `/assets/diagrams/C2_containers/`

| Diagram | Files | Description |
|----------|--------|--------------|
| **C2_Container_Diagram** | `.mmd`, `.svg`, `.png` | Overview of the 12 core services (C2-01 … C2-12) and their interactions. |
| **C2_Dataflow** | `.mmd`, `.svg`, `.png` | Illustrates major data exchanges between containers. |
| **C2_Deployment** | `.mmd`, `.svg`, `.png` | Logical deployment view: API, Federation, Knowledge, Metrics, Security. |
| **C2_API_Surface** | `.mmd`, `.svg`, `.png` | Unified API surface showing REST/gRPC/GraphQL entry points and cross-service exposure. |

---

## Level C3 — Components / Models / States

### Components
**Path:** `/assets/diagrams/C3_containers/`  
Contains per-container component breakdowns (C2-01 … C2-12).

| Diagram | Description |
|----------|--------------|
| `C3_01_Resonance_Service.mmd` … `C3_12_UI.mmd` | Each file describes internal components (API Controller, Engine, Guards, Workers, etc.) for its container. |

### Domain Models
**Path:** `/assets/diagrams/C3_models/`

| Diagram | Files | Description |
|----------|--------|--------------|
| **C3_Domain_ERD** | `.mmd`, `.svg`, `.png` | Entity–Relationship Diagram (ERD) showing all domain entities, IDs, and DDD relationships. |

### State Machines
**Path:** `/assets/diagrams/C3_states/`

| State Machine | Entity | Container | Description |
|----------------|----------|-------------|--------------|
| `SM-01.01_Resonance_Calculation_State` | RESONANCE_SAMPLE | C2-01 | Resonance computation and anomaly detection. |
| `SM-02.01_Contribution_Lifecycle` | CONTRIBUTION | C2-02 | From submission to validation and resonance update. |
| `SM-02.02_Decay_Recompute_Cycle` | LEDGER_ENTRY | C2-02 | Recomputes decayed CP/W values over time. |
| `SM-03.01_Proposal_Lifecycle` | PROPOSAL | C2-03 | Proposal creation, voting, execution, archive. |
| `SM-03.02_Appeal_Dispute_Flow` | APPEAL | C2-03 | Handles appeals and disputes. |
| `SM-04.01_Quadratic_Funding_Round` | QF_ROUND | C2-04 | Funding round setup → matching → payout. |
| `SM-04.02_Streaming_Payout_Lifecycle` | PAYOUT_STREAM | C2-04 | Stream open/pause/resume/close lifecycle. |
| `SM-05.01_Identity_Verification_Attestation` | DID / ATTESTATION | C2-05 | Identity creation, verification, credential issuance. |
| `SM-05.02_Reputation_Update_Cycle` | REPUTATION_SCORE | C2-05 | Reputation decay and aggregation over time. |
| `SM-06.01_Hub_Sync_State` | HUB_SYNC_FRAME | C2-06 | CRDT synchronization across hubs. |
| `SM-06.02_Project_Lifecycle` | PROJECT | C2-06 | Local project setup, milestones, funding. |
| `SM-07.01_Snapshot_KPI_Aggregation` | KPI_SNAPSHOT | C2-07 | KPI aggregation and SRI updates. |
| `SM-08.01_Ethics_Evaluation_Flow` | ETHICS_EVAL | C2-08 | Evaluates contributions against rubrics and issues attestations. |
| `SM-09.01_Knowledge_Ingestion_Pipeline` | KG_ENTITY | C2-09 | Discovery → Embedding → Integration → Synthesis. |
| `SM-10.01_Incident_Lifecycle` | INCIDENT | C2-10 | Incident detection → containment → disclosure. |
| `SM-10.02_Transparency_Report_Lifecycle` | TRANSPARENCY_REPORT | C2-10 | Audit report generation and publication. |

---

## Level C4 — Sequences

**Path:** `/assets/diagrams/C4_sequences/`

| Sequence | Domain | Description |
|-----------|----------|--------------|
| `C4-01_Contribution_to_Metrics` → `C4-36_Hub_Resource_Request` | Cross-service end-to-end flows mapping DDD events to runtime interactions. Each file corresponds to one `C4-xx` row in the master sequence table. |

All `.mmd` files follow the same visual standard:  
🟪 UI   🟨 API   🟧 Core   🟥 Risk   🟩 External.

---

## DDD — Strategic Design

**Path:** `/assets/diagrams/ddd/`

| Diagram | Files | Description |
|----------|--------|--------------|
| **DDD_Domain_Context_Map** | `.mmd`, `.svg`, `.png` | Context map linking bounded contexts and events. |
| **DDD_Subdomain_Map** | `.mmd`, `.svg`, `.png` | Core / Supporting / Generic subdomain classification. |
| **DDD_Team_Context_Alignment** | `.mmd`, `.svg`, `.png` | Conway/Team-Topologies alignment between teams and contexts. |
| **DDD_Contract_Types_Overview** | `.mmd`, `.svg`, `.png` | Shows Shared Kernels, ACLs, Published Languages, and Open Host Services. |

---

## Maintenance Guidelines

1. **Always version `.mmd` first**, then export `.svg` and `.png`.  
2. Use consistent **Mermaid themes** (`theme: base`, `sequenceNumberColor: #334155`).  
3. Each new diagram must be referenced in this `Manifest.md`.  
4. Keep all filenames **without spaces** and **stable across commits**.  
5. Use relative links in docs, e.g.:  
   ```markdown
   ![C2 Container Diagram](../C2_containers/C2_Container_Diagram.svg)

---

Author: Coherosphere Architecture Guild
Updated: 2025-10-31
License: CC BY 4.0
