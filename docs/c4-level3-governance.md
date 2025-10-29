
**`docs/c4-level3-governance.md`**
```markdown
# C4 Level-3 — Governance Service (Components)

```mermaid
flowchart LR
 subgraph RS["Resonance Service (Container)"]
        API["API Controller<br>(REST/gRPC)"]
        VAL["Schema &amp; Policy Guard<br>(JSON-Schema • Rate • Caps)"]
        CMD["Command Handler<br>(Create Contribution • Recompute Request)"]
        ENG["Resonance Engine<br>(Impact×Alignment • Time Decay λ=T→ln2/T)"]
        SUBLIN["Sublinear Mapper<br>(W = CP^α, 0&lt;α&lt;1)"]
        KPIS["KPI Aggregator<br>(Member CP • W • Project Resonance)"]
        SRI["Systemic Resonance Index<br>(SRI Aggregation)"]
        ANOM["Anomaly Detector<br>(spam • sybil • outliers)"]
        RECOMP["Recompute Worker<br>(Batch decay • Snapshots)"]
        OUTBOX["Outbox / Event Publisher"]
        PROJ["Read Models / Views<br>(Leaderboards • Profiles)"]
        CFG["Policy Config<br>(from Meta-Governance)"]
  end
    API --> VAL
    VAL --> CMD
    CMD --> ENG & Q["Queue / Scheduler<br>(QStash/NATS)"]
    ENG --> KPIS & OUTBOX & DB["Operational DB<br>(Postgres)"]
    KPIS --> SRI & PROJ & DB & OLAP["Analytics / Dashboards<br>(ClickHouse/DuckDB)"]
    SUBLIN --> PROJ
    RECOMP --> ENG
    ANOM --> CMD
    CFG --> VAL & ENG
    META["Meta-Governance Service"] --> CFG
    PROJ --> C["Cache<br>(Upstash Redis)"]
    OUTBOX --> ES["Event Store<br>(append-only)"]
    Q --> RECOMP
    SRI --> OLAP
    ENG -. optional alignment assist .-> QVAC["QvAC API<br>(AI assist for alignment scoring, optional)"]
     API:::core
     VAL:::meta
     CMD:::core
     ENG:::core
     KPIS:::core
     SRI:::core
     ANOM:::meta
     RECOMP:::core
     OUTBOX:::queue
     PROJ:::cache
     CFG:::meta
     Q:::queue
     DB:::data
     OLAP:::olap
     META:::meta
     C:::cache
     ES:::data
     QVAC:::ai
    classDef core fill:#FF7A00,stroke:#CC5200,color:#FFFFFF,font-weight:bold
    classDef meta fill:#6A6EFF,stroke:#3C3EFF,color:#FFFFFF,font-weight:bold
    classDef data fill:#EFEFEF,stroke:#BFBFBF,color:#333333
    classDef cache fill:#F2FFE6,stroke:#9CD67C,color:#2B4D1E
    classDef queue fill:#FFF4D6,stroke:#E9B24C,color:#6B4A0F
    classDef olap fill:#EAF6FF,stroke:#88C6F2,color:#0D3D66
    classDef ai fill:#6A6EFF,stroke:#3C3EFF,color:#FFFFFF

