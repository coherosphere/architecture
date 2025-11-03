#!/usr/bin/env python3
"""
Builds a repository glossary by scanning Mermaid (.mmd), Markdown (.md),
and Event spec JSON files under assets/specs/events/**.

Features:
- MDX-safe output (escapes <, >, |, {, })
- self-closing <br /> for compatibility
- "Other" rendered as clean alphabetical bullet list
- ignores its own output file to avoid recursion
"""

import os
import re
import json
import html
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime

try:
    import yaml  # optional for canonical names/synonyms
except Exception:
    yaml = None

# ---------------------------------------------------------------------------
# Repo & Config
# ---------------------------------------------------------------------------

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(os.getenv("GLOSSARY_OUTPUT", "assets/docs/audit/glossary.md"))
CANON_PATH = ROOT / "scripts" / "canonical_names.yaml"

EXCLUDES = {
    ".git", ".github", "node_modules", ".venv", "dist", "build",
    ".docusaurus", ".cache"
}
MM_EXT = {".mmd"}
MD_EXT = {".md"}
JSON_EXT = {".json"}

DEFAULT_DENY = {
    "service", "api", "gateway", "event bus", "database", "db", "monitoring", "alerts",
    "participant", "note", "subgraph", "mermaid", "sequence diagram", "flowchart",
    "readme", "license", "changelog", "contributing"
}
DEFAULT_ALLOW = set()


# ---------------------------------------------------------------------------
# Utility functions
# ---------------------------------------------------------------------------

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
    if "/docs/" in s:
        name = s.split("/docs/")[-1]
        if name.startswith("c1-"): return "C1"
        if name.startswith("c2-"): return "C2"
        if name.startswith("c3-"): return "C3"
        if name.startswith("c4-"): return "C4"
        if name.startswith("ddd-"): return "DDD"
        if "overview" in name: return "Overview"
        return "Docs"
    return "Other"


def iter_files(root: Path):
    """Yield files under root, skipping EXCLUDES."""
    for dirpath, _, filenames in os.walk(root):
        rel = Path(dirpath).relative_to(root)
        if any(part in EXCLUDES for part in rel.parts):
            continue
        for fn in filenames:
            yield Path(dirpath) / fn


# ---------------------------------------------------------------------------
# Extractors
# ---------------------------------------------------------------------------

RE_NODE_LABEL     = re.compile(r'[A-Za-z0-9_]+\s*\[\s*"([^"]+)"\s*\]')
RE_SUBGRAPH_LABEL = re.compile(r'subgraph\s+[^\["\n]+?\s*\[\s*"([^"]+)"\s*\]', re.I)
RE_PARTICIPANT    = re.compile(r'participant\s+[A-Za-z0-9_]+\s+as\s+(.+)$', re.I)
RE_STATE_LABEL    = re.compile(r'state\s+"([^"]+)"', re.I)
RE_H1 = re.compile(r'^\#\s+(.+)$')
RE_H2 = re.compile(r'^\#\#\s+(.+)$')
RE_H3 = re.compile(r'^\#\#\#\s+(.+)$')
JSON_KEYS = ("title", "name", "summary")


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


# ---------------------------------------------------------------------------
# MDX Escaping and Rendering
# ---------------------------------------------------------------------------

def _escape_mdx(s: str) -> str:
    """Make any text safe for Docusaurus MDX tables and lists."""
    if s is None:
        return ""
    s = html.escape(str(s), quote=False)
    s = s.replace("|", r"\|")
    s = s.replace("{", r"\{").replace("}", r"\}")
    s = re.sub(r"\s*\n\s*", "; ", s)
    s = re.sub(r"[ \t]{2,}", " ", s)
    return s.strip()


def render_table_section(title: str, rows: list, columns: list) -> str:
    """Render one glossary section as Markdown table."""
    out = [f"## {title}", ""]
    header = " | ".join(col[0] for col in columns)
    sep = " | ".join("---" for _ in columns)
    out.append(header)
    out.append(sep)
    for r in rows:
        cells = []
        for label, key in columns:
            val = r.get(key, "")
            if isinstance(val, (list, tuple, set)):
                val = ", ".join(_escape_mdx(x) for x in val)
            else:
                val = _escape_mdx(val)
            cells.append(val)
        out.append(" | ".join(cells))
    out.append("")
    return "\n".join(out)


def render_other_section(other_terms: list) -> str:
    """Render the 'Other' section as alphabetical bullet list."""
    if not other_terms:
        return ""
    normalized = []
    for r in other_terms:
        term = _escape_mdx(r.get("term", ""))
        files = r.get("files") or []
        notes = _escape_mdx(r.get("notes", ""))
        files_list = ", ".join(_escape_mdx(f) for f in files)
        normalized.append((term.lower(), term, files_list, notes))

    normalized.sort(key=lambda x: x[0])
    out = ["## Other", ""]
    current_letter = None
    for _, term, files_list, notes in normalized:
        first = term[:1].upper() if term else "#"
        if first != current_letter:
            current_letter = first
            out.append(f"### {current_letter}")
        line = f"- **{term}**"
        meta = []
        if files_list:
            meta.append(f"_appears in:_ {files_list}")
        if notes:
            meta.append(f"_notes:_ {notes}")
        if meta:
            line += " — " + "; ".join(meta)
        out.append(line)
    out.append("")
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    by_layer = defaultdict(list)
    origin_map = defaultdict(list)

    out_abs = (ROOT / OUT).resolve()
    out_rel_norm = str(OUT).replace("\\", "/")

    for p in iter_files(ROOT):
        # Skip generated file
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

    # Deduplicate
    for layer, terms in by_layer.items():
        by_layer[layer] = list(dict.fromkeys(terms))

    # Drop trivial singletons in "Other"
    filtered_by_layer = defaultdict(list)
    for layer, terms in by_layer.items():
        if layer != "Other":
            filtered_by_layer[layer] = terms
            continue
        keep = []
        for t in terms:
            if len(set(origin_map[(layer, t)])) > 1:
                keep.append(t)
        filtered_by_layer["Other"] = keep
    by_layer = filtered_by_layer

    # Collect rows per layer
    layer_rows = {}
    for layer, terms in by_layer.items():
        rows = []
        for t in terms:
            files = sorted(set(origin_map[(layer, t)]))
            rows.append({"term": t, "files": files})
        layer_rows[layer] = rows

    # Write MDX-safe Markdown
    (ROOT / OUT).parent.mkdir(parents=True, exist_ok=True)
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
    all_terms = [t for terms in by_layer.values() for t in terms]
    counts = Counter(all_terms)
    lines.append("## Overview (Top Terms)")
    lines.append("")
    lines.append("Term | Count")
    lines.append("---|---")
    for term, cnt in counts.most_common(50):
        lines.append(f"{_escape_mdx(term)} | {cnt}")
    lines.append("")

    # Layer sections
    for layer in sorted(k for k in layer_rows.keys() if k != "Other"):
        lines.append(render_table_section(
            layer,
            layer_rows[layer],
            [("Term", "term"), ("Appears in", "files")]
        ))

    # Other as bullet list
    lines.append(render_other_section(layer_rows.get("Other", [])))

    (ROOT / OUT).write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
