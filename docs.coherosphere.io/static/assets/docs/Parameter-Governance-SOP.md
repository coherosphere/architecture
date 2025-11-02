# Coherosphere — Parameter Governance SOP (v1.0)

**Objective:**  
Establish a consistent procedure for versioning, modification, and rollback of systemic parameters (`λ`, `α`, `q`, `θ`, rubric versions, etc.).  

**Scope:**  
Applies to the following modules:  
**C2-01 Resonance**, **C2-02 Proof-of-Contribution**, **C2-03 Governance**, **C2-04 Treasury**, **C2-07 Metrics**, **C2-08 Ethics**.

---

## 1. Parameter Registry

- **Format:** Signed JSON documents stored under `assets/specs/params/<name>.json`  
- **Signatures:** Ed25519; key owned by Meta-Governance multisig (M-of-N scheme)  
- **Example:**
```json
{
  "version": "2025-10-31",
  "lambda": 0.012,
  "alpha": 0.65,
  "quorum": 0.2,
  "threshold": 0.6,
  "rubric": "eth.v3",
  "meta": {
    "proposedBy": "C2-03:proposal-abc",
    "notes": "Decay tuned to a 30-day half-life"
  }
}
```

---

## 2. Roles & Responsibilities

| Role | Responsibility |
|------|----------------|
| **Owner** | Meta-Governance Circle (DAO mandate) |
| **Reviewer(s)** | Resonance Core Team, Treasury Ops, Ethics Guard |
| **Sign-Off** | Multisig (M-of-N) signature + `DecisionRecorded` event |

---

## 3. Change Procedure

1. **Create Proposal (C4-02):**  
   Submit a governance proposal including parameter deltas and justification.  
2. **Impact Simulation:**  
   Execute end-to-end simulations on golden datasets (C4-01/03/04); define deviation tolerances.  
3. **Voting & Decision:**  
   Process governed by the current quorum and threshold settings.  
4. **Signing & Publishing:**  
   Commit updated JSON under `assets/specs/params/` along with detached `.sig` file.  
5. **Rollout Sequence:**  
   `C2-01 → C2-02 → C2-07 → C2-04 → C2-03 → C2-08` (controlled orchestration).  
6. **Monitoring:**  
   Observe 7-/30-/90-day SRI drift; trigger incident if threshold exceeded.

---

## 4. Rollback Strategy

- **Hard Stop:**  
  Immediate reversion to the last stable version upon a critical or security incident.  
- **Soft Revert:**  
  If metric drift > X % within 7 days, issue an automated revert recommendation.  
- **Documentation:**  
  Every rollback emits a `PolicyChanged` event and an entry in `assets/specs/params/CHANGELOG.md`.

---

## 5. Audit & Transparency

- All parameter updates emit both `DecisionRecorded` and `PolicyChanged` events.  
- Transparency reports document the active parameter set and its effect on SRI / KPI aggregates.  
- Continuous validation in CI/CD: schema conformance, signature verification, and reference integrity (valid `proposalId`).

---

## 6. References

- **Events:** `DecisionRecorded.v1`, `PolicyChanged.v1`  
- **Flows:** `C4-02 Governance Lifecycle`, `C4-05 Decay Cycle`, `C4-11 Treasury Rebalancing`  
- **State Machines:** `SM-03.01 (Proposal)`, `SM-01.01 (Resonance Calculation)`  
