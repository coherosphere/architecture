
**`docs/c4-level2-container.md`**

```mermaid
flowchart LR
 subgraph FE["Frontend Layer"]
        WEBSITE["Website<br>(coherosphere.com)"]
        APP["Web App / DAO UI<br>(app.coherosphere.com)"]
  end
 subgraph CORE["coherosphere core system (Containers)"]
        RS["Resonance Service<br>(Scoring • Decay • KPIs • Leaderboards)"]
        GOV["Governance Service<br>(Proposals • Votes • Quorum/Thresholds • Audit)"]
        ID["Identity Service<br>(Nostr Verify NIP-07/98 • Scoped JWT/Capabilities)"]
        META["Meta-Governance Service<br>(Feedback • Policy Evolution • Experiments/A-B)"]
        ADP["Integration Adapters<br>(Simplicity • Alby • Nostr • QvAC)"]
  end
 subgraph DATA["Data Layer"]
        ES["Event Store (append-only)<br>(e.g., Postgres JSONB / ClickHouse)"]
        DB["Operational DB (ACID)<br>(Postgres)"]
        C["Cache<br>(Upstash Redis)"]
        Q["Queue / Scheduler<br>(QStash / NATS)"]
        OLAP["Analytics / SRI Dashboards<br>(ClickHouse / DuckDB)"]
  end
 subgraph OPSSEC["Ops / Observability / Security"]
        OBS["Observability<br>(OpenTelemetry: logs • traces • metrics)"]
        VAULT["Key &amp; Secrets Vault<br>(Signing • Secrets • Rotation)"]
        WORM["WORM Storage<br>(Immutable audit artifacts)"]
  end
 subgraph BASE["base networks (out of control)"]
        BTC["Bitcoin Base Layer"]
        LND["Lightning Network"]
        NOSTR["Nostr Relay Network"]
  end
    WEBSITE -- Public fetch / links --> EDGE["Edge API Gateway<br>(AuthN/Z • Routing • Rate-Limiting • Schema Validation • Idempotency)"]
    APP -- RPC (REST/gRPC/WebSocket) --> EDGE
    EDGE -- RPC --> RS & GOV & ID
    RS <-- signals/config --> META
    GOV <-- signals/config --> META
    RS --> ES & DB & C & OLAP & OBS & WORM & VAULT
    RS <-- jobs --> Q
    GOV --> ES & DB & C & OBS & WORM & VAULT
    GOV <-- jobs --> Q
    ID --> DB & C & OBS & VAULT
    META --> OLAP
    META <-- experiments / param updates --> RS & GOV
    ADP --> OBS
    ADP -- RPC --> SIMP["Blockstream Simplicity<br>(Blockchain Logic Layer)"] & ALBY["Alby API<br>(Lightning Bridge)"]
    ADP <-- pub/sub --> NOSTR
    SIMP <-- "on-chain read/write" --> BTC
    ALBY -- RPC --> LND
    LND -- "on-chain tx" --> BTC
    RS <-- events / commands --> Q
    GOV <-- events / commands --> Q
    ADP <-- events / commands --> Q
    QVAC["QvAC API<br>(AI Inference / Scoring / Analysis)"]
     WEBSITE:::ext
     APP:::ext
     RS:::core
     GOV:::core
     ID:::core
     META:::meta
     ADP:::ext
     ES:::data
     DB:::data
     C:::cache
     Q:::queue
     OLAP:::olap
     OBS:::obs
     VAULT:::vault
     WORM:::worm
     BTC:::btc
     LND:::lnd
     NOSTR:::nostr
     EDGE:::edge
     SIMP:::logic
     ALBY:::ext
     QVAC:::ai
    classDef edge fill:#E5E5E5,stroke:#999999,color:#333333
    classDef core fill:#FF7A00,stroke:#CC5200,color:#FFFFFF,font-weight:bold
    classDef meta fill:#6A6EFF,stroke:#3C3EFF,color:#FFFFFF,font-weight:bold
    classDef ext fill:#D1C9FF,stroke:#6A6EFF,color:#1E0A5C
    classDef ai fill:#6A6EFF,stroke:#3C3EFF,color:#FFFFFF
    classDef logic fill:#F7931A,stroke:#B56200,color:#FFFFFF
    classDef btc fill:#F7931A,stroke:#B56200,color:#FFFFFF
    classDef lnd fill:#FFD300,stroke:#C0A000,color:#000000
    classDef nostr fill:#8C6EFF,stroke:#5A46B0,color:#FFFFFF
    classDef data fill:#EFEFEF,stroke:#BFBFBF,color:#333333
    classDef cache fill:#F2FFE6,stroke:#9CD67C,color:#2B4D1E
    classDef queue fill:#FFF4D6,stroke:#E9B24C,color:#6B4A0F
    classDef olap fill:#EAF6FF,stroke:#88C6F2,color:#0D3D66
    classDef obs fill:#E1F5FE,stroke:#4FC3F7,color:#0D47A1
    classDef vault fill:#FDEFEF,stroke:#E57373,color:#7F0000
    classDef worm fill:#F3E5F5,stroke:#AB47BC,color:#4A148C
    classDef actor fill:#A3D4FF,stroke:#4C9FFF,color:#003366,font-weight:bold
    classDef operator fill:#FFB347,stroke:#CC7A00,color:#4A2C00,font-weight:bold
[PASTE HIER DEIN L2 MERMAID CODE MIT FARBTHEMA]
