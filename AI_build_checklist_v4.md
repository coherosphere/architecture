# Coherosphere — AI Build Checklist (v4.0)

Ziel dieses Dokuments ist es, den vollständigen, maschinenlesbaren Aufbau der *Coherosphere*-Architektur zu definieren.  
Es beschreibt, welche Artefakte, Prüfungen und Abhängigkeiten erforderlich sind, damit ein automatisiertes System (oder eine AI)  
das Gesamtsystem deterministisch neu generieren, validieren und deployen kann.

---

## 1. Übersicht

| Ebene | Zweck | Quelle | Artefakte |
|--------|--------|--------|-----------|
| **C1 – System Context** | Akteure, Zonen, Vertrauensgrenzen | `assets/diagrams/C1_system/` | Mermaid-Diagramme |
| **C2 – Container** | 12 Kerndienste und Schnittstellen | `assets/diagrams/C2_containers/` | Mermaid-Diagramme + API-Surface |
| **C3 – Komponenten / States** | Interne Logik & Zustände pro Service | `assets/diagrams/C3_components/`, `assets/diagrams/C3_states/` | Komponenten- und Zustandsdiagramme |
| **C4 – Sequenzen** | End-to-End-Flows zwischen Services | `assets/diagrams/C4_sequences/` | ca. 34 Sequenzdiagramme |
| **DDD – Domain Design** | Context Map, Subdomains, Verträge | `assets/diagrams/DDD/` | Context Map, Subdomain-, Contract-Views |
| **Specs** | APIs, Events, Governance, SLOs | `assets/specs/` | YAML / JSON Schema |
| **Infra Config** | CORS, DNS, CI-Regeln | `assets/config/` | JSON-Policies, Terraform, Workflow-Dateien |
| **Docs** | Docusaurus-Content | `coherosphere/docs` | Markdown + auto-pulled Architekturdateien |

---

## 2. Kanonische Domains

Alle Artefakte müssen ausschließlich folgende Domains verwenden:

```
https://api.coherosphere.io
https://staging.api.coherosphere.io
https://app.coherosphere.com
https://coherosphere.com
https://docs.coherosphere.io
https://schemas.coherosphere.io
https://chat.coherosphere.io
https://data.coherosphere.io
https://ai.coherosphere.io
http://localhost:3000
http://localhost:5173
```

Pflicht:
- Alle **OpenAPI `servers.url`** zeigen auf `https://api.coherosphere.io` (prod) oder `https://staging.api.coherosphere.io` (stage)
- **CORS-Policy** (in `assets/config/cors/cors-policy.json`) ist verbindlich
- **COEP / CORP / COOP Policies** müssen für App und Docs spezifiziert werden

---

## 3. API-Validierung

**CI-Check:** `.github/workflows/validate-api-domain.yml`

1. Extrahiere alle URLs aus `assets/specs/openapi/**/*.yaml`
2. Vergleiche gegen Whitelist (`cors-policy.json`)
3. Prüfe Syntax (OpenAPI 3.1, YAML, JSON Schema)
4. Führe Linting mit [Spectral](https://github.com/stoplightio/spectral) durch:
   - Pflichtfelder: `info.version`, `info.title`, `servers`, `tags`
   - Kein externer Domain-Host
   - `x-api-version` vorhanden

---

## 4. Event-Schemas (CloudEvents 1.0)

Pfad: `assets/specs/events/`

- Format: JSON Schema Draft 2020-12  
- `$id` = `https://schemas.coherosphere.io/events/<domain>/<version>.json`
- Pflichtfelder: `type`, `source`, `time`, `data`
- Jeder Eventtyp enthält:
  - Beispiel-Payload (`examples`)
  - Versionierung (`x-schema-version`)
  - Beschreibung (`description`)
- Validierung per **AJV CLI**:
  ```bash
  ajv validate -s schema.json -d example.json --spec=draft2020
  ```

---

## 5. Mermaid-Validierung

**Ziel:** Alle `.mmd`-Dateien (C1–C4, DDD, SM) werden automatisch gerendert und auf Syntaxfehler geprüft.

Workflow:
```bash
mmdc -i <input.mmd> -o <output.svg> --check
```

Pflicht:
- Alle Diagramme müssen valide Mermaid-Syntax haben
- Kein unaufgelöstes Label, kein fehlendes `end` oder `subgraph`
- SVGs oder PNGs im Build-Prozess als Artefakt speichern

---

## 6. DDD-Konsistenz

- Jeder **Bounded Context** (z. B. Governance, Treasury, PoC) muss auf seine C2-ID referenzieren  
- Context Map und C4-Sequenzen sind verknüpft:
  - Jeder C4-Flow enthält Events aus dem DDD-Event-Katalog
- Beziehungen:  
  `Context Map → C2 → Events → C4 Sequence`

Pflicht:
- Gemeinsame Eventnamen in DDD und Schemas (`type`)
- Alle Subdomains (Core / Supporting / Generic) dokumentiert

---

## 7. Versionierung

- OpenAPI: `info.version` (semver, z. B. `1.2.0`)
- Events: `$id`-Suffix `/v1` oder `/v1.1`
- C4-Sequenzen: `title: "C4-0X – <Name> (v1.0)"`

Änderungen an Specs oder Schemas triggern automatische Versions-Bumps in Docs.

---

## 8. CI / Automatische Prüfungen

Pflicht-Workflows:
| Name | Zweck |
|-------|--------|
| `validate-api-domain.yml` | API-Hostprüfung |
| `validate-event-schemas.yml` | JSON Schema Validierung |
| `validate-mermaid.yml` | Diagrammprüfung |
| `deploy-docs.yml` | Docusaurus Build + GitHub Pages Deploy |
| `spectral-lint.yml` | OpenAPI-Linting |
| `sbom-generate.yml` | SBOM-Erzeugung für CI-Transparenz |

---

## 9. Dokumentation (Docusaurus)

Repo: [`coherosphere/docs`](https://github.com/coherosphere/docs)  
Deployment: `https://docs.coherosphere.io`

Pipeline:
1. CI checkt `coherosphere/architecture`
2. Kopiert:
   - `assets/diagrams` → `static/diagrams`
   - `assets/specs/openapi` → `static/openapi`
   - `assets/docs` → `docs/architecture`
3. Baut mit `npm run build`
4. Deploy zu GitHub Pages (`gh-pages` Branch, CNAME `docs.coherosphere.io`)

---

## 10. Sicherheits- und Governance-Checks

- **CORS + COEP + CORP** validiert in CI  
- **DNS** wird über `assets/config/dns/dns-records.json` geprüft  
- **SBOM (CycloneDX)** erzeugt aus OpenAPI, Event-Schemas, Workflows  
- **Audit-Trail:** Jede Änderung an einer Policy oder einem Schema muss einen Git-Commit-Hash referenzieren

---

## 11. Vollständigkeitsprüfung

AI- oder CI-System darf den Build nur als „valid“ markieren, wenn:
- alle 12 C2-Container vorhanden sind
- ≥ 30 C4-Sequenzen syntaktisch valide sind
- alle OpenAPI-Files `servers.url` und `version` enthalten
- alle Event-Schemas gültig gegen `ajv`
- alle Mermaid-Dateien renderbar sind
- Docusaurus erfolgreich baut

---

## 12. Erweiterung für maschinellen Build

Ein vollständiger AI-Build folgt dieser Reihenfolge:

1. **Parse:** alle C1–C4 + DDD Diagramme  
2. **Validiere:** OpenAPI, Events, Governance-Schemas  
3. **Generiere:** Code-Skeletons pro C2-Container  
4. **Integriere:** Policies (CORS, DNS, CI)  
5. **Kompiliere:** Docusaurus-Doku  
6. **Deploy:** Pages, API, App, Docs  

---

## 13. Lizenz & Offenheit

- Lizenz: **Creative Commons Attribution 4.0 (CC BY 4.0)**  
- Alle generierten Artefakte sind frei verwendbar, mit Namensnennung  
- Änderungen müssen als Pull Request mit gültigen CI-Checks erfolgen

---

## 14. Zuständigkeiten (CODEOWNERS)

| Bereich | Verantwortlich |
|----------|----------------|
| C2–C3 Architektur | Systemarchitektur-Team |
| OpenAPI + Events | API-Team |
| C4-Sequenzen | Governance & Treasury |
| CORS / DNS / CI | DevOps |
| Docusaurus Docs | Dokumentationsteam |

---

**Version:** 4.0  
**Stand:** Oktober 2025  
**Maintainer:** Coherosphere Collective  
**Lizenz:** CC BY 4.0
