# DNS Config Bundle (v1)

Machine-readable DNS records + ready-to-use templates for Cloudflare (Terraform) and BIND.

## Canonical source
- `dns-records.json` / `dns-records.yaml` — edit these first (placeholders included).

## Providers
- `terraform/` — Cloudflare provider (`variables.tf`, `main.tf`).
  ```sh
  terraform init
  terraform plan -var="cf_api_token=YOUR_TOKEN"
  terraform apply
  ```
- `bind/` — Zone file templates (`*.zone.tpl`). Replace placeholders and load it in your DNS.

## Notes
- Replace placeholder targets with real endpoints (Base44, LB, CDN, etc.).
- Decide whether `metric` should be `metrics`.
- SPF currently `-all` (no mail). Adjust if you plan to send email.
