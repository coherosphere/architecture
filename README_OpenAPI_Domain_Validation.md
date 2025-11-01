# OpenAPI Domain Validation (CI)

This repository enforces a strict domain policy for OpenAPI specs.

**Rules**
- Only these base URLs are allowed in `servers[*].url`:
  - `https://api.coherosphere.io`
  - `https://staging.api.coherosphere.io`
- `https` required, no `.com` domains.
- Do not use a trailing slash on bare domains (e.g., `https://api.coherosphere.io/`).
- `info.version` must be valid SemVer (`MAJOR.MINOR.PATCH`).
- Each spec must include `x-c2-id: C2-xx`, matching the filename prefix (e.g., `C2-03_Governance.yaml`).

**Run locally**
```bash
python scripts/validate_openapi_domains.py   --root assets/specs/openapi   --allow "https://api.coherosphere.io,https://staging.api.coherosphere.io"   --report openapi_domain_report.json
```

**CI**
The workflow file `.github/workflows/validate-openapi-domains.yml` runs this check on every push/PR that touches OpenAPI specs.
