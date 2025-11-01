# OpenAPI Specs — Fixed Headers Bundle

This bundle normalizes all C2 OpenAPI specs:
- Proper top-level indentation for `openapi`, `info`, `servers`.
- Populates `info.x-c2-id` per container.
- Enforces HTTPS servers only (`api.coherosphere.io`, `staging.api.coherosphere.io`).
- Minimal valid body (`paths: {}`, `components: {}`) for you to extend.

Include the contents into `assets/specs/openapi/` in your repo.
