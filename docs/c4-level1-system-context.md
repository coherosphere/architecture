# C4 Level-1 — System Context

```mermaid
flowchart TD
 subgraph CORE["coherosphere core system"]
        RS["Operational Layer<br>(Resonance, Governance, Identity)"]
        META["Meta-Governance Layer<br>(Feedback, Learning, Policy Evolution)"]
  end
 subgraph BASE["base networks (out of control)"]
        BTC["Bitcoin Base Layer"]
        LND["Lightning Network"]
        NOSTR["Nostr Relay Network"]
  end
    RS <-- signals / config --> META
    VISITOR["Visitor (Public)"] -- Read / Learn --> WEBSITE["coherosphere.com<br>(Public Website / Docs)"]
    User["User (Web/App)"] -- Use / Interact --> APP["app.coherosphere.com<br>(Web App / DAO Interface)"]
    APP -- RPC (REST/gRPC) --> EDGE["Edge API Gateway<br>(AuthN/Z, Routing, Rate-Limiting)"]
    WEBSITE -- RPC (REST/gRPC) --> EDGE
    EDGE -- RPC --> RS
    OPS["Core Maintainers / DAO (Deployment / Operations)"] -- Deploy / Monitor --> CORE
    META <-- Analysis / Policy Tuning --> QVAC["QvAC API<br>(AI Inference / Scoring)"]
    RS -- RPC --> SIMP["Blockstream Simplicity<br>(Blockchain Logic Layer)"] & ALBY["Alby API<br>(Lightning Bridge)"]
    SIMP <-- "on-chain read / write" --> BTC
    RS -- pub / sub --> NOSTR
    ALBY -- RPC --> LND
    LND -- "on-chain tx" --> BTC
     RS:::core
     META:::meta
     BTC:::btc
     LND:::lnd
     NOSTR:::nostr
     VISITOR:::actor
     WEBSITE:::ext
     User:::actor
     APP:::ext
     EDGE:::edge
     OPS:::operator
     QVAC:::ai
     SIMP:::logic
     ALBY:::ext
    classDef actor fill:#A3D4FF,stroke:#4C9FFF,color:#003366,font-weight:bold
    classDef operator fill:#FFB347,stroke:#CC7A00,color:#4A2C00,font-weight:bold
    classDef edge fill:#E5E5E5,stroke:#999999,color:#333333
    classDef core fill:#FF7A00,stroke:#CC5200,color:#FFFFFF,font-weight:bold
    classDef meta fill:#6A6EFF,stroke:#3C3EFF,color:#FFFFFF,font-weight:bold
    classDef ai fill:#6A6EFF,stroke:#3C3EFF,color:#FFFFFF
    classDef logic fill:#F7931A,stroke:#B56200,color:#FFFFFF
    classDef ext fill:#D1C9FF,stroke:#6A6EFF,color:#1E0A5C
    classDef btc fill:#F7931A,stroke:#B56200,color:#FFFFFF
    classDef lnd fill:#FFD300,stroke:#C0A000,color:#000000
    classDef nostr fill:#8C6EFF,stroke:#5A46B0,color:#FFFFFF

