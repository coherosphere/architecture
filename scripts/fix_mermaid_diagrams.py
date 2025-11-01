#!/usr/bin/env python3
"""
Create cleaned, renderable copies of Mermaid .mmd files without modifying originals.

- Reads:  assets/diagrams/**/*.mmd
- Writes: assets/.mermaid_clean/<same relative path>

Cleans:
  • UTF-8 BOM
  • YAML frontmatter blocks at file start (--- ... ---)
  • Markdown code fences ```mermaid ... ```
  • Stray 'title:' / 'config:' headers *before* the Mermaid directive
  • CRLF → LF, ensures trailing newline

Keeps:
  • Mermaid comments (%% ...)
  • init blocks (%%{init: ...}%%)
  • Everything after the first valid Mermaid directive

Exit code 0 with a small JSON report.
"""

from __future__ import annotations
import sys, json, re, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  # repo root (…/architecture)
SRC_DIR = ROOT / "assets" / "diagrams"
OUT_DIR = ROOT / "assets" / ".mermaid_clean"

VALID_STARTERS = (
    "flowchart", "graph", "sequenceDiagram", "classDiagram",
    "stateDiagram-v2", "stateDiagram", "erDiagram", "gantt",
    "journey", "pie", "quadrantChart", "mindmap", "timeline", "gitGraph"
)

FRONTMATTER_START = re.compile(r'^\s*---\s*$')
FRONTMATTER_END   = re.compile(r'^\s*---\s*$')
CODEFENCE_START   = re.compile(r'^\s*```(?:mermaid)?\s*$', re.IGNORECASE)
CODEFENCE_END     = re.compile(r'^\s*```\s*$')

def strip_bom(text: str) -> str:
    return text.lstrip('\ufeff')

def normalize_newlines(text: str) -> str:
    return text.replace('\r\n', '\n').replace('\r', '\n')

def split_lines(text: str) -> list[str]:
    return text.split('\n')

def strip_frontmatter(lines: list[str]) -> list[str]:
    """Remove YAML frontmatter only if it is the very first block."""
    if not lines:
        return lines
    i = 0
    # skip leading blank lines
    while i < len(lines) and not lines[i].strip():
        i += 1
    if i < len(lines) and FRONTMATTER_START.match(lines[i]):
        i += 1
        while i < len(lines) and not FRONTMATTER_END.match(lines[i]):
            i += 1
        if i < len(lines):
            i += 1  # drop the closing ---
        # drop any blank lines following frontmatter
        while i < len(lines) and not lines[i].strip():
            i += 1
        return lines[i:]
    return lines

def strip_markdown_fence(lines: list[str]) -> list[str]:
    """Remove a top-level ``` or ```mermaid fence pair if present."""
    if not lines:
        return lines
    i = 0
    while i < len(lines) and not lines[i].strip():
        i += 1
    if i < len(lines) and CODEFENCE_START.match(lines[i]):
        i += 1
        body = []
        while i < len(lines) and not CODEFENCE_END.match(lines[i]):
            body.append(lines[i])
            i += 1
        # if we found a closing fence, consume it; else, keep what we have
        return body
    return lines

def is_mermaid_directive(line: str) -> bool:
    s = line.strip()
    if not s or s.startswith('%%'):
        return False
    # allow init block as prelude
    if s.startswith('%%{') and s.endswith('}%%'):
        return False
    return any(s.startswith(k) for k in VALID_STARTERS)

def clean_prelude(lines: list[str]) -> list[str]:
    """
    Drop any non-mermaid headers (e.g., 'title:' or 'config:' YAML-ish lines)
    that appear *before* the first real mermaid directive. Keep comments and init blocks.
    """
    out = []
    seen_directive = False
    i = 0
    while i < len(lines):
        line = lines[i]
        s = line.strip()

        if not seen_directive:
            if s.startswith('%%'):            # keep comments
                out.append(line)
            elif s.startswith('%%{') and s.endswith('}%%'):  # keep init
                out.append(line)
            elif is_mermaid_directive(s):
                seen_directive = True
                out.append(line)
            else:
                # drop stray YAML-like headers (title:, config:, etc.) and blank prelude
                # keep only if obviously mermaid (rare corner-case)
                pass
        else:
            out.append(line)
        i += 1
    return out

def ensure_trailing_newline(text: str) -> str:
    return text if text.endswith('\n') else text + '\n'

def clean_mermaid_text(raw: str) -> str:
    t = strip_bom(raw)
    t = normalize_newlines(t)
    lines = split_lines(t)

    # 1) remove YAML frontmatter at top
    lines = strip_frontmatter(lines)
    # 2) remove markdown code fences
    lines = strip_markdown_fence(lines)
    # 3) drop non-mermaid prelude like 'title:' / 'config:' before the directive
    lines = clean_prelude(lines)

    cleaned = '\n'.join(lines)
    cleaned = ensure_trailing_newline(cleaned)
    return cleaned

def main() -> int:
    if not SRC_DIR.exists():
        print(json.dumps({"status":"error","message":f"Source dir not found: {SRC_DIR.as_posix()}"}))
        return 0  # don't fail CI if folder is missing

    # reset output dir
    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    files = sorted(SRC_DIR.rglob("*.mmd"))
    report = {"source": str(SRC_DIR), "output": str(OUT_DIR), "processed": [], "skipped": []}

    for src in files:
        try:
            rel = src.relative_to(SRC_DIR)
        except ValueError:
            # shouldn't happen, but skip safely
            report["skipped"].append(str(src))
            continue

        dst = OUT_DIR / rel
        dst.parent.mkdir(parents=True, exist_ok=True)

        raw = src.read_text(encoding="utf-8", errors="replace")
        cleaned = clean_mermaid_text(raw)

        # sanity: ensure we didn’t accidentally concatenate tokens (the bug you saw)
        # We guard by forcing a newline between adjacent keywords if needed.
        cleaned = re.sub(r'(flowchart\s+\w+)(flowchart|graph|sequenceDiagram|classDiagram|stateDiagram(?:-v2)?|erDiagram|gantt|journey|pie|quadrantChart|mindmap|timeline|gitGraph)',
                         r'\1\n\2', cleaned)

        dst.write_text(cleaned, encoding="utf-8")
        report["processed"].append(str(rel))

    print(json.dumps({"status":"ok","report":report}, indent=2))
    return 0

if __name__ == "__main__":
    sys.exit(main())