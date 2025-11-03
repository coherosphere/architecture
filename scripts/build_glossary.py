#!/usr/bin/env python3
import os, re, json, hashlib
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime
try:
    import yaml  # type: ignore
except Exception:
    yaml = None

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(os.getenv("GLOSSARY_OUTPUT", ROOT / "docs" / "audit" / "glossary.md"))
CANON_PATH = ROOT / ".github" / "scripts" / "canonical_names.yaml"

EXCLUDES = {".git", ".github", "node_modules", ".venv", "dist", "build", ".docusaurus"}
MM_EXT = {".mmd"}
MD_EXT = {".md"}
JSON_EXT = {".json"}
YAML_EXT = {".yaml", ".yml"}  # optional, only if you add support below

# Mermaid regex (simple & robust)
RE_NODE_LABEL = re.compile(r'[A-Za-z0-9_]+\s*\[\s*"([^"]+)"\s*\]')
RE_SUBGRAPH_LABEL = re.compile(r'subgraph\s+[^\["\n]+?\s*\[\s*"([^"]+)"\s*\]', re.I)
RE_PARTICIPANT = re.compile(r'participant\s+[A-Za-z0-9_]+\s+as\s+(.+)$', re.I)

# Markdown headings as "terms"
RE_H1 = re.compile(r'^#\s+(.+)$')
RE_H2 = re.compile(r'^##\s+(.+)$')
RE_H3 = re.compile(r'^###\s+(.+)$')

# Event JSON fields to index
JSON_KEYS = ("title", "name", "summary")

# Optional deny/allow lists
DEFAULT_DENY = {
    "service", "api", "gateway", "event bus", "database", "db", "monitoring", "alerts",
    "participant", "note", "subgraph", "mermaid", "sequence diagram", "flowchart"
}
DEFAULT_ALLOW = set()

def load_canonical():
    if CANON_PATH.exists() and yaml is not None:
        try:
            data = yaml.safe_load(CANON_PATH.read_text(encoding="utf-8"))
            canonical = data.get("canonical", {})
            synonyms = data.get("synonyms", {})
            deny = set(map(str.lower, data.get("denylist", [])))
            allow = set(map(str.lower, data.get("allowlist", [])))
            return canonical, synonyms, deny, allow
        except Exception:
            pass
    return {}, {}, set(), set()

CANONICAL, SYNONYMS, DENY_EXT, ALLOW_EXT = load_canonical()
DENY = set(t.lower() for t in DEFAULT_DENY) | DENY_EXT
ALLOW = set(t.lower() for t in DEFAULT_ALLOW) | ALLOW_EXT

def norm(s: str) -> str:
    s = s.strip()
    s = re.sub(r'\s+', ' ', s)
    return s

def to_key(s: str) -> str:
    return norm(s).lower()

def canonicalize(term: str) -> str:
    key = to_key(term)
    if key in SYNONYMS:
        return SYNONYMS[key]
    return CANONICAL.get(key, term)

def layer_from_path(p: Path) -> str:
    s = str(p).replace("\\", "/").lower()
    if "/assets/diagrams/c1_" in s or "/c1_system/" in s:
        return "C1"
    if "/assets/diagrams/c2_" in s or "/c2_containers/" in s:
        return "C2"
    if "/assets/diagrams/c3_" in s or "/c3_components/" in s or "/c3_states/" in s or "/c3_models/" in s:
        return "C3"
    if "/assets/diagrams/c4_" in s or "/c4_sequences/" in s or "/c4_deployment/" in s:
        return "C4"
    if "/assets/diagrams/ddd/" in s:
        return "DDD"
    if "/assets/diagrams/overview/" in s:
        return "Overview"
    if "/assets/specs/events/" in s:
        return "Events"
    return "Other"

def iter_files(root: Path):
    for dirpath, dirnames, filenames in os.walk(root):
        rel = Path(dirpath).relative_to(root)
        if any(part in EXCLUDES for part in rel.parts):
            continue
        for fn in filenames:
            p = Path(dirpath) / fn
            yield p

def extract_terms_from_mmd(p: Path):
    terms = []
    try:
        text = p.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return terms
    for r in (RE_NODE_LABEL, RE_SUBGRAPH_LABEL):
        for m in r.finditer(text):
            terms.append(norm(m.group(1)))
    for m in RE_PARTICIPANT.finditer(text):
        terms.append(norm(m.group(1)))
    return terms

def extract_terms_from_md(p: Path):
    terms = []
    try:
        for line in p.read_text(encoding="utf-8", errors="ignore").splitlines():
            for rx in (RE_H1, RE_H2, RE_H3):
                m = rx.match(line)
                if m:
                    terms.append(norm(m.group(1)))
    except Exception:
        pass
    return terms

def extract_terms_from_json(p: Path):
    terms = []
    try:
        obj = json.loads(p.read_text(encoding="utf-8", errors="ignore"))
    except Exception:
        return terms
    def walk(o):
        if isinstance(o, dict):
            for k,v in o.items():
                if k in JSON_KEYS and isinstance(v, str):
                    terms.append(norm(v))
                else:
                    walk(v)
        elif isinstance(o, list):
            for x in o:
                walk(x)
    walk(obj)
    return terms

def should_keep(term: str) -> bool:
    key = to_key(term)
    if key in DENY:
        return False
    if ALLOW and key not in ALLOW:
        return False
    if len(key) <= 2:
        return False
    return True

def main():
    by_layer = defaultdict(list)
    origin_map = defaultdict(list)

    for p in iter_files(ROOT):
        ext = p.suffix.lower()
        terms = []
        if ext in MM_EXT:
            terms = extract_terms_from_mmd(p)
        elif ext in MD_EXT:
            terms = extract_terms_from_md(p)
        elif ext in JSON_EXT and "assets/specs/events/" in str(p).replace("\\","/"):
            terms = extract_terms_from_json(p)
        else:
            continue

        layer = layer_from_path(p)
        for t in terms:
            if not t:
                continue
            if not should_keep(t):
                continue
            ct = canonicalize(t)
            by_layer[layer].append(ct)
            origin_map[(layer, ct)].append(str(p.relative_to(ROOT)))

    # Stable dedupe per layer
    for layer in list(by_layer.keys()):
        seen = set()
        deduped = []
        for v in by_layer[layer]:
            if v not in seen:
                seen.add(v)
                deduped.append(v)
        by_layer[layer] = deduped

    global_counter = Counter()
    for layer, terms in by_layer.items():
        global_counter.update(terms)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    max_top = int(os.getenv("MAX_TOP_TERMS", "50"))

    lines = []
    lines.append("# Repository Glossary")
    lines.append("")
    lines.append(f"_Generated_: {datetime.utcnow().isoformat()}Z")
    lines.append("")
    lines.append("This document is auto-generated from Mermaid (`.mmd`), Markdown (`.md`), and Event specs (`assets/specs/events/*.json`).")
    if CANON_PATH.exists():
        lines.append("Canonicalization and synonyms are applied from `.github/scripts/canonical_names.yaml`.")
    lines.append("")

    lines.append("## Overview (Top Terms)")
    lines.append("")
    lines.append("Term | Count")
    lines.append("---|---")
    for term, cnt in global_counter.most_common(max_top):
        lines.append(f"{term} | {cnt}")
    lines.append("")

    for layer in sorted(by_layer.keys()):
        terms = by_layer[layer]
        lines.append(f"## {layer}")
        lines.append("")
        lines.append("Term | Sources")
        lines.append("---|---")
        for t in terms:
            srcs = sorted(set(origin_map[(layer, t)]))[:8]
            src_str = "<br>".join(srcs)
            lines.append(f"{t} | {src_str}")
        lines.append("")

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT}")

if __name__ == "__main__":
    main()
