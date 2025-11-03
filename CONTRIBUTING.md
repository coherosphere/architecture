# Contributing to the coherosphere Architecture

> “Contribute in resonance — align value, ethics, and structure.”

The coherosphere/architecture repository is the technical backbone of the coherosphere:
a living documentation space where philosophy meets system design.
Every contribution — whether code, text, or diagram — strengthens the collective field of coherence.

---

## Guiding Principles

- **Architectural Integrity** – All contributions should reinforce structural clarity and systemic coherence.
- **Collective Resonance** – Peer-aligned review replaces hierarchy. We evolve through reflection, not control.
- **Transparency by Design** – All decisions and discussions remain public and versioned.
- **Ethical Alignment** – Contributions must stay consistent with the [coherosphere Manifesto](https://github.com/coherosphere/manifesto) and its principles.

---

## Scope of Contribution

You can contribute in several ways:

| Domain | Examples | Standards |
|--------|-----------|-----------|
| Documentation | Markdown files, architectural narratives, glossary updates | Docusaurus markdown (`/docs`), plain and versioned |
| Architecture Diagrams | C4, Mermaid, UML, or system maps | Stored under `/assets/diagrams/`; must be self-explanatory |
| Automation Scripts | Python or Node scripts for build and audit processes | Place under `/scripts/`; use minimal dependencies |
| Discussions | Conceptual design, terminology, meta-governance | Use [GitHub Discussions](../../discussions) |

---

## Contribution Flow

The coherosphere follows an open GitHub Flow:

1. Fork the repository.
2. Create a branch for your feature or fix.
   ```bash
   git checkout -b feature/add-resonance-diagram
   ```
3. Make your changes — document clearly, commit intentionally.
4. Submit a Pull Request to the `main` branch.
   - Provide a clear description of what was changed and why.
   - Reference related issues or architecture sections.

Each pull request represents a proposal of resonance — a signal to the collective field.

---

## Peer-Aligned Review

- A PR requires two peer approvals from active contributors or maintainers.
- Reviews assess clarity, coherence, and consistency — not authority or style.
- Comments should improve resonance, not enforce preference.

If feedback loops emerge, consider them part of the resonance-tuning process — iteration is learning.

---

## Architectural Integrity Guidelines

When adding or modifying content:

1. Preserve systemic relationships – update related diagrams or docs if dependencies change.
2. Reference sources – cite Manifesto, Whitepaper, or relevant diagram (`see /assets/docs/...`).
3. Keep everything reproducible – diagrams and data should be buildable from source.
4. Document feedback loops – where coherence depends on cyclical relationships, visualize them.
5. Prefer clarity over complexity – diagrams and explanations should be human-readable first, technical second.

---

## Commit and Branch Naming

- Use lowercase, dash-separated branches: `feature/add-diagram`, `fix/typo-metrics`.
- Write concise commit messages:
  - `add: new resonance diagram`
  - `fix: glossary link correction`
  - `update: governance sequence diagram`

---

## Build and Preview

The documentation uses **Docusaurus** for static generation.

To preview locally:

```bash
npm install
npm run start
```

All Mermaid or C4 diagrams are rendered automatically on build.
Ensure diagrams compile before committing.

---

## Licensing and Attribution

By contributing, you agree that your work will be released under:

- **Code** – MIT License
- **Documentation & Diagrams** – CC BY-SA 4.0 License

Include attribution where applicable and keep coherence principles intact.

---

Thank you for contributing to the coherosphere Architecture.
Your input helps maintain not only code, but coherence itself.
