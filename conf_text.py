head = """port: 7890
socks-port: 7891
mixed-port: 7893
mode: rule
log-level: silent
allow-lan: true
external-controller: 0.0.0.0:9090
bind-address: "*"
ipv6: false
dns:
  enable: true
  ipv6: false
  listen: 0.0.0.0:7894
  fallback-filter:
    geoip: false
    ipcidr:
      - 240.0.0.0/4
  nameserver:
    - https://puredns.org/dns-query
    - tls://puredns.org:853
  fallback:
    - tcp://108.137.44.39
    - tcp://108.137.44.9
    - 108.137.44.39
    - 108.137.44.9
tun:
  enable: true
  stack: system
  macOS-auto-route: true
  macOS-auto-detect-interface: true
  dns-hijack:
    - tcp://108.137.44.39:53
experimental:
  interface-name: en0
proxies:"""

proxy = """
  - name: {name}
    server: {server}
    port: {port}
    type: {type}
    uuid: {uuid}
    sni: {sni}
    alterId: {alterID}
    cipher: auto
    tls: {tls}
    skip-cert-verify: true
    udp: false
    network: {network}\n"""
header = """    ws-opts:
      path: {path}
      headers:
        Host: {HOST}\n"""

fotter = """proxy-groups:
  - name: select1999
    type: select
    proxies:
    - url1999 پینگ خودکار💜
{pp}

  - name: url1999 پینگ خودکار💜
    type: url-test
    url: http://www.gstatic.com/generate_204
    interval: 300
    tolerance: 50
    proxies:
{gg}

rules:
  - GEOIP,IR,DIRECT
  - DOMAIN-KEYWORD,ir,DIRECT 
  - MATCH,url1999 پینگ خودکار💜
"""
