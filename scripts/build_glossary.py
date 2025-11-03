#!/usr/bin/env python3
"""
Builds a repository glossary by scanning Mermaid (.mmd), Markdown (.md),
and Event spec JSON files under assets/specs/events/**.
MDX-safe output (self-closing <br />, table cell escaping including braces).

Usage (in GitHub Actions or locally):
  GLOSSARY_OUTPUT="assets/docs/audit/glossary.md" python scripts/build_glossary.py
"""

import os
import re
import json
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime

try:
    import yaml  # optional; used for canonical names/synonyms
except Exception:
    yaml = None

# --- Repo layout -------------------------------------------------------------
# Script is located at repo_root/scripts/build_glossary.py
ROOT = Path(__file__).resolve().parents[1]

# Output file (relative to repo root). Example: assets/docs/audit/glossary.md
OUT = Path(os.getenv("GLOSSARY_OUTPUT", "assets/docs/audit/glossary.md"))

# Optional canonical/synonym file (relative to repo root)
CANON_PATH = ROOT / "scripts" / "canonical_names.yaml"

# --- Scanning config ---------------------------------------------------------
EXCLUDES = {
    ".git", ".github", "node_modules", ".venv", "dist", "build", ".docusaurus", ".cache"
}
MM_EXT = {".mmd"}
MD_EXT = {".md"}
JSON_EXT = {".json"}

# Mermaid patterns (robust label extraction; not a full parser)
RE_NODE_LABEL       = re.compile(r'[A-Za-z0-9_]+\s*\[\s*"([^"]+)"\s*\]')
RE_SUBGRAPH_LABEL   = re.compile(r'subgraph\s+[^\["\n]+?\s*\[\s*"([^"]+)"\s*\]', re.I)
RE_PARTICIPANT      = re.compile(r'participant\s+[A-Za-z0-9_]+\s+as\s+(.+)$', re.I)
RE_STATE_LABEL      = re.compile(r'state\s+"([^"]+)"', re.I)  # stateDiagram notes

# Markdown headings as “terms”
RE_H1 = re.compile(r'^\#\s+(.+)$')
RE_H2 = re.compile(r'^\#\#\s+(.+)$')
RE_H3 = re.compile(r'^\#\#\#\s+(.+)$')

# JSON fields to pick
JSON_KEYS = ("title", "name", "summary")

# Default deny/allow lists (lowercased)
DEFAULT_DENY = {
    "service", "api", "gateway", "event bus", "database", "db", "monitoring", "alerts",
    "participant", "note", "subgraph", "mermaid", "sequence diagram", "flowchart"
}
DEFAULT_ALLOW = set()  # empty means allow all not-denied


# --- Helpers -----------------------------------------------------------------
def load_canonical():
    """Load canonical forms / synonyms / deny & allow lists from YAML."""
    if CANON_PATH.exists() and yaml is not None:
        try:
            data = yaml.safe_load(CANON_PATH.read_text(encoding="utf-8"))
            canonical = data.get("canonical", {}) or {}
            synonyms  = data.get("synonyms",  {}) or {}
            deny      = set(map(str.lower, data.get("denylist",  []) or []))
            allow     = set(map(str.lower, data.get("allowlist", []) or []))
            return canonical, synonyms, deny, allow
        except Exception:
            pass
    return {}, {}, set(), set()


CANONICAL, SYNONYMS, DENY_EXT, ALLOW_EXT = load_canonical()
DENY  = set(t.lower() for t in DEFAULT_DENY) | DENY_EXT
ALLOW = set(t.lower() for t in DEFAULT_ALLOW) | ALLOW_EXT


def norm(s: str) -> str:
    s = (s or "").strip()
    s = re.sub(r"\s+", " ", s)
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
    if ("/assets/diagrams/c3_" in s or "/c3_components/" in s
        or "/c3_states/" in s or "/c3_models/" in s):
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
    """Yield files under root, skipping EXCLUDES."""
    for dirpath, dirnames, filenames in os.walk(root):
        rel = Path(dirpath).relative_to(root)
        if any(part in EXCLUDES for part in rel.parts):
            continue
        for fn in filenames:
            yield Path(dirpath) / fn


def extract_terms_from_mmd(p: Path):
    terms = []
    try:
        text = p.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return terms
    for r in (RE_NODE_LABEL, RE_SUBGRAPH_LABEL, RE_STATE_LABEL):
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
                    terms.append(norm(m.group(1))))
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
            for k, v in o.items():
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


# --- MDX-safe escaping -------------------------------------------------------
def mdx_cell(s: str) -> str:
    """Escape content for MDX table cells (HTML + pipe + MDX braces)."""
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    s = s.replace("|", "&#124;")
    # Prevent MDX expression evaluation like {id}
    s = s.replace("{", "&#123;").replace("}", "&#125;")
    return s


def main():
    by_layer = defaultdict(list)
    origin_map = defaultdict(list)

    out_abs = (ROOT / OUT).resolve()
    out_rel_norm = str(OUT).replace("\\", "/")

    for p in iter_files(ROOT):
        # Skip generated output to avoid re-ingesting our own file
        if str(p.resolve()) == str(out_abs):
            continue
        if str(p).replace("\\", "/").endswith(out_rel_norm):
            continue

        ext = p.suffix.lower()
        terms = []
        if ext in MM_EXT:
            terms = extract_terms_from_mmd(p)
        elif ext in MD_EXT:
            terms = extract_terms_from_md(p)
        elif ext in JSON_EXT and "assets/specs/events/" in str(p).replace("\\", "/"):
            terms = extract_terms_from_json(p)
        else:
            continue

        layer = layer_from_path(p)
        rel_path = str(p.relative_to(ROOT)).replace("\\", "/")
        for t in terms:
            if not t or not should_keep(t):
                continue
            ct = canonicalize(t)
            by_layer[layer].append(ct)
            origin_map[(layer, ct)].append(rel_path)

    # Stable dedupe per layer
    for layer in list(by_layer.keys()):
        seen, deduped = set(), []
        for v in by_layer[layer]:
            if v not in seen:
                seen.add(v)
                deduped.append(v)
        by_layer[layer] = deduped

    # Global counts
    global_counter = Counter()
    for layer, terms in by_layer.items():
        global_counter.update(terms)

    # Write MDX-safe Markdown
    (ROOT / OUT).parent.mkdir(parents=True, exist_ok=True)
    max_top = int(os.getenv("MAX_TOP_TERMS", "50"))

    lines = []
    lines.append("# Repository Glossary")
    lines.append("")
    lines.append(f"_Generated_: {datetime.utcnow().isoformat()}Z")
    lines.append("")
    lines.append("This document is auto-generated from Mermaid (`.mmd`), Markdown (`.md`), and Event specs (`assets/specs/events/*.json`).")
    if CANON_PATH.exists():
        lines.append("Canonicalization and synonyms are applied from `scripts/canonical_names.yaml`.")
    lines.append("")

    # Overview
    lines.append("## Overview (Top Terms)")
    lines.append("")
    lines.append("Term | Count")
    lines.append("---|---")
    for term, cnt in global_counter.most_common(max_top):
        lines.append(f"{mdx_cell(term)} | {cnt}")
    lines.append("")

    # Per layer
    for layer in sorted(by_layer.keys()):
        terms = by_layer[layer]
        lines.append(f"## {layer}")
        lines.append("")
        lines.append("Term | Sources")
        lines.append("---|---")
        for t in terms:
            srcs = sorted(set(origin_map[(layer, t)]))[:8]
            srcs = [mdx_cell(x) for x in srcs]
            # MDX requires self-closing <br /> inside tables
            src_str = "<br />".join(srcs)
            lines.append(f"{mdx_cell(t)} | {src_str}")
        lines.append("")

    (ROOT / OUT).write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
