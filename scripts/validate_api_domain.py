#!/usr/bin/env python3
import sys, yaml, pathlib
BASE = pathlib.Path("assets/specs/openapi")
REQUIRED = "https://api.coherosphere.io"
ok = True
for file in BASE.rglob("*.yaml"):
    try:
        with open(file, "r", encoding="utf-8") as f:
            spec = yaml.safe_load(f)
        servers = [s.get("url", "") for s in spec.get("servers", [])]
        if REQUIRED not in servers:
            print(f"❌ Missing production URL in {file}")
            ok = False
    except Exception as e:
        print(f"⚠️ Error reading {file}: {e}")
        ok = False
if not ok:
    print("\n❌ API domain validation failed.")
    sys.exit(1)
print("✅ All OpenAPI specs use https://api.coherosphere.io")
