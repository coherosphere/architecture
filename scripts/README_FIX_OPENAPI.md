
# OpenAPI Domain Fix Kit

This kit updates all OpenAPI specs under `assets/specs/openapi`:

- Replaces the `servers` list with only:
  - `https://api.coherosphere.io` (Production)
  - `https://staging.api.coherosphere.io` (Staging)
- Ensures `info.x-c2-id: C2-xx` matches the filename (e.g., `C2-03_Governance.yaml`).

## Usage

From the repository root:

```bash
python scripts/fix_openapi_domains.py \
  --root assets/specs/openapi \
  --prod https://api.coherosphere.io \
  --staging https://staging.api.coherosphere.io \
  --write

# A JSON report will be written to ./openapi_domain_fix_report.json
```

### Dry-run

```bash
python scripts/fix_openapi_domains.py --root assets/specs/openapi
```

### Commit

```bash
git add assets/specs/openapi/*.yml assets/specs/openapi/*.yaml openapi_domain_fix_report.json
git commit -m "chore(openapi): enforce https servers + add info.x-c2-id"
git push
```
