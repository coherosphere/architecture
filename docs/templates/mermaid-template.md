# mermaid template — coherosphere style

> Use this template to create new architecture diagrams (any C4 level).
> Works directly in GitHub markdown preview.

```mermaid
%% ───────────────────────────────────────────────
%%  C4 Diagram Template — coherosphere Colors
%% ───────────────────────────────────────────────
%%  Usage:
%%  - Remove this header comment before publishing
%%  - Replace flowchart type if needed (TD, LR, BT)
%%  - Replace placeholders with your own nodes & edges
%% ───────────────────────────────────────────────

flowchart TD
  %% Example nodes
  A["Example Component A<br/>(short description)"]:::core
  B["Example Component B<br/>(short description)"]:::meta
  C["External System C"]:::ext

  %% Connections
  A -->|"RPC / API"| B
  B -->|"pub/sub"| C

  %% coherosphere Color Theme
  classDef core fill:#FF7A00,stroke:#CC5200,color:#FFFFFF,font-weight:bold
  classDef meta fill:#6A6EFF,stroke:#3C3EFF,color:#FFFFFF,font-weight:bold
  classDef data fill:#EFEFEF,stroke:#BFBFBF,color:#333333
  classDef cache fill:#F2FFE6,stroke:#9CD67C,color:#2B4D1E
  classDef queue fill:#FFF4D6,stroke:#E9B24C,color:#6B4A0F
  classDef olap fill:#EAF6FF,stroke:#88C6F2,color:#0D3D66
  classDef ai fill:#6A6EFF,stroke:#3C3EFF,color:#FFFFFF
  classDef ext fill:#D1C9FF,stroke:#6A6EFF,color:#1E0A5C
  classDef btc fill:#F7931A,stroke:#B56200,color:#FFFFFF
  classDef lnd fill:#FFD300,stroke:#C0A000,color:#000000
  classDef nostr fill:#8C6EFF,stroke:#5A46B0,color:#FFFFFF
