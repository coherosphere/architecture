terraform {
  required_providers { cloudflare = { source = "cloudflare/cloudflare", version = "~> 4.0" } }
}
provider "cloudflare" { api_token = var.cf_api_token }

data "cloudflare_zones" "com" { filter { name = var.zone_com } }
data "cloudflare_zones" "io"  { filter { name = var.zone_io  } }

locals {
  zone_id_com = one(data.cloudflare_zones.com.zones).id
  zone_id_io  = one(data.cloudflare_zones.io.zones).id
}

resource "cloudflare_record" "com_root_a" {
  zone_id = local.zone_id_com
  name    = "@"
  type    = "A"
  value   = "203.0.113.10"
  ttl     = 300
  proxied = false
}

resource "cloudflare_record" "com_root_aaaa" {
  zone_id = local.zone_id_com
  name    = "@"
  type    = "AAAA"
  value   = "2001:db8::10"
  ttl     = 300
  proxied = false
}

resource "cloudflare_record" "com_app" {
  zone_id = local.zone_id_com
  name    = "app"
  type    = "CNAME"
  value   = var.base44_target
  ttl     = 300
  proxied = true
}

resource "cloudflare_record" "com_caa" {
  zone_id = local.zone_id_com
  name    = "@"
  type    = "CAA"
  data = { flags = 0, tag = "issue", value = "letsencrypt.org" }
  ttl = 86400
}

resource "cloudflare_record" "com_spf" {
  zone_id = local.zone_id_com
  name    = "@"
  type    = "TXT"
  value   = "v=spf1 -all"
  ttl     = 86400
}

# IO
resource "cloudflare_record" "io_api"         { zone_id = local.zone_id_io name = "api"         type = "CNAME" value = var.api_lb         ttl = 60  proxied = true }
resource "cloudflare_record" "io_api_staging" { zone_id = local.zone_id_io name = "staging.api" type = "CNAME" value = var.staging_api_lb ttl = 60  proxied = true }
resource "cloudflare_record" "io_docs"        { zone_id = local.zone_id_io name = "docs"        type = "CNAME" value = var.docs_target    ttl = 300 proxied = true }
resource "cloudflare_record" "io_schemas"     { zone_id = local.zone_id_io name = "schemas"     type = "CNAME" value = var.schemas_cdn    ttl = 300 proxied = true }
resource "cloudflare_record" "io_status"      { zone_id = local.zone_id_io name = "status"      type = "CNAME" value = var.status_target  ttl = 300 proxied = false }
resource "cloudflare_record" "io_governance"  { zone_id = local.zone_id_io name = "governance"  type = "CNAME" value = var.governance_target ttl = 300 proxied = true }
resource "cloudflare_record" "io_dev"         { zone_id = local.zone_id_io name = "dev"         type = "CNAME" value = var.dev_target     ttl = 300 proxied = true }
resource "cloudflare_record" "io_events"      { zone_id = local.zone_id_io name = "events"      type = "CNAME" value = var.events_target  ttl = 60  proxied = true }
resource "cloudflare_record" "io_metric"      { zone_id = local.zone_id_io name = "metric"      type = "CNAME" value = var.metric_target  ttl = 300 proxied = true }
resource "cloudflare_record" "io_audit"       { zone_id = local.zone_id_io name = "audit"       type = "CNAME" value = var.audit_target   ttl = 300 proxied = true }
resource "cloudflare_record" "io_chat"        { zone_id = local.zone_id_io name = "chat"        type = "CNAME" value = var.chat_target    ttl = 300 proxied = true }
resource "cloudflare_record" "io_data"        { zone_id = local.zone_id_io name = "data"        type = "CNAME" value = var.data_target    ttl = 300 proxied = true }
resource "cloudflare_record" "io_ai"          { zone_id = local.zone_id_io name = "ai"          type = "CNAME" value = var.ai_target      ttl = 300 proxied = true }

resource "cloudflare_record" "io_caa" {
  zone_id = local.zone_id_io
  name    = "@"
  type    = "CAA"
  data = { flags = 0, tag = "issue", value = "letsencrypt.org" }
  ttl = 86400
}

resource "cloudflare_record" "io_spf" {
  zone_id = local.zone_id_io
  name    = "@"
  type    = "TXT"
  value   = "v=spf1 -all"
  ttl     = 86400
}
