# Architecture Consistency Audit

## Summary

| Metric | Count |
|----------|----------|
| manifest files | 79 |
| c1 items | 8 |
| c2 items | 12 |
| c3 items | 69 |
| c3 state items | 16 |
| c4 items | 35 |
| Missing in manifest | 77 |
| Names used across multiple layers | 0 |

## Findings

### A. Items missing in Manifest.md

| Layer | Name |
|----------|----------|
| C1 | AI Systems & Agents |
| C1 | Bitcoin / Hard Asset Layer |
| C1 | Coherosphere System (Sphere of Coherence) |
| C1 | Developers & Architects |
| C1 | External DAOs & Web3 Systems |
| C1 | Local Communities & Institutions |
| C1 | Member / Contributor |
| C1 | Public / Society |
| C2 | Identity & Reputation Service (PoCI) |
| C2 | Knowledge Graph / Collective Intelligence Service |
| C2 | Proof-of-Contribution (PoC) Service |
| C2 | Resonance Metric Stack / Analytics |
| C3 | API Controller |
| C3 | API Controller |
| C3 | Accessibility & i18n |
| C3 | Alignment Evaluator |
| C3 | Anomaly Detection |
| C3 | Anomaly Detector |
| C3 | Appeals Handler |
| C3 | Attestation Issuer |
| C3 | Audit Trail Writer |
| C3 | Auth Hub |
| C3 | CP Calculator |
| C3 | CRDT Resolver |
| C3 | Command Handler |
| C3 | Compliance & Risk Checks |
| C3 | Contribution Validator |
| C3 | Credential Issuer (VC/SBT) |
| C3 | DID Manager |
| C3 | Dashboard Feed |
| C3 | Dashboard Renderer |
| C3 | Embedding Generator |
| C3 | Ethics Policy Engine |
| C3 | Ethics Preflight Client |
| C3 | Event Publisher |
| C3 | Event Publisher |
| C3 | Execution Manager |
| C3 | Feature Store |
| C3 | Federation Client |
| C3 | Graph Ingest Pipeline |
| C3 | Health Monitor |
| C3 | Identity/Wallet Adapter |
| C3 | Incident Response |
| C3 | KPI Aggregator |
| C3 | Ledger Monitor |
| C3 | On-Chain Adapter |
| C3 | Ontology Manager |
| C3 | Payout Orchestrator |
| C3 | PoC Ledger |
| C3 | Project Registry |
| C3 | Proposal Engine |
| C3 | QF Engine |
| C3 | Quorum & Threshold Logic |
| C3 | RAG Orchestrator |
| C3 | Rate & Quota Manager |
| C3 | Recompute Worker |
| C3 | Reputation Graph |
| C3 | Reserve Manager |
| C3 | Resonance Engine |
| C3 | Rubric Manager |
| C3 | SIEM Collector |
| C3 | SRI Engine |
| C3 | Schema & Policy Guard |
| C3 | Schema Guard |
| C3 | Smart Router |
| C3 | Stream Client |
| C3 | Stream Ingest |
| C3 | Sublinear Mapper |
| C3 | Sybil Resistance |
| C3 | Sync Orchestrator |
| C3 | Synthesis Engine |
| C3 | Telemetry |
| C3 | Transparency Reporter |
| C3 | Verifier |
| C3 | Voting Service |
| C3 | Voting Weight Calculator |
| C3 | Workbenches |

### B. Names used across multiple layers (potential consistency hot-spots)

No significant cross-layer name reuse detected.

### C. C3 Components linked in C4 Sequences

| Component | Linked in C4? | Example sequence name |
|----------|----------|----------|
| Developer Portal | yes | c4 32 developer portal key issuance monitoring |
| GraphQL Federation | yes | c4 31 graphql federation update |
| Parameter Versioning | yes | c4 07 rule evolution parameter versioning q |
| Risk Scoring | yes | c4 25 event logging siem risk scoring |
| API Controller | no |  |
| API Controller | no |  |
| Accessibility & i18n | no |  |
| Alignment Evaluator | no |  |
| Anomaly Detection | no |  |
| Anomaly Detector | no |  |
| Appeals Handler | no |  |
| Attestation Issuer | no |  |
| Audit Trail Writer | no |  |
| Auth Hub | no |  |
| CP Calculator | no |  |
| CRDT Resolver | no |  |
| Command Handler | no |  |
| Compliance & Risk Checks | no |  |
| Contribution Validator | no |  |
| Credential Issuer (VC/SBT) | no |  |
| DID Manager | no |  |
| Dashboard Feed | no |  |
| Dashboard Renderer | no |  |
| Embedding Generator | no |  |
| Ethics Policy Engine | no |  |
| Ethics Preflight Client | no |  |
| Event Publisher | no |  |
| Execution Manager | no |  |
| Feature Store | no |  |
| Federation Client | no |  |
| Graph Ingest Pipeline | no |  |
| Health Monitor | no |  |
| Identity/Wallet Adapter | no |  |
| Incident Response | no |  |
| KPI Aggregator | no |  |
| Ledger Monitor | no |  |
| On-Chain Adapter | no |  |
| Ontology Manager | no |  |
| Payout Orchestrator | no |  |
| PoC Ledger | no |  |
| Project Registry | no |  |
| Proposal Engine | no |  |
| QF Engine | no |  |
| Quorum & Threshold Logic | no |  |
| RAG Orchestrator | no |  |
| Rate & Quota Manager | no |  |
| Recompute Worker | no |  |
| Reputation Graph | no |  |
| Reserve Manager | no |  |
| Resonance Engine | no |  |
| Rubric Manager | no |  |
| SIEM Collector | no |  |
| SRI Engine | no |  |
| Schema & Policy Guard | no |  |
| Schema Guard | no |  |
| Smart Router | no |  |
| Stream Client | no |  |
| Stream Ingest | no |  |
| Sublinear Mapper | no |  |
| Sybil Resistance | no |  |
| Sync Orchestrator | no |  |
| Synthesis Engine | no |  |
| Telemetry | no |  |
| Transparency Reporter | no |  |
| Verifier | no |  |
| Voting Service | no |  |
| Voting Weight Calculator | no |  |
| Workbenches | no |  |

## Recommendations

- Add missing files to the manifest or delete **Manifest.md** if Docusaurus dynamically indexes diagrams.
- Maintain a **central naming YAML source** for multi-layer names used by diagram generators.
- Ensure each **C3 component** has at least one **C4 sequence reference** (design or operational flow).
