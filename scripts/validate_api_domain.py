#!/usr/bin/env python3
import sys, yaml, pathlib, re

API_DOMAIN = "https://api.coherosphere.io"
spec_dir = pathlib.Path("assets/specs/openapi")

def validate_file(path: pathlib.Path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            doc = yaml.safe_load(f)
        servers = doc.get("servers", [])
        urls = [s.get("url", "") for s in servers if isinstance(s, dict)]
        if not any(API_DOMAIN in url for url in urls):
            print(f"❌ {path} — missing required domain: {API_DOMAIN}")
            return False
        return True
    except Exception as e:
        print(f"⚠️ Error reading {path}: {e}")
        return False

def main():
    specs = list(spec_dir.rglob("*.y*ml"))
    if not specs:
        print("No OpenAPI specs found under assets/specs/openapi/")
        sys.exit(0)

    ok = all(validate_file(p) for p in specs)
    if not ok:
        print("\n❌ Validation failed: one or more OpenAPI specs have incorrect or missing domain URLs.")
        sys.exit(1)
    print("\n✅ All OpenAPI specs use the correct domain:", API_DOMAIN)

if __name__ == "__main__":
    main()
