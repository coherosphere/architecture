# Repository Glossary

_Generated_: 2025-11-03T12:50:52.309469Z

This document is auto-generated from Mermaid (`.mmd`), Markdown (`.md`), and Event specs (`assets/specs/events/*.json`).
Canonicalization and synonyms are applied from `scripts/canonical_names.yaml`.

## Overview (Top Terms)

Term | Count
---|---
C2-01 Resonance Service | 6
C2-11 Public API Gateway | 5
C2-01 Resonance | 4
C2-10 Security &amp; Audit Layer | 4
C2-12 Resonance Board / UI | 4
C2-03 Governance &amp; DAO | 4
C2-04 Treasury &amp; Funding | 4
C2-08 Manifesto &amp; Ethics Guard | 4
C1-06 Bitcoin / Hard Asset Layer | 4
C2-09 Knowledge Graph | 4
C2-02 Proof of Contribution | 3
C2-07 Metrics / Analytics | 3
C2-07 Resonance Metric Stack / Analytics | 3
C2-03 Governance | 3
C2-04 Treasury | 3
C2-06 Local Hubs | 3
C2-10 Security &amp; Audit | 3
C2-05 Identity (PoCI) | 3
C2-06 Local Hub / Federation | 3
C1-07 Developers / Architects | 3
C2-09 Knowledge Graph / Collective Intelligence | 3
C1-02 Member / Contributor | 3
Governance BC ⟷ C2-03 Governance &amp; DAO Service | 2
C2-03 Proposal &amp; Voting\n(quorum • threshold • sublinear weights) | 2
Contribution &amp; Evaluation BC ⟷ C2-02 PoC • C2-01 Resonance • C2-08 Ethics | 2
C2-02 Proof of Contribution\nR = I × A × e^(−λ·Δt)\nContribution Points CP_i | 2
C2-08 Resonance Filters\n(alignment checks) | 2
C2-01 Resonance Engine\n(weight W_i • SRI inputs) | 2
Identity &amp; Reputation (PoCI) BC ⟷ C2-05 Identity &amp; Reputation | 2
C2-05 PoCI Identity\n(reputation ledger • attestations) | 2
Treasury &amp; Funding BC ⟷ C2-04 Treasury &amp; Funding | 2
C2-04 Quadratic Funding\n(resonant allocation) | 2
C2-04 Treasury Reserve\n(sound money policy) | 2
Projects &amp; Local Hubs BC ⟷ C2-06 Local Hub / Federation | 2
C2-06 Projects &amp; Grants\n(lifecycle • milestones) | 2
C2-06 Local Hubs\n(semi-autonomous units) | 2
Meta-Governance &amp; Audit BC ⟷ C2-03 Governance • C2-10 Security &amp; Audit | 2
Rule Versioning\n(λ, α, q, θ) | 2
Audits &amp; Anomaly Detection | 2
Metrics &amp; Observability BC ⟷ C2-07 Metrics • C2-12 UI | 2
C2-07 KPI System\n(A_j • R_j • CP_i • W_i • SRI) | 2
C2-12 Resonance Board UI\n(live dashboards) | 2
Manifesto &amp; Ethics Guard BC ⟷ C2-08 Ethics Guard | 2
Knowledge Graph / Collective Intelligence BC ⟷ C2-09 Knowledge Graph | 2
Core Subdomains | 2
C2-03 Governance and DAO | 2
C2-04 Treasury and Funding | 2
C2-08 Manifesto and Ethics Guard | 2
Supporting Subdomains | 2
C2-05 Identity and Reputation PoCI | 2
C2-06 Local Hub and Federation | 2
C2-07 Metrics and Analytics | 2
C2-09 Knowledge Graph and Collective Intelligence | 2
Generic and Infrastructure | 2
C2-10 Security and Audit | 2
C2-12 Resonance Board UI | 2
Legend | 2
--- Shared Kernel | 2
-. Anti Corruption Layer .-&gt; | 2
--&gt; Published Language with DDD EVT and C4 | 2
--&gt; Conformist with DDD EVT and C4 | 2
--&gt; Open Host Service | 2
Teams | 2
Governance Team\ntype Stream aligned | 2
Resonance Core Team\ntype Complicated subsystem | 2
PoC and Identity Team\ntype Stream aligned | 2
Treasury Ops Team\ntype Stream aligned | 2
Federation and Hubs Team\ntype Stream aligned | 2
Metrics and Knowledge Team\ntype Stream aligned | 2
Security and Audit Team\ntype Enabling | 2
API Gateway and UI Team\ntype Platform | 2
DevOps and Platform Eng\ntype Platform | 2
Bounded Contexts and Subdomains | 2
Ops and Deployment Layer\nnot a C2 container | 2
Generic and Infrastructure Subdomains | 2

## C1

Term | Sources
---|---
C1-01 Coherosphere System (Sphere of Coherence) | assets/.mermaid_clean/C1_system/C1_System_Context_Diagram.mmd<br />assets/diagrams/C1_system/C1_System_Context_Diagram.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_System_Context_Diagram.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_System_Context_Diagram.mmd
C2-01 Resonance Service&lt;br&gt;(impact × alignment × time decay) | assets/.mermaid_clean/C1_system/C1_System_Context_Diagram.mmd<br />assets/diagrams/C1_system/C1_System_Context_Diagram.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_System_Context_Diagram.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_System_Context_Diagram.mmd
C2-02 Proof-of-Contribution Service&lt;br&gt;(contribution points • voting weight) | assets/.mermaid_clean/C1_system/C1_System_Context_Diagram.mmd<br />assets/diagrams/C1_system/C1_System_Context_Diagram.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_System_Context_Diagram.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_System_Context_Diagram.mmd
C2-03 Governance &amp;amp; DAO Service&lt;br&gt;(proposals • voting • execution) | assets/.mermaid_clean/C1_system/C1_System_Context_Diagram.mmd<br />assets/diagrams/C1_system/C1_System_Context_Diagram.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_System_Context_Diagram.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_System_Context_Diagram.mmd
C2-04 Treasury &amp;amp; Funding Service&lt;br&gt;(quadratic funding • streaming payouts) | assets/.mermaid_clean/C1_system/C1_System_Context_Diagram.mmd<br />assets/diagrams/C1_system/C1_System_Context_Diagram.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_System_Context_Diagram.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_System_Context_Diagram.mmd
C2-05 Identity &amp;amp; Reputation Service (PoCI)&lt;br&gt;(DID/VC/SBT • sybil resistance) | assets/.mermaid_clean/C1_system/C1_System_Context_Diagram.mmd<br />assets/diagrams/C1_system/C1_System_Context_Diagram.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_System_Context_Diagram.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_System_Context_Diagram.mmd
C2-06 Local Hub / Federation Service&lt;br&gt;(edge sync • CRDT • federation API) | assets/.mermaid_clean/C1_system/C1_System_Context_Diagram.mmd<br />assets/diagrams/C1_system/C1_System_Context_Diagram.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_System_Context_Diagram.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_System_Context_Diagram.mmd
C2-07 Resonance Metric Stack / Analytics&lt;br&gt;(KPIs • systemic resonance index) | assets/.mermaid_clean/C1_system/C1_System_Context_Diagram.mmd<br />assets/diagrams/C1_system/C1_System_Context_Diagram.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_System_Context_Diagram.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_System_Context_Diagram.mmd
C2-08 Manifesto &amp;amp; Ethics Guard&lt;br&gt;(alignment validation • rubrics) | assets/.mermaid_clean/C1_system/C1_System_Context_Diagram.mmd<br />assets/diagrams/C1_system/C1_System_Context_Diagram.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_System_Context_Diagram.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_System_Context_Diagram.mmd
C2-09 Knowledge Graph / Collective Intelligence&lt;br&gt;(ontology • vector • RAG) | assets/.mermaid_clean/C1_system/C1_System_Context_Diagram.mmd<br />assets/diagrams/C1_system/C1_System_Context_Diagram.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_System_Context_Diagram.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_System_Context_Diagram.mmd
C2-10 Security &amp;amp; Audit Layer&lt;br&gt;(SIEM • integrity • compliance) | assets/.mermaid_clean/C1_system/C1_System_Context_Diagram.mmd<br />assets/diagrams/C1_system/C1_System_Context_Diagram.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_System_Context_Diagram.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_System_Context_Diagram.mmd
C2-12 Resonance Board / UI&lt;br&gt;(dashboards • transparency) | assets/.mermaid_clean/C1_system/C1_System_Context_Diagram.mmd<br />assets/diagrams/C1_system/C1_System_Context_Diagram.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_System_Context_Diagram.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_System_Context_Diagram.mmd
C1-02 Member / Contributor&lt;br&gt;(creates contributions &amp;amp; votes) | assets/.mermaid_clean/C1_system/C1_System_Context_Diagram.mmd<br />assets/diagrams/C1_system/C1_System_Context_Diagram.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_System_Context_Diagram.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_System_Context_Diagram.mmd
C1-03 AI Systems &amp;amp; Agents&lt;br&gt;(alignment analytics &amp;amp; feedback models) | assets/.mermaid_clean/C1_system/C1_System_Context_Diagram.mmd<br />assets/diagrams/C1_system/C1_System_Context_Diagram.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_System_Context_Diagram.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_System_Context_Diagram.mmd
C1-04 External DAOs &amp;amp; Web3 Systems&lt;br&gt;(interoperable governance &amp;amp; funding) | assets/.mermaid_clean/C1_system/C1_System_Context_Diagram.mmd<br />assets/diagrams/C1_system/C1_System_Context_Diagram.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_System_Context_Diagram.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_System_Context_Diagram.mmd
C1-05 Local Communities &amp;amp; Institutions&lt;br&gt;(education • regeneration • healthcare) | assets/.mermaid_clean/C1_system/C1_System_Context_Diagram.mmd<br />assets/diagrams/C1_system/C1_System_Context_Diagram.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_System_Context_Diagram.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_System_Context_Diagram.mmd
C1-07 Developers &amp;amp; Architects&lt;br&gt;(maintain open-source infrastructure) | assets/.mermaid_clean/C1_system/C1_System_Context_Diagram.mmd<br />assets/diagrams/C1_system/C1_System_Context_Diagram.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_System_Context_Diagram.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_System_Context_Diagram.mmd
C1-06 Bitcoin / Hard Asset Layer&lt;br&gt;(sound money • treasury base) | assets/.mermaid_clean/C1_system/C1_System_Context_Diagram.mmd<br />assets/diagrams/C1_system/C1_System_Context_Diagram.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_System_Context_Diagram.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_System_Context_Diagram.mmd
C1-08 Public / Society&lt;br&gt;(observes resonance • benefits from coherence) | assets/.mermaid_clean/C1_system/C1_System_Context_Diagram.mmd<br />assets/diagrams/C1_system/C1_System_Context_Diagram.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_System_Context_Diagram.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_System_Context_Diagram.mmd
C1-01 Coherosphere System\n(Sphere of Coherence) | assets/.mermaid_clean/C1_system/C1_Stakeholders.mmd<br />assets/diagrams/C1_system/C1_Stakeholders.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_Stakeholders.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_Stakeholders.mmd
C1-02 Members / Contributors\n(create content • vote • earn reputation) | assets/.mermaid_clean/C1_system/C1_Stakeholders.mmd<br />assets/diagrams/C1_system/C1_Stakeholders.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_Stakeholders.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_Stakeholders.mmd
C1-07 Developers / Architects\n(extend code • maintain open infra) | assets/.mermaid_clean/C1_system/C1_Stakeholders.mmd<br />assets/diagrams/C1_system/C1_Stakeholders.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_Stakeholders.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_Stakeholders.mmd
C1-05 Local Communities / Institutions\n(education • health • regeneration) | assets/.mermaid_clean/C1_system/C1_Stakeholders.mmd<br />assets/diagrams/C1_system/C1_Stakeholders.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_Stakeholders.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_Stakeholders.mmd
C1-08 Public / Society\n(observes resonance • benefits from coherence) | assets/.mermaid_clean/C1_system/C1_Stakeholders.mmd<br />assets/diagrams/C1_system/C1_Stakeholders.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_Stakeholders.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_Stakeholders.mmd
C1-06 Bitcoin / Hard Asset Layer\n(treasury base • sound money) | assets/.mermaid_clean/C1_system/C1_Stakeholders.mmd<br />assets/diagrams/C1_system/C1_Stakeholders.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_Stakeholders.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_Stakeholders.mmd
C1-04 External DAOs / Web3 Systems\n(interoperable governance • funding bridges) | assets/.mermaid_clean/C1_system/C1_Stakeholders.mmd<br />assets/diagrams/C1_system/C1_Stakeholders.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_Stakeholders.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_Stakeholders.mmd
C1-03 AI Systems / Agents\n(alignment analytics • feedback models) | assets/.mermaid_clean/C1_system/C1_Stakeholders.mmd<br />assets/diagrams/C1_system/C1_Stakeholders.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_Stakeholders.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_Stakeholders.mmd
Human &amp; Organizational Actors | assets/.mermaid_clean/C1_system/C1_Stakeholders.mmd<br />assets/diagrams/C1_system/C1_Stakeholders.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_Stakeholders.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_Stakeholders.mmd
External Digital Ecosystem | assets/.mermaid_clean/C1_system/C1_Stakeholders.mmd<br />assets/diagrams/C1_system/C1_Stakeholders.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_Stakeholders.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_Stakeholders.mmd
Trust Zone A — PUBLIC EDGE (Browsers • Wallets • Public Web) | assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />assets/diagrams/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_Trust_Boundaries.mmd
C1-02 Members / Contributors | assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />assets/diagrams/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_Trust_Boundaries.mmd
C1-08 Public / Society | assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />assets/diagrams/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_Trust_Boundaries.mmd
C1-07 Developers / Architects | assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />assets/diagrams/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_Trust_Boundaries.mmd
C2-12 Resonance Board / UI | assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />assets/diagrams/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_Trust_Boundaries.mmd
Trust Zone B — SEMI-TRUSTED (Federation • API Gateway) | assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />assets/diagrams/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_Trust_Boundaries.mmd
C2-06 Local Hubs / Federation | assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />assets/diagrams/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_Trust_Boundaries.mmd
C2-11 Public API Gateway | assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />assets/diagrams/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_Trust_Boundaries.mmd
Trust Zone C — CORE (Coherosphere Services) | assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />assets/diagrams/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_Trust_Boundaries.mmd
C2-01 Resonance Service | assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />assets/diagrams/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_Trust_Boundaries.mmd
C2-02 Proof-of-Contribution | assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />assets/diagrams/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_Trust_Boundaries.mmd
C2-03 Governance &amp; DAO | assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />assets/diagrams/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_Trust_Boundaries.mmd
C2-04 Treasury &amp; Funding | assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />assets/diagrams/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_Trust_Boundaries.mmd
C2-05 Identity &amp; Reputation (PoCI) | assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />assets/diagrams/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_Trust_Boundaries.mmd
C2-07 Metrics / Analytics | assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />assets/diagrams/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_Trust_Boundaries.mmd
C2-08 Manifesto &amp; Ethics Guard | assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />assets/diagrams/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_Trust_Boundaries.mmd
C2-09 Knowledge Graph | assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />assets/diagrams/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_Trust_Boundaries.mmd
Trust Zone D — SECURE LEDGER &amp; KEYS (Audit • Reserves • Attestations) | assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />assets/diagrams/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_Trust_Boundaries.mmd
C2-10 Security &amp; Audit Layer | assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />assets/diagrams/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_Trust_Boundaries.mmd
Treasury Ledger / Escrows | assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />assets/diagrams/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_Trust_Boundaries.mmd
Attestation Registry (PoCI / Ethics) | assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />assets/diagrams/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_Trust_Boundaries.mmd
External Ecosystem (Untrusted / Third-Party) | assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />assets/diagrams/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_Trust_Boundaries.mmd
C1-06 Bitcoin / Hard Asset Layer | assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />assets/diagrams/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_Trust_Boundaries.mmd
C1-04 External DAOs / Web3 Systems | assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />assets/diagrams/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_Trust_Boundaries.mmd
C1-03 AI Systems / Agents | assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />assets/diagrams/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C1_system/C1_Trust_Boundaries.mmd<br />docs.coherosphere.io/static/assets/diagrams/C1_system/C1_Trust_Boundaries.mmd

## C2

Term | Sources
---|---
C1-01 Coherosphere System (Sphere of Coherence) | assets/.mermaid_clean/C2_containers/C2_Container_Diagram.mmd<br />assets/diagrams/C2_containers/C2_Container_Diagram.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Container_Diagram.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Container_Diagram.mmd
C2-01 Resonance Service&lt;br&gt;(C3-01.xx: Resonance Engine • SRI • Anomaly) | assets/.mermaid_clean/C2_containers/C2_Container_Diagram.mmd<br />assets/diagrams/C2_containers/C2_Container_Diagram.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Container_Diagram.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Container_Diagram.mmd
C2-02 Proof-of-Contribution Service&lt;br&gt;(C3-02.xx: CP Accumulator • Time Decay • Voting Mapper) | assets/.mermaid_clean/C2_containers/C2_Container_Diagram.mmd<br />assets/diagrams/C2_containers/C2_Container_Diagram.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Container_Diagram.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Container_Diagram.mmd
C2-03 Governance &amp; DAO Service&lt;br&gt;(C3-03.xx: Proposal • Quorum/Threshold • Execution) | assets/.mermaid_clean/C2_containers/C2_Container_Diagram.mmd<br />assets/diagrams/C2_containers/C2_Container_Diagram.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Container_Diagram.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Container_Diagram.mmd
C2-04 Treasury &amp; Funding Service&lt;br&gt;(C3-04.xx: QF Engine • Escrow • Reserve) | assets/.mermaid_clean/C2_containers/C2_Container_Diagram.mmd<br />assets/diagrams/C2_containers/C2_Container_Diagram.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Container_Diagram.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Container_Diagram.mmd
C2-05 Identity &amp;amp; Reputation (PoCI)&lt;br&gt;(C3-05.xx: DID • VC Registry • Reputation Graph) | assets/.mermaid_clean/C2_containers/C2_Container_Diagram.mmd<br />assets/diagrams/C2_containers/C2_Container_Diagram.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Container_Diagram.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Container_Diagram.mmd
C2-06 Local Hub / Federation&lt;br&gt;(C3-06.xx: Sync Orchestrator • Edge Store • CRDT) | assets/.mermaid_clean/C2_containers/C2_Container_Diagram.mmd<br />assets/diagrams/C2_containers/C2_Container_Diagram.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Container_Diagram.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Container_Diagram.mmd
C2-07 Resonance Metric Stack / Analytics&lt;br&gt;(C3-07.xx: KPI Aggregator • SRI • Feature Store) | assets/.mermaid_clean/C2_containers/C2_Container_Diagram.mmd<br />assets/diagrams/C2_containers/C2_Container_Diagram.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Container_Diagram.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Container_Diagram.mmd
C2-08 Manifesto &amp;amp; Ethics Guard&lt;br&gt;(C3-08.xx: Alignment • Rubrics • Attestations) | assets/.mermaid_clean/C2_containers/C2_Container_Diagram.mmd<br />assets/diagrams/C2_containers/C2_Container_Diagram.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Container_Diagram.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Container_Diagram.mmd
C2-09 Knowledge Graph / Collective Intelligence&lt;br&gt;(C3-09.xx: Ontology • RAG Orchestrator • Synthesis) | assets/.mermaid_clean/C2_containers/C2_Container_Diagram.mmd<br />assets/diagrams/C2_containers/C2_Container_Diagram.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Container_Diagram.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Container_Diagram.mmd
C2-10 Security &amp;amp; Audit Layer&lt;br&gt;(C3-10.xx: Ledger Monitor • SIEM • Forensics) | assets/.mermaid_clean/C2_containers/C2_Container_Diagram.mmd<br />assets/diagrams/C2_containers/C2_Container_Diagram.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Container_Diagram.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Container_Diagram.mmd
C2-11 Public API Gateway&lt;br&gt;(C3-11.xx: Smart Router • GraphQL Federation • Auth) | assets/.mermaid_clean/C2_containers/C2_Container_Diagram.mmd<br />assets/diagrams/C2_containers/C2_Container_Diagram.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Container_Diagram.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Container_Diagram.mmd
C2-12 Resonance Board / UI&lt;br&gt;(C3-12.xx: Dashboards • Heatmaps • Workbenches) | assets/.mermaid_clean/C2_containers/C2_Container_Diagram.mmd<br />assets/diagrams/C2_containers/C2_Container_Diagram.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Container_Diagram.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Container_Diagram.mmd
C1-02 Member / Contributor | assets/.mermaid_clean/C2_containers/C2_Container_Diagram.mmd<br />assets/diagrams/C2_containers/C2_Container_Diagram.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Container_Diagram.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Container_Diagram.mmd
C1-07 Developers &amp; Architects | assets/.mermaid_clean/C2_containers/C2_Container_Diagram.mmd<br />assets/diagrams/C2_containers/C2_Container_Diagram.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Container_Diagram.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Container_Diagram.mmd
C1-04 External DAOs / Web3 Systems | assets/.mermaid_clean/C2_containers/C2_Container_Diagram.mmd<br />assets/.mermaid_clean/C2_containers/C2_Dataflow.mmd<br />assets/diagrams/C2_containers/C2_Container_Diagram.mmd<br />assets/diagrams/C2_containers/C2_Dataflow.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Container_Diagram.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Dataflow.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Container_Diagram.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Dataflow.mmd
C1-05 Local Communities &amp; Institutions | assets/.mermaid_clean/C2_containers/C2_Container_Diagram.mmd<br />assets/diagrams/C2_containers/C2_Container_Diagram.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Container_Diagram.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Container_Diagram.mmd
C1-03 AI Systems &amp; Agents&lt;br&gt;(Alignment Analytics • Feedback Models) | assets/.mermaid_clean/C2_containers/C2_Container_Diagram.mmd<br />assets/diagrams/C2_containers/C2_Container_Diagram.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Container_Diagram.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Container_Diagram.mmd
C1-06 Bitcoin / Hard Asset Layer | assets/.mermaid_clean/C2_containers/C2_Container_Diagram.mmd<br />assets/.mermaid_clean/C2_containers/C2_Dataflow.mmd<br />assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />assets/diagrams/C2_containers/C2_Container_Diagram.mmd<br />assets/diagrams/C2_containers/C2_Dataflow.mmd<br />assets/diagrams/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Container_Diagram.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Dataflow.mmd
C1-08 Public / Society&lt;br&gt;(observes resonance • benefits from coherence) | assets/.mermaid_clean/C2_containers/C2_Container_Diagram.mmd<br />assets/diagrams/C2_containers/C2_Container_Diagram.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Container_Diagram.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Container_Diagram.mmd
Access Layer — Anycast + CDN + WAF | assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />assets/diagrams/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Deployment.mmd
Global Ingress (CDN/WAF)\nTLS Termination • Rate Caps | assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />assets/diagrams/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Deployment.mmd
C2-11 Public API Gateway\n(REST/gRPC/GraphQL)\nreplicas: x3 | assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />assets/diagrams/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Deployment.mmd
C2-12 Resonance Board / UI\n(static + stream clients)\nAZ: Multi-AZ | assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />assets/diagrams/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Deployment.mmd
Core Region — eu-central (Multi-AZ) | assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />assets/diagrams/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Deployment.mmd
C2-01 Resonance Service\nreplicas: x3 | assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />assets/diagrams/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Deployment.mmd
C2-02 Proof-of-Contribution\nreplicas: x3 | assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />assets/diagrams/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Deployment.mmd
C2-03 Governance &amp; DAO\nreplicas: x3 | assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />assets/diagrams/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Deployment.mmd
C2-04 Treasury &amp; Funding\nreplicas: x2 | assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />assets/diagrams/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Deployment.mmd
C2-05 Identity &amp; Reputation (PoCI)\nreplicas: x2 | assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />assets/diagrams/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Deployment.mmd
C2-07 Metrics / Analytics\nreplicas: x3 | assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />assets/diagrams/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Deployment.mmd
C2-08 Manifesto &amp; Ethics Guard\nreplicas: x2 | assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />assets/diagrams/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Deployment.mmd
C2-09 Knowledge Graph\nreplicas: x2 | assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />assets/diagrams/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Deployment.mmd
Core Data Stores | assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />assets/diagrams/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Deployment.mmd
PoC Ledger\n(event store)\nRPO ≤ 5m | assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />assets/diagrams/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Deployment.mmd
Metrics DB / Feature Store\nRPO ≤ 5m | assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />assets/diagrams/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Deployment.mmd
Graph DB + Vector DB\nRPO ≤ 10m | assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />assets/diagrams/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Deployment.mmd
Secure Zone — HSM • Audit • Reserves | assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />assets/diagrams/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Deployment.mmd
C2-10 Security &amp; Audit Layer\nreplicas: x2 | assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />assets/diagrams/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Deployment.mmd
HSM / Key Vault\n(signing • custody) | assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />assets/diagrams/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Deployment.mmd
Treasury Ledger / Escrows\n(settlement journal) | assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />assets/diagrams/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Deployment.mmd
Attestation Registry\n(PoCI/Ethics) | assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />assets/diagrams/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Deployment.mmd
Audit Vault (append-only) | assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />assets/diagrams/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Deployment.mmd
Federation Edge — Local Hubs (CRDT Sync) | assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />assets/diagrams/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Deployment.mmd
C2-06 Local Hub — CH-001\nSync Orchestrator + Edge Store | assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />assets/diagrams/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Deployment.mmd
C2-06 Local Hub — JP-101\nSync Orchestrator + Edge Store | assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />assets/diagrams/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Deployment.mmd
Edge Store (CRDT)\nlocal cache | assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />assets/diagrams/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Deployment.mmd
DR Region — eu-west (Warm Standby) | assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />assets/diagrams/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Deployment.mmd
Resonance (warm)\nreplicas: x1 | assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />assets/diagrams/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Deployment.mmd
PoC (warm)\nreplicas: x1 | assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />assets/diagrams/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Deployment.mmd
Governance (warm)\nreplicas: x1 | assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />assets/diagrams/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Deployment.mmd
Metrics (warm)\nreplicas: x1 | assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />assets/diagrams/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Deployment.mmd
Async Snapshots\nRPO ≤ 15m | assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />assets/diagrams/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Deployment.mmd
External Ecosystem | assets/.mermaid_clean/C2_containers/C2_Dataflow.mmd<br />assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />assets/diagrams/C2_containers/C2_Dataflow.mmd<br />assets/diagrams/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Dataflow.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Dataflow.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Deployment.mmd
C1-04 External DAOs / Web3 | assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />assets/diagrams/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Deployment.mmd
C1-03 AI Systems / Agents | assets/.mermaid_clean/C2_containers/C2_Dataflow.mmd<br />assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />assets/diagrams/C2_containers/C2_Dataflow.mmd<br />assets/diagrams/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Dataflow.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Deployment.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Dataflow.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Deployment.mmd
C1-07 Developers / Clients | assets/.mermaid_clean/C2_containers/C2_API_Surface.mmd<br />assets/diagrams/C2_containers/C2_API_Surface.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_API_Surface.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_API_Surface.mmd
C2-12 Resonance Board / UI | assets/.mermaid_clean/C2_containers/C2_API_Surface.mmd<br />assets/.mermaid_clean/C2_containers/C2_Dataflow.mmd<br />assets/diagrams/C2_containers/C2_API_Surface.mmd<br />assets/diagrams/C2_containers/C2_Dataflow.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_API_Surface.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Dataflow.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_API_Surface.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Dataflow.mmd
C2-11 Public API Gateway\nREST • gRPC • GraphQL | assets/.mermaid_clean/C2_containers/C2_API_Surface.mmd<br />assets/diagrams/C2_containers/C2_API_Surface.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_API_Surface.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_API_Surface.mmd
C2-01 Resonance\nPOST /v1/resonance/compute\nPOST /v1/decay/apply | assets/.mermaid_clean/C2_containers/C2_API_Surface.mmd<br />assets/diagrams/C2_containers/C2_API_Surface.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_API_Surface.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_API_Surface.mmd
C2-02 PoC\nPOST /v1/contributions\nGET /v1/members/&#123;id&#125;/scores | assets/.mermaid_clean/C2_containers/C2_API_Surface.mmd<br />assets/diagrams/C2_containers/C2_API_Surface.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_API_Surface.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_API_Surface.mmd
C2-03 Governance\nPOST /v1/proposals\nPOST /v1/proposals/&#123;id&#125;/votes | assets/.mermaid_clean/C2_containers/C2_API_Surface.mmd<br />assets/diagrams/C2_containers/C2_API_Surface.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_API_Surface.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_API_Surface.mmd
C2-04 Treasury\nPOST /v1/rounds\nPOST /v1/payouts/stream | assets/.mermaid_clean/C2_containers/C2_API_Surface.mmd<br />assets/diagrams/C2_containers/C2_API_Surface.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_API_Surface.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_API_Surface.mmd
C2-05 Identity (PoCI)\nPOST /v1/dids\nPOST /v1/credentials/issue | assets/.mermaid_clean/C2_containers/C2_API_Surface.mmd<br />assets/diagrams/C2_containers/C2_API_Surface.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_API_Surface.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_API_Surface.mmd
C2-06 Local Hubs\nPOST /v1/projects\nPOST /v1/sync/push&#124;pull | assets/.mermaid_clean/C2_containers/C2_API_Surface.mmd<br />assets/diagrams/C2_containers/C2_API_Surface.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_API_Surface.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_API_Surface.mmd
C2-07 Metrics\nGET /v1/kpi\nGET /v1/kpi/series | assets/.mermaid_clean/C2_containers/C2_API_Surface.mmd<br />assets/diagrams/C2_containers/C2_API_Surface.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_API_Surface.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_API_Surface.mmd
C2-08 Ethics\nPOST /v1/ethics/preflight\nPOST /v1/ethics/appeals | assets/.mermaid_clean/C2_containers/C2_API_Surface.mmd<br />assets/diagrams/C2_containers/C2_API_Surface.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_API_Surface.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_API_Surface.mmd
C2-09 Knowledge Graph\nPOST /v1/ingest\nPOST /v1/rag/query | assets/.mermaid_clean/C2_containers/C2_API_Surface.mmd<br />assets/diagrams/C2_containers/C2_API_Surface.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_API_Surface.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_API_Surface.mmd
C2-10 Security &amp; Audit\nPOST /v1/siem\nPOST /v1/incidents | assets/.mermaid_clean/C2_containers/C2_API_Surface.mmd<br />assets/diagrams/C2_containers/C2_API_Surface.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_API_Surface.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_API_Surface.mmd
Streams: /v1/streams/kpi\nWebhooks: metrics.kpi_updated, treasury.tx_posted, ... | assets/.mermaid_clean/C2_containers/C2_API_Surface.mmd<br />assets/diagrams/C2_containers/C2_API_Surface.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_API_Surface.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_API_Surface.mmd
Coherosphere Core Services | assets/.mermaid_clean/C2_containers/C2_Dataflow.mmd<br />assets/diagrams/C2_containers/C2_Dataflow.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Dataflow.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Dataflow.mmd
C2-01 Resonance Service | assets/.mermaid_clean/C2_containers/C2_Dataflow.mmd<br />assets/diagrams/C2_containers/C2_Dataflow.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Dataflow.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Dataflow.mmd
C2-02 Proof-of-Contribution (PoC) | assets/.mermaid_clean/C2_containers/C2_Dataflow.mmd<br />assets/diagrams/C2_containers/C2_Dataflow.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Dataflow.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Dataflow.mmd
C2-03 Governance &amp; DAO | assets/.mermaid_clean/C2_containers/C2_Dataflow.mmd<br />assets/diagrams/C2_containers/C2_Dataflow.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Dataflow.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Dataflow.mmd
C2-04 Treasury &amp; Funding | assets/.mermaid_clean/C2_containers/C2_Dataflow.mmd<br />assets/diagrams/C2_containers/C2_Dataflow.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Dataflow.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Dataflow.mmd
C2-05 Identity &amp; Reputation (PoCI) | assets/.mermaid_clean/C2_containers/C2_Dataflow.mmd<br />assets/diagrams/C2_containers/C2_Dataflow.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Dataflow.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Dataflow.mmd
C2-06 Local Hub / Federation | assets/.mermaid_clean/C2_containers/C2_Dataflow.mmd<br />assets/diagrams/C2_containers/C2_Dataflow.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Dataflow.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Dataflow.mmd
C2-07 Resonance Metric Stack / Analytics | assets/.mermaid_clean/C2_containers/C2_Dataflow.mmd<br />assets/diagrams/C2_containers/C2_Dataflow.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Dataflow.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Dataflow.mmd
C2-08 Manifesto &amp; Ethics Guard | assets/.mermaid_clean/C2_containers/C2_Dataflow.mmd<br />assets/diagrams/C2_containers/C2_Dataflow.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Dataflow.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Dataflow.mmd
C2-09 Knowledge Graph / Collective Intelligence | assets/.mermaid_clean/C2_containers/C2_Dataflow.mmd<br />assets/diagrams/C2_containers/C2_Dataflow.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Dataflow.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Dataflow.mmd
C2-10 Security &amp; Audit Layer | assets/.mermaid_clean/C2_containers/C2_Dataflow.mmd<br />assets/diagrams/C2_containers/C2_Dataflow.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Dataflow.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Dataflow.mmd
Access &amp; Interfaces | assets/.mermaid_clean/C2_containers/C2_Dataflow.mmd<br />assets/diagrams/C2_containers/C2_Dataflow.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Dataflow.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Dataflow.mmd
C2-11 Public API Gateway | assets/.mermaid_clean/C2_containers/C2_Dataflow.mmd<br />assets/diagrams/C2_containers/C2_Dataflow.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C2_containers/C2_Dataflow.mmd<br />docs.coherosphere.io/static/assets/diagrams/C2_containers/C2_Dataflow.mmd
Trust Boundary: Clients | assets/diagrams/C2_containers/C2_Governance_Flows_MetaGov_Loop.mmd
Member Web App\n(app.coherosphere.com) | assets/diagrams/C2_containers/C2_Governance_Flows_MetaGov_Loop.mmd
Evaluators / Guardians\n(human+AI) | assets/diagrams/C2_containers/C2_Governance_Flows_MetaGov_Loop.mmd
Public Dashboard\n(metrics.coherosphere) | assets/diagrams/C2_containers/C2_Governance_Flows_MetaGov_Loop.mmd
Trust Boundary: Cohere Cloud (Off-Chain) | assets/diagrams/C2_containers/C2_Governance_Flows_MetaGov_Loop.mmd
API Gateway\n(api.coherosphere.io) | assets/diagrams/C2_containers/C2_Governance_Flows_MetaGov_Loop.mmd
Proposal Service\n(lifecycle, quorum checks) | assets/diagrams/C2_containers/C2_Governance_Flows_MetaGov_Loop.mmd
Guardian / Policy Service\n(alignment, eligibility) | assets/diagrams/C2_containers/C2_Governance_Flows_MetaGov_Loop.mmd
Anomaly Service\n(sybil/spam/outliers) | assets/diagrams/C2_containers/C2_Governance_Flows_MetaGov_Loop.mmd
Resonance Service\n(impact×alignment • time-decay) | assets/diagrams/C2_containers/C2_Governance_Flows_MetaGov_Loop.mmd
Metrics / SRI Service\n(KPIs, SRI, trend) | assets/diagrams/C2_containers/C2_Governance_Flows_MetaGov_Loop.mmd
Audit Mirror (off-chain) | assets/diagrams/C2_containers/C2_Governance_Flows_MetaGov_Loop.mmd
Trust Boundary: Public Blockchain (On-Chain) | assets/diagrams/C2_containers/C2_Governance_Flows_MetaGov_Loop.mmd<br />assets/diagrams/C2_containers/C2_On_Off_Chain_Map.mmd
Governance Smart Contracts\n(proposals, voting, execution) | assets/diagrams/C2_containers/C2_Governance_Flows_MetaGov_Loop.mmd
Meta-Governance SCs\n(params, rule versioning) | assets/diagrams/C2_containers/C2_Governance_Flows_MetaGov_Loop.mmd
Treasury SCs\n(QF, disbursements) | assets/diagrams/C2_containers/C2_Governance_Flows_MetaGov_Loop.mmd
Identity/PoCI SCs\n(contribution proofs) | assets/diagrams/C2_containers/C2_Governance_Flows_MetaGov_Loop.mmd
On-chain Event Log\n(immutable) | assets/diagrams/C2_containers/C2_Governance_Flows_MetaGov_Loop.mmd
C2-01 Governance SCs\nProposals • Voting • Execution | assets/diagrams/C2_containers/C2_On_Off_Chain_Map.mmd
C2-02 Treasury SCs\nQF Matching • Disbursements | assets/diagrams/C2_containers/C2_On_Off_Chain_Map.mmd
C2-03 Identity/PoCI SCs\nProof-of-Contribution Ledger | assets/diagrams/C2_containers/C2_On_Off_Chain_Map.mmd
C2-04 Meta-Governance SCs\nParam/Rules Versioning | assets/diagrams/C2_containers/C2_On_Off_Chain_Map.mmd
On-chain Event Log\n(Immutable) | assets/diagrams/C2_containers/C2_On_Off_Chain_Map.mmd
Trust Boundary: Cohere Cloud (Off-Chain Services) | assets/diagrams/C2_containers/C2_On_Off_Chain_Map.mmd
C2-05 API Gateway\nhttps://api.coherosphere.io | assets/diagrams/C2_containers/C2_On_Off_Chain_Map.mmd
C2-06 Resonance Service\nImpact×Alignment • Time Decay | assets/diagrams/C2_containers/C2_On_Off_Chain_Map.mmd
C2-07 Proposal Service\nLifecycle/Quorum | assets/diagrams/C2_containers/C2_On_Off_Chain_Map.mmd
C2-08 Funding Service\nQF Calc • Payout Orchestration | assets/diagrams/C2_containers/C2_On_Off_Chain_Map.mmd
C2-09 Identity Aggregator\nPoCI Aggregation | assets/diagrams/C2_containers/C2_On_Off_Chain_Map.mmd
C2-10 Guardian Service\nAlignment/Policy Checks | assets/diagrams/C2_containers/C2_On_Off_Chain_Map.mmd
C2-11 Anomaly Service\nSybil/Spam/Outliers | assets/diagrams/C2_containers/C2_On_Off_Chain_Map.mmd
C2-12 Metrics/SRI Service\nDashboards • KPIs | assets/diagrams/C2_containers/C2_On_Off_Chain_Map.mmd
Event/Messaging Bus | assets/diagrams/C2_containers/C2_On_Off_Chain_Map.mmd
Operational DB | assets/diagrams/C2_containers/C2_On_Off_Chain_Map.mmd
Analytics Lake | assets/diagrams/C2_containers/C2_On_Off_Chain_Map.mmd
Audit Log (off-chain mirror) | assets/diagrams/C2_containers/C2_On_Off_Chain_Map.mmd
Trust Boundary: Clients &amp; Hubs | assets/diagrams/C2_containers/C2_On_Off_Chain_Map.mmd
Member UI (Web)\nhttps://app.coherosphere.com | assets/diagrams/C2_containers/C2_On_Off_Chain_Map.mmd
Contributor CLI/API | assets/diagrams/C2_containers/C2_On_Off_Chain_Map.mmd
Local Hub Node\n(sync w/ chain) | assets/diagrams/C2_containers/C2_On_Off_Chain_Map.mmd

## C3

Term | Sources
---|---
C2-01 — Resonance Service | assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />assets/diagrams/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_states/State_Machines_Overview..mmd
SM-01.01 Resonance Calculation State\nEntity: RESONANCE_SAMPLE\nEvents: ResonanceRequested • ResonanceUpdated • AnomalyDetected | assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />assets/diagrams/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_states/State_Machines_Overview..mmd
C2-02 — Proof-of-Contribution | assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />assets/diagrams/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_states/State_Machines_Overview..mmd
SM-02.01 Contribution Lifecycle\nEntity: CONTRIBUTION\nEvents: ContributionSubmitted • ImpactScored • AlignmentChecked • CPUpdated | assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />assets/diagrams/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_states/State_Machines_Overview..mmd
SM-02.02 Decay &amp; Recompute Cycle\nEntity: LEDGER_ENTRY\nEvents: DecayApplied • RecomputeFinished | assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />assets/diagrams/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_states/State_Machines_Overview..mmd
C2-03 — Governance &amp; DAO | assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />assets/diagrams/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_states/State_Machines_Overview..mmd
SM-03.01 Proposal Lifecycle\nEntity: PROPOSAL\nEvents: ProposalCreated • VoteCast • VoteTallied • DecisionRecorded • PolicyChanged | assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />assets/diagrams/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_states/State_Machines_Overview..mmd
SM-03.02 Appeal / Dispute Flow\nEntity: APPEAL\nEvents: AppealOpened • AppealResolved | assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />assets/diagrams/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_states/State_Machines_Overview..mmd
C2-04 — Treasury &amp; Funding | assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />assets/diagrams/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_states/State_Machines_Overview..mmd
SM-04.01 Quadratic Funding Round\nEntity: QF_ROUND\nEvents: RoundOpened • DonationRecorded • FundingAllocated • RoundClosed | assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />assets/diagrams/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_states/State_Machines_Overview..mmd
SM-04.02 Streaming Payout Lifecycle\nEntity: PAYOUT_STREAM\nEvents: StreamOpened • StreamPaused • StreamResumed • StreamClosed | assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />assets/diagrams/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_states/State_Machines_Overview..mmd
C2-05 — Identity &amp; Reputation (PoCI) | assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />assets/diagrams/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_states/State_Machines_Overview..mmd
SM-05.01 Identity Verification &amp; Attestation\nEntity: DID / ATTESTATION\nEvents: IdentityVerified • AttestationIssued • AttestationRevoked | assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />assets/diagrams/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_states/State_Machines_Overview..mmd
SM-05.02 Reputation Update Cycle\nEntity: REPUTATION_SCORE\nEvents: ReputationUpdated • DecayApplied | assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />assets/diagrams/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_states/State_Machines_Overview..mmd
C2-06 — Local Hub / Federation | assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />assets/diagrams/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_states/State_Machines_Overview..mmd
SM-06.01 Hub Sync State\nEntity: HUB_SYNC_FRAME\nEvents: SyncRequested • SyncMerged • SyncConfirmed | assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />assets/diagrams/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_states/State_Machines_Overview..mmd
SM-06.02 Project Lifecycle\nEntity: PROJECT\nEvents: ProjectCreated • MilestoneReported • ProjectCompleted | assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />assets/diagrams/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_states/State_Machines_Overview..mmd
C2-07 — Metrics / Analytics | assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />assets/diagrams/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_states/State_Machines_Overview..mmd
SM-07.01 Snapshot &amp; KPI Aggregation\nEntity: KPI_SNAPSHOT\nEvents: SnapshotStarted • SRIComputed • KPIUpdated | assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />assets/diagrams/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_states/State_Machines_Overview..mmd
C2-08 — Manifesto &amp; Ethics Guard | assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />assets/diagrams/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_states/State_Machines_Overview..mmd
SM-08.01 Ethics Evaluation Flow\nEntity: ETHICS_EVAL\nEvents: AlignmentChecked • AttestationIssued • AppealResolved | assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />assets/diagrams/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_states/State_Machines_Overview..mmd
C2-09 — Knowledge Graph / Collective Intelligence | assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />assets/diagrams/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_states/State_Machines_Overview..mmd
SM-09.01 Knowledge Ingestion Pipeline\nEntity: KG_ENTITY\nEvents: SourceDiscovered • EmbeddingGenerated • KnowledgeUpdated | assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />assets/diagrams/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_states/State_Machines_Overview..mmd
C2-10 — Security &amp; Audit | assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />assets/diagrams/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_states/State_Machines_Overview..mmd
SM-10.01 Incident Lifecycle\nEntity: INCIDENT\nEvents: IncidentOpened • IncidentResolved • TransparencyReportPublished | assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />assets/diagrams/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_states/State_Machines_Overview..mmd
SM-10.02 Transparency Report Lifecycle\nEntity: TRANSPARENCY_REPORT\nEvents: ReportGenerated • ReportPublished | assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />assets/diagrams/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_states/State_Machines_Overview..mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_states/State_Machines_Overview..mmd
Trust Boundary: Public Blockchain | assets/diagrams/c3_components/C3_Metrics_System.mmd
Governance SCs\n(votes, exec events) | assets/diagrams/c3_components/C3_Metrics_System.mmd
Treasury SCs\n(payouts, qf events) | assets/diagrams/c3_components/C3_Metrics_System.mmd
Identity/PoCI SCs\n(proofs) | assets/diagrams/c3_components/C3_Metrics_System.mmd
Trust Boundary: Cohere Cloud — Processing | assets/diagrams/c3_components/C3_Metrics_System.mmd
Ingest Gateway\n(webhooks, indexers) | assets/diagrams/c3_components/C3_Metrics_System.mmd
Event Stream\n(kinesis/kafka/nats) | assets/diagrams/c3_components/C3_Metrics_System.mmd
Resonance Engine\n(I×A, decay) | assets/diagrams/c3_components/C3_Metrics_System.mmd
Signal Enricher\n(tags, cohort, hub) | assets/diagrams/c3_components/C3_Metrics_System.mmd
Metrics Aggregator\n(windowed rollups) | assets/diagrams/c3_components/C3_Metrics_System.mmd
SRI Calculator\n(Systemic Resonance Index) | assets/diagrams/c3_components/C3_Metrics_System.mmd
Radar Composer\n(multiaxial buckets) | assets/diagrams/c3_components/C3_Metrics_System.mmd
Heatmap Builder\n(grid tiles) | assets/diagrams/c3_components/C3_Metrics_System.mmd
Threshold/Trend Detector\n(alerts) | assets/diagrams/c3_components/C3_Metrics_System.mmd
Trust Boundary: Data Stores | assets/diagrams/c3_components/C3_Metrics_System.mmd
Time-Series DB\n(raw, rollups) | assets/diagrams/c3_components/C3_Metrics_System.mmd
Analytics Lake\n(historical/ML) | assets/diagrams/c3_components/C3_Metrics_System.mmd
Realtime Cache\n(WS/SSE payloads) | assets/diagrams/c3_components/C3_Metrics_System.mmd
Audit Mirror\n(immutable-like) | assets/diagrams/c3_components/C3_Metrics_System.mmd
Trust Boundary: Delivery &amp; UI | assets/diagrams/c3_components/C3_Metrics_System.mmd
Metrics API\n(/radar, /heatmap, /kpis) | assets/diagrams/c3_components/C3_Metrics_System.mmd
Realtime Gateway\n(WebSocket/SSE) | assets/diagrams/c3_components/C3_Metrics_System.mmd
Public Dashboard\n(metrics.coherosphere) | assets/diagrams/c3_components/C3_Metrics_System.mmd
Radar Widget\n(dynamic axes) | assets/diagrams/c3_components/C3_Metrics_System.mmd
Heatmap Widget\n(zoom/pan) | assets/diagrams/c3_components/C3_Metrics_System.mmd
KPI Tiles\n(SLA, health, trend) | assets/diagrams/c3_components/C3_Metrics_System.mmd
C2-10 Security &amp; Audit Layer | assets/diagrams/C3_containers/C2-04_Treasury_Funding_Service.mmd<br />assets/diagrams/C3_containers/C2-05_Identity_Reputation_PoCI.mmd<br />assets/diagrams/C3_containers/C2-10_Security_Audit_Layer.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-04_Treasury_Funding_Service.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-05_Identity_Reputation_PoCI.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-10_Security_Audit_Layer.mmd
C3-10.01 Ledger Monitor (Integrity/Reconcile) | assets/diagrams/C3_containers/C2-10_Security_Audit_Layer.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-10_Security_Audit_Layer.mmd
C3-10.02 SIEM Collector (Logs/Telemetry) | assets/diagrams/C3_containers/C2-10_Security_Audit_Layer.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-10_Security_Audit_Layer.mmd
C3-10.03 Anomaly Detection | assets/diagrams/C3_containers/C2-10_Security_Audit_Layer.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-10_Security_Audit_Layer.mmd
C3-10.04 Risk Scoring | assets/diagrams/C3_containers/C2-10_Security_Audit_Layer.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-10_Security_Audit_Layer.mmd
C3-10.05 Incident Response (IR runbooks) | assets/diagrams/C3_containers/C2-10_Security_Audit_Layer.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-10_Security_Audit_Layer.mmd
C3-10.06 Transparency Reporter (Public Bundles) | assets/diagrams/C3_containers/C2-10_Security_Audit_Layer.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-10_Security_Audit_Layer.mmd
Audit-DB | assets/diagrams/C3_containers/C2-10_Security_Audit_Layer.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-10_Security_Audit_Layer.mmd
SIEM-Store | assets/diagrams/C3_containers/C2-10_Security_Audit_Layer.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-10_Security_Audit_Layer.mmd
IR-DB | assets/diagrams/C3_containers/C2-10_Security_Audit_Layer.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-10_Security_Audit_Layer.mmd
C2-11 Public API Gateway | assets/diagrams/C3_containers/C2-10_Security_Audit_Layer.mmd<br />assets/diagrams/C3_containers/C2-11_Public_API_Gateway.mmd<br />assets/diagrams/C3_containers/C2-12_Resonance_Board_UI.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-10_Security_Audit_Layer.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-11_Public_API_Gateway.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-12_Resonance_Board_UI.mmd
C2-12 Resonance Board / UI | assets/diagrams/C3_containers/C2-02_Proof_of_Contribution.mmd<br />assets/diagrams/C3_containers/C2-03_Governance_DAO_Service.mmd<br />assets/diagrams/C3_containers/C2-05_Identity_Reputation_PoCI.mmd<br />assets/diagrams/C3_containers/C2-06_Local_Hub_Federation_Service.mmd<br />assets/diagrams/C3_containers/C2-07_Resonance_Metric_Stack.mmd<br />assets/diagrams/C3_containers/C2-08_Manifesto_Ethics_Guard_Service.mmd<br />assets/diagrams/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd<br />assets/diagrams/C3_containers/C2-10_Security_Audit_Layer.mmd
C2-07 Metrics / Analytics | assets/diagrams/C3_containers/C2-01_Resonance_Service.mmd.mmd<br />assets/diagrams/C3_containers/C2-03_Governance_DAO_Service.mmd<br />assets/diagrams/C3_containers/C2-04_Treasury_Funding_Service.mmd<br />assets/diagrams/C3_containers/C2-05_Identity_Reputation_PoCI.mmd<br />assets/diagrams/C3_containers/C2-06_Local_Hub_Federation_Service.mmd<br />assets/diagrams/C3_containers/C2-08_Manifesto_Ethics_Guard_Service.mmd<br />assets/diagrams/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd<br />assets/diagrams/C3_containers/C2-10_Security_Audit_Layer.mmd
C2-03 Governance &amp; DAO | assets/diagrams/C3_containers/C2-10_Security_Audit_Layer.mmd<br />assets/diagrams/C3_containers/C2-12_Resonance_Board_UI.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-10_Security_Audit_Layer.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-12_Resonance_Board_UI.mmd
C2-04 Treasury &amp; Funding | assets/diagrams/C3_containers/C2-03_Governance_DAO_Service.mmd<br />assets/diagrams/C3_containers/C2-06_Local_Hub_Federation_Service.mmd<br />assets/diagrams/C3_containers/C2-10_Security_Audit_Layer.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-03_Governance_DAO_Service.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-06_Local_Hub_Federation_Service.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-10_Security_Audit_Layer.mmd
C2-07 Resonance Metric Stack / Analytics | assets/diagrams/C3_containers/C2-07_Resonance_Metric_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-07_Resonance_Metric_Stack.mmd
C3-07.01 Stream Ingest (Events &amp; Signals) | assets/diagrams/C3_containers/C2-07_Resonance_Metric_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-07_Resonance_Metric_Stack.mmd
C3-07.02 KPI Aggregator (A_j, R_j, CP_i, W_i) | assets/diagrams/C3_containers/C2-07_Resonance_Metric_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-07_Resonance_Metric_Stack.mmd
C3-07.03 Systemic Resonance Index (SRI Engine) | assets/diagrams/C3_containers/C2-07_Resonance_Metric_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-07_Resonance_Metric_Stack.mmd
C3-07.04 Feature Store (Derived Metrics) | assets/diagrams/C3_containers/C2-07_Resonance_Metric_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-07_Resonance_Metric_Stack.mmd
C3-07.05 Anomaly Detector | assets/diagrams/C3_containers/C2-07_Resonance_Metric_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-07_Resonance_Metric_Stack.mmd
C3-07.06 Dashboard Feed / Stream API | assets/diagrams/C3_containers/C2-07_Resonance_Metric_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-07_Resonance_Metric_Stack.mmd
C3-07.07 Metrics Data Store | assets/diagrams/C3_containers/C2-07_Resonance_Metric_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-07_Resonance_Metric_Stack.mmd
C3-07.08 Batch Snapshot Worker | assets/diagrams/C3_containers/C2-07_Resonance_Metric_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-07_Resonance_Metric_Stack.mmd
C2-01 Resonance Service | assets/diagrams/C3_containers/C2-01_Resonance_Service.mmd.mmd<br />assets/diagrams/C3_containers/C2-02_Proof_of_Contribution.mmd<br />assets/diagrams/C3_containers/C2-07_Resonance_Metric_Stack.mmd<br />assets/diagrams/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd<br />assets/diagrams/C3_containers/C2-12_Resonance_Board_UI.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-01_Resonance_Service.mmd.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-02_Proof_of_Contribution.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-07_Resonance_Metric_Stack.mmd
C2-02 PoC Service | assets/diagrams/C3_containers/C2-01_Resonance_Service.mmd.mmd<br />assets/diagrams/C3_containers/C2-03_Governance_DAO_Service.mmd<br />assets/diagrams/C3_containers/C2-04_Treasury_Funding_Service.mmd<br />assets/diagrams/C3_containers/C2-05_Identity_Reputation_PoCI.mmd<br />assets/diagrams/C3_containers/C2-07_Resonance_Metric_Stack.mmd<br />assets/diagrams/C3_containers/C2-08_Manifesto_Ethics_Guard_Service.mmd<br />assets/diagrams/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd<br />assets/diagrams/C3_containers/C2-11_Public_API_Gateway.mmd
C2-03 Governance | assets/diagrams/C3_containers/C2-02_Proof_of_Contribution.mmd<br />assets/diagrams/C3_containers/C2-07_Resonance_Metric_Stack.mmd<br />assets/diagrams/C3_containers/C2-11_Public_API_Gateway.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-02_Proof_of_Contribution.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-07_Resonance_Metric_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-11_Public_API_Gateway.mmd
C2-04 Treasury | assets/diagrams/C3_containers/C2-07_Resonance_Metric_Stack.mmd<br />assets/diagrams/C3_containers/C2-11_Public_API_Gateway.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-07_Resonance_Metric_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-11_Public_API_Gateway.mmd
C2-06 Local Hubs | assets/diagrams/C3_containers/C2-07_Resonance_Metric_Stack.mmd<br />assets/diagrams/C3_containers/C2-11_Public_API_Gateway.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-07_Resonance_Metric_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-11_Public_API_Gateway.mmd
C2-08 Manifesto &amp; Ethics Guard | assets/diagrams/C3_containers/C2-02_Proof_of_Contribution.mmd<br />assets/diagrams/C3_containers/C2-03_Governance_DAO_Service.mmd<br />assets/diagrams/C3_containers/C2-05_Identity_Reputation_PoCI.mmd<br />assets/diagrams/C3_containers/C2-07_Resonance_Metric_Stack.mmd<br />assets/diagrams/C3_containers/C2-08_Manifesto_Ethics_Guard_Service.mmd<br />assets/diagrams/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd<br />assets/diagrams/C3_containers/C2-12_Resonance_Board_UI.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-02_Proof_of_Contribution.mmd
C2-10 Security &amp; Audit | assets/diagrams/C3_containers/C2-02_Proof_of_Contribution.mmd<br />assets/diagrams/C3_containers/C2-03_Governance_DAO_Service.mmd<br />assets/diagrams/C3_containers/C2-06_Local_Hub_Federation_Service.mmd<br />assets/diagrams/C3_containers/C2-07_Resonance_Metric_Stack.mmd<br />assets/diagrams/C3_containers/C2-08_Manifesto_Ethics_Guard_Service.mmd<br />assets/diagrams/C3_containers/C2-11_Public_API_Gateway.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-02_Proof_of_Contribution.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-03_Governance_DAO_Service.mmd
C2-04 Treasury &amp; Funding Service | assets/diagrams/C3_containers/C2-04_Treasury_Funding_Service.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-04_Treasury_Funding_Service.mmd
C3-04.01 Quadratic Funding Engine | assets/diagrams/C3_containers/C2-04_Treasury_Funding_Service.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-04_Treasury_Funding_Service.mmd
C3-04.02 Payout Orchestrator | assets/diagrams/C3_containers/C2-04_Treasury_Funding_Service.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-04_Treasury_Funding_Service.mmd
C3-04.03 Reserve Manager | assets/diagrams/C3_containers/C2-04_Treasury_Funding_Service.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-04_Treasury_Funding_Service.mmd
C3-04.04 Compliance &amp; Risk Checks | assets/diagrams/C3_containers/C2-04_Treasury_Funding_Service.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-04_Treasury_Funding_Service.mmd
C3-04.05 Escrow Processor | assets/diagrams/C3_containers/C2-04_Treasury_Funding_Service.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-04_Treasury_Funding_Service.mmd
C3-04.06 On-Chain Adapter (Tx Bridge) | assets/diagrams/C3_containers/C2-04_Treasury_Funding_Service.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-04_Treasury_Funding_Service.mmd
C3-04.07 Treasury Ledger / DB | assets/diagrams/C3_containers/C2-04_Treasury_Funding_Service.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-04_Treasury_Funding_Service.mmd
C3-04.08 Event Publisher (Funding Signals) | assets/diagrams/C3_containers/C2-04_Treasury_Funding_Service.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-04_Treasury_Funding_Service.mmd
C2-03 Governance Service | assets/diagrams/C3_containers/C2-04_Treasury_Funding_Service.mmd<br />assets/diagrams/C3_containers/C2-05_Identity_Reputation_PoCI.mmd<br />assets/diagrams/C3_containers/C2-06_Local_Hub_Federation_Service.mmd<br />assets/diagrams/C3_containers/C2-08_Manifesto_Ethics_Guard_Service.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-04_Treasury_Funding_Service.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-05_Identity_Reputation_PoCI.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-06_Local_Hub_Federation_Service.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-08_Manifesto_Ethics_Guard_Service.mmd
C2-05 Identity (PoCI) | assets/diagrams/C3_containers/C2-02_Proof_of_Contribution.mmd<br />assets/diagrams/C3_containers/C2-03_Governance_DAO_Service.mmd<br />assets/diagrams/C3_containers/C2-04_Treasury_Funding_Service.mmd<br />assets/diagrams/C3_containers/C2-08_Manifesto_Ethics_Guard_Service.mmd<br />assets/diagrams/C3_containers/C2-11_Public_API_Gateway.mmd<br />assets/diagrams/C3_containers/C2-12_Resonance_Board_UI.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-02_Proof_of_Contribution.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-03_Governance_DAO_Service.mmd
C1-06 Bitcoin / Hard Asset Layer | assets/diagrams/C3_containers/C2-04_Treasury_Funding_Service.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-04_Treasury_Funding_Service.mmd
C2-06 Local Hub / Federation | assets/diagrams/C3_containers/C2-04_Treasury_Funding_Service.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-04_Treasury_Funding_Service.mmd
C3-11.01 Smart Router (REST/gRPC) | assets/diagrams/C3_containers/C2-11_Public_API_Gateway.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-11_Public_API_Gateway.mmd
C3-11.02 GraphQL Federation | assets/diagrams/C3_containers/C2-11_Public_API_Gateway.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-11_Public_API_Gateway.mmd
C3-11.03 Auth Hub (Tokens, Sessions) | assets/diagrams/C3_containers/C2-11_Public_API_Gateway.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-11_Public_API_Gateway.mmd
C3-11.04 Rate &amp; Quota Manager | assets/diagrams/C3_containers/C2-11_Public_API_Gateway.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-11_Public_API_Gateway.mmd
C3-11.05 Schema Guard &amp; Policy Validator | assets/diagrams/C3_containers/C2-11_Public_API_Gateway.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-11_Public_API_Gateway.mmd
C3-11.06 Telemetry Collector | assets/diagrams/C3_containers/C2-11_Public_API_Gateway.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-11_Public_API_Gateway.mmd
C3-11.07 Developer Portal (Docs, Keys) | assets/diagrams/C3_containers/C2-11_Public_API_Gateway.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-11_Public_API_Gateway.mmd
C3-11.08 API Log Store | assets/diagrams/C3_containers/C2-11_Public_API_Gateway.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-11_Public_API_Gateway.mmd
C3-11.09 Event Publisher (API Metrics) | assets/diagrams/C3_containers/C2-11_Public_API_Gateway.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-11_Public_API_Gateway.mmd
C1-07 Developers / Architects | assets/diagrams/C3_containers/C2-11_Public_API_Gateway.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-11_Public_API_Gateway.mmd
C2-01 Resonance | assets/diagrams/C3_containers/C2-11_Public_API_Gateway.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-11_Public_API_Gateway.mmd
C2-08 Ethics Guard | assets/diagrams/C3_containers/C2-01_Resonance_Service.mmd.mmd<br />assets/diagrams/C3_containers/C2-11_Public_API_Gateway.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-01_Resonance_Service.mmd.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-11_Public_API_Gateway.mmd
C2-09 Knowledge Graph | assets/diagrams/C3_containers/C2-06_Local_Hub_Federation_Service.mmd<br />assets/diagrams/C3_containers/C2-08_Manifesto_Ethics_Guard_Service.mmd<br />assets/diagrams/C3_containers/C2-11_Public_API_Gateway.mmd<br />assets/diagrams/C3_containers/C2-12_Resonance_Board_UI.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-06_Local_Hub_Federation_Service.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-08_Manifesto_Ethics_Guard_Service.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-11_Public_API_Gateway.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-12_Resonance_Board_UI.mmd
C2-03 Governance &amp; DAO Service | assets/diagrams/C3_containers/C2-03_Governance_DAO_Service.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-03_Governance_DAO_Service.mmd
C3-03.01 Proposal Engine | assets/diagrams/C3_containers/C2-03_Governance_DAO_Service.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-03_Governance_DAO_Service.mmd
C3-03.02 Quorum &amp; Threshold Logic | assets/diagrams/C3_containers/C2-03_Governance_DAO_Service.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-03_Governance_DAO_Service.mmd
C3-03.03 Voting Service | assets/diagrams/C3_containers/C2-03_Governance_DAO_Service.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-03_Governance_DAO_Service.mmd
C3-03.04 Execution Manager | assets/diagrams/C3_containers/C2-03_Governance_DAO_Service.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-03_Governance_DAO_Service.mmd
C3-03.05 Parameter Versioning (λ, α, q, θ) | assets/diagrams/C3_containers/C2-03_Governance_DAO_Service.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-03_Governance_DAO_Service.mmd
C3-03.06 Audit Trail Writer | assets/diagrams/C3_containers/C2-03_Governance_DAO_Service.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-03_Governance_DAO_Service.mmd
C2-06 Local Hub / Federation Service | assets/diagrams/C3_containers/C2-06_Local_Hub_Federation_Service.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-06_Local_Hub_Federation_Service.mmd
C3-06.01 Sync Orchestrator | assets/diagrams/C3_containers/C2-06_Local_Hub_Federation_Service.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-06_Local_Hub_Federation_Service.mmd
C3-06.02 CRDT Resolver | assets/diagrams/C3_containers/C2-06_Local_Hub_Federation_Service.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-06_Local_Hub_Federation_Service.mmd
C3-06.03 Project Registry | assets/diagrams/C3_containers/C2-06_Local_Hub_Federation_Service.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-06_Local_Hub_Federation_Service.mmd
C3-06.04 Federation Client (Bus/Signals) | assets/diagrams/C3_containers/C2-06_Local_Hub_Federation_Service.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-06_Local_Hub_Federation_Service.mmd
C3-06.05 Health &amp; Telemetry Monitor | assets/diagrams/C3_containers/C2-06_Local_Hub_Federation_Service.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-06_Local_Hub_Federation_Service.mmd
C3-06.06 Edge Store (Local State) | assets/diagrams/C3_containers/C2-06_Local_Hub_Federation_Service.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-06_Local_Hub_Federation_Service.mmd
C1-05 Local Communities / Institutions | assets/diagrams/C3_containers/C2-06_Local_Hub_Federation_Service.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-06_Local_Hub_Federation_Service.mmd
C2-09 Knowledge Graph / Collective Intelligence | assets/diagrams/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd
C3-09.01 Ontology Manager | assets/diagrams/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd
C3-09.02 Graph Ingest Pipeline | assets/diagrams/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd
C3-09.03 Embedding Generator | assets/diagrams/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd
C3-09.04 RAG Orchestrator | assets/diagrams/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd
C3-09.05 Synthesis Engine | assets/diagrams/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd
C3-09.06 KG-Store (Graph DB) | assets/diagrams/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd
C3-09.07 Vector-DB | assets/diagrams/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd
C3-09.08 Knowledge Event Publisher | assets/diagrams/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd
C2-06 Local Hubs / Projects | assets/diagrams/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd
C3-01.01 API Controller | assets/diagrams/C3_containers/C2-01_Resonance_Service.mmd.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-01_Resonance_Service.mmd.mmd
C3-01.02 Schema &amp; Policy Guard | assets/diagrams/C3_containers/C2-01_Resonance_Service.mmd.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-01_Resonance_Service.mmd.mmd
C3-01.03 Command Handler | assets/diagrams/C3_containers/C2-01_Resonance_Service.mmd.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-01_Resonance_Service.mmd.mmd
C3-01.04 Resonance Engine (R = I × A × e^(−λΔt)) | assets/diagrams/C3_containers/C2-01_Resonance_Service.mmd.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-01_Resonance_Service.mmd.mmd
C3-01.05 Sublinear Mapper (W = CP^α) | assets/diagrams/C3_containers/C2-01_Resonance_Service.mmd.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-01_Resonance_Service.mmd.mmd
C3-01.06 Anomaly Detector | assets/diagrams/C3_containers/C2-01_Resonance_Service.mmd.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-01_Resonance_Service.mmd.mmd
C3-01.07 Recompute Worker (batch decay/snapshots) | assets/diagrams/C3_containers/C2-01_Resonance_Service.mmd.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-01_Resonance_Service.mmd.mmd
C3-01.08 Event Publisher | assets/diagrams/C3_containers/C2-01_Resonance_Service.mmd.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-01_Resonance_Service.mmd.mmd
Snapshot Store | assets/diagrams/C3_containers/C2-01_Resonance_Service.mmd.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-01_Resonance_Service.mmd.mmd
C2-05 Identity &amp; Reputation Service (PoCI) | assets/diagrams/C3_containers/C2-05_Identity_Reputation_PoCI.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-05_Identity_Reputation_PoCI.mmd
C3-05.01 DID Manager | assets/diagrams/C3_containers/C2-05_Identity_Reputation_PoCI.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-05_Identity_Reputation_PoCI.mmd
C3-05.02 Credential Issuer (VC / SBT) | assets/diagrams/C3_containers/C2-05_Identity_Reputation_PoCI.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-05_Identity_Reputation_PoCI.mmd
C3-05.03 Reputation Graph | assets/diagrams/C3_containers/C2-05_Identity_Reputation_PoCI.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-05_Identity_Reputation_PoCI.mmd
C3-05.04 Sybil Resistance Evaluator | assets/diagrams/C3_containers/C2-05_Identity_Reputation_PoCI.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-05_Identity_Reputation_PoCI.mmd
C3-05.05 Verifier / Attestation Checker | assets/diagrams/C3_containers/C2-05_Identity_Reputation_PoCI.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-05_Identity_Reputation_PoCI.mmd
C3-05.06 Attestation Registry | assets/diagrams/C3_containers/C2-05_Identity_Reputation_PoCI.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-05_Identity_Reputation_PoCI.mmd
C3-05.07 PoCI Data Store | assets/diagrams/C3_containers/C2-05_Identity_Reputation_PoCI.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-05_Identity_Reputation_PoCI.mmd
C3-05.08 Reputation Event Publisher | assets/diagrams/C3_containers/C2-05_Identity_Reputation_PoCI.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-05_Identity_Reputation_PoCI.mmd
C3-08.02 Rubric Manager (versioning) | assets/diagrams/C3_containers/C2-08_Manifesto_Ethics_Guard_Service.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-08_Manifesto_Ethics_Guard_Service.mmd
C3-08.01 Alignment Evaluator | assets/diagrams/C3_containers/C2-08_Manifesto_Ethics_Guard_Service.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-08_Manifesto_Ethics_Guard_Service.mmd
C3-08.03 Ethics Policy Engine (allow/deny) | assets/diagrams/C3_containers/C2-08_Manifesto_Ethics_Guard_Service.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-08_Manifesto_Ethics_Guard_Service.mmd
C3-08.04 Attestation Issuer | assets/diagrams/C3_containers/C2-08_Manifesto_Ethics_Guard_Service.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-08_Manifesto_Ethics_Guard_Service.mmd
C3-08.05 Appeals Handler / Re-evaluation | assets/diagrams/C3_containers/C2-08_Manifesto_Ethics_Guard_Service.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-08_Manifesto_Ethics_Guard_Service.mmd
C3-08.06 Ethics Data Store | assets/diagrams/C3_containers/C2-08_Manifesto_Ethics_Guard_Service.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-08_Manifesto_Ethics_Guard_Service.mmd
C3-08.07 Governance Guidance Feed | assets/diagrams/C3_containers/C2-08_Manifesto_Ethics_Guard_Service.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-08_Manifesto_Ethics_Guard_Service.mmd
C2-02 Proof-of-Contribution (PoC) Service | assets/diagrams/C3_containers/C2-02_Proof_of_Contribution.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-02_Proof_of_Contribution.mmd
C3-02.01 API Controller | assets/diagrams/C3_containers/C2-02_Proof_of_Contribution.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-02_Proof_of_Contribution.mmd
C3-02.02 Schema &amp; Policy Guard | assets/diagrams/C3_containers/C2-02_Proof_of_Contribution.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-02_Proof_of_Contribution.mmd
C3-02.03 Contribution Normalizer | assets/diagrams/C3_containers/C2-02_Proof_of_Contribution.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-02_Proof_of_Contribution.mmd
C3-02.04 Alignment &amp; Impact Intake | assets/diagrams/C3_containers/C2-02_Proof_of_Contribution.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-02_Proof_of_Contribution.mmd
C3-02.05 Time Decay Updater (λ) | assets/diagrams/C3_containers/C2-02_Proof_of_Contribution.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-02_Proof_of_Contribution.mmd
C3-02.06 Contribution Accumulator (CP) | assets/diagrams/C3_containers/C2-02_Proof_of_Contribution.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-02_Proof_of_Contribution.mmd
C3-02.07 Voting Weight Mapper (W = CP^α) | assets/diagrams/C3_containers/C2-02_Proof_of_Contribution.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-02_Proof_of_Contribution.mmd
C3-02.08 PoC Ledger (Immutable) | assets/diagrams/C3_containers/C2-02_Proof_of_Contribution.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-02_Proof_of_Contribution.mmd
C3-02.09 Snapshotter &amp; Recompute Worker | assets/diagrams/C3_containers/C2-02_Proof_of_Contribution.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-02_Proof_of_Contribution.mmd
C3-02.10 Reconciliation &amp; Oracles | assets/diagrams/C3_containers/C2-02_Proof_of_Contribution.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-02_Proof_of_Contribution.mmd
C3-02.11 Sybil / Spam Guard | assets/diagrams/C3_containers/C2-02_Proof_of_Contribution.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-02_Proof_of_Contribution.mmd
C3-02.12 Events &amp; Exports | assets/diagrams/C3_containers/C2-02_Proof_of_Contribution.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-02_Proof_of_Contribution.mmd
C1-02 Member / Contributor | assets/diagrams/C3_containers/C2-02_Proof_of_Contribution.mmd<br />assets/diagrams/C3_containers/C2-12_Resonance_Board_UI.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-02_Proof_of_Contribution.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-12_Resonance_Board_UI.mmd
C2-06 Local Hub Adapter | assets/diagrams/C3_containers/C2-02_Proof_of_Contribution.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-02_Proof_of_Contribution.mmd
C2-07 Metrics / SRI | assets/diagrams/C3_containers/C2-02_Proof_of_Contribution.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-02_Proof_of_Contribution.mmd
External Oracles / Repos | assets/diagrams/C3_containers/C2-02_Proof_of_Contribution.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-02_Proof_of_Contribution.mmd
C3-12.01 Dashboard Renderer | assets/diagrams/C3_containers/C2-12_Resonance_Board_UI.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-12_Resonance_Board_UI.mmd
C3-12.02 Live Stream Client | assets/diagrams/C3_containers/C2-12_Resonance_Board_UI.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-12_Resonance_Board_UI.mmd
C3-12.03 Identity / Wallet Adapter | assets/diagrams/C3_containers/C2-12_Resonance_Board_UI.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-12_Resonance_Board_UI.mmd
C3-12.04 Workbench (Interaction Tools) | assets/diagrams/C3_containers/C2-12_Resonance_Board_UI.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-12_Resonance_Board_UI.mmd
C3-12.05 Accessibility &amp; i18n Layer | assets/diagrams/C3_containers/C2-12_Resonance_Board_UI.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-12_Resonance_Board_UI.mmd
C3-12.06 Local Cache / State Store | assets/diagrams/C3_containers/C2-12_Resonance_Board_UI.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-12_Resonance_Board_UI.mmd
C3-12.07 Notification &amp; Alert Manager | assets/diagrams/C3_containers/C2-12_Resonance_Board_UI.mmd<br />docs.coherosphere.io/static/assets/diagrams/C3_containers/C2-12_Resonance_Board_UI.mmd

## C4

Term | Sources
---|---
Clients (Internet) | assets/diagrams/C4_deployment/C4_Deployment_View.mmd
Web App — app.coherosphere.com | assets/diagrams/C4_deployment/C4_Deployment_View.mmd
Contributor Tools (CLI/API) | assets/diagrams/C4_deployment/C4_Deployment_View.mmd
User Wallet / Keys (non-custodial) | assets/diagrams/C4_deployment/C4_Deployment_View.mmd
Edge / Access | assets/diagrams/C4_deployment/C4_Deployment_View.mmd
Auth Gateway (OIDC) | assets/diagrams/C4_deployment/C4_Deployment_View.mmd
WAF / CDN | assets/diagrams/C4_deployment/C4_Deployment_View.mmd
Microservices | assets/diagrams/C4_deployment/C4_Deployment_View.mmd
Resonance Service | assets/diagrams/C4_deployment/C4_Deployment_View.mmd
Proposal Service | assets/diagrams/C4_deployment/C4_Deployment_View.mmd
Funding Service | assets/diagrams/C4_deployment/C4_Deployment_View.mmd
Identity Aggregator (PoCI) | assets/diagrams/C4_deployment/C4_Deployment_View.mmd
Guardian / Policy Service | assets/diagrams/C4_deployment/C4_Deployment_View.mmd
Anomaly Service | assets/diagrams/C4_deployment/C4_Deployment_View.mmd
Metrics / SRI Service | assets/diagrams/C4_deployment/C4_Deployment_View.mmd
Cohere Cloud (Prod) | assets/diagrams/C4_deployment/C4_Deployment_View.mmd
API Gateway — api.coherosphere.io | assets/diagrams/C4_deployment/C4_Deployment_View.mmd
Operational DB (HA) | assets/diagrams/C4_deployment/C4_Deployment_View.mmd
Analytics Lake / Warehouse | assets/diagrams/C4_deployment/C4_Deployment_View.mmd
Audit Mirror (immutable-like) | assets/diagrams/C4_deployment/C4_Deployment_View.mmd
Monitoring / Alerts | assets/diagrams/C4_deployment/C4_Deployment_View.mmd
Public Blockchain (Mainnet) | assets/diagrams/C4_deployment/C4_Deployment_View.mmd
Governance SCs | assets/diagrams/C4_deployment/C4_Deployment_View.mmd
Treasury SCs | assets/diagrams/C4_deployment/C4_Deployment_View.mmd
Identity / PoCI SCs | assets/diagrams/C4_deployment/C4_Deployment_View.mmd
Meta-Gov SCs | assets/diagrams/C4_deployment/C4_Deployment_View.mmd
On-chain Logs | assets/diagrams/C4_deployment/C4_Deployment_View.mmd
External Infra | assets/diagrams/C4_deployment/C4_Deployment_View.mmd
IPFS / Pinning (artifacts) | assets/diagrams/C4_deployment/C4_Deployment_View.mmd
BTC / Stable Reserve (treasury base) | assets/diagrams/C4_deployment/C4_Deployment_View.mmd
Local Hubs / Field Nodes | assets/diagrams/C4_deployment/C4_Deployment_View.mmd
Hub Node (local cache, chain sync) | assets/diagrams/C4_deployment/C4_Deployment_View.mmd
Hub Ops (programs, events) | assets/diagrams/C4_deployment/C4_Deployment_View.mmd

## DDD

Term | Sources
---|---
Governance BC ⟷ C2-03 Governance &amp; DAO Service | assets/diagrams/ddd/DDD_Domain_Context_Map.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Domain_Context_Map.mmd
C2-03 Proposal &amp; Voting\n(quorum • threshold • sublinear weights) | assets/diagrams/ddd/DDD_Domain_Context_Map.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Domain_Context_Map.mmd
Contribution &amp; Evaluation BC ⟷ C2-02 PoC • C2-01 Resonance • C2-08 Ethics | assets/diagrams/ddd/DDD_Domain_Context_Map.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Domain_Context_Map.mmd
C2-02 Proof of Contribution\nR = I × A × e^(−λ·Δt)\nContribution Points CP_i | assets/diagrams/ddd/DDD_Domain_Context_Map.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Domain_Context_Map.mmd
C2-08 Resonance Filters\n(alignment checks) | assets/diagrams/ddd/DDD_Domain_Context_Map.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Domain_Context_Map.mmd
C2-01 Resonance Engine\n(weight W_i • SRI inputs) | assets/diagrams/ddd/DDD_Domain_Context_Map.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Domain_Context_Map.mmd
Identity &amp; Reputation (PoCI) BC ⟷ C2-05 Identity &amp; Reputation | assets/diagrams/ddd/DDD_Domain_Context_Map.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Domain_Context_Map.mmd
C2-05 PoCI Identity\n(reputation ledger • attestations) | assets/diagrams/ddd/DDD_Domain_Context_Map.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Domain_Context_Map.mmd
Treasury &amp; Funding BC ⟷ C2-04 Treasury &amp; Funding | assets/diagrams/ddd/DDD_Domain_Context_Map.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Domain_Context_Map.mmd
C2-04 Quadratic Funding\n(resonant allocation) | assets/diagrams/ddd/DDD_Domain_Context_Map.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Domain_Context_Map.mmd
C2-04 Treasury Reserve\n(sound money policy) | assets/diagrams/ddd/DDD_Domain_Context_Map.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Domain_Context_Map.mmd
Projects &amp; Local Hubs BC ⟷ C2-06 Local Hub / Federation | assets/diagrams/ddd/DDD_Domain_Context_Map.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Domain_Context_Map.mmd
C2-06 Projects &amp; Grants\n(lifecycle • milestones) | assets/diagrams/ddd/DDD_Domain_Context_Map.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Domain_Context_Map.mmd
C2-06 Local Hubs\n(semi-autonomous units) | assets/diagrams/ddd/DDD_Domain_Context_Map.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Domain_Context_Map.mmd
Meta-Governance &amp; Audit BC ⟷ C2-03 Governance • C2-10 Security &amp; Audit | assets/diagrams/ddd/DDD_Domain_Context_Map.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Domain_Context_Map.mmd
Rule Versioning\n(λ, α, q, θ) | assets/diagrams/ddd/DDD_Domain_Context_Map.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Domain_Context_Map.mmd
Audits &amp; Anomaly Detection | assets/diagrams/ddd/DDD_Domain_Context_Map.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Domain_Context_Map.mmd
Metrics &amp; Observability BC ⟷ C2-07 Metrics • C2-12 UI | assets/diagrams/ddd/DDD_Domain_Context_Map.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Domain_Context_Map.mmd
C2-07 KPI System\n(A_j • R_j • CP_i • W_i • SRI) | assets/diagrams/ddd/DDD_Domain_Context_Map.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Domain_Context_Map.mmd
C2-12 Resonance Board UI\n(live dashboards) | assets/diagrams/ddd/DDD_Domain_Context_Map.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Domain_Context_Map.mmd
Manifesto &amp; Ethics Guard BC ⟷ C2-08 Ethics Guard | assets/diagrams/ddd/DDD_Domain_Context_Map.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Domain_Context_Map.mmd
Knowledge Graph / Collective Intelligence BC ⟷ C2-09 Knowledge Graph | assets/diagrams/ddd/DDD_Domain_Context_Map.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Domain_Context_Map.mmd
Core Subdomains | assets/diagrams/ddd/DDD_Contract_Types_Overview.mmd<br />assets/diagrams/ddd/DDD_Subdomain_Map.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Contract_Types_Overview.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Subdomain_Map.mmd
C2-03 Governance and DAO | assets/diagrams/ddd/DDD_Contract_Types_Overview.mmd<br />assets/diagrams/ddd/DDD_Subdomain_Map.mmd<br />assets/diagrams/ddd/DDD_Team_Context_Alignment.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Contract_Types_Overview.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Subdomain_Map.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Team_Context_Alignment.mmd
C2-02 Proof of Contribution | assets/diagrams/ddd/DDD_Contract_Types_Overview.mmd<br />assets/diagrams/ddd/DDD_Subdomain_Map.mmd<br />assets/diagrams/ddd/DDD_Team_Context_Alignment.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Contract_Types_Overview.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Subdomain_Map.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Team_Context_Alignment.mmd
C2-01 Resonance Service | assets/diagrams/ddd/DDD_Contract_Types_Overview.mmd<br />assets/diagrams/ddd/DDD_Subdomain_Map.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Contract_Types_Overview.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Subdomain_Map.mmd
C2-04 Treasury and Funding | assets/diagrams/ddd/DDD_Contract_Types_Overview.mmd<br />assets/diagrams/ddd/DDD_Subdomain_Map.mmd<br />assets/diagrams/ddd/DDD_Team_Context_Alignment.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Contract_Types_Overview.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Subdomain_Map.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Team_Context_Alignment.mmd
C2-08 Manifesto and Ethics Guard | assets/diagrams/ddd/DDD_Contract_Types_Overview.mmd<br />assets/diagrams/ddd/DDD_Subdomain_Map.mmd<br />assets/diagrams/ddd/DDD_Team_Context_Alignment.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Contract_Types_Overview.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Subdomain_Map.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Team_Context_Alignment.mmd
Supporting Subdomains | assets/diagrams/ddd/DDD_Contract_Types_Overview.mmd<br />assets/diagrams/ddd/DDD_Subdomain_Map.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Contract_Types_Overview.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Subdomain_Map.mmd
C2-05 Identity and Reputation PoCI | assets/diagrams/ddd/DDD_Contract_Types_Overview.mmd<br />assets/diagrams/ddd/DDD_Subdomain_Map.mmd<br />assets/diagrams/ddd/DDD_Team_Context_Alignment.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Contract_Types_Overview.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Subdomain_Map.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Team_Context_Alignment.mmd
C2-06 Local Hub and Federation | assets/diagrams/ddd/DDD_Contract_Types_Overview.mmd<br />assets/diagrams/ddd/DDD_Subdomain_Map.mmd<br />assets/diagrams/ddd/DDD_Team_Context_Alignment.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Contract_Types_Overview.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Subdomain_Map.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Team_Context_Alignment.mmd
C2-07 Metrics and Analytics | assets/diagrams/ddd/DDD_Contract_Types_Overview.mmd<br />assets/diagrams/ddd/DDD_Subdomain_Map.mmd<br />assets/diagrams/ddd/DDD_Team_Context_Alignment.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Contract_Types_Overview.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Subdomain_Map.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Team_Context_Alignment.mmd
C2-09 Knowledge Graph and Collective Intelligence | assets/diagrams/ddd/DDD_Contract_Types_Overview.mmd<br />assets/diagrams/ddd/DDD_Subdomain_Map.mmd<br />assets/diagrams/ddd/DDD_Team_Context_Alignment.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Contract_Types_Overview.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Subdomain_Map.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Team_Context_Alignment.mmd
Generic and Infrastructure | assets/diagrams/ddd/DDD_Contract_Types_Overview.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Contract_Types_Overview.mmd
C2-11 Public API Gateway | assets/diagrams/ddd/DDD_Contract_Types_Overview.mmd<br />assets/diagrams/ddd/DDD_Subdomain_Map.mmd<br />assets/diagrams/ddd/DDD_Team_Context_Alignment.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Contract_Types_Overview.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Subdomain_Map.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Team_Context_Alignment.mmd
C2-10 Security and Audit | assets/diagrams/ddd/DDD_Contract_Types_Overview.mmd<br />assets/diagrams/ddd/DDD_Subdomain_Map.mmd<br />assets/diagrams/ddd/DDD_Team_Context_Alignment.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Contract_Types_Overview.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Subdomain_Map.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Team_Context_Alignment.mmd
C2-12 Resonance Board UI | assets/diagrams/ddd/DDD_Contract_Types_Overview.mmd<br />assets/diagrams/ddd/DDD_Subdomain_Map.mmd<br />assets/diagrams/ddd/DDD_Team_Context_Alignment.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Contract_Types_Overview.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Subdomain_Map.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Team_Context_Alignment.mmd
Legend | assets/diagrams/ddd/DDD_Contract_Types_Overview.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Contract_Types_Overview.mmd
--- Shared Kernel | assets/diagrams/ddd/DDD_Contract_Types_Overview.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Contract_Types_Overview.mmd
-. Anti Corruption Layer .-&gt; | assets/diagrams/ddd/DDD_Contract_Types_Overview.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Contract_Types_Overview.mmd
--&gt; Published Language with DDD EVT and C4 | assets/diagrams/ddd/DDD_Contract_Types_Overview.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Contract_Types_Overview.mmd
--&gt; Conformist with DDD EVT and C4 | assets/diagrams/ddd/DDD_Contract_Types_Overview.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Contract_Types_Overview.mmd
--&gt; Open Host Service | assets/diagrams/ddd/DDD_Contract_Types_Overview.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Contract_Types_Overview.mmd
Teams | assets/diagrams/ddd/DDD_Team_Context_Alignment.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Team_Context_Alignment.mmd
Governance Team\ntype Stream aligned | assets/diagrams/ddd/DDD_Team_Context_Alignment.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Team_Context_Alignment.mmd
Resonance Core Team\ntype Complicated subsystem | assets/diagrams/ddd/DDD_Team_Context_Alignment.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Team_Context_Alignment.mmd
PoC and Identity Team\ntype Stream aligned | assets/diagrams/ddd/DDD_Team_Context_Alignment.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Team_Context_Alignment.mmd
Treasury Ops Team\ntype Stream aligned | assets/diagrams/ddd/DDD_Team_Context_Alignment.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Team_Context_Alignment.mmd
Federation and Hubs Team\ntype Stream aligned | assets/diagrams/ddd/DDD_Team_Context_Alignment.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Team_Context_Alignment.mmd
Metrics and Knowledge Team\ntype Stream aligned | assets/diagrams/ddd/DDD_Team_Context_Alignment.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Team_Context_Alignment.mmd
Security and Audit Team\ntype Enabling | assets/diagrams/ddd/DDD_Team_Context_Alignment.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Team_Context_Alignment.mmd
API Gateway and UI Team\ntype Platform | assets/diagrams/ddd/DDD_Team_Context_Alignment.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Team_Context_Alignment.mmd
DevOps and Platform Eng\ntype Platform | assets/diagrams/ddd/DDD_Team_Context_Alignment.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Team_Context_Alignment.mmd
Bounded Contexts and Subdomains | assets/diagrams/ddd/DDD_Team_Context_Alignment.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Team_Context_Alignment.mmd
C2-01 Resonance | assets/diagrams/ddd/DDD_Team_Context_Alignment.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Team_Context_Alignment.mmd
Ops and Deployment Layer\nnot a C2 container | assets/diagrams/ddd/DDD_Team_Context_Alignment.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Team_Context_Alignment.mmd
Generic and Infrastructure Subdomains | assets/diagrams/ddd/DDD_Subdomain_Map.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Subdomain_Map.mmd
Ops and Deployment Layer (non C2) | assets/diagrams/ddd/DDD_Subdomain_Map.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Subdomain_Map.mmd
Bitcoin and Hard Asset Layer (external) | assets/diagrams/ddd/DDD_Subdomain_Map.mmd<br />docs.coherosphere.io/static/assets/diagrams/ddd/DDD_Subdomain_Map.mmd

## Events

Term | Sources
---|---
DDD-EVT-77 | assets/specs/events/DDD-EVT-77.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-77.json
DDD-EVT-50 | assets/specs/events/DDD-EVT-50.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-50.json
DDD-EVT-78 | assets/specs/events/DDD-EVT-78.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-78.json
DDD-EVT-73 | assets/specs/events/DDD-EVT-73.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-73.json
DDD-EVT-38 | assets/specs/events/DDD-EVT-38.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-38.json
DDD-EVT-62 | assets/specs/events/DDD-EVT-62.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-62.json
DDD-EVT-45 | assets/specs/events/DDD-EVT-45.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-45.json
DDD-EVT-03 | assets/specs/events/DDD-EVT-03.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-03.json
DDD-EVT-06 | assets/specs/events/DDD-EVT-06.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-06.json
DDD-EVT-83 | assets/specs/events/DDD-EVT-83.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-83.json
DDD-EVT-44 | assets/specs/events/DDD-EVT-44.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-44.json
DDD-EVT-74 | assets/specs/events/DDD-EVT-74.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-74.json
DDD-EVT-43 | assets/specs/events/DDD-EVT-43.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-43.json
DDD-EVT-16 | assets/specs/events/DDD-EVT-16.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-16.json
DDD-EVT-60 | assets/specs/events/DDD-EVT-60.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-60.json
DDD-EVT-10 | assets/specs/events/DDD-EVT-10.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-10.json
DDD-EVT-55 | assets/specs/events/DDD-EVT-55.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-55.json
DDD-EVT-63 | assets/specs/events/DDD-EVT-63.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-63.json
DDD-EVT-20 | assets/specs/events/DDD-EVT-20.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-20.json
DDD-EVT-21 | assets/specs/events/DDD-EVT-21.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-21.json
DDD-EVT-91 | assets/specs/events/DDD-EVT-91.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-91.json
DDD-EVT-49 | assets/specs/events/DDD-EVT-49.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-49.json
DDD-EVT-52 | assets/specs/events/DDD-EVT-52.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-52.json
DDD-EVT-59 | assets/specs/events/DDD-EVT-59.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-59.json
DDD-EVT-53 | assets/specs/events/DDD-EVT-53.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-53.json
DDD-EVT-66 | assets/specs/events/DDD-EVT-66.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-66.json
DDD-EVT-11 | assets/specs/events/DDD-EVT-11.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-11.json
DDD-EVT-79 | assets/specs/events/DDD-EVT-79.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-79.json
DDD-EVT-68 | assets/specs/events/DDD-EVT-68.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-68.json
DDD-EVT-02 | assets/specs/events/DDD-EVT-02.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-02.json
DDD-EVT-42 | assets/specs/events/DDD-EVT-42.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-42.json
DDD-EVT-28 | assets/specs/events/DDD-EVT-28.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-28.json
DDD-EVT-41 | assets/specs/events/DDD-EVT-41.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-41.json
DDD-EVT-47 | assets/specs/events/DDD-EVT-47.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-47.json
DDD-EVT-40 | assets/specs/events/DDD-EVT-40.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-40.json
DDD-EVT-04 | assets/specs/events/DDD-EVT-04.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-04.json
DDD-EVT-86 | assets/specs/events/DDD-EVT-86.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-86.json
DDD-EVT-05 | assets/specs/events/DDD-EVT-05.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-05.json
DDD-EVT-19 | assets/specs/events/DDD-EVT-19.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-19.json
DDD-EVT-18 | assets/specs/events/DDD-EVT-18.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-18.json
DDD-EVT-37 | assets/specs/events/DDD-EVT-37.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-37.json
DDD-EVT-22 | assets/specs/events/DDD-EVT-22.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-22.json
DDD-EVT-01 | assets/specs/events/DDD-EVT-01.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-01.json
DDD-EVT-90 | assets/specs/events/DDD-EVT-90.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-90.json
Coherosphere Event Schemas (v1) | assets/specs/events/README.md<br />docs.coherosphere.io/static/assets/specs/events/README.md
Index | assets/specs/events/README.md<br />docs.coherosphere.io/static/assets/specs/events/README.md
DDD-EVT-65 | assets/specs/events/DDD-EVT-65.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-65.json
DDD-EVT-14 | assets/specs/events/DDD-EVT-14.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-14.json
DDD-EVT-23 | assets/specs/events/DDD-EVT-23.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-23.json
DDD-EVT-64 | assets/specs/events/DDD-EVT-64.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-64.json
DDD-EVT-84 | assets/specs/events/DDD-EVT-84.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-84.json
DDD-EVT-35 | assets/specs/events/DDD-EVT-35.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-35.json
DDD-EVT-82 | assets/specs/events/DDD-EVT-82.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-82.json
DDD-EVT-88 | assets/specs/events/DDD-EVT-88.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-88.json
DDD-EVT-07 | assets/specs/events/DDD-EVT-07.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-07.json
DDD-EVT-08 | assets/specs/events/DDD-EVT-08.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-08.json
DDD-EVT-80 | assets/specs/events/DDD-EVT-80.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-80.json
DDD-EVT-36 | assets/specs/events/DDD-EVT-36.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-36.json
DDD-EVT-92 | assets/specs/events/DDD-EVT-92.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-92.json
DDD-EVT-72 | assets/specs/events/DDD-EVT-72.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-72.json
DDD-EVT-75 | assets/specs/events/DDD-EVT-75.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-75.json
DDD-EVT-27 | assets/specs/events/DDD-EVT-27.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-27.json
DDD-EVT-69 | assets/specs/events/DDD-EVT-69.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-69.json
DDD-EVT-61 | assets/specs/events/DDD-EVT-61.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-61.json
DDD-EVT-85 | assets/specs/events/DDD-EVT-85.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-85.json
DDD-EVT-26 | assets/specs/events/DDD-EVT-26.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-26.json
DDD-EVT-54 | assets/specs/events/DDD-EVT-54.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-54.json
DDD-EVT-87 | assets/specs/events/DDD-EVT-87.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-87.json
DDD-EVT-57 | assets/specs/events/DDD-EVT-57.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-57.json
DDD-EVT-81 | assets/specs/events/DDD-EVT-81.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-81.json
DDD-EVT-58 | assets/specs/events/DDD-EVT-58.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-58.json
DDD-EVT-17 | assets/specs/events/DDD-EVT-17.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-17.json
DDD-EVT-89 | assets/specs/events/DDD-EVT-89.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-89.json
DDD-EVT-67 | assets/specs/events/DDD-EVT-67.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-67.json
DDD-EVT-30 | assets/specs/events/DDD-EVT-30.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-30.json
DDD-EVT-71 | assets/specs/events/DDD-EVT-71.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-71.json
DDD-EVT-24 | assets/specs/events/DDD-EVT-24.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-24.json
DDD-EVT-29 | assets/specs/events/DDD-EVT-29.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-29.json
DDD-EVT-76 | assets/specs/events/DDD-EVT-76.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-76.json
DDD-EVT-70 | assets/specs/events/DDD-EVT-70.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-70.json
DDD-EVT-13 | assets/specs/events/DDD-EVT-13.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-13.json
DDD-EVT-12 | assets/specs/events/DDD-EVT-12.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-12.json
DDD-EVT-48 | assets/specs/events/DDD-EVT-48.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-48.json
DDD-EVT-51 | assets/specs/events/DDD-EVT-51.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-51.json
DDD-EVT-39 | assets/specs/events/DDD-EVT-39.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-39.json
DDD-EVT-56 | assets/specs/events/DDD-EVT-56.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-56.json
DDD-EVT-46 | assets/specs/events/DDD-EVT-46.json<br />docs.coherosphere.io/static/assets/specs/events/DDD-EVT-46.json
Ethics.AttestationIssued | assets/specs/events/ethics/AttestationIssued.v1.json<br />docs.coherosphere.io/static/assets/specs/events/ethics/AttestationIssued.v1.json
Ethics.AlignmentChecked | assets/specs/events/ethics/AlignmentChecked.v1.json<br />docs.coherosphere.io/static/assets/specs/events/ethics/AlignmentChecked.v1.json
Metrics.KPIUpdated | assets/specs/events/metrics/KPIUpdated.v1.json<br />docs.coherosphere.io/static/assets/specs/events/metrics/KPIUpdated.v1.json
Metrics.SRIComputed | assets/specs/events/metrics/SRIComputed.v1.json<br />docs.coherosphere.io/static/assets/specs/events/metrics/SRIComputed.v1.json
Common Fragments | assets/specs/events/_meta/common.json<br />docs.coherosphere.io/static/assets/specs/events/_meta/common.json
Coherosphere — Event Schemas (v2) | assets/specs/events/_meta/README.md<br />docs.coherosphere.io/static/assets/specs/events/_meta/README.md
Coherosphere Event Schemas Index | assets/specs/events/_meta/index.json<br />docs.coherosphere.io/static/assets/specs/events/_meta/index.json
Treasury.RoundClosed | assets/specs/events/treasury/RoundClosed.v1.json<br />docs.coherosphere.io/static/assets/specs/events/treasury/RoundClosed.v1.json
Treasury.StreamCreated | assets/specs/events/treasury/StreamCreated.v1.json<br />docs.coherosphere.io/static/assets/specs/events/treasury/StreamCreated.v1.json
Treasury.FundingAllocated | assets/specs/events/treasury/FundingAllocated.v1.json<br />docs.coherosphere.io/static/assets/specs/events/treasury/FundingAllocated.v1.json
Treasury.RoundOpened | assets/specs/events/treasury/RoundOpened.v1.json<br />docs.coherosphere.io/static/assets/specs/events/treasury/RoundOpened.v1.json
Resonance.ResonanceUpdated | assets/specs/events/resonance/ResonanceUpdated.v1.json<br />docs.coherosphere.io/static/assets/specs/events/resonance/ResonanceUpdated.v1.json
Security.IncidentOpened | assets/specs/events/security/IncidentOpened.v1.json<br />docs.coherosphere.io/static/assets/specs/events/security/IncidentOpened.v1.json
Security.TransparencyReportPublished | assets/specs/events/security/TransparencyReportPublished.v1.json<br />docs.coherosphere.io/static/assets/specs/events/security/TransparencyReportPublished.v1.json
PoC.CPUpdated | assets/specs/events/poc/CPUpdated.v1.json<br />docs.coherosphere.io/static/assets/specs/events/poc/CPUpdated.v1.json
PoC.ContributionSubmitted | assets/specs/events/poc/ContributionSubmitted.v1.json<br />docs.coherosphere.io/static/assets/specs/events/poc/ContributionSubmitted.v1.json
Hubs.ProjectCreated | assets/specs/events/hubs/ProjectCreated.v1.json<br />docs.coherosphere.io/static/assets/specs/events/hubs/ProjectCreated.v1.json
Hubs.SyncMerged | assets/specs/events/hubs/SyncMerged.v1.json<br />docs.coherosphere.io/static/assets/specs/events/hubs/SyncMerged.v1.json
Hubs.MilestoneReported | assets/specs/events/hubs/MilestoneReported.v1.json<br />docs.coherosphere.io/static/assets/specs/events/hubs/MilestoneReported.v1.json
Gov.VoteCast | assets/specs/events/gov/VoteCast.v1.json<br />docs.coherosphere.io/static/assets/specs/events/gov/VoteCast.v1.json
Gov.DecisionRecorded | assets/specs/events/gov/DecisionRecorded.v1.json<br />docs.coherosphere.io/static/assets/specs/events/gov/DecisionRecorded.v1.json
Gov.PolicyChanged | assets/specs/events/gov/PolicyChanged.v1.json<br />docs.coherosphere.io/static/assets/specs/events/gov/PolicyChanged.v1.json
Gov.ProposalCreated | assets/specs/events/gov/ProposalCreated.v1.json<br />docs.coherosphere.io/static/assets/specs/events/gov/ProposalCreated.v1.json

## Other

Term | Sources
---|---
OpenAPI Specs — Fixed Headers Bundle | README_FIX_OPENAPI.md
API Domain Validation (v2.0) | README_API_Domain_Validation.md
Purpose | README_API_Domain_Validation.md
Validation Workflow | README_API_Domain_Validation.md
1. Configuration Files | README_API_Domain_Validation.md
2. Approved Domains | README_API_Domain_Validation.md
3. Validation Logic | README_API_Domain_Validation.md
4. GitHub Workflow | README_API_Domain_Validation.md
5. Local Testing | README_API_Domain_Validation.md
6. Related Components | README_API_Domain_Validation.md
7. Summary | README_API_Domain_Validation.md
Coherosphere — Architecture Repository | README.md
1. Structure | README.md
2. Related Repositories | README.md
3. Core Models and Artifacts | README.md
4. Design Principles | README.md
5. Validation and CI | README.md
6. Build and Reproduction | README.md
7. Deployment Domains | README.md
8. License and Attribution | README.md
9. Connect | README.md
OpenAPI Domain Validation (CI) | README_OpenAPI_Domain_Validation.md
OpenAPI Domain Fix Kit | scripts/README_FIX_OPENAPI.md
Usage | assets/config/cors/README.md<br />c4_schema_alignment/README.md<br />docs.coherosphere.io/static/assets/config/cors/README.md<br />scripts/README_FIX_OPENAPI.md
A JSON report will be written to ./openapi_domain_fix_report.json | scripts/README_FIX_OPENAPI.md
Dry-run | scripts/README_FIX_OPENAPI.md
Commit | scripts/README_FIX_OPENAPI.md
C4 ↔ DDD Event Schema Alignment Validator | c4_schema_alignment/README.md
Optional strict mode | c4_schema_alignment/README.md
Coherosphere — Canonical Domain Configuration (FINAL) | assets/specs/Canonical-Domain-Manifest.md<br />docs.coherosphere.io/static/assets/specs/Canonical-Domain-Manifest.md
Landing / Marketing | assets/specs/Canonical-Domain-Manifest.md<br />docs.coherosphere.io/static/assets/specs/Canonical-Domain-Manifest.md
App Layer | assets/specs/Canonical-Domain-Manifest.md<br />docs.coherosphere.io/static/assets/specs/Canonical-Domain-Manifest.md
Docs Layer | assets/specs/Canonical-Domain-Manifest.md<br />docs.coherosphere.io/static/assets/specs/Canonical-Domain-Manifest.md
API Layer | assets/specs/Canonical-Domain-Manifest.md<br />docs.coherosphere.io/static/assets/specs/Canonical-Domain-Manifest.md
Reserved (optional) | assets/specs/Canonical-Domain-Manifest.md<br />docs.coherosphere.io/static/assets/specs/Canonical-Domain-Manifest.md
README Patch Hints (Domains) | assets/specs/README-Patch-Hints.md<br />docs.coherosphere.io/static/assets/specs/README-Patch-Hints.md
Governance BC ⟷ C2-03 Governance &amp; DAO Service | assets/.mermaid_clean/ddd/DDD_Domain_Context_Map.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Domain_Context_Map.mmd
C2-03 Proposal &amp; Voting\n(quorum • threshold • sublinear weights) | assets/.mermaid_clean/ddd/DDD_Domain_Context_Map.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Domain_Context_Map.mmd
Contribution &amp; Evaluation BC ⟷ C2-02 PoC • C2-01 Resonance • C2-08 Ethics | assets/.mermaid_clean/ddd/DDD_Domain_Context_Map.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Domain_Context_Map.mmd
C2-02 Proof of Contribution\nR = I × A × e^(−λ·Δt)\nContribution Points CP_i | assets/.mermaid_clean/ddd/DDD_Domain_Context_Map.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Domain_Context_Map.mmd
C2-08 Resonance Filters\n(alignment checks) | assets/.mermaid_clean/ddd/DDD_Domain_Context_Map.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Domain_Context_Map.mmd
C2-01 Resonance Engine\n(weight W_i • SRI inputs) | assets/.mermaid_clean/ddd/DDD_Domain_Context_Map.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Domain_Context_Map.mmd
Identity &amp; Reputation (PoCI) BC ⟷ C2-05 Identity &amp; Reputation | assets/.mermaid_clean/ddd/DDD_Domain_Context_Map.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Domain_Context_Map.mmd
C2-05 PoCI Identity\n(reputation ledger • attestations) | assets/.mermaid_clean/ddd/DDD_Domain_Context_Map.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Domain_Context_Map.mmd
Treasury &amp; Funding BC ⟷ C2-04 Treasury &amp; Funding | assets/.mermaid_clean/ddd/DDD_Domain_Context_Map.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Domain_Context_Map.mmd
C2-04 Quadratic Funding\n(resonant allocation) | assets/.mermaid_clean/ddd/DDD_Domain_Context_Map.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Domain_Context_Map.mmd
C2-04 Treasury Reserve\n(sound money policy) | assets/.mermaid_clean/ddd/DDD_Domain_Context_Map.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Domain_Context_Map.mmd
Projects &amp; Local Hubs BC ⟷ C2-06 Local Hub / Federation | assets/.mermaid_clean/ddd/DDD_Domain_Context_Map.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Domain_Context_Map.mmd
C2-06 Projects &amp; Grants\n(lifecycle • milestones) | assets/.mermaid_clean/ddd/DDD_Domain_Context_Map.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Domain_Context_Map.mmd
C2-06 Local Hubs\n(semi-autonomous units) | assets/.mermaid_clean/ddd/DDD_Domain_Context_Map.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Domain_Context_Map.mmd
Meta-Governance &amp; Audit BC ⟷ C2-03 Governance • C2-10 Security &amp; Audit | assets/.mermaid_clean/ddd/DDD_Domain_Context_Map.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Domain_Context_Map.mmd
Rule Versioning\n(λ, α, q, θ) | assets/.mermaid_clean/ddd/DDD_Domain_Context_Map.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Domain_Context_Map.mmd
Audits &amp; Anomaly Detection | assets/.mermaid_clean/ddd/DDD_Domain_Context_Map.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Domain_Context_Map.mmd
Metrics &amp; Observability BC ⟷ C2-07 Metrics • C2-12 UI | assets/.mermaid_clean/ddd/DDD_Domain_Context_Map.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Domain_Context_Map.mmd
C2-07 KPI System\n(A_j • R_j • CP_i • W_i • SRI) | assets/.mermaid_clean/ddd/DDD_Domain_Context_Map.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Domain_Context_Map.mmd
C2-12 Resonance Board UI\n(live dashboards) | assets/.mermaid_clean/ddd/DDD_Domain_Context_Map.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Domain_Context_Map.mmd
Manifesto &amp; Ethics Guard BC ⟷ C2-08 Ethics Guard | assets/.mermaid_clean/ddd/DDD_Domain_Context_Map.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Domain_Context_Map.mmd
Knowledge Graph / Collective Intelligence BC ⟷ C2-09 Knowledge Graph | assets/.mermaid_clean/ddd/DDD_Domain_Context_Map.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Domain_Context_Map.mmd
Core Subdomains | assets/.mermaid_clean/ddd/DDD_Contract_Types_Overview.mmd<br />assets/.mermaid_clean/ddd/DDD_Subdomain_Map.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Contract_Types_Overview.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Subdomain_Map.mmd
C2-03 Governance and DAO | assets/.mermaid_clean/ddd/DDD_Contract_Types_Overview.mmd<br />assets/.mermaid_clean/ddd/DDD_Subdomain_Map.mmd<br />assets/.mermaid_clean/ddd/DDD_Team_Context_Alignment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Contract_Types_Overview.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Subdomain_Map.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Team_Context_Alignment.mmd
C2-02 Proof of Contribution | assets/.mermaid_clean/ddd/DDD_Contract_Types_Overview.mmd<br />assets/.mermaid_clean/ddd/DDD_Subdomain_Map.mmd<br />assets/.mermaid_clean/ddd/DDD_Team_Context_Alignment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Contract_Types_Overview.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Subdomain_Map.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Team_Context_Alignment.mmd
C2-01 Resonance Service | assets/.mermaid_clean/C3_containers/C2-01_Resonance_Service.mmd.mmd<br />assets/.mermaid_clean/C3_containers/C2-02_Proof_of_Contribution.mmd<br />assets/.mermaid_clean/C3_containers/C2-07_Resonance_Metric_Stack.mmd<br />assets/.mermaid_clean/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd<br />assets/.mermaid_clean/C3_containers/C2-12_Resonance_Board_UI.mmd<br />assets/.mermaid_clean/ddd/DDD_Contract_Types_Overview.mmd<br />assets/.mermaid_clean/ddd/DDD_Subdomain_Map.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-01_Resonance_Service.mmd.mmd
C2-04 Treasury and Funding | assets/.mermaid_clean/ddd/DDD_Contract_Types_Overview.mmd<br />assets/.mermaid_clean/ddd/DDD_Subdomain_Map.mmd<br />assets/.mermaid_clean/ddd/DDD_Team_Context_Alignment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Contract_Types_Overview.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Subdomain_Map.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Team_Context_Alignment.mmd
C2-08 Manifesto and Ethics Guard | assets/.mermaid_clean/ddd/DDD_Contract_Types_Overview.mmd<br />assets/.mermaid_clean/ddd/DDD_Subdomain_Map.mmd<br />assets/.mermaid_clean/ddd/DDD_Team_Context_Alignment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Contract_Types_Overview.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Subdomain_Map.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Team_Context_Alignment.mmd
Supporting Subdomains | assets/.mermaid_clean/ddd/DDD_Contract_Types_Overview.mmd<br />assets/.mermaid_clean/ddd/DDD_Subdomain_Map.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Contract_Types_Overview.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Subdomain_Map.mmd
C2-05 Identity and Reputation PoCI | assets/.mermaid_clean/ddd/DDD_Contract_Types_Overview.mmd<br />assets/.mermaid_clean/ddd/DDD_Subdomain_Map.mmd<br />assets/.mermaid_clean/ddd/DDD_Team_Context_Alignment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Contract_Types_Overview.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Subdomain_Map.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Team_Context_Alignment.mmd
C2-06 Local Hub and Federation | assets/.mermaid_clean/ddd/DDD_Contract_Types_Overview.mmd<br />assets/.mermaid_clean/ddd/DDD_Subdomain_Map.mmd<br />assets/.mermaid_clean/ddd/DDD_Team_Context_Alignment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Contract_Types_Overview.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Subdomain_Map.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Team_Context_Alignment.mmd
C2-07 Metrics and Analytics | assets/.mermaid_clean/ddd/DDD_Contract_Types_Overview.mmd<br />assets/.mermaid_clean/ddd/DDD_Subdomain_Map.mmd<br />assets/.mermaid_clean/ddd/DDD_Team_Context_Alignment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Contract_Types_Overview.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Subdomain_Map.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Team_Context_Alignment.mmd
C2-09 Knowledge Graph and Collective Intelligence | assets/.mermaid_clean/ddd/DDD_Contract_Types_Overview.mmd<br />assets/.mermaid_clean/ddd/DDD_Subdomain_Map.mmd<br />assets/.mermaid_clean/ddd/DDD_Team_Context_Alignment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Contract_Types_Overview.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Subdomain_Map.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Team_Context_Alignment.mmd
Generic and Infrastructure | assets/.mermaid_clean/ddd/DDD_Contract_Types_Overview.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Contract_Types_Overview.mmd
C2-11 Public API Gateway | assets/.mermaid_clean/C3_containers/C2-10_Security_Audit_Layer.mmd<br />assets/.mermaid_clean/C3_containers/C2-11_Public_API_Gateway.mmd<br />assets/.mermaid_clean/C3_containers/C2-12_Resonance_Board_UI.mmd<br />assets/.mermaid_clean/ddd/DDD_Contract_Types_Overview.mmd<br />assets/.mermaid_clean/ddd/DDD_Subdomain_Map.mmd<br />assets/.mermaid_clean/ddd/DDD_Team_Context_Alignment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-10_Security_Audit_Layer.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-11_Public_API_Gateway.mmd
C2-10 Security and Audit | assets/.mermaid_clean/ddd/DDD_Contract_Types_Overview.mmd<br />assets/.mermaid_clean/ddd/DDD_Subdomain_Map.mmd<br />assets/.mermaid_clean/ddd/DDD_Team_Context_Alignment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Contract_Types_Overview.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Subdomain_Map.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Team_Context_Alignment.mmd
C2-12 Resonance Board UI | assets/.mermaid_clean/ddd/DDD_Contract_Types_Overview.mmd<br />assets/.mermaid_clean/ddd/DDD_Subdomain_Map.mmd<br />assets/.mermaid_clean/ddd/DDD_Team_Context_Alignment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Contract_Types_Overview.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Subdomain_Map.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Team_Context_Alignment.mmd
Legend | assets/.mermaid_clean/ddd/DDD_Contract_Types_Overview.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Contract_Types_Overview.mmd
--- Shared Kernel | assets/.mermaid_clean/ddd/DDD_Contract_Types_Overview.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Contract_Types_Overview.mmd
-. Anti Corruption Layer .-&gt; | assets/.mermaid_clean/ddd/DDD_Contract_Types_Overview.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Contract_Types_Overview.mmd
--&gt; Published Language with DDD EVT and C4 | assets/.mermaid_clean/ddd/DDD_Contract_Types_Overview.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Contract_Types_Overview.mmd
--&gt; Conformist with DDD EVT and C4 | assets/.mermaid_clean/ddd/DDD_Contract_Types_Overview.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Contract_Types_Overview.mmd
--&gt; Open Host Service | assets/.mermaid_clean/ddd/DDD_Contract_Types_Overview.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Contract_Types_Overview.mmd
Teams | assets/.mermaid_clean/ddd/DDD_Team_Context_Alignment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Team_Context_Alignment.mmd
Governance Team\ntype Stream aligned | assets/.mermaid_clean/ddd/DDD_Team_Context_Alignment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Team_Context_Alignment.mmd
Resonance Core Team\ntype Complicated subsystem | assets/.mermaid_clean/ddd/DDD_Team_Context_Alignment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Team_Context_Alignment.mmd
PoC and Identity Team\ntype Stream aligned | assets/.mermaid_clean/ddd/DDD_Team_Context_Alignment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Team_Context_Alignment.mmd
Treasury Ops Team\ntype Stream aligned | assets/.mermaid_clean/ddd/DDD_Team_Context_Alignment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Team_Context_Alignment.mmd
Federation and Hubs Team\ntype Stream aligned | assets/.mermaid_clean/ddd/DDD_Team_Context_Alignment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Team_Context_Alignment.mmd
Metrics and Knowledge Team\ntype Stream aligned | assets/.mermaid_clean/ddd/DDD_Team_Context_Alignment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Team_Context_Alignment.mmd
Security and Audit Team\ntype Enabling | assets/.mermaid_clean/ddd/DDD_Team_Context_Alignment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Team_Context_Alignment.mmd
API Gateway and UI Team\ntype Platform | assets/.mermaid_clean/ddd/DDD_Team_Context_Alignment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Team_Context_Alignment.mmd
DevOps and Platform Eng\ntype Platform | assets/.mermaid_clean/ddd/DDD_Team_Context_Alignment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Team_Context_Alignment.mmd
Bounded Contexts and Subdomains | assets/.mermaid_clean/ddd/DDD_Team_Context_Alignment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Team_Context_Alignment.mmd
C2-01 Resonance | assets/.mermaid_clean/C3_containers/C2-11_Public_API_Gateway.mmd<br />assets/.mermaid_clean/ddd/DDD_Team_Context_Alignment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-11_Public_API_Gateway.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Team_Context_Alignment.mmd
Ops and Deployment Layer\nnot a C2 container | assets/.mermaid_clean/ddd/DDD_Team_Context_Alignment.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Team_Context_Alignment.mmd
Generic and Infrastructure Subdomains | assets/.mermaid_clean/ddd/DDD_Subdomain_Map.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Subdomain_Map.mmd
Ops and Deployment Layer (non C2) | assets/.mermaid_clean/ddd/DDD_Subdomain_Map.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Subdomain_Map.mmd
Bitcoin and Hard Asset Layer (external) | assets/.mermaid_clean/ddd/DDD_Subdomain_Map.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/ddd/DDD_Subdomain_Map.mmd
C2-10 Security &amp; Audit Layer | assets/.mermaid_clean/C3_containers/C2-04_Treasury_Funding_Service.mmd<br />assets/.mermaid_clean/C3_containers/C2-05_Identity_Reputation_PoCI.mmd<br />assets/.mermaid_clean/C3_containers/C2-10_Security_Audit_Layer.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-04_Treasury_Funding_Service.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-05_Identity_Reputation_PoCI.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-10_Security_Audit_Layer.mmd
C3-10.01 Ledger Monitor (Integrity/Reconcile) | assets/.mermaid_clean/C3_containers/C2-10_Security_Audit_Layer.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-10_Security_Audit_Layer.mmd
C3-10.02 SIEM Collector (Logs/Telemetry) | assets/.mermaid_clean/C3_containers/C2-10_Security_Audit_Layer.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-10_Security_Audit_Layer.mmd
C3-10.03 Anomaly Detection | assets/.mermaid_clean/C3_containers/C2-10_Security_Audit_Layer.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-10_Security_Audit_Layer.mmd
C3-10.04 Risk Scoring | assets/.mermaid_clean/C3_containers/C2-10_Security_Audit_Layer.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-10_Security_Audit_Layer.mmd
C3-10.05 Incident Response (IR runbooks) | assets/.mermaid_clean/C3_containers/C2-10_Security_Audit_Layer.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-10_Security_Audit_Layer.mmd
C3-10.06 Transparency Reporter (Public Bundles) | assets/.mermaid_clean/C3_containers/C2-10_Security_Audit_Layer.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-10_Security_Audit_Layer.mmd
Audit-DB | assets/.mermaid_clean/C3_containers/C2-10_Security_Audit_Layer.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-10_Security_Audit_Layer.mmd
SIEM-Store | assets/.mermaid_clean/C3_containers/C2-10_Security_Audit_Layer.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-10_Security_Audit_Layer.mmd
IR-DB | assets/.mermaid_clean/C3_containers/C2-10_Security_Audit_Layer.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-10_Security_Audit_Layer.mmd
C2-12 Resonance Board / UI | assets/.mermaid_clean/C3_containers/C2-02_Proof_of_Contribution.mmd<br />assets/.mermaid_clean/C3_containers/C2-03_Governance_DAO_Service.mmd<br />assets/.mermaid_clean/C3_containers/C2-05_Identity_Reputation_PoCI.mmd<br />assets/.mermaid_clean/C3_containers/C2-06_Local_Hub_Federation_Service.mmd<br />assets/.mermaid_clean/C3_containers/C2-07_Resonance_Metric_Stack.mmd<br />assets/.mermaid_clean/C3_containers/C2-08_Manifesto_Ethics_Guard_Service.mmd<br />assets/.mermaid_clean/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd<br />assets/.mermaid_clean/C3_containers/C2-10_Security_Audit_Layer.mmd
C2-07 Metrics / Analytics | assets/.mermaid_clean/C3_containers/C2-01_Resonance_Service.mmd.mmd<br />assets/.mermaid_clean/C3_containers/C2-03_Governance_DAO_Service.mmd<br />assets/.mermaid_clean/C3_containers/C2-04_Treasury_Funding_Service.mmd<br />assets/.mermaid_clean/C3_containers/C2-05_Identity_Reputation_PoCI.mmd<br />assets/.mermaid_clean/C3_containers/C2-06_Local_Hub_Federation_Service.mmd<br />assets/.mermaid_clean/C3_containers/C2-08_Manifesto_Ethics_Guard_Service.mmd<br />assets/.mermaid_clean/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd<br />assets/.mermaid_clean/C3_containers/C2-10_Security_Audit_Layer.mmd
C2-03 Governance &amp; DAO | assets/.mermaid_clean/C3_containers/C2-10_Security_Audit_Layer.mmd<br />assets/.mermaid_clean/C3_containers/C2-12_Resonance_Board_UI.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-10_Security_Audit_Layer.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-12_Resonance_Board_UI.mmd
C2-04 Treasury &amp; Funding | assets/.mermaid_clean/C3_containers/C2-03_Governance_DAO_Service.mmd<br />assets/.mermaid_clean/C3_containers/C2-06_Local_Hub_Federation_Service.mmd<br />assets/.mermaid_clean/C3_containers/C2-10_Security_Audit_Layer.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-03_Governance_DAO_Service.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-06_Local_Hub_Federation_Service.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-10_Security_Audit_Layer.mmd
C2-07 Resonance Metric Stack / Analytics | assets/.mermaid_clean/C3_containers/C2-07_Resonance_Metric_Stack.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-07_Resonance_Metric_Stack.mmd
C3-07.01 Stream Ingest (Events &amp; Signals) | assets/.mermaid_clean/C3_containers/C2-07_Resonance_Metric_Stack.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-07_Resonance_Metric_Stack.mmd
C3-07.02 KPI Aggregator (A_j, R_j, CP_i, W_i) | assets/.mermaid_clean/C3_containers/C2-07_Resonance_Metric_Stack.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-07_Resonance_Metric_Stack.mmd
C3-07.03 Systemic Resonance Index (SRI Engine) | assets/.mermaid_clean/C3_containers/C2-07_Resonance_Metric_Stack.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-07_Resonance_Metric_Stack.mmd
C3-07.04 Feature Store (Derived Metrics) | assets/.mermaid_clean/C3_containers/C2-07_Resonance_Metric_Stack.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-07_Resonance_Metric_Stack.mmd
C3-07.05 Anomaly Detector | assets/.mermaid_clean/C3_containers/C2-07_Resonance_Metric_Stack.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-07_Resonance_Metric_Stack.mmd
C3-07.06 Dashboard Feed / Stream API | assets/.mermaid_clean/C3_containers/C2-07_Resonance_Metric_Stack.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-07_Resonance_Metric_Stack.mmd
C3-07.07 Metrics Data Store | assets/.mermaid_clean/C3_containers/C2-07_Resonance_Metric_Stack.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-07_Resonance_Metric_Stack.mmd
C3-07.08 Batch Snapshot Worker | assets/.mermaid_clean/C3_containers/C2-07_Resonance_Metric_Stack.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-07_Resonance_Metric_Stack.mmd
C2-02 PoC Service | assets/.mermaid_clean/C3_containers/C2-01_Resonance_Service.mmd.mmd<br />assets/.mermaid_clean/C3_containers/C2-03_Governance_DAO_Service.mmd<br />assets/.mermaid_clean/C3_containers/C2-04_Treasury_Funding_Service.mmd<br />assets/.mermaid_clean/C3_containers/C2-05_Identity_Reputation_PoCI.mmd<br />assets/.mermaid_clean/C3_containers/C2-07_Resonance_Metric_Stack.mmd<br />assets/.mermaid_clean/C3_containers/C2-08_Manifesto_Ethics_Guard_Service.mmd<br />assets/.mermaid_clean/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd<br />assets/.mermaid_clean/C3_containers/C2-11_Public_API_Gateway.mmd
C2-03 Governance | assets/.mermaid_clean/C3_containers/C2-02_Proof_of_Contribution.mmd<br />assets/.mermaid_clean/C3_containers/C2-07_Resonance_Metric_Stack.mmd<br />assets/.mermaid_clean/C3_containers/C2-11_Public_API_Gateway.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-02_Proof_of_Contribution.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-07_Resonance_Metric_Stack.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-11_Public_API_Gateway.mmd
C2-04 Treasury | assets/.mermaid_clean/C3_containers/C2-07_Resonance_Metric_Stack.mmd<br />assets/.mermaid_clean/C3_containers/C2-11_Public_API_Gateway.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-07_Resonance_Metric_Stack.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-11_Public_API_Gateway.mmd
C2-06 Local Hubs | assets/.mermaid_clean/C3_containers/C2-07_Resonance_Metric_Stack.mmd<br />assets/.mermaid_clean/C3_containers/C2-11_Public_API_Gateway.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-07_Resonance_Metric_Stack.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-11_Public_API_Gateway.mmd
C2-08 Manifesto &amp; Ethics Guard | assets/.mermaid_clean/C3_containers/C2-02_Proof_of_Contribution.mmd<br />assets/.mermaid_clean/C3_containers/C2-03_Governance_DAO_Service.mmd<br />assets/.mermaid_clean/C3_containers/C2-05_Identity_Reputation_PoCI.mmd<br />assets/.mermaid_clean/C3_containers/C2-07_Resonance_Metric_Stack.mmd<br />assets/.mermaid_clean/C3_containers/C2-08_Manifesto_Ethics_Guard_Service.mmd<br />assets/.mermaid_clean/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd<br />assets/.mermaid_clean/C3_containers/C2-12_Resonance_Board_UI.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-02_Proof_of_Contribution.mmd
C2-10 Security &amp; Audit | assets/.mermaid_clean/C3_containers/C2-02_Proof_of_Contribution.mmd<br />assets/.mermaid_clean/C3_containers/C2-03_Governance_DAO_Service.mmd<br />assets/.mermaid_clean/C3_containers/C2-06_Local_Hub_Federation_Service.mmd<br />assets/.mermaid_clean/C3_containers/C2-07_Resonance_Metric_Stack.mmd<br />assets/.mermaid_clean/C3_containers/C2-08_Manifesto_Ethics_Guard_Service.mmd<br />assets/.mermaid_clean/C3_containers/C2-11_Public_API_Gateway.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-02_Proof_of_Contribution.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-03_Governance_DAO_Service.mmd
C2-04 Treasury &amp; Funding Service | assets/.mermaid_clean/C3_containers/C2-04_Treasury_Funding_Service.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-04_Treasury_Funding_Service.mmd
C3-04.01 Quadratic Funding Engine | assets/.mermaid_clean/C3_containers/C2-04_Treasury_Funding_Service.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-04_Treasury_Funding_Service.mmd
C3-04.02 Payout Orchestrator | assets/.mermaid_clean/C3_containers/C2-04_Treasury_Funding_Service.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-04_Treasury_Funding_Service.mmd
C3-04.03 Reserve Manager | assets/.mermaid_clean/C3_containers/C2-04_Treasury_Funding_Service.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-04_Treasury_Funding_Service.mmd
C3-04.04 Compliance &amp; Risk Checks | assets/.mermaid_clean/C3_containers/C2-04_Treasury_Funding_Service.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-04_Treasury_Funding_Service.mmd
C3-04.05 Escrow Processor | assets/.mermaid_clean/C3_containers/C2-04_Treasury_Funding_Service.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-04_Treasury_Funding_Service.mmd
C3-04.06 On-Chain Adapter (Tx Bridge) | assets/.mermaid_clean/C3_containers/C2-04_Treasury_Funding_Service.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-04_Treasury_Funding_Service.mmd
C3-04.07 Treasury Ledger / DB | assets/.mermaid_clean/C3_containers/C2-04_Treasury_Funding_Service.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-04_Treasury_Funding_Service.mmd
C3-04.08 Event Publisher (Funding Signals) | assets/.mermaid_clean/C3_containers/C2-04_Treasury_Funding_Service.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-04_Treasury_Funding_Service.mmd
C2-03 Governance Service | assets/.mermaid_clean/C3_containers/C2-04_Treasury_Funding_Service.mmd<br />assets/.mermaid_clean/C3_containers/C2-05_Identity_Reputation_PoCI.mmd<br />assets/.mermaid_clean/C3_containers/C2-06_Local_Hub_Federation_Service.mmd<br />assets/.mermaid_clean/C3_containers/C2-08_Manifesto_Ethics_Guard_Service.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-04_Treasury_Funding_Service.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-05_Identity_Reputation_PoCI.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-06_Local_Hub_Federation_Service.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-08_Manifesto_Ethics_Guard_Service.mmd
C2-05 Identity (PoCI) | assets/.mermaid_clean/C3_containers/C2-02_Proof_of_Contribution.mmd<br />assets/.mermaid_clean/C3_containers/C2-03_Governance_DAO_Service.mmd<br />assets/.mermaid_clean/C3_containers/C2-04_Treasury_Funding_Service.mmd<br />assets/.mermaid_clean/C3_containers/C2-08_Manifesto_Ethics_Guard_Service.mmd<br />assets/.mermaid_clean/C3_containers/C2-11_Public_API_Gateway.mmd<br />assets/.mermaid_clean/C3_containers/C2-12_Resonance_Board_UI.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-02_Proof_of_Contribution.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-03_Governance_DAO_Service.mmd
C1-06 Bitcoin / Hard Asset Layer | assets/.mermaid_clean/C3_containers/C2-04_Treasury_Funding_Service.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-04_Treasury_Funding_Service.mmd
C2-06 Local Hub / Federation | assets/.mermaid_clean/C3_containers/C2-04_Treasury_Funding_Service.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-04_Treasury_Funding_Service.mmd
C3-11.01 Smart Router (REST/gRPC) | assets/.mermaid_clean/C3_containers/C2-11_Public_API_Gateway.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-11_Public_API_Gateway.mmd
C3-11.02 GraphQL Federation | assets/.mermaid_clean/C3_containers/C2-11_Public_API_Gateway.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-11_Public_API_Gateway.mmd
C3-11.03 Auth Hub (Tokens, Sessions) | assets/.mermaid_clean/C3_containers/C2-11_Public_API_Gateway.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-11_Public_API_Gateway.mmd
C3-11.04 Rate &amp; Quota Manager | assets/.mermaid_clean/C3_containers/C2-11_Public_API_Gateway.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-11_Public_API_Gateway.mmd
C3-11.05 Schema Guard &amp; Policy Validator | assets/.mermaid_clean/C3_containers/C2-11_Public_API_Gateway.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-11_Public_API_Gateway.mmd
C3-11.06 Telemetry Collector | assets/.mermaid_clean/C3_containers/C2-11_Public_API_Gateway.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-11_Public_API_Gateway.mmd
C3-11.07 Developer Portal (Docs, Keys) | assets/.mermaid_clean/C3_containers/C2-11_Public_API_Gateway.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-11_Public_API_Gateway.mmd
C3-11.08 API Log Store | assets/.mermaid_clean/C3_containers/C2-11_Public_API_Gateway.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-11_Public_API_Gateway.mmd
C3-11.09 Event Publisher (API Metrics) | assets/.mermaid_clean/C3_containers/C2-11_Public_API_Gateway.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-11_Public_API_Gateway.mmd
C1-07 Developers / Architects | assets/.mermaid_clean/C3_containers/C2-11_Public_API_Gateway.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-11_Public_API_Gateway.mmd
C2-08 Ethics Guard | assets/.mermaid_clean/C3_containers/C2-01_Resonance_Service.mmd.mmd<br />assets/.mermaid_clean/C3_containers/C2-11_Public_API_Gateway.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-01_Resonance_Service.mmd.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-11_Public_API_Gateway.mmd
C2-09 Knowledge Graph | assets/.mermaid_clean/C3_containers/C2-06_Local_Hub_Federation_Service.mmd<br />assets/.mermaid_clean/C3_containers/C2-08_Manifesto_Ethics_Guard_Service.mmd<br />assets/.mermaid_clean/C3_containers/C2-11_Public_API_Gateway.mmd<br />assets/.mermaid_clean/C3_containers/C2-12_Resonance_Board_UI.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-06_Local_Hub_Federation_Service.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-08_Manifesto_Ethics_Guard_Service.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-11_Public_API_Gateway.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-12_Resonance_Board_UI.mmd
C2-03 Governance &amp; DAO Service | assets/.mermaid_clean/C3_containers/C2-03_Governance_DAO_Service.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-03_Governance_DAO_Service.mmd
C3-03.01 Proposal Engine | assets/.mermaid_clean/C3_containers/C2-03_Governance_DAO_Service.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-03_Governance_DAO_Service.mmd
C3-03.02 Quorum &amp; Threshold Logic | assets/.mermaid_clean/C3_containers/C2-03_Governance_DAO_Service.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-03_Governance_DAO_Service.mmd
C3-03.03 Voting Service | assets/.mermaid_clean/C3_containers/C2-03_Governance_DAO_Service.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-03_Governance_DAO_Service.mmd
C3-03.04 Execution Manager | assets/.mermaid_clean/C3_containers/C2-03_Governance_DAO_Service.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-03_Governance_DAO_Service.mmd
C3-03.05 Parameter Versioning (λ, α, q, θ) | assets/.mermaid_clean/C3_containers/C2-03_Governance_DAO_Service.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-03_Governance_DAO_Service.mmd
C3-03.06 Audit Trail Writer | assets/.mermaid_clean/C3_containers/C2-03_Governance_DAO_Service.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-03_Governance_DAO_Service.mmd
C2-06 Local Hub / Federation Service | assets/.mermaid_clean/C3_containers/C2-06_Local_Hub_Federation_Service.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-06_Local_Hub_Federation_Service.mmd
C3-06.01 Sync Orchestrator | assets/.mermaid_clean/C3_containers/C2-06_Local_Hub_Federation_Service.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-06_Local_Hub_Federation_Service.mmd
C3-06.02 CRDT Resolver | assets/.mermaid_clean/C3_containers/C2-06_Local_Hub_Federation_Service.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-06_Local_Hub_Federation_Service.mmd
C3-06.03 Project Registry | assets/.mermaid_clean/C3_containers/C2-06_Local_Hub_Federation_Service.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-06_Local_Hub_Federation_Service.mmd
C3-06.04 Federation Client (Bus/Signals) | assets/.mermaid_clean/C3_containers/C2-06_Local_Hub_Federation_Service.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-06_Local_Hub_Federation_Service.mmd
C3-06.05 Health &amp; Telemetry Monitor | assets/.mermaid_clean/C3_containers/C2-06_Local_Hub_Federation_Service.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-06_Local_Hub_Federation_Service.mmd
C3-06.06 Edge Store (Local State) | assets/.mermaid_clean/C3_containers/C2-06_Local_Hub_Federation_Service.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-06_Local_Hub_Federation_Service.mmd
C1-05 Local Communities / Institutions | assets/.mermaid_clean/C3_containers/C2-06_Local_Hub_Federation_Service.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-06_Local_Hub_Federation_Service.mmd
C2-09 Knowledge Graph / Collective Intelligence | assets/.mermaid_clean/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd
C3-09.01 Ontology Manager | assets/.mermaid_clean/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd
C3-09.02 Graph Ingest Pipeline | assets/.mermaid_clean/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd
C3-09.03 Embedding Generator | assets/.mermaid_clean/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd
C3-09.04 RAG Orchestrator | assets/.mermaid_clean/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd
C3-09.05 Synthesis Engine | assets/.mermaid_clean/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd
C3-09.06 KG-Store (Graph DB) | assets/.mermaid_clean/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd
C3-09.07 Vector-DB | assets/.mermaid_clean/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd
C3-09.08 Knowledge Event Publisher | assets/.mermaid_clean/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd
C2-06 Local Hubs / Projects | assets/.mermaid_clean/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-09_Knowledge_Graph_Collective_Intelligence.mmd
C3-01.01 API Controller | assets/.mermaid_clean/C3_containers/C2-01_Resonance_Service.mmd.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-01_Resonance_Service.mmd.mmd
C3-01.02 Schema &amp; Policy Guard | assets/.mermaid_clean/C3_containers/C2-01_Resonance_Service.mmd.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-01_Resonance_Service.mmd.mmd
C3-01.03 Command Handler | assets/.mermaid_clean/C3_containers/C2-01_Resonance_Service.mmd.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-01_Resonance_Service.mmd.mmd
C3-01.04 Resonance Engine (R = I × A × e^(−λΔt)) | assets/.mermaid_clean/C3_containers/C2-01_Resonance_Service.mmd.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-01_Resonance_Service.mmd.mmd
C3-01.05 Sublinear Mapper (W = CP^α) | assets/.mermaid_clean/C3_containers/C2-01_Resonance_Service.mmd.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-01_Resonance_Service.mmd.mmd
C3-01.06 Anomaly Detector | assets/.mermaid_clean/C3_containers/C2-01_Resonance_Service.mmd.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-01_Resonance_Service.mmd.mmd
C3-01.07 Recompute Worker (batch decay/snapshots) | assets/.mermaid_clean/C3_containers/C2-01_Resonance_Service.mmd.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-01_Resonance_Service.mmd.mmd
C3-01.08 Event Publisher | assets/.mermaid_clean/C3_containers/C2-01_Resonance_Service.mmd.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-01_Resonance_Service.mmd.mmd
Snapshot Store | assets/.mermaid_clean/C3_containers/C2-01_Resonance_Service.mmd.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-01_Resonance_Service.mmd.mmd
C2-05 Identity &amp; Reputation Service (PoCI) | assets/.mermaid_clean/C3_containers/C2-05_Identity_Reputation_PoCI.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-05_Identity_Reputation_PoCI.mmd
C3-05.01 DID Manager | assets/.mermaid_clean/C3_containers/C2-05_Identity_Reputation_PoCI.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-05_Identity_Reputation_PoCI.mmd
C3-05.02 Credential Issuer (VC / SBT) | assets/.mermaid_clean/C3_containers/C2-05_Identity_Reputation_PoCI.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-05_Identity_Reputation_PoCI.mmd
C3-05.03 Reputation Graph | assets/.mermaid_clean/C3_containers/C2-05_Identity_Reputation_PoCI.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-05_Identity_Reputation_PoCI.mmd
C3-05.04 Sybil Resistance Evaluator | assets/.mermaid_clean/C3_containers/C2-05_Identity_Reputation_PoCI.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-05_Identity_Reputation_PoCI.mmd
C3-05.05 Verifier / Attestation Checker | assets/.mermaid_clean/C3_containers/C2-05_Identity_Reputation_PoCI.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-05_Identity_Reputation_PoCI.mmd
C3-05.06 Attestation Registry | assets/.mermaid_clean/C3_containers/C2-05_Identity_Reputation_PoCI.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-05_Identity_Reputation_PoCI.mmd
C3-05.07 PoCI Data Store | assets/.mermaid_clean/C3_containers/C2-05_Identity_Reputation_PoCI.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-05_Identity_Reputation_PoCI.mmd
C3-05.08 Reputation Event Publisher | assets/.mermaid_clean/C3_containers/C2-05_Identity_Reputation_PoCI.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-05_Identity_Reputation_PoCI.mmd
C3-08.02 Rubric Manager (versioning) | assets/.mermaid_clean/C3_containers/C2-08_Manifesto_Ethics_Guard_Service.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-08_Manifesto_Ethics_Guard_Service.mmd
C3-08.01 Alignment Evaluator | assets/.mermaid_clean/C3_containers/C2-08_Manifesto_Ethics_Guard_Service.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-08_Manifesto_Ethics_Guard_Service.mmd
C3-08.03 Ethics Policy Engine (allow/deny) | assets/.mermaid_clean/C3_containers/C2-08_Manifesto_Ethics_Guard_Service.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-08_Manifesto_Ethics_Guard_Service.mmd
C3-08.04 Attestation Issuer | assets/.mermaid_clean/C3_containers/C2-08_Manifesto_Ethics_Guard_Service.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-08_Manifesto_Ethics_Guard_Service.mmd
C3-08.05 Appeals Handler / Re-evaluation | assets/.mermaid_clean/C3_containers/C2-08_Manifesto_Ethics_Guard_Service.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-08_Manifesto_Ethics_Guard_Service.mmd
C3-08.06 Ethics Data Store | assets/.mermaid_clean/C3_containers/C2-08_Manifesto_Ethics_Guard_Service.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-08_Manifesto_Ethics_Guard_Service.mmd
C3-08.07 Governance Guidance Feed | assets/.mermaid_clean/C3_containers/C2-08_Manifesto_Ethics_Guard_Service.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-08_Manifesto_Ethics_Guard_Service.mmd
C2-02 Proof-of-Contribution (PoC) Service | assets/.mermaid_clean/C3_containers/C2-02_Proof_of_Contribution.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-02_Proof_of_Contribution.mmd
C3-02.01 API Controller | assets/.mermaid_clean/C3_containers/C2-02_Proof_of_Contribution.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-02_Proof_of_Contribution.mmd
C3-02.02 Schema &amp; Policy Guard | assets/.mermaid_clean/C3_containers/C2-02_Proof_of_Contribution.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-02_Proof_of_Contribution.mmd
C3-02.03 Contribution Normalizer | assets/.mermaid_clean/C3_containers/C2-02_Proof_of_Contribution.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-02_Proof_of_Contribution.mmd
C3-02.04 Alignment &amp; Impact Intake | assets/.mermaid_clean/C3_containers/C2-02_Proof_of_Contribution.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-02_Proof_of_Contribution.mmd
C3-02.05 Time Decay Updater (λ) | assets/.mermaid_clean/C3_containers/C2-02_Proof_of_Contribution.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-02_Proof_of_Contribution.mmd
C3-02.06 Contribution Accumulator (CP) | assets/.mermaid_clean/C3_containers/C2-02_Proof_of_Contribution.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-02_Proof_of_Contribution.mmd
C3-02.07 Voting Weight Mapper (W = CP^α) | assets/.mermaid_clean/C3_containers/C2-02_Proof_of_Contribution.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-02_Proof_of_Contribution.mmd
C3-02.08 PoC Ledger (Immutable) | assets/.mermaid_clean/C3_containers/C2-02_Proof_of_Contribution.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-02_Proof_of_Contribution.mmd
C3-02.09 Snapshotter &amp; Recompute Worker | assets/.mermaid_clean/C3_containers/C2-02_Proof_of_Contribution.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-02_Proof_of_Contribution.mmd
C3-02.10 Reconciliation &amp; Oracles | assets/.mermaid_clean/C3_containers/C2-02_Proof_of_Contribution.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-02_Proof_of_Contribution.mmd
C3-02.11 Sybil / Spam Guard | assets/.mermaid_clean/C3_containers/C2-02_Proof_of_Contribution.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-02_Proof_of_Contribution.mmd
C3-02.12 Events &amp; Exports | assets/.mermaid_clean/C3_containers/C2-02_Proof_of_Contribution.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-02_Proof_of_Contribution.mmd
C1-02 Member / Contributor | assets/.mermaid_clean/C3_containers/C2-02_Proof_of_Contribution.mmd<br />assets/.mermaid_clean/C3_containers/C2-12_Resonance_Board_UI.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-02_Proof_of_Contribution.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-12_Resonance_Board_UI.mmd
C2-06 Local Hub Adapter | assets/.mermaid_clean/C3_containers/C2-02_Proof_of_Contribution.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-02_Proof_of_Contribution.mmd
C2-07 Metrics / SRI | assets/.mermaid_clean/C3_containers/C2-02_Proof_of_Contribution.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-02_Proof_of_Contribution.mmd
External Oracles / Repos | assets/.mermaid_clean/C3_containers/C2-02_Proof_of_Contribution.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-02_Proof_of_Contribution.mmd
C3-12.01 Dashboard Renderer | assets/.mermaid_clean/C3_containers/C2-12_Resonance_Board_UI.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-12_Resonance_Board_UI.mmd
C3-12.02 Live Stream Client | assets/.mermaid_clean/C3_containers/C2-12_Resonance_Board_UI.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-12_Resonance_Board_UI.mmd
C3-12.03 Identity / Wallet Adapter | assets/.mermaid_clean/C3_containers/C2-12_Resonance_Board_UI.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-12_Resonance_Board_UI.mmd
C3-12.04 Workbench (Interaction Tools) | assets/.mermaid_clean/C3_containers/C2-12_Resonance_Board_UI.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-12_Resonance_Board_UI.mmd
C3-12.05 Accessibility &amp; i18n Layer | assets/.mermaid_clean/C3_containers/C2-12_Resonance_Board_UI.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-12_Resonance_Board_UI.mmd
C3-12.06 Local Cache / State Store | assets/.mermaid_clean/C3_containers/C2-12_Resonance_Board_UI.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-12_Resonance_Board_UI.mmd
C3-12.07 Notification &amp; Alert Manager | assets/.mermaid_clean/C3_containers/C2-12_Resonance_Board_UI.mmd<br />docs.coherosphere.io/static/assets/.mermaid_clean/C3_containers/C2-12_Resonance_Board_UI.mmd
Diagram Color System | assets/docs/diagramcolors.md<br />docs.coherosphere.io/static/assets/docs/diagramcolors.md
Color Semantics Overview | assets/docs/diagramcolors.md<br />docs.coherosphere.io/static/assets/docs/diagramcolors.md
Reading a Diagram | assets/docs/diagramcolors.md<br />docs.coherosphere.io/static/assets/docs/diagramcolors.md
Architecture Consistency Audit | assets/docs/consistency_audit.md
Summary | assets/docs/consistency_audit.md
Findings | assets/docs/consistency_audit.md
A. Items missing in Manifest.md | assets/docs/consistency_audit.md
B. Names used across multiple layers (potential consistency hot-spots) | assets/docs/consistency_audit.md
C. C3 Components linked in C4 Sequences | assets/docs/consistency_audit.md
Recommendations | assets/docs/consistency_audit.md
Architecture Manifest | assets/docs/Manifest.md<br />docs.coherosphere.io/static/assets/docs/Manifest.md
1. System Overview | assets/docs/Manifest.md<br />docs.coherosphere.io/static/assets/docs/Manifest.md
2. Domain Architecture (C2) | assets/docs/Manifest.md<br />docs.coherosphere.io/static/assets/docs/Manifest.md
3. Parameter Governance | assets/docs/Manifest.md<br />docs.coherosphere.io/static/assets/docs/Manifest.md
4. AI Build Automation | assets/docs/Manifest.md<br />docs.coherosphere.io/static/assets/docs/Manifest.md
5. Documentation and Index Generation | assets/docs/Manifest.md<br />docs.coherosphere.io/static/assets/docs/Manifest.md
6. Validation &amp; Integrity | assets/docs/Manifest.md<br />docs.coherosphere.io/static/assets/docs/Manifest.md
7. Versioning and Evolution | assets/docs/Manifest.md<br />docs.coherosphere.io/static/assets/docs/Manifest.md
8. Governance Model | assets/docs/Manifest.md<br />docs.coherosphere.io/static/assets/docs/Manifest.md
SLO/SLA Targets | assets/docs/slo_table.md<br />docs.coherosphere.io/static/assets/docs/slo_table.md
To-Do List | assets/docs/architecture_todo.md<br />docs.coherosphere.io/static/assets/docs/architecture_todo.md
1. C4 Sequences (Behavioral Flows) | assets/docs/architecture_todo.md<br />docs.coherosphere.io/static/assets/docs/architecture_todo.md
2. Event Specifications (Specs / JSON Schemas) | assets/docs/architecture_todo.md<br />docs.coherosphere.io/static/assets/docs/architecture_todo.md
3. Docs &amp; Publishing | assets/docs/architecture_todo.md<br />docs.coherosphere.io/static/assets/docs/architecture_todo.md
4. CI/CD &amp; Validation | assets/docs/architecture_todo.md<br />docs.coherosphere.io/static/assets/docs/architecture_todo.md
5. AI Build Readiness | assets/docs/architecture_todo.md<br />docs.coherosphere.io/static/assets/docs/architecture_todo.md
6. Architecture Assets | assets/docs/architecture_todo.md<br />docs.coherosphere.io/static/assets/docs/architecture_todo.md
7. Infrastructure Alignment | assets/docs/architecture_todo.md<br />docs.coherosphere.io/static/assets/docs/architecture_todo.md
8. Runtime Navigation (New) | assets/docs/architecture_todo.md<br />docs.coherosphere.io/static/assets/docs/architecture_todo.md
Priority Summary | assets/docs/architecture_todo.md<br />docs.coherosphere.io/static/assets/docs/architecture_todo.md
Verdict | assets/docs/architecture_todo.md<br />docs.coherosphere.io/static/assets/docs/architecture_todo.md
Architecture Status Report | assets/docs/architecture_status.md<br />docs.coherosphere.io/static/assets/docs/architecture_status.md
1. Executive Summary | assets/docs/architecture_status.md
2. Scorecard | assets/docs/architecture_status.md
3. Architecture Overview | assets/docs/architecture_status.md
4. Architecture Artifacts | assets/docs/architecture_status.md
5. Workstreams (kept + extended) | assets/docs/architecture_status.md
5.1 Docs System | assets/docs/architecture_status.md
5.2 Specs System | assets/docs/architecture_status.md
5.3 Governance &amp; Parameters | assets/docs/architecture_status.md
5.4 Observability KPIs | assets/docs/architecture_status.md
6. CI / CD Workflows (full list preserved + clarified) | assets/docs/architecture_status.md
7. Architecture Invariants (unchanged) | assets/docs/architecture_status.md
8. Risks &amp; Mitigations (expanded, none removed) | assets/docs/architecture_status.md
9. Decision Log (kept + added) | assets/docs/architecture_status.md
10. Milestones | assets/docs/architecture_status.md
11. Appendix | assets/docs/architecture_status.md
11.1 Notation | assets/docs/architecture_status.md
11.2 Useful Paths | assets/docs/architecture_status.md
Parameter Governance SOP | assets/docs/param_governance.md<br />docs.coherosphere.io/static/assets/docs/param_governance.md
1. Parameter Registry | assets/docs/param_governance.md<br />docs.coherosphere.io/static/assets/docs/param_governance.md
2. Roles &amp; Responsibilities | assets/docs/param_governance.md<br />docs.coherosphere.io/static/assets/docs/param_governance.md
3. Change Procedure | assets/docs/param_governance.md<br />docs.coherosphere.io/static/assets/docs/param_governance.md
4. Rollback Strategy | assets/docs/param_governance.md<br />docs.coherosphere.io/static/assets/docs/param_governance.md
5. Audit &amp; Transparency | assets/docs/param_governance.md<br />docs.coherosphere.io/static/assets/docs/param_governance.md
6. References | assets/docs/param_governance.md<br />docs.coherosphere.io/static/assets/docs/param_governance.md
Event Schema Catalog | assets/docs/event_schema_catalog.md<br />docs.coherosphere.io/static/assets/docs/event_schema_catalog.md
Index | assets/docs/event_schema_catalog.md<br />docs.coherosphere.io/static/assets/docs/event_schema_catalog.md
Shared JSON Schema Fragments | assets/docs/event_schema_catalog.md<br />docs.coherosphere.io/static/assets/docs/event_schema_catalog.md
Example: PoC — ContributionSubmitted.v1 | assets/docs/event_schema_catalog.md<br />docs.coherosphere.io/static/assets/docs/event_schema_catalog.md
JSON Schema | assets/docs/event_schema_catalog.md<br />docs.coherosphere.io/static/assets/docs/event_schema_catalog.md
CloudEvent Example | assets/docs/event_schema_catalog.md<br />docs.coherosphere.io/static/assets/docs/event_schema_catalog.md
Ethics — AlignmentChecked.v1 | assets/docs/event_schema_catalog.md<br />docs.coherosphere.io/static/assets/docs/event_schema_catalog.md
Resonance — ResonanceUpdated.v1 | assets/docs/event_schema_catalog.md<br />docs.coherosphere.io/static/assets/docs/event_schema_catalog.md
Metrics — KPIUpdated.v1 / SRIComputed.v1 | assets/docs/event_schema_catalog.md<br />docs.coherosphere.io/static/assets/docs/event_schema_catalog.md
Governance — ProposalCreated / VoteCast / DecisionRecorded / PolicyChanged | assets/docs/event_schema_catalog.md<br />docs.coherosphere.io/static/assets/docs/event_schema_catalog.md
Treasury — FundingAllocated / RoundOpened / RoundClosed / StreamCreated | assets/docs/event_schema_catalog.md<br />docs.coherosphere.io/static/assets/docs/event_schema_catalog.md
Security — IncidentOpened / TransparencyReportPublished | assets/docs/event_schema_catalog.md<br />docs.coherosphere.io/static/assets/docs/event_schema_catalog.md
Validation &amp; Tooling | assets/docs/event_schema_catalog.md<br />docs.coherosphere.io/static/assets/docs/event_schema_catalog.md
AI Build Guide | assets/docs/ai_guide.md<br />docs.coherosphere.io/static/assets/docs/ai_guide.md
1. Build Philosophy | assets/docs/ai_guide.md<br />docs.coherosphere.io/static/assets/docs/ai_guide.md
2. Build Flow Overview | assets/docs/ai_guide.md<br />docs.coherosphere.io/static/assets/docs/ai_guide.md
3. C-ID Mapping | assets/docs/ai_guide.md<br />docs.coherosphere.io/static/assets/docs/ai_guide.md
4. Parameter Governance Integration | assets/docs/ai_guide.md<br />docs.coherosphere.io/static/assets/docs/ai_guide.md
5. Dynamic Asset Generation | assets/docs/ai_guide.md<br />docs.coherosphere.io/static/assets/docs/ai_guide.md
6. CI Workflows Summary | assets/docs/ai_guide.md<br />docs.coherosphere.io/static/assets/docs/ai_guide.md
7. Deployment Process | assets/docs/ai_guide.md<br />docs.coherosphere.io/static/assets/docs/ai_guide.md
8. SBOM and Integrity Verification | assets/docs/ai_guide.md<br />docs.coherosphere.io/static/assets/docs/ai_guide.md
9. Version History | assets/docs/ai_guide.md<br />docs.coherosphere.io/static/assets/docs/ai_guide.md
Coherosphere — Unified CORS Policy (v1.2.0) | assets/config/cors/README.md<br />docs.coherosphere.io/static/assets/config/cors/README.md
File | assets/config/cors/README.md<br />docs.coherosphere.io/static/assets/config/cors/README.md
Environments | assets/config/cors/README.md<br />docs.coherosphere.io/static/assets/config/cors/README.md
Allowed Origins (production) | assets/config/cors/README.md<br />docs.coherosphere.io/static/assets/config/cors/README.md
Extras (staging only) | assets/config/cors/README.md<br />docs.coherosphere.io/static/assets/config/cors/README.md
Methods / Headers | assets/config/cors/README.md<br />docs.coherosphere.io/static/assets/config/cors/README.md
Coherosphere — Base44 Hosting Checklist (app.coherosphere.com) | assets/config/base44/Base44-Hosting-Checklist.md<br />docs.coherosphere.io/static/assets/config/base44/Base44-Hosting-Checklist.md
1) DNS &amp; TLS | assets/config/base44/Base44-Hosting-Checklist.md<br />docs.coherosphere.io/static/assets/config/base44/Base44-Hosting-Checklist.md
2) Environment / Config | assets/config/base44/Base44-Hosting-Checklist.md<br />docs.coherosphere.io/static/assets/config/base44/Base44-Hosting-Checklist.md
3) CORS &amp; Cookies | assets/config/base44/Base44-Hosting-Checklist.md<br />docs.coherosphere.io/static/assets/config/base44/Base44-Hosting-Checklist.md
4) Auth | assets/config/base44/Base44-Hosting-Checklist.md<br />docs.coherosphere.io/static/assets/config/base44/Base44-Hosting-Checklist.md
5) Realtime | assets/config/base44/Base44-Hosting-Checklist.md<br />docs.coherosphere.io/static/assets/config/base44/Base44-Hosting-Checklist.md
6) Performance | assets/config/base44/Base44-Hosting-Checklist.md<br />docs.coherosphere.io/static/assets/config/base44/Base44-Hosting-Checklist.md
7) Security Headers (baseline) | assets/config/base44/Base44-Hosting-Checklist.md<br />docs.coherosphere.io/static/assets/config/base44/Base44-Hosting-Checklist.md
8) Observability | assets/config/base44/Base44-Hosting-Checklist.md<br />docs.coherosphere.io/static/assets/config/base44/Base44-Hosting-Checklist.md
9) CI/CD | assets/config/base44/Base44-Hosting-Checklist.md<br />docs.coherosphere.io/static/assets/config/base44/Base44-Hosting-Checklist.md
Base44 Integration — Coherosphere | assets/config/base44/README.md<br />docs.coherosphere.io/static/assets/config/base44/README.md
Folders | assets/config/base44/README.md<br />docs.coherosphere.io/static/assets/config/base44/README.md
Required GitHub secrets | assets/config/base44/README.md<br />docs.coherosphere.io/static/assets/config/base44/README.md
DNS Config Bundle (v1) | assets/config/dns/README.md<br />docs.coherosphere.io/static/assets/config/dns/README.md
Canonical source | assets/config/dns/README.md<br />docs.coherosphere.io/static/assets/config/dns/README.md
Providers | assets/config/dns/README.md<br />docs.coherosphere.io/static/assets/config/dns/README.md
Notes | assets/config/dns/README.md<br />docs.coherosphere.io/static/assets/config/dns/README.md
Website | docs.coherosphere.io/README.md
Installation | docs.coherosphere.io/README.md
Local Development | docs.coherosphere.io/README.md
Build | docs.coherosphere.io/README.md
Deployment | docs.coherosphere.io/README.md
Architecture Assets Manifest | docs.coherosphere.io/static/assets/diagrams/Manifest.md
Diagrams | docs.coherosphere.io/static/assets/diagrams/Manifest.md
OpenAPI Specs | docs.coherosphere.io/static/assets/diagrams/Manifest.md
Event Schemas | docs.coherosphere.io/static/assets/diagrams/Manifest.md
1) Executive Summary | docs.coherosphere.io/static/assets/docs/architecture_status.md
2) Scorecard | docs.coherosphere.io/static/assets/docs/architecture_status.md
3) Workstreams (kept + extended) | docs.coherosphere.io/static/assets/docs/architecture_status.md
3.1 Docs System | docs.coherosphere.io/static/assets/docs/architecture_status.md
3.2 Specs System | docs.coherosphere.io/static/assets/docs/architecture_status.md
3.3 Governance &amp; Parameters | docs.coherosphere.io/static/assets/docs/architecture_status.md
3.4 Observability KPIs | docs.coherosphere.io/static/assets/docs/architecture_status.md
4) CI / CD Workflows (full list preserved + clarified) | docs.coherosphere.io/static/assets/docs/architecture_status.md
5) Architecture Invariants (unchanged) | docs.coherosphere.io/static/assets/docs/architecture_status.md
6) Risks &amp; Mitigations (expanded, none removed) | docs.coherosphere.io/static/assets/docs/architecture_status.md
7) Decision Log (kept + added) | docs.coherosphere.io/static/assets/docs/architecture_status.md
8) Milestones | docs.coherosphere.io/static/assets/docs/architecture_status.md
9) Appendix | docs.coherosphere.io/static/assets/docs/architecture_status.md
9.1 Notation | docs.coherosphere.io/static/assets/docs/architecture_status.md
9.2 Useful Paths | docs.coherosphere.io/static/assets/docs/architecture_status.md
Tutorial Intro | docs.coherosphere.io/docs/intro.md
Getting Started | docs.coherosphere.io/docs/intro.md
What you'll need | docs.coherosphere.io/docs/intro.md
Generate a new site | docs.coherosphere.io/docs/intro.md
Start your site | docs.coherosphere.io/docs/intro.md
Create a Document | docs.coherosphere.io/docs/tutorial-basics/create-a-document.md
Create your first Doc | docs.coherosphere.io/docs/tutorial-basics/create-a-document.md
Hello | docs.coherosphere.io/docs/tutorial-basics/create-a-document.md
Configure the Sidebar | docs.coherosphere.io/docs/tutorial-basics/create-a-document.md
Congratulations! | docs.coherosphere.io/docs/tutorial-basics/congratulations.md
What's next? | docs.coherosphere.io/docs/tutorial-basics/congratulations.md
Deploy your site | docs.coherosphere.io/docs/tutorial-basics/deploy-your-site.md
Build your site | docs.coherosphere.io/docs/tutorial-basics/deploy-your-site.md
Create a Blog Post | docs.coherosphere.io/docs/tutorial-basics/create-a-blog-post.md
Create your first Post | docs.coherosphere.io/docs/tutorial-basics/create-a-blog-post.md
Create a Page | docs.coherosphere.io/docs/tutorial-basics/create-a-page.md
Create your first React Page | docs.coherosphere.io/docs/tutorial-basics/create-a-page.md
Create your first Markdown Page | docs.coherosphere.io/docs/tutorial-basics/create-a-page.md
My Markdown page | docs.coherosphere.io/docs/tutorial-basics/create-a-page.md
Translate your site | docs.coherosphere.io/docs/tutorial-extras/translate-your-site.md
Configure i18n | docs.coherosphere.io/docs/tutorial-extras/translate-your-site.md
Translate a doc | docs.coherosphere.io/docs/tutorial-extras/translate-your-site.md
Start your localized site | docs.coherosphere.io/docs/tutorial-extras/translate-your-site.md
Add a Locale Dropdown | docs.coherosphere.io/docs/tutorial-extras/translate-your-site.md
Build your localized site | docs.coherosphere.io/docs/tutorial-extras/translate-your-site.md
Manage Docs Versions | docs.coherosphere.io/docs/tutorial-extras/manage-docs-versions.md
Create a docs version | docs.coherosphere.io/docs/tutorial-extras/manage-docs-versions.md
Add a Version Dropdown | docs.coherosphere.io/docs/tutorial-extras/manage-docs-versions.md
Update an existing version | docs.coherosphere.io/docs/tutorial-extras/manage-docs-versions.md
Markdown page example | docs.coherosphere.io/src/pages/markdown-page.md

## Overview

Term | Sources
---|---
C1 — System Context | assets/diagrams/overview/Architecture_Stack.mmd<br />assets/diagrams/overview/C4_Layers_Summary.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/Architecture_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/C4_Layers_Summary.mmd
Stakeholders &amp; Trust Boundaries | assets/diagrams/overview/C4_Layers_Summary.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/C4_Layers_Summary.mmd
External Systems &amp; Policies | assets/diagrams/overview/C4_Layers_Summary.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/C4_Layers_Summary.mmd
C2 — Containers / Services | assets/diagrams/overview/Architecture_Stack.mmd<br />assets/diagrams/overview/C4_Layers_Summary.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/Architecture_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/C4_Layers_Summary.mmd
C2-01 Resonance Service | assets/diagrams/overview/C4_Layers_Summary.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/C4_Layers_Summary.mmd
C2-02 Proof of Contribution | assets/diagrams/overview/Architecture_Stack.mmd<br />assets/diagrams/overview/C4_Layers_Summary.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/Architecture_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/C4_Layers_Summary.mmd
C2-03 Governance DAO | assets/diagrams/overview/C4_Layers_Summary.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/C4_Layers_Summary.mmd
C2-04 Treasury | assets/diagrams/overview/Architecture_Stack.mmd<br />assets/diagrams/overview/C4_Layers_Summary.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/Architecture_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/C4_Layers_Summary.mmd
C2-05 Identity (PoCI) | assets/diagrams/overview/Architecture_Stack.mmd<br />assets/diagrams/overview/C4_Layers_Summary.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/Architecture_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/C4_Layers_Summary.mmd
C2-06 Local Hubs | assets/diagrams/overview/Architecture_Stack.mmd<br />assets/diagrams/overview/C4_Layers_Summary.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/Architecture_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/C4_Layers_Summary.mmd
C2-07 Metrics | assets/diagrams/overview/Architecture_Stack.mmd<br />assets/diagrams/overview/C4_Layers_Summary.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/Architecture_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/C4_Layers_Summary.mmd
C2-08 Ethics | assets/diagrams/overview/Architecture_Stack.mmd<br />assets/diagrams/overview/C4_Layers_Summary.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/Architecture_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/C4_Layers_Summary.mmd
C2-09 Knowledge Graph | assets/diagrams/overview/Architecture_Stack.mmd<br />assets/diagrams/overview/C4_Layers_Summary.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/Architecture_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/C4_Layers_Summary.mmd
C2-10 Security &amp; Audit | assets/diagrams/overview/Architecture_Stack.mmd<br />assets/diagrams/overview/C4_Layers_Summary.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/Architecture_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/C4_Layers_Summary.mmd
C2-11 API Gateway | assets/diagrams/overview/Architecture_Stack.mmd<br />assets/diagrams/overview/C4_Layers_Summary.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/Architecture_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/C4_Layers_Summary.mmd
C3 — Models / States | assets/diagrams/overview/C4_Layers_Summary.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/C4_Layers_Summary.mmd
Domain Model (ERD) | assets/diagrams/overview/C4_Layers_Summary.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/C4_Layers_Summary.mmd
State Machines (SM-xx) | assets/diagrams/overview/Architecture_Stack.mmd<br />assets/diagrams/overview/C4_Layers_Summary.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/Architecture_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/C4_Layers_Summary.mmd
C4 — Sequences (Behavior) | assets/diagrams/overview/Architecture_Stack.mmd<br />assets/diagrams/overview/C4_Layers_Summary.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/Architecture_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/C4_Layers_Summary.mmd
C4-02 Proposal→Vote→Execution | assets/diagrams/overview/Architecture_Stack.mmd<br />assets/diagrams/overview/C4_Layers_Summary.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/Architecture_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/C4_Layers_Summary.mmd
C4-11 Treasury Rebalancing | assets/diagrams/overview/Architecture_Stack.mmd<br />assets/diagrams/overview/C4_Layers_Summary.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/Architecture_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/C4_Layers_Summary.mmd
C4-21 Ethical Evaluation | assets/diagrams/overview/Architecture_Stack.mmd<br />assets/diagrams/overview/C4_Layers_Summary.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/Architecture_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/C4_Layers_Summary.mmd
C4-34 DSR &amp; Erasure Workflow | assets/diagrams/overview/Architecture_Stack.mmd<br />assets/diagrams/overview/C4_Layers_Summary.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/Architecture_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/C4_Layers_Summary.mmd
C4-35 Funding Pause/Resume via Risk | assets/diagrams/overview/Architecture_Stack.mmd<br />assets/diagrams/overview/C4_Layers_Summary.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/Architecture_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/C4_Layers_Summary.mmd
DDD — Events (DDD-EVT-xx) | assets/diagrams/overview/C4_Layers_Summary.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/C4_Layers_Summary.mmd
Schemas + CloudEvents Envelope | assets/diagrams/overview/C4_Layers_Summary.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/C4_Layers_Summary.mmd
C4 ↔ EVT Alignment (84/84) | assets/diagrams/overview/C4_Layers_Summary.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/C4_Layers_Summary.mmd
Specifications | assets/diagrams/overview/C4_Layers_Summary.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/C4_Layers_Summary.mmd
OpenAPI (C2-xx, HTTPS, x-c2-id) | assets/diagrams/overview/Architecture_Stack.mmd<br />assets/diagrams/overview/C4_Layers_Summary.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/Architecture_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/C4_Layers_Summary.mmd
Event Schemas (/assets/specs/events) | assets/diagrams/overview/C4_Layers_Summary.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/C4_Layers_Summary.mmd
Mermaid Diagrams (/assets/diagrams) | assets/diagrams/overview/C4_Layers_Summary.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/C4_Layers_Summary.mmd
Validation &amp; Build | assets/diagrams/overview/C4_Layers_Summary.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/C4_Layers_Summary.mmd
CI: Validate OpenAPI (Redocly+Spectral) | assets/diagrams/overview/C4_Layers_Summary.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/C4_Layers_Summary.mmd
CI: C4 ↔ DDD Schema Check | assets/diagrams/overview/C4_Layers_Summary.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/C4_Layers_Summary.mmd
CI: Mermaid Syntax Guard | assets/diagrams/overview/C4_Layers_Summary.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/C4_Layers_Summary.mmd
AI Build Mapping (cid-registry.json) | assets/diagrams/overview/Architecture_Stack.mmd<br />assets/diagrams/overview/C4_Layers_Summary.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/Architecture_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/C4_Layers_Summary.mmd
Codegen Harness (SDK + Contracts) | assets/diagrams/overview/C4_Layers_Summary.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/C4_Layers_Summary.mmd
Users &amp; Integrations | assets/diagrams/overview/Architecture_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/Architecture_Stack.mmd
End Users / UI (C2-12) | assets/diagrams/overview/Architecture_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/Architecture_Stack.mmd
Developers / Clients | assets/diagrams/overview/Architecture_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/Architecture_Stack.mmd
External Systems | assets/diagrams/overview/Architecture_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/Architecture_Stack.mmd
Stakeholders | assets/diagrams/overview/Architecture_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/Architecture_Stack.mmd
Trust Boundaries | assets/diagrams/overview/Architecture_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/Architecture_Stack.mmd
External Policies | assets/diagrams/overview/Architecture_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/Architecture_Stack.mmd
C2-01 Resonance | assets/diagrams/overview/Architecture_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/Architecture_Stack.mmd
C2-03 Governance | assets/diagrams/overview/Architecture_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/Architecture_Stack.mmd
C3 — Models &amp; States | assets/diagrams/overview/Architecture_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/Architecture_Stack.mmd
Domain ERD / Aggregates | assets/diagrams/overview/Architecture_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/Architecture_Stack.mmd
DDD — Events &amp; Specifications | assets/diagrams/overview/Architecture_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/Architecture_Stack.mmd
DDD-EVT-xx JSON Schemas | assets/diagrams/overview/Architecture_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/Architecture_Stack.mmd
CloudEvents Envelope (source/subject/type) | assets/diagrams/overview/Architecture_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/Architecture_Stack.mmd
Mermaid Diagrams (C1–C4, DDD) | assets/diagrams/overview/Architecture_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/Architecture_Stack.mmd
CI/CD — Validation &amp; Codegen | assets/diagrams/overview/Architecture_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/Architecture_Stack.mmd
Validate OpenAPI (Redocly + Spectral) | assets/diagrams/overview/Architecture_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/Architecture_Stack.mmd
C4 ↔ DDD Schema Alignment | assets/diagrams/overview/Architecture_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/Architecture_Stack.mmd
Mermaid Syntax Guard (mmdc) | assets/diagrams/overview/Architecture_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/Architecture_Stack.mmd
Codegen Harness (SDK) | assets/diagrams/overview/Architecture_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/Architecture_Stack.mmd
Contract Tests (Prism + Schemathesis) | assets/diagrams/overview/Architecture_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/Architecture_Stack.mmd
Runtime &amp; Observability | assets/diagrams/overview/Architecture_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/Architecture_Stack.mmd
Gateway (C2-11) | assets/diagrams/overview/Architecture_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/Architecture_Stack.mmd
Service Mesh / Policies | assets/diagrams/overview/Architecture_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/Architecture_Stack.mmd
Metrics &amp; Logs (C2-07, C2-10) | assets/diagrams/overview/Architecture_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/Architecture_Stack.mmd
Transparency Reports | assets/diagrams/overview/Architecture_Stack.mmd<br />docs.coherosphere.io/static/assets/diagrams/overview/Architecture_Stack.mmd
