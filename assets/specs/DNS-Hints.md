# DNS Configuration — coherosphere (FINAL)

Type | Host | Value | Notes
-----|------|-------|------
A    | coherosphere.com         | <landing host IP/CNAME>   | Root site
CNAME| app.coherosphere.com     | <frontend host>           | e.g., Vercel/Netlify
CNAME| docs.coherosphere.io     | coherosphere.github.io     | GitHub Pages (docs)
CNAME| api.coherosphere.io      | <API load balancer>        | Kubernetes/Gateway
CNAME| status.coherosphere.io   | <status provider>          | (optional)
CNAME| data.coherosphere.io     | <data CDN>                 | (optional)
