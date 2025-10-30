# contributing to coherosphere architecture docs

Thank you for helping maintain the coherosphere architectural documentation.
This repository serves as the **single source of truth** for the entire system architecture.

---

## 🧩 1. Structure

All architecture documents live under:

docs/
├─ c4-overview.md
├─ c4-level1-system-context.md
├─ c4-level2-container.md
├─ c4-level3-resonance.md
├─ c4-level3-governance.md
└─ assets/
└─ templates/
└─ mermaid-template.md


Each file represents a **C4 level**:
- **Level 1:** System Context (external actors and systems)
- **Level 2:** Containers (main subsystems)
- **Level 3:** Components (internals of each service)
- **Level 4 (optional):** Code examples

---

## 🧠 2. Mermaid Style Guide

- Use the **template** in `docs/templates/mermaid-template.md`.
- Keep diagrams **GitHub-compatible**:
  - Use one ` ```mermaid ... ``` ` block
  - No YAML `config:` header
  - Use `<br/>` for line breaks, not `&lt;` or `&amp;`
- Preferred flow directions:
  - `TD` (Top–Down) for context diagrams
  - `LR` (Left–Right) for container and component diagrams

---

## 🎨 3. Color & Class Definitions

| Type | Class | Color |
|------|--------|--------|
| Core logic | `:::core` | ![#FF7A00](https://via.placeholder.com/15/FF7A00/000000?text=+) Orange |
| Meta / AI | `:::meta` / `:::ai` | ![#6A6EFF](https://via.placeholder.com/15/6A6EFF/000000?text=+) Indigo |
| External system | `:::ext` | ![#D1C9FF](https://via.placeholder.com/15/D1C9FF/000000?text=+) Light Violet |
| Data | `:::data` | ![#EFEFEF](https://via.placeholder.com/15/EFEFEF/000000?text=+) Gray |
| Cache | `:::cache` | ![#F2FFE6](https://via.placeholder.com/15/F2FFE6/000000?text=+) Greenish |
| Queue | `:::queue` | ![#FFF4D6](https://via.placeholder.com/15/FFF4D6/000000?text=+) Yellow |
| OLAP / Analytics | `:::olap` | ![#EAF6FF](https://via.placeholder.com/15/EAF6FF/000000?text=+) Blue |
| Bitcoin | `:::btc` | ![#F7931A](https://via.placeholder.com/15/F7931A/000000?text=+) Orange |
| Lightning | `:::lnd` | ![#FFD300](https://via.placeholder.com/15/FFD300/000000?text=+) Yellow |
| Nostr | `:::nostr` | ![#8C6EFF](https://via.placeholder.com/15/8C6EFF/000000?text=+) Purple |

---

## 🧰 4. Naming Convention

Files follow:
c4-level<N>-<name>.md

Examples:
- `c4-level1-system-context.md`
- `c4-level2-container.md`
- `c4-level3-resonance.md`

---

## 🚀 5. Adding New Diagrams

1. Duplicate the template from `docs/templates/mermaid-template.md`
2. Add your diagram code inside ` ```mermaid ... ``` `
3. Save it as `docs/c4-levelX-[topic].md`
4. Link it in the main `README.md` and in `docs/links.md`
5. Commit using a clear message:

Add C4 Level-3 — [Service Name] components diagram


---

## 🧩 6. References

- C4 Model: [https://c4model.com](https://c4model.com)
- MermaidJS Docs: [https://mermaid.js.org](https://mermaid.js.org)
- GitHub Markdown + Mermaid Support: [https://github.blog/changelog/2022-02-14-mermaid-diagrams](https://github.blog/changelog/2022-02-14-mermaid-diagrams)
