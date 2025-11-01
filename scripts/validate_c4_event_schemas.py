# scripts/validate_c4_event_schemas.py
import argparse, json, re, sys
from pathlib import Path
from typing import Dict, List, Set, Tuple

try:
    from jsonschema import Draft202012Validator
except Exception as e:
    print("ERROR: jsonschema not installed. pip install jsonschema", file=sys.stderr)
    sys.exit(2)

C4_EVT_RE = re.compile(r"\bDDD\s*EVT\s*(\d{1,3})\b", re.IGNORECASE)
SCHEMA_ID_RE = re.compile(r"^DDD-EVT-\d{2,3}$")

def load_json(p: Path) -> Tuple[dict, List[str]]:
    errs = []
    try:
        return json.loads(p.read_text(encoding="utf-8")), errs
    except Exception as e:
        errs.append(f"{p}: invalid JSON ({e})")
        return {}, errs

def find_event_ids_in_c4(c4_dir: Path) -> Dict[str, Set[str]]:
    hits: Dict[str, Set[str]] = {}
    for mmd in sorted(c4_dir.glob("*.mmd")):
        text = mmd.read_text(encoding="utf-8", errors="ignore")
        ids = set(f"DDD-EVT-{int(n):02d}" for n in C4_EVT_RE.findall(text))
        hits[mmd.name] = ids
    return hits

def read_schema_ids(events_dir: Path) -> Dict[str, Path]:
    ids = {}
    for p in sorted(events_dir.glob("DDD-EVT-*.json")):
        j, errs = load_json(p)
        if errs:
            print("\n".join(errs), file=sys.stderr)
            continue
        sid = j.get("$id") or j.get("id")
        if not sid:
            print(f"{p}: missing $id", file=sys.stderr)
            continue
        if not SCHEMA_ID_RE.match(sid):
            print(f"{p}: $id '{sid}' must match DDD-EVT-XX/XXX", file=sys.stderr)
            continue
        ids[sid] = p
    return ids

def validate_examples(schema_path: Path, schema: dict) -> List[str]:
    msgs = []
    examples = schema.get("examples") or []
    if not examples:
        return msgs
    validator = Draft202012Validator(schema)
    for i, ex in enumerate(examples):
        try:
            validator.validate(ex)
        except Exception as e:
            msgs.append(f"{schema_path}: example[{i}] invalid: {e}")
    return msgs

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--events-dir", required=True)
    ap.add_argument("--c4-dir", required=True)
    ap.add_argument("--report-path", default="c4_schema_report.json")
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    events_dir = Path(args.events_dir)
    c4_dir = Path(args.c4_dir)

    c4_refs = find_event_ids_in_c4(c4_dir)
    schema_ids = read_schema_ids(events_dir)

    all_c4_ids: Set[str] = set().union(*c4_refs.values()) if c4_refs else set()
    all_schema_ids: Set[str] = set(schema_ids.keys())

    missing_in_schema = sorted(all_c4_ids - all_schema_ids)
    unused_schemas = sorted(all_schema_ids - all_c4_ids)

    example_errors = []
    for sid, p in schema_ids.items():
        j, errs = load_json(p)
        if errs:
            example_errors.extend(errs)
            continue
        example_errors.extend(validate_examples(p, j))

    report = {
        "summary": {
            "c4_files": len(c4_refs),
            "c4_event_refs": len(all_c4_ids),
            "schemas_found": len(all_schema_ids),
            "missing_in_schema": len(missing_in_schema),
            "unused_schemas": len(unused_schemas),
            "example_errors": len(example_errors),
        },
        "missing_in_schema": missing_in_schema,
        "unused_schemas": unused_schemas,
        "files": {k: sorted(list(v)) for k, v in c4_refs.items()},
        "example_errors": example_errors,
    }

    Path(args.report_path).write_text(json.dumps(report, indent=2), encoding="utf-8")

    # human-friendly output
    if args.verbose:
        print(json.dumps(report, indent=2))

    # exit codes:
    # 0 ok, 1 validation problems, 2 environment issues
    problems = report["summary"]["missing_in_schema"] or report["summary"]["example_errors"]
    if args.strict and problems:
        # print explicit messages
        if missing_in_schema:
            print("\nMissing schemas for these event IDs:", file=sys.stderr)
            for mid in missing_in_schema:
                # show where referenced
                refs = [f for f, ids in c4_refs.items() if mid in ids]
                print(f"  - {mid}  (used in: {', '.join(refs)})", file=sys.stderr)
        if example_errors:
            print("\nExample validation errors:", file=sys.stderr)
            for e in example_errors:
                print(f"  - {e}", file=sys.stderr)
        sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    main()
