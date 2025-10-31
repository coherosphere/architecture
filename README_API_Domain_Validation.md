# API Domain Validation (CI Rule)

**Purpose:** Prevent OpenAPI specifications from referencing incorrect API domains.

## Rule
All OpenAPI files under `assets/specs/openapi/` must include:
```
servers:
  - url: https://api.coherosphere.io
```
If a different or missing domain is detected, the workflow fails.

## Placement
- `.github/workflows/validate-api-domain.yml`
- `scripts/validate_api_domain.py`

## Run locally
```bash
pip install pyyaml
python scripts/validate_api_domain.py
```

Expected output:
```
✅ All OpenAPI specs use the correct domain: https://api.coherosphere.io
```
