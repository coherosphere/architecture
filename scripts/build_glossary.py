
#!/usr/bin/env python3
# (file: scripts/build_glossary.py)
"""
Final build_glossary.py — MDX-safe, canonicalized, consistent sections.
Fix: Markdown tables now use leading & trailing pipes on header, separator, and rows.
"""
import os, re, json, html
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime

try:
    import yaml
except Exception:
    yaml = None

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(os.getenv("GLOSSARY_OUTPUT", "assets/docs/audit/glossary.md"))
CANON_PATH = ROOT / "scripts" / "canonical_names.yaml"

EXCLUDES = {".git",".github","node_modules",".venv","dist","build",".docusaurus",".cache"}
MM_EXT = {".mmd"}
MD_EXT = {".md"}
JSON_EXT = {".json"}

DEFAULT_DENY = {
    "service","api","gateway","event bus","database","db","monitoring","alerts",
    "participant","note","subgraph","mermaid","sequence diagram","flowchart",
    "readme","license","changelog","contributing","table of contents","breadcrumbs","badges"
}
DEFAULT_ALLOW = set()

MD_ALLOWED_PREFIXES = ("docs/","assets/diagrams/","assets/specs/events/")

def load_canonical():
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

def norm(s:str)->str:
    s = (s or "").strip()
    return re.sub(r"\s+"," ",s)

def to_key(s:str)->str:
    return norm(s).lower()

def canonicalize(term:str)->str:
    key = to_key(term)
    if key in SYNONYMS: return SYNONYMS[key]
    return CANONICAL.get(key, term)

def layer_from_path(p:Path)->str:
    s = str(p).replace("\\","/").lower()
    if "/assets/diagrams/c1_" in s or "/c1_system/" in s: return "C1"
    if "/assets/diagrams/c2_" in s or "/c2_containers/" in s: return "C2"
    if ("/assets/diagrams/c3_" in s or "/c3_components/" in s or "/c3_states/" in s or "/c3_models/" in s): return "C3"
    if "/assets/diagrams/c4_" in s or "/c4_sequences/" in s or "/c4_deployment/" in s: return "C4"
    if "/assets/diagrams/ddd/" in s: return "DDD"
    if "/assets/diagrams/overview/" in s: return "Overview"
    if "/assets/specs/events/" in s: return "Events"
    if "/docs/" in s:
        name = s.split("/docs/")[-1]
        if name.startswith("c1-"): return "C1"
        if name.startswith("c2-"): return "C2"
        if name.startswith("c3-"): return "C3"
        if name.startswith("c4-"): return "C4"
        if name.startswith("ddd-"): return "DDD"
        if "overview" in name: return "Overview"
        return "Docs"
    if any(t in s for t in ("/.github/","/ci/","/scripts/","openapi","workflow")): return "CI & Tooling"
    if any(t in s for t in ("/dns/","cors","domain","manifest")): return "Config & Domains"
    return "Other"

def iter_files(root:Path):
    for dirpath,_,filenames in os.walk(root):
        rel = Path(dirpath).relative_to(root)
        if any(part in EXCLUDES for part in rel.parts): continue
        for fn in filenames:
            yield Path(dirpath)/fn

RE_NODE_LABEL     = re.compile(r'[A-Za-z0-9_]+\s*\[\s*"([^"]+)"\s*\]')
RE_SUBGRAPH_LABEL = re.compile(r'subgraph\s+[^\["\n]+?\s*\[\s*"([^"]+)"\s*\]', re.I)
RE_PARTICIPANT    = re.compile(r'participant\s+[A-Za-z0-9_]+\s+as\s+(.+)$', re.I)
RE_STATE_LABEL    = re.compile(r'state\s+"([^"]+)"', re.I)
RE_H1 = re.compile(r'^\#\s+(.+)$')
RE_H2 = re.compile(r'^\#\#\s+(.+)$')
RE_H3 = re.compile(r'^\#\#\#\s+(.+)$')
JSON_KEYS = ("title","name","summary")

def extract_terms_from_mmd(p:Path):
    terms=[]
    try: text = p.read_text(encoding="utf-8", errors="ignore")
    except Exception: return terms
    for r in (RE_NODE_LABEL, RE_SUBGRAPH_LABEL, RE_STATE_LABEL):
        for m in r.finditer(text): terms.append(norm(m.group(1)))
    for m in RE_PARTICIPANT.finditer(text): terms.append(norm(m.group(1)))
    return terms

def extract_terms_from_md(p:Path):
    rel = str(p.relative_to(ROOT)).replace("\\","/")
    if not rel.startswith(MD_ALLOWED_PREFIXES): return []
    terms=[]
    try:
        for line in p.read_text(encoding="utf-8", errors="ignore").splitlines():
            for rx in (RE_H1, RE_H2, RE_H3):
                m = rx.match(line)
                if m: terms.append(norm(m.group(1)))
    except Exception: pass
    return terms

def extract_terms_from_json(p:Path):
    terms=[]
    try: obj = json.loads(p.read_text(encoding="utf-8", errors="ignore"))
    except Exception: return terms
    def walk(o):
        if isinstance(o, dict):
            for k,v in o.items():
                if k in JSON_KEYS and isinstance(v,str): terms.append(norm(v))
                else: walk(v)
        elif isinstance(o, list):
            for x in o: walk(x)
    walk(obj); return terms

def should_keep(term:str)->bool:
    key = to_key(term)
    if key in DENY: return False
    if ALLOW and key not in ALLOW: return False
    if len(key) <= 2: return False
    return True

def _escape_mdx(s:str)->str:
    """Escape content for MDX tables safely: keep pipes literal by escaping them and collapse newlines."""
    if s is None: return ""
    s = html.escape(str(s), quote=False)
    s = s.replace("|", r"\|")  # ensure table cells don't break
    s = s.replace("{", r"\{").replace("}", r"\}")
    s = re.sub(r"\s*\n\s*", "; ", s)
    s = re.sub(r"[ \t]{2,}", " ", s)
    return s.strip()

def _mk_table_row(cells:list)->str:
    """Render a table row with leading & trailing pipes."""
    return "| " + " | ".join(cells) + " |"

def render_table_section(title:str, rows:list, columns:list)->str:
    """Render a markdown table with proper leading/trailing pipes."""
    out=[f"## {title}",""]
    header=_mk_table_row([col[0] for col in columns])
    sep=_mk_table_row([":---" for _ in columns])  # left-align
    out.append(header); out.append(sep)
    for r in rows:
        cells=[]
        for _,key in columns:
            val=r.get(key,"")
            if isinstance(val,(list,tuple,set)):
                val=", ".join(_escape_mdx(x) for x in val)
            else:
                val=_escape_mdx(val)
            cells.append(val)
        out.append(_mk_table_row(cells))
    out.append("")
    return "\n".join(out)

def render_other_section(other_terms:list)->str:
    if not other_terms: return ""
    normd=[]
    for r in other_terms:
        term=_escape_mdx(r.get("term",""))
        files=r.get("files") or []
        notes=_escape_mdx(r.get("notes",""))
        files_list=", ".join(_escape_mdx(f) for f in files)
        normd.append((term.lower(),term,files_list,notes))
    normd.sort(key=lambda x:x[0])
    out=["## Other",""]
    current=None
    for _,term,files_list,notes in normd:
        first=term[:1].upper() if term else "#"
        if first!=current:
            current=first
            out.append(f"### {current}")
        line=f"- **{term}**"
        meta=[]
        if files_list: meta.append(f"_appears in:_ {files_list}")
        if notes: meta.append(f"_notes:_ {notes}")
        if meta: line+=" — "+"; ".join(meta)
        out.append(line)
    out.append("")
    return "\n".join(out)

def main():
    by_layer=defaultdict(list)
    origin_map=defaultdict(list)

    out_abs=(ROOT/OUT).resolve()
    out_rel_norm=str(OUT).replace("\\","/")

    for p in iter_files(ROOT):
        if str(p.resolve())==str(out_abs): continue
        if str(p).replace("\\","/").endswith(out_rel_norm): continue

        ext=p.suffix.lower()
        terms=[]
        if ext in MM_EXT: terms=extract_terms_from_mmd(p)
        elif ext in MD_EXT: terms=extract_terms_from_md(p)
        elif ext in JSON_EXT and "assets/specs/events/" in str(p).replace("\\","/"):
            terms=extract_terms_from_json(p)
        else: continue

        layer=layer_from_path(p)
        rel_path=str(p.relative_to(ROOT)).replace("\\","/")
        for t in terms:
            if not t or not should_keep(t): continue
            ct=canonicalize(t)
            by_layer[layer].append(ct)
            origin_map[(layer,ct)].append(rel_path)

    # Deduplicate per layer
    for layer,terms in by_layer.items():
        by_layer[layer]=list(dict.fromkeys(terms))

    # Drop trivial singletons in Other
    filtered=defaultdict(list)
    for layer,terms in by_layer.items():
        if layer!="Other":
            filtered[layer]=terms; continue
        keep=[]
        for t in terms:
            if len(set(origin_map[(layer,t)]))>1: keep.append(t)
        filtered["Other"]=keep
    by_layer=filtered

    # Rows per layer
    layer_rows={}
    for layer,terms in by_layer.items():
        rows=[]
        for t in terms:
            files=sorted(set(origin_map[(layer,t)]))
            rows.append({"term":t,"files":files})
        layer_rows[layer]=rows

    # Canonicalized Top Terms
    all_terms_canon=[canonicalize(r["term"]) for rows in layer_rows.values() for r in rows]
    counts=Counter(all_terms_canon)

    # Write MDX-safe Markdown with Front Matter
    (ROOT/OUT).parent.mkdir(parents=True, exist_ok=True)
    lines=[]
    lines.append("---")
    lines.append("id: glossary")
    lines.append("title: Repository Glossary")
    lines.append('description: Auto-generated glossary across diagrams, docs, and specs (canonicalized & MDX-safe).')
    lines.append("sidebar_label: Glossary")
    lines.append("---")
    lines.append("")
    lines.append(f"_Generated_: {datetime.utcnow().isoformat()}Z")
    lines.append("")
    lines.append("This page is auto-generated from Mermaid (`.mmd`), Markdown (`.md`), and Event specs (`assets/specs/events/*.json`).")
    if CANON_PATH.exists():
        lines.append("Canonicalization and synonyms are applied from `scripts/canonical_names.yaml`.")
    lines.append("")

    # Overview table with proper pipes
    lines.append("## Overview (Top Terms)")
    lines.append("")
    header = "| Term | Count |"
    sep    = "| :--- | :---: |"
    lines.append(header)
    lines.append(sep)
    for term,cnt in counts.most_common(50):
        lines.append("| " + _escape_mdx(term) + " | " + str(cnt) + " |")
    lines.append("")

    SECTION_ORDER=["C1","C2","C3","C4","DDD","Overview","Docs","Events","CI & Tooling","Config & Domains"]
    for section in SECTION_ORDER:
        if section in layer_rows and layer_rows[section]:
            lines.append(render_table_section(section, layer_rows[section], [("Term","term"),("Sources","files")]))

    lines.append(render_other_section(layer_rows.get("Other",[])))

    (ROOT/OUT).write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT}")

if __name__=="__main__":
    main()
