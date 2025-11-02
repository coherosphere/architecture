$TTL 300
@   IN SOA ns1.example.com. hostmaster.cohersphere.com. ( 2025103101 3600 900 1209600 300 )
    IN NS ns1.example.com.
    IN NS ns2.example.com.

@      IN A      203.0.113.10
@      IN AAAA   2001:db8::10
app    IN CNAME  YOUR-BASE44-TARGET.example.com.

@      IN CAA    0 issue "letsencrypt.org"
@      IN TXT    "v=spf1 -all"
