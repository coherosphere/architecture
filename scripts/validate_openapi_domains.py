\
#!/usr/bin/env python3
import argparse, json, re, sys, os, pathlib

ALLOWED_DEFAULT = ["https://api.coherosphere.io", "https://staging.api.coherosphere.io"]

def scan_file(path, allowed):
    text = pathlib.Path(path).read_text(encoding="utf-8", errors="ignore")
    problems = []

    # Collect server URLs (yaml or json naive)
    urls = []
    # YAML-style: url: https://...
    for m in re.finditer(r'^\s*-\s*url\s*:\s*["\']?([^\s"\']+)', text, flags=re.MULTILINE):
        urls.append(m.group(1).strip())

    # JSON-style: "url": "https://..."
    for m in re.finditer(r'"url"\s*:\s*"([^"]+)"', text):
        urls.append(m.group(1).strip())

    # Deduplicate
    urls = list(dict.fromkeys(urls))

    if not urls:
        problems.append("No server URLs found (expect servers[*].url).")

    # Check each URL against policy
    for u in urls:
        if not u.startswith("https://"):
            problems.append(f"Non-HTTPS server: {u}")
        if ".coherosphere.com" in u:
            problems.append(f"Prohibited domain (.com) detected: {u}")
        if not any(u.startswith(a) for a in allowed):
            problems.append(f"URL not in allowed list {allowed}: {u}")
        if u.endswith("/") and u.count("/") == 2:
            problems.append(f"Do not use trailing slash on bare domain: {u}")

    # Info version
    vm = re.search(r'^\s*version\s*:\s*([^\s#]+)', text, flags=re.MULTILINE)
    if not vm:
        vm = re.search(r'"version"\s*:\s*"([^"]+)"', text)
    if vm:
        version = vm.group(1).strip().strip('"').strip("'")
        if not re.match(r'^\d+\.\d+\.\d+(-[A-Za-z0-9_.-]+)?$', version):
            problems.append(f"Non-semver version: {version}")
    else:
        problems.append("Missing info.version (semver expected).")

    # x-c2-id must match file prefix C2-xx
    fn = os.path.basename(path)
    pref = None
    pm = re.match(r'(C2-\d{2})_', fn)
    if pm:
        pref = pm.group(1)
        x = None
        xm = re.search(r'^\s*x-c2-id\s*:\s*(C2-\d{2})', text, flags=re.MULTILINE)
        if not xm:
            xm = re.search(r'"x-c2-id"\s*:\s*"(C2-\d{2})"', text)
        if xm:
            x = xm.group(1)
            if x != pref:
                problems.append(f"x-c2-id={x} does not match filename prefix {pref}")
        else:
            problems.append("Missing x-c2-id extension (should be C2-xx).")
    else:
        problems.append("Filename should start with C2-xx_.")

    return problems, urls

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True, help="Directory with OpenAPI specs")
    ap.add_argument("--allow", default=",".join(ALLOWED_DEFAULT), help="Comma-separated list of allowed server base URLs")
    ap.add_argument("--report", default="openapi_domain_report.json")
    args = ap.parse_args()

    allowed = [s.strip().rstrip("/") for s in args.allow.split(",") if s.strip()]
    files = {}
    count = 0
    for dirpath, _, filenames in os.walk(args.root):
        for name in filenames:
            if not name.lower().endswith((".yml",".yaml",".json")):
                continue
            p = os.path.join(dirpath, name)
            probs, urls = scan_file(p, allowed)
            files[os.path.relpath(p)] = probs
            count += 1

    total_violations = sum(len(v) for v in files.values())
    status = "ok" if total_violations == 0 and count > 0 else "fail"

    report = {
        "status": status,
        "files_scanned": count,
        "allowed": allowed,
        "files": files,
    }
    with open(args.report, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    # Print a concise summary
    bad = {k:v for k,v in files.items() if v}
    if bad:
        print("Violations:", file=sys.stderr)
        for k, v in bad.items():
            for msg in v:
                print(f" - {k}: {msg}", file=sys.stderr)

    print(json.dumps(report, indent=2))
    sys.exit(0 if status == "ok" else 1)

if __name__ == "__main__":
    main()
