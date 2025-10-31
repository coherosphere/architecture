# Coherosphere — SLO/SLA Targets (v1.0)

**Ziel:** Nicht-funktionale Anforderungen (Verfügbarkeit, Latenz, Freshness) für Kern-Services (C2-01…C2-12).  
**Hinweis:** SLO = Ziel; SLA = vertragliche Zusicherung (nur Public APIs).

| C2-ID | Service | Metric | Target | Window | Notes |
|------:|---------|--------|--------|--------|-------|
| C2-11 | Public API Gateway | p95 latency (read) | ≤ 200 ms | 30d | Edge cache allowed |
| C2-11 | Public API Gateway | availability | ≥ 99.95% | 30d | Multi-region |
| C2-02 | PoC | ingest p95 | ≤ 300 ms | 30d | Idempotent POST |
| C2-02 | PoC | event durability | 99.999% | 30d | At-least-once + de-dup |
| C2-01 | Resonance | compute batch | ≤ 5 min | hourly | Windowed recompute |
| C2-07 | Metrics | dashboard freshness | ≤ 60 s lag | realtime | Streaming preferred |
| C2-03 | Governance | vote record p95 | ≤ 400 ms | 30d | Signed, append-only |
| C2-04 | Treasury | payout creation p95 | ≤ 500 ms | 30d | On-chain delay excluded |
| C2-05 | Identity (PoCI) | verification p95 | ≤ 300 ms | 30d | Cache verifiable proofs |
| C2-06 | Hubs | CRDT sync convergence | ≤ 5 s | 95th | Under normal connectivity |
| C2-08 | Ethics | preflight eval p95 | ≤ 800 ms | 30d | With model cache |
| C2-10 | Security | incident alerting | ≤ 60 s | realtime | SIEM → Pager |
| C2-12 | Resonance Board / UI | TTFB | ≤ 150 ms | 30d | CDN + SSR |

**Error Budgets:** 1−SLO per window; burn alerts at 25/50/75%.  
**Escalation:** Pager rotation, 15-min acknowledge, 1h mitigation for Sev-1.  
**Monitoring:** Prometheus + OpenTelemetry traces; public status page for SLA’d endpoints.
