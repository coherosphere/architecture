# Coherosphere — Parameter-Governance SOP (v1.0)

**Ziel:** Verfahren zur Versionierung, Änderung und Rollback von Systemparametern (λ, α, q, θ, Rubrik-Versionen etc.)  
**Geltungsbereich:** C2-01 Resonance, C2-02 PoC, C2-03 Governance, C2-04 Treasury, C2-07 Metrics, C2-08 Ethics

---

## 1. Parameter-Registry

- Format: signierte JSON-Dateien im Repo: `assets/specs/params/<name>.json`
- Signaturen: Ed25519; Key der Meta-Governance (multisig, M-of-N)
- Beispielstruktur:
```json
{
  "version": "2025-10-31",
  "lambda": 0.012,
  "alpha": 0.65,
  "quorum": 0.2,
  "threshold": 0.6,
  "rubric": "eth.v3",
  "meta": { "proposedBy": "C2-03:proposal-abc", "notes": "Decay tuned to 30d half-life" }
}
```

## 2. Zuständigkeiten

- **Owner:** Meta-Governance Kreis (DAO-Mandat)
- **Reviewer:** Resonance Core Team, Treasury Ops, Ethics Guard
- **Sign-Off:** M-of-N Signatur + `DecisionRecorded` Event

## 3. Änderungsprozess

1. **Proposal erstellen (C4-02):** Governance-Proposal mit Param-Delta und Begründung.  
2. **Impact-Simulation:** E2E-Simulation auf Golden Datasets (C4-01/03/04), Abweichungstoleranzen definieren.  
3. **Abstimmung & Entscheidung:** Quorum/Threshold gemäß aktueller Parameter.  
4. **Signatur & Veröffentlichung:** JSON in `assets/specs/params/` + Signaturdatei `.sig`.  
5. **Rollout:** Orchestriertes Update: C2-01 → C2-02 → C2-07 → C2-04 → C2-03 → C2-08.  
6. **Monitoring:** 7/30/90-Tage SRI-Drift, Incident-Trigger bei Schwellenüberschreitungen.

## 4. Rollback-Strategie

- **Hard Stop:** Bei Incident (Security/Severity High) sofort auf letzte stabile Version zurück.  
- **Soft Revert:** Bei Metrik-Drift > X% in 7 Tagen automatische Revert-Empfehlung.  
- **Dokumentation:** `PolicyChanged` Event + Changelog in `assets/specs/params/CHANGELOG.md`.

## 5. Audit & Transparenz

- Alle Parameteränderungen erzeugen `DecisionRecorded` + `PolicyChanged` Events.  
- Transparenzberichte listen Parameterstände und Effekte auf SRI/KPIs.  
- Validierung in CI: Schema, Signatur, Referenzen (Proposal-ID vorhanden).

## 6. Anhang: Referenzen

- **Events:** DecisionRecorded.v1, PolicyChanged.v1  
- **Flows:** C4-02 Governance Lifecycle, C4-05 Decay Cycle, C4-11 Treasury Rebalancing  
- **SM:** SM-03.01 (Proposal), SM-01.01 (Resonance Calc)
