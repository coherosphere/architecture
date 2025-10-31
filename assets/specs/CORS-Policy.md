# Coherosphere — CORS & Security Policy (Final)

## Allowed Origins
- https://app.coherosphere.com
- https://docs.coherosphere.io

## Allowed Methods
GET, POST, PUT, DELETE, PATCH, OPTIONS

## Allowed Headers
Content-Type, Authorization, X-Request-ID, X-Correlation-ID

## Credentials
true

## Example Deployment (Kubernetes)
env:
  - name: CORS_ALLOWED_ORIGINS
    value: "https://app.coherosphere.com,https://docs.coherosphere.io"
  - name: CORS_ALLOWED_METHODS
    value: "GET,POST,PUT,DELETE,PATCH,OPTIONS"
  - name: CORS_ALLOWED_HEADERS
    value: "Content-Type,Authorization,X-Request-ID,X-Correlation-ID"
  - name: CORS_ALLOW_CREDENTIALS
    value: "true"
