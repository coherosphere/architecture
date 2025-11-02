variable "cf_api_token" { type = string }
variable "zone_com" { type = string, default = "coherosphere.com" }
variable "zone_io"  { type = string, default = "coherosphere.io" }

# Targets
variable "base44_target"     { type = string, default = "YOUR-BASE44-TARGET.example.com" }
variable "api_lb"            { type = string, default = "api-lb.your-cloud.example.com" }
variable "staging_api_lb"    { type = string, default = "staging-api-lb.your-cloud.example.com" }
variable "docs_target"       { type = string, default = "your-gh-pages.example.com" }
variable "schemas_cdn"       { type = string, default = "schemas-cdn.your-cloud.example.com" }
variable "status_target"     { type = string, default = "status.uptimerobot.com" }
variable "governance_target" { type = string, default = "governance-ui.your-cloud.example.com" }
variable "dev_target"        { type = string, default = "dev-portal.your-cloud.example.com" }
variable "events_target"     { type = string, default = "events-broker.your-cloud.example.com" }
variable "metric_target"     { type = string, default = "grafana.your-cloud.example.com" }
variable "audit_target"      { type = string, default = "audit-logs.your-cloud.example.com" }
variable "chat_target"       { type = string, default = "chat.copilot.example.com" }
variable "data_target"       { type = string, default = "datalake.your-cloud.example.com" }
variable "ai_target"         { type = string, default = "ai-semantic.your-cloud.example.com" }
