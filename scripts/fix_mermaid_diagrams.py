#!/usr/bin/env python3
import re, sys, json
from pathlib import Path

SRC = Path("assets/diagrams")
OUT = Path("assets/.mermaid_clean")

FRONTMATTER_RE = re.compile(r"^\s*---\s*$", re.MULTILINE)
TITLE_RE       = re.compile(r"^\s*title\s*:\s*\"?([^\n\"]+)\"?\s*$", re.IGNORECASE)
LAYOUT_RE      = re.compile(r"^\s*config\s*:\s*(?:\n|\r\n)([\s\S]*?)$", re.IGNORECASE)
LAYOUT_LINE_RE = re.compile(r"^\s*layout\s*:\s*([A-Za-z0-9_-]+)\s*$", re.MULTILINE)

# Erlaubte Start-Direktiven in Mermaid
DIA_START_RE   = re.compile(r"^\s*(flowchart|sequenceDiagram|stateDiagram-v2|classDiagram|erDiagram|journey|gantt|pie)\b")

def split_frontmatter(txt: str):
    """Find frontmatter block (--- ... ---) at file start."""
    m = list(FRONTMATTER_RE.finditer(txt))
    if len(m) >= 2 and m[0].start() == 0:
        start = m[0].end()
        end   = m[1].start()
        front = txt[start:end]
        rest  = txt[m[1].end():]
        return front, rest
    return None, txt

def extract_title(front: str):
    if not front: return None
    mt = TITLE_RE.search(front)
    return mt.group(1).strip() if mt else None

def extract_layout(front: str):
    if not front: return None
    # Grob den config-Block aufnehmen und dort nach "layout:" suchen
    ml = LAYOUT_RE.search(front)
    if not ml: return None
    cfg_block = ml.group(1)
    mlayout = LAYOUT_LINE_RE.search(cfg_block)
    return mlayout.group(1).strip() if mlayout else None

def has_init_directive(txt: str):
    return "%%{init:" in txt

def ensure_single_graph_start(txt: str):
    """Sicherstellen, dass die erste Diagramm-Direktive in eigener Zeile sauber beginnt."""
    # Entferne führende BOM/Whitespace
    txt = txt.lstrip("\ufeff\r\n\t ")
    # Falls zwei Direktiven direkt aneinander kleben (z.B. ...}%%flowchart), Newline einfügen
    txt = re.sub(r"(%%\{init:[^\n]*\}\%\%)(\s*)(?=(\S))", r"\1\n\n", txt, count=1)
    # Falls 'title' Kommentar direkt vor der Direktive ohne LF klebt, Newline einfügen
    txt = re.sub(r"(%%\s*title:.*?%%)(\s*)(?=(\S))", r"\1\n\n", txt, count=1, flags=re.IGNORECASE)
    return txt

def build_header(title, layout, already_has_init):
    lines = []
    if layout and not already_has_init:
        # Minimal gültige init-Direktive
        lines.append(f'%%{{init: {{"config":{{"layout":"{layout}"}}}}}}%%')
    if title:
        # Nur Kommentar, Mermaid-Parser-sicher
        lines.append(f'%% title: {title} %%')
    # Zwei Zeilen Abstand vor Diagramm-Direktive (reduziert Klebe-Risiko)
    if lines:
        lines.append("")
    return "\n".join(lines)

def process_one(src: Path, dst: Path):
    raw = src.read_text(encoding="utf-8")
    front, rest = split_frontmatter(raw)
    title  = extract_title(front) if front is not None else None
    layout = extract_layout(front) if front is not None else None

    # Falls bereits init existiert, nicht doppelt einfügen
    already_has_init = has_init_directive(rest)

    header = build_header(title, layout, already_has_init)
    body   = ensure_single_graph_start(rest)

    # Safety: Falls der Body nicht mit einer der Diagramm-Direktiven startet, unverändert lassen
    # (wir wollen nur Frontmatter bereinigen, nichts "reparieren", was evtl. kein Mermaid ist).
    check = body.lstrip()
    if not DIA_START_RE.match(check) and not already_has_init:
        # Trotzdem Titel-Kommentar zulassen, aber kein init erzwingen
        header = ("\n".join([l for l in header.splitlines() if not l.startswith("%%{init:")]) + "\n").lstrip()

    out = (header + body).lstrip()

    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(out, encoding="utf-8")

def main():
    processed = []
    skipped = []
    for src in SRC.rglob("*.mmd"):
        rel = src.relative_to(SRC)
        dst = OUT / rel
        try:
            process_one(src, dst)
            processed.append(str(rel))
        except Exception as e:
            skipped.append({"file": str(rel), "error": str(e)})
    print(json.dumps({
        "status": "ok",
        "report": {
            "source": str(SRC.resolve()),
            "output": str(OUT.resolve()),
            "processed": processed,
            "skipped": skipped
        }
    }, indent=2))

if __name__ == "__main__":
    main()