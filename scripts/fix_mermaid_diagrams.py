#!/usr/bin/env python3
import re, sys, pathlib, subprocess, shutil

ROOT = pathlib.Path("assets/diagrams")
MMDC = shutil.which("mmdc")  # optional: wenn vorhanden, testen wir danach

# Erkenner
SEQ = re.compile(r'^\s*sequenceDiagram\b', re.I)
FLOW = re.compile(r'^\s*flowchart\b|\s*graph\s+[TB|LR|RL|BT]\b', re.I)
STATE = re.compile(r'^\s*stateDiagram-v2\b', re.I)
FRONTMATTER_START = re.compile(r'^\s*---\s*$')
FRONTMATTER_KEYS = re.compile(r'^\s*(title|config)\s*:', re.I)

# Erlaubte init-Zeile
INIT_BLOCK = "%%{init: {'theme':'base','themeVariables':{ 'fontFamily':'Inter,Arial', 'primaryColor':'#ff8b00','lineColor':'#334155'}}}%%"

# Zeichenersetzungen, die mmdc robuster machen
REPLACEMENTS = {
    '“':'"', '”':'"', '’':"'", '–':'-', '—':'-', '•':'·', '–':'-',
}

def normalize_text(txt:str)->str:
    for k,v in REPLACEMENTS.items():
        txt = txt.replace(k,v)
    # Mermaid mag keine “title” direkt an Diagramm-Typ ohne NL:
    txt = re.sub(r'^(stateDiagram-v2)title\b', r'\1\n title ', txt, flags=re.M)
    return txt

def strip_frontmatter(lines:list[str])->tuple[list[str], str|None]:
    """Entfernt YAML-Frontmatter am Anfang und holt optional einen Titel."""
    if not lines or not FRONTMATTER_START.match(lines[0]): 
        return lines, None
    title = None
    i = 1
    while i < len(lines) and not FRONTMATTER_START.match(lines[i]):
        m = FRONTMATTER_KEYS.match(lines[i])
        if m and m.group(1).lower()=='title':
            # hole den Rest der Zeile als Titel
            # Beispiele: title: "Foo"  |  title: Foo
            tline = lines[i].split(':',1)[1].strip()
            title = tline.strip().strip('"').strip("'")
        i+=1
    # i steht jetzt auf der schließenden '---' oder EOF
    i = i+1 if i < len(lines) else i
    return lines[i:], title

def ensure_header(lines:list[str], inferred_title:str|None)->list[str]:
    """Sorgt für INIT-Block, korrekten Diagrammtyp und 'title' Zeile, falls sinnvoll."""
    content = "".join(lines).lstrip()
    # Prüfe, ob bereits Diagrammtyp da ist
    has_type = bool(SEQ.match(content) or FLOW.match(content) or STATE.match(content))
    new = []

    # INIT block oben einfügen (nur einmal)
    new.append(INIT_BLOCK+"\n")

    if has_type:
        # Titel-Zeile direkt NACH Diagrammtyp einfügen, wenn noch nicht vorhanden
        if inferred_title:
            # Falls schon 'title ' existiert, nicht doppeln
            if not re.search(r'^\s*title\s+', content, re.M):
                # Füge 'title …' nach der ersten Diagrammtyp-Zeile ein
                lines2 = content.splitlines(True)
                for idx, L in enumerate(lines2):
                    if SEQ.match(L) or FLOW.match(L) or STATE.match(L):
                        lines2.insert(idx+1, f"title {inferred_title}\n")
                        break
                content = "".join(lines2)
        return new + [content]
    else:
        # Kein Diagrammtyp gefunden → versuche zu raten (Heuristik)
        guessed = "flowchart LR"
        text = "".join(lines)
        if "sequenceDiagram" in text: guessed = "sequenceDiagram"
        if "state " in text or "stateDiagram" in text: guessed = "stateDiagram-v2"
        new.append(guessed+"\n")
        if inferred_title:
            new.append(f"title {inferred_title}\n")
        new.append(text)
        return new

def fix_file(path: pathlib.Path)->tuple[bool,str]:
    raw = path.read_text(encoding="utf-8", errors="ignore")
    raw = normalize_text(raw)
    lines = raw.splitlines(True)

    # 1) Frontmatter weg, Titel merken
    lines, title = strip_frontmatter(lines)

    # 2) Header/Init/Titel sicherstellen
    fixed_lines = ensure_header(lines, title)

    # 3) Letztes Nl
    if fixed_lines and not fixed_lines[-1].endswith("\n"):
        fixed_lines[-1] += "\n"

    new = "".join(fixed_lines)
    if new != raw:
        path.write_text(new, encoding="utf-8")
        return True, "fixed"
    return False, "ok"

def main():
    # 0) doppelte Endungen beheben
    for p in ROOT.rglob("*.mmd.mmd"):
        p.rename(p.with_suffix(""))  # entfernt eine .mmd
    for p in ROOT.rglob("*.mmd"):
        changed, status = fix_file(p)
        print(f"[{status}] {p}")

    # 4) optional render-test
    if MMDC:
        fails=0
        for p in ROOT.rglob("*.mmd"):
            try:
                subprocess.run([MMDC, "-i", str(p), "-o", "/tmp/_out.svg"], check=True,
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except subprocess.CalledProcessError:
                print(f"[mmdc FAIL] {p}")
                fails+=1
        if fails:
            print(f"mmdc render failures: {fails} file(s)")
            sys.exit(1)

if __name__ == "__main__":
    main()