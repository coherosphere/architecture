#!/usr/bin/env python3
import sys, json, pathlib

BASE = pathlib.Path("assets/specs/events")
BASE_ID = "https://schemas.coherosphere.io/events/"
ok = True

for path in BASE.rglob("*.json"):
    if "_meta" in path.parts and path.name == "README.md":
        continue
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        sid = data.get("$id","")
        schema = data.get("$schema","")
        if not sid.startswith(BASE_ID):
            print(f"❌ $id mismatch: {path} -> {sid}")
            ok = False
        if schema != "https://json-schema.org/draft/2020-12/schema":
            print(f"❌ $schema must be 2020-12: {path} -> {schema}")
            ok = False
        if data.get("type") != "object":
            print(f"❌ root type must be object: {path}")
            ok = False
        req = data.get("required", [])
        if not isinstance(req, list) or not req:
            print(f"❌ required[] must be non-empty: {path}")
            ok = False
    except Exception as e:
        print(f"⚠️ error reading {path}: {e}")
        ok = False

if not ok:
    print("\n❌ Event schema validation failed.")
    sys.exit(1)
print("✅ Event schemas valid.")