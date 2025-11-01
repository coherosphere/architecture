#!/usr/bin/env python3
import os, re, json, sys, argparse, glob

C4_DIR = "assets/diagrams/C4_sequences"
EVT_DIR = "assets/specs/events"
RE_EVT = re.compile(r'\b(?:DDD[\s\-]?EVT[\s\-]?\s*|DDD-EVT-)\s*(\d{1,3})\b', re.IGNORECASE)
RE_C4  = re.compile(r'\bC4[-\s]?(\d{1,3})\b', re.IGNORECASE)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", default=".", help="Repository root (default=.)")
    ap.add_argument("--fail-on-warn", action="store_true", help="Treat warnings as failures")
    args = ap.parse_args()

    repo = os.path.abspath(args.repo_root)

    c4_files = sorted(glob.glob(os.path.join(repo, C4_DIR, "*.mmd")))
    schemas = { os.path.basename(f): f for f in glob.glob(os.path.join(repo, EVT_DIR, "DDD-EVT-*.json")) }

    evt_index = {}
    for fname in schemas:
        m = re.match(r"DDD-EVT-(\d{2,3})_", fname)
        if m:
            evt_index[int(m.group(1))] = fname

    missing_evt = []
    missing_c4enum = []
    envelope_warnings = []
    ok_refs = []

    for mmd in c4_files:
        with open(mmd, "r", encoding="utf-8") as f:
            content = f.read()

        c4_ids = set(int(x) for x in RE_C4.findall(content))
        if not c4_ids:
            b = os.path.basename(mmd)
            m = re.search(r"C4[-_](\d{2,3})", b, re.IGNORECASE)
            c4_ids = {int(m.group(1))} if m else set()

        evts = set(int(x) for x in RE_EVT.findall(content))

        for eid in sorted(evts):
            if eid not in evt_index:
                missing_evt.append({
                    "c4File": os.path.relpath(mmd, repo),
                    "c4Ids": sorted(c4_ids),
                    "dddEventId": f"DDD-EVT-{eid:02d}",
                    "problem": "Schema not found"
                })
                continue

            sfname = evt_index[eid]
            spath = schemas[sfname]
            try:
                with open(spath, "r", encoding="utf-8") as f:
                    s = json.load(f)
            except Exception as e:
                missing_evt.append({
                    "c4File": os.path.relpath(mmd, repo),
                    "c4Ids": sorted(c4_ids),
                    "dddEventId": f"DDD-EVT-{eid:02d}",
                    "problem": f"Schema unreadable: {e}"
                })
                continue

            seq_prop = s.get("properties", {}).get("c4Sequence")
            if seq_prop and "enum" in seq_prop and c4_ids:
                enums = set()
                for v in seq_prop["enum"]:
                    if isinstance(v, str) and v.upper().startswith("C4-"):
                        try:
                            enums.add(int(v.split("-")[1]))
                        except:
                            pass
                if enums and not any(cid in enums for cid in c4_ids):
                    missing_c4enum.append({
                        "c4File": os.path.relpath(mmd, repo),
                        "c4Ids": sorted(c4_ids),
                        "schema": os.path.relpath(spath, repo),
                        "dddEventId": f"DDD-EVT-{eid:02d}",
                        "problem": f"Schema c4Sequence enum {sorted(enums)} does not include any of {sorted(c4_ids)}"
                    })

            required = ["specversion","id","source","type","subject","time","datacontenttype","data"]
            props = s.get("properties", {})
            missing_keys = [k for k in required if k not in props]
            if missing_keys:
                envelope_warnings.append({
                    "schema": os.path.relpath(spath, repo),
                    "missingKeys": missing_keys
                })
            else:
                ok_refs.append({
                    "c4File": os.path.relpath(mmd, repo),
                    "dddEventId": f"DDD-EVT-{eid:02d}",
                    "schema": os.path.relpath(spath, repo)
                })

    report = {
        "summary": {
            "c4Files": len(c4_files),
            "schemas": len(schemas),
            "okRefs": len(ok_refs),
            "missingEvt": len(missing_evt),
            "missingC4Enum": len(missing_c4enum),
            "envelopeWarnings": len(envelope_warnings)
        },
        "okRefs": ok_refs,
        "missingEvt": missing_evt,
        "missingC4Enum": missing_c4enum,
        "envelopeWarnings": envelope_warnings
    }

    print(json.dumps(report, indent=2))
    if report["missingEvt"] or report["missingC4Enum"]:
        sys.exit(1)

if __name__ == "__main__":
    main()
