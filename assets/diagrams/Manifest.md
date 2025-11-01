# Coherosphere — Diagrams Manifest (v4)

This file serves as the **index of all architecture diagrams** in the Coherosphere repository.  
It follows the **C4 model** (Context → Containers → Components → Code) and extends it with  
**DDD Strategic Views** and **State Machines**.

All diagrams are written in **Mermaid (`.mmd`)**, rendered as **SVG** for GitHub display, and exported as **PNG** for offline use.

_Last updated: 2025-11-01_

---

## Level C1 — System Context

**Path:** `/assets/diagrams/C1_system/`

| Diagram | Files | Description |
|----------|--------|-------------|
| `C1_system_context_diagram` | `.mmd`, `.svg`, `.png` | Global system view including external actors and integrated systems. |
| `C1_stakeholders` | `.mmd`, `.svg`, `.png` | Stakeholder classes — Members, Developers, Institutions, AI Systems, DAOs, Society. |
| `C1_trust_boundaries` | `.mmd`, `.svg`, `.png` | Security and trust zones (Public • DAO • Federation • Core). |

---

## Level C2 — Containers

**Path:** `/assets/diagrams/C2_containers/`

| Diagram | Files | Description |
|----------|--------|-------------|
| `C2_container_diagram` | `.mmd`, `.svg`, `.png` | Overview of all 12 core containers (C2-01 … C2-12) and their relations. |
| `C2_dataflow` | `.mmd`, `.svg`, `.png` | Logical and event-driven data flow between containers. |
| `C2_deployment` | `.mmd`, `.svg`, `.png` | Deployment topology across zones, hubs, and API layers. |
| `C2_api_surface` | `.mmd`, `.svg`, `.png` | API surface documentation across REST/gRPC/GraphQL layers. |

---

## Level C3 — Components & States

**Paths:**  
- Components: `/assets/diagrams/C3_containers/`  
- State Machines: `/assets/diagrams/C3_states/`

### C3 Components (per Container)

| C2-ID | Filename | Description |
|--------|-----------|-------------|
| C2-01 | `C2-01_resonance_service.mmd` | Core resonance computation engine and anomaly detection. |
| C2-02 | `C2-02_proof_of_contribution.mmd` | Contribution intake, weighting, and ledgering. |
| C2-03 | `C2-03_governance_dao_service.mmd` | Proposal lifecycle, voting, and policy execution. |
| C2-04 | `C2-04_treasury_funding_service.mmd` | Funding allocation, QF rounds, and treasury management. |
| C2-05 | `C2-05_identity_reputation_service.mmd` | PoCI, DIDs, credential issuance, and Sybil resistance. |
| C2-06 | `C2-06_local_hub_federation.mmd` | Hub federation, CRDT sync, and project lifecycle. |
| C2-07 | `C2-07_metrics_analytics.mmd` | KPI aggregation, SRI computation, and dashboard metrics. |
| C2-08 | `C2-08_manifesto_ethics_guard.mmd` | Ethics filtering, manifesto alignment, and attestations. |
| C2-09 | `C2-09_knowledge_graph_collective_intelligence.mmd` | Knowledge ingestion, semantic graph, RAG orchestration. |
| C2-10 | `C2-10_security_audit_layer.mmd` | Ledger integrity, anomaly detection, and forensics. |
| C2-11 | `C2-11_public_api_gateway.mmd` | Unified API ingress, routing, and federation. |
| C2-12 | `C2-12_resonance_board_ui.mmd` | User-facing dashboard and visualization layer. |

---

### C3 State Machines

| SM-ID | Filename | Entity | Description |
|--------|-----------|---------|-------------|
| SM-01.01 | `SM-01.01_resonance_calculation_state.mmd` | `RESONANCE_SAMPLE` | Tracks resonance calculation, anomaly detection, and metric output. |
| SM-02.01 | `SM-02.01_contribution_lifecycle.mmd` | `CONTRIBUTION` | From submission → validation → resonance update. |
| SM-02.02 | `SM-02.02_decay_recompute_cycle.mmd` | `LEDGER_ENTRY` | Models CP decay and recomputation of weights. |
| SM-03.01 | `SM-03.01_proposal_lifecycle.mmd` | `PROPOSAL` | Creation, voting, execution, and archival. |
| SM-03.02 | `SM-03.02_appeal_dispute_flow.mmd` | `APPEAL` | Manages disputes and appeal resolution. |
| SM-04.01 | `SM-04.01_quadratic_funding_round.mmd` | `QF_ROUND` | Round setup → matching → payout. |
| SM-04.02 | `SM-04.02_streaming_payout_lifecycle.mmd` | `PAYOUT_STREAM` | Payment streams with pause/resume logic. |
| SM-05.01 | `SM-05.01_identity_verification_attestation.mmd` | `DID / ATTESTATION` | Credential lifecycle (issue, verify, revoke). |
| SM-05.02 | `SM-05.02_reputation_update_cycle.mmd` | `REPUTATION_SCORE` | Aggregates and decays reputation scores. |
| SM-06.01 | `SM-06.01_hub_sync_state.mmd` | `HUB_SYNC_FRAME` | CRDT sync and conflict resolution. |
| SM-06.02 | `SM-06.02_project_lifecycle.mmd` | `PROJECT` | Project creation → milestones → completion. |
| SM-07.01 | `SM-07.01_snapshot_kpi_aggregation.mmd` | `KPI_SNAPSHOT` | KPI computation and SRI update. |
| SM-08.01 | `SM-08.01_ethics_evaluation_flow.mmd` | `ETHICS_EVAL` | Evaluation of contributions vs. rubrics. |
| SM-09.01 | `SM-09.01_knowledge_ingestion_pipeline.mmd` | `KG_ENTITY` | Knowledge ingestion, embedding, and integration. |
| SM-10.01 | `SM-10.01_incident_lifecycle.mmd` | `INCIDENT` | Incident detection, containment, resolution. |
| SM-10.02 | `SM-10.02_transparency_report_lifecycle.mmd` | `TRANSPARENCY_REPORT` | Report drafting, signing, and publication. |

---

## Level C4 — Sequences

**Path:** `/assets/diagrams/C4_sequences/`

Includes all **end-to-end workflows (C4-01 … C4-36)** covering governance, ethics, metrics, treasury, and knowledge processes.  
Each `.mmd` file represents one sequence and follows the standard naming:

`C4-XX_<sequence_name>.mmd`

Example:  
`C4-02_governance_lifecycle.mmd` → Full proposal → vote → audit sequence.  
`C4-20_ai_assisted_interpretation_loop.mmd` → Knowledge graph + metrics visualization.

---

## DDD — Strategic Diagrams

**Path:** `/assets/diagrams/ddd/`

| Diagram | Files | Description |
|----------|--------|-------------|
| `DDD_domain_context_map` | `.mmd`, `.svg`, `.png` | Full bounded-context network and domain events. |
| `DDD_subdomain_map` | `.mmd`, `.svg`, `.png` | Core / Supporting / Generic domain separation. |
| `DDD_team_context_alignment` | `.mmd`, `.svg`, `.png` | Conway’s Law / Team Topologies mapping. |
| `DDD_contract_types_overview` | `.mmd`, `.svg`, `.png` | Shared Kernel, ACL, Published Language links across domains. |

---

## Versioning

Each diagram is semantically tied to a Cx-ID (C1–C4 or SM-ID).  
Files should retain their ID prefix for clarity and traceability in CI/CD pipelines.

---

**Technology that serves life. Governance that learns. Money that remembers truth.**  
_— The Coherosphere Collective, 2025_
