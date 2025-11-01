#!/usr/bin/env python3
"""
Fix OpenAPI spec domains + x-c2-id.

Usage:
  python fix_openapi_domains.py \
    --root assets/specs/openapi \
    --prod https://api.coherosphere.io \
    --staging https://staging.api.coherosphere.io \
    --write

If --write is omitted, the script runs in dry-run mode and only prints a report.
"""
import argparse, os, re, json, sys
from typing import List, Dict

try:
    import yaml  # type: ignore
except Exception as e:
    yaml = None

SERVER_BLOCK = lambda prod, staging: [
    {"url": prod, "description": "Production"},
    {"url": staging, "description": "Staging"},
]

C2_RE = re.compile(r'(C2-\d{2})')

def infer_c2_id(filename: str) -> str:
    m = C2_RE.search(os.path.basename(filename))
    return m.group(1) if m else ""

def load_yaml(path: str):
    text = open(path, "r", encoding="utf-8").read()
    if yaml:
        return yaml.safe_load(text), text
    # Fallback: naive loader
    return None, text

def dump_yaml(data) -> str:
    if yaml:
        return yaml.safe_dump(data, sort_keys=False, allow_unicode=True)
    # Fallback keeps original text (no change capability without YAML)
    return None

def ensure_servers(data, prod: str, staging: str) -> Dict[str, str]:
    changed = {"replaced_servers": "no"}
    if data is None:
        changed["replaced_servers"] = "skipped_no_yaml_parser"
        return changed
    current = data.get("servers")
    desired = SERVER_BLOCK(prod, staging)
    if current != desired:
        data["servers"] = desired
        changed["replaced_servers"] = "yes"
    return changed

def ensure_x_c2_id(data, c2_id: str) -> Dict[str, str]:
    changed = {"set_x_c2_id": "no"}
    if data is None:
        changed["set_x_c2_id"] = "skipped_no_yaml_parser"
        return changed
    if "info" not in data or not isinstance(data["info"], dict):
        data["info"] = {}
    if data["info"].get("x-c2-id") != c2_id and c2_id:
        data["info"]["x-c2-id"] = c2_id
        changed["set_x_c2_id"] = "yes"
    return changed

def process_file(path: str, prod: str, staging: str, write: bool):
    c2_id = infer_c2_id(path)
    result = {
        "file": path,
        "c2_id": c2_id,
        "changed": False,
        "details": {},
        "errors": None,
    }
    try:
        data, original = load_yaml(path)
        details = {}
        details.update(ensure_servers(data, prod, staging))
        details.update(ensure_x_c2_id(data, c2_id))
        result["details"] = details
        if data is not None:
            rendered = dump_yaml(data)
            if rendered is None:
                result["errors"] = "Could not dump YAML (no parser available)."
            else:
                if rendered != original:
                    result["changed"] = True
                    if write:
                        with open(path, "w", encoding="utf-8") as f:
                            f.write(rendered)
        else:
            result["errors"] = "Could not parse YAML."
    except Exception as e:
        result["errors"] = f"{type(e).__name__}: {e}"
    return result

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="assets/specs/openapi")
    ap.add_argument("--prod", default="https://api.coherosphere.io")
    ap.add_argument("--staging", default="https://staging.api.coherosphere.io")
    ap.add_argument("--report", default="openapi_domain_fix_report.json")
    ap.add_argument("--write", action="store_true", help="write changes to files")
    args = ap.parse_args()

    report = {
        "root": args.root,
        "prod": args.prod,
        "staging": args.staging,
        "write_mode": args.write,
        "files": [],
        "summary": {"scanned": 0, "changed": 0, "errors": 0}
    }

    if not os.path.isdir(args.root):
        print(f"[ERROR] Root not found: {args.root}", file=sys.stderr)
        print(json.dumps(report, indent=2))
        sys.exit(2)

    for base, _, files in os.walk(args.root):
        for fn in files:
            if not fn.lower().endswith((".yml", ".yaml")):
                continue
            path = os.path.join(base, fn)
            res = process_file(path, args.prod, args.staging, args.write)
            report["files"].append(res)
            report["summary"]["scanned"] += 1
            if res["changed"]:
                report["summary"]["changed"] += 1
            if res["errors"]:
                report["summary"]["errors"] += 1

    with open(args.report, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    # Exit code: 0 even in dry-run; non-zero only if parse/dump errors
    sys.exit(1 if report["summary"]["errors"] else 0)

if __name__ == "__main__":
    main()
