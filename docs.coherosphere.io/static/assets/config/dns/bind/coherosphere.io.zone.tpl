$TTL 300
@   IN SOA ns1.example.com. hostmaster.cohersphere.io. ( 2025103101 3600 900 1209600 300 )
    IN NS ns1.example.com.
    IN NS ns2.example.com.

api           IN CNAME  api-lb.your-cloud.example.com.
staging.api   IN CNAME  staging-api-lb.your-cloud.example.com.
docs          IN CNAME  your-gh-pages.example.com.
schemas       IN CNAME  schemas-cdn.your-cloud.example.com.
status        IN CNAME  status.uptimerobot.com.
governance    IN CNAME  governance-ui.your-cloud.example.com.
dev           IN CNAME  dev-portal.your-cloud.example.com.
events        IN CNAME  events-broker.your-cloud.example.com.
metric        IN CNAME  grafana.your-cloud.example.com.
audit         IN CNAME  audit-logs.your-cloud.example.com.
chat          IN CNAME  chat.copilot.example.com.
data          IN CNAME  datalake.your-cloud.example.com.
ai            IN CNAME  ai-semantic.your-cloud.example.com.

@      IN CAA    0 issue "letsencrypt.org"
@      IN TXT    "v=spf1 -all"
