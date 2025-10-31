# API Domain Validation (v2.0)

This document describes the automated validation of all Coherosphere API specifications, ensuring  
that every declared endpoint resolves to a valid and authorized domain under **`*.coherosphere.io`**.

---

## Purpose

To maintain architectural integrity and prevent external API misconfiguration,  
the CI pipeline validates that all OpenAPI and Event specs reference **only approved domains**.

This validation is applied automatically on every commit and pull request.

---

## Validation Workflow

### 1. Configuration Files

| File | Purpose | Path |
|-------|----------|------|
| `assets/config/cors/cors-policy.json` | Canonical list of allowed origins | Used as whitelist |
| `scripts/validate_api_domain.py` | Python validation script | Domain extraction and check logic |
| `.github/workflows/validate-api-domain.yml` | GitHub Action | Executes the validation automatically |

---

### 2. Approved Domains

The following domains are considered valid for all API and event schemas:

```
https://api.coherosphere.io
https://staging.api.coherosphere.io
https://app.coherosphere.com
https://coherosphere.com
https://docs.coherosphere.io
https://schemas.coherosphere.io
https://governance.coherosphere.io
https://dev.coherosphere.io
https://events.coherosphere.io
https://metric.coherosphere.io
https://audit.coherosphere.io
https://status.coherosphere.io
https://chat.coherosphere.io
https://data.coherosphere.io
https://ai.coherosphere.io
http://localhost:3000
http://localhost:5173
```

> The list is synchronized automatically from `cors-policy.json`.

---

### 3. Validation Logic

The Python script (`scripts/validate_api_domain.py`) performs the following steps:

1. Parse all OpenAPI and Event schema files under `assets/specs/**`.
2. Extract every URL value from paths, servers, and examples.
3. Check each extracted URL against the allowed origins defined in `cors-policy.json`.
4. Report any unauthorized domain references as build errors.

Example output:
```
❌ Invalid domain detected: https://external-service.net (in openapi/poc.yaml)
✅ All other endpoints validated successfully.
```

---

### 4. GitHub Workflow

Defined in `.github/workflows/validate-api-domain.yml`:

```yaml
name: Validate API Domains
on: [push, pull_request]
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Validate API Domains
        run: python3 scripts/validate_api_domain.py
```

If invalid domains are found, the CI build fails automatically.

---

### 5. Local Testing

To run the same validation locally:

```bash
pip install -r requirements.txt
python scripts/validate_api_domain.py
```

---

### 6. Related Components

| Component | Purpose |
|------------|----------|
| `validate-event-schemas.yml` | Checks JSON Schema compliance for event specs |
| `validate_event_schemas.py` | Performs structural validation for all event definitions |
| `cors-policy.json` | Central origin and domain reference used by all CI validation steps |

---

### 7. Summary

- Centralized domain validation via `cors-policy.json`
- Automatic enforcement through CI (no manual review needed)
- Synchronization between OpenAPI specs, Events, and Infrastructure
- Consistent security boundaries across all Coherosphere subdomains

---

**Version:** 2.0  
**Maintained by:** Coherosphere Collective  
**License:** CC BY 4.0
