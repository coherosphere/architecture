---
id: slo_table
slug: /slo_table
title: SLO Table
---

# SLO/SLA Targets

**Objective:** Define non-functional requirements (availability, latency, freshness) for core services (C2-01…C2-12).  
**Note:** SLO = target objective; SLA = contractual guarantee (applies to public APIs only).

| C2-ID | Service | Metric | Target | Window | Notes |
|------:|----------|---------|---------|---------|-------|
| C2-11 | Public API Gateway | p95 latency (read) | ≤ 200 ms | 30d | Edge cache allowed |
| C2-11 | Public API Gateway | availability | ≥ 99.95% | 30d | Multi-region setup |
| C2-02 | Proof of Contribution (PoC) | ingest p95 | ≤ 300 ms | 30d | Idempotent POST |
| C2-02 | PoC | event durability | 99.999% | 30d | At-least-once delivery + deduplication |
| C2-01 | Resonance | batch compute | ≤ 5 min | hourly | Sliding window recompute |
| C2-07 | Metrics | dashboard freshness | ≤ 60 s lag | realtime | Streaming preferred |
| C2-03 | Governance | vote record p95 | ≤ 400 ms | 30d | Signed, append-only |
| C2-04 | Treasury | payout creation p95 | ≤ 500 ms | 30d | Excludes on-chain latency |
| C2-05 | Identity (PoCI) | verification p95 | ≤ 300 ms | 30d | Cached verifiable proofs |
| C2-06 | Hubs | CRDT sync convergence | ≤ 5 s | 95th | Under normal connectivity |
| C2-08 | Ethics | preflight evaluation p95 | ≤ 800 ms | 30d | Model cache enabled |
| C2-10 | Security | incident alerting | ≤ 60 s | realtime | SIEM → PagerDuty |
| C2-12 | Resonance Board / UI | TTFB | ≤ 150 ms | 30d | CDN + SSR enabled |

**Error Budgets:** 1−SLO per window; alert thresholds at 25%, 50%, and 75% burn.  
**Escalation:** Pager rotation; 15-min acknowledgment; 1h mitigation for Sev-1 incidents.  
**Monitoring:** Prometheus + OpenTelemetry traces; public status page for SLA-bound endpoints.
