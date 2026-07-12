# Skopos Recon Report
**Target:** scanme.nmap.org
**Date:** 2026-07-12 18:01:18

---

# Security Reconnaissance Report for scanme.nmap.org

## Executive Summary
The target scanme.nmap.org has several open ports identified by nmap, including SSH (OpenSSH 6.6.1p1) and HTTP (Apache httpd 2.4.7). Whatweb fingerprinting confirmed these technologies and their versions. Directory enumeration found multiple directory paths with various HTTP status codes, including access restrictions (403) and redirects (301). WHOIS lookup for the root domain nmap.org provided detailed domain registration and ownership information. A CVE search revealed one notable vulnerability for Apache httpd 2.4.7.

## Open Ports & Services

| Port | Protocol | Service | Version                               | Source (nmap)                  |
|------|----------|---------|-------------------------------------|-------------------------------|
| 22   | tcp      | ssh     | OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.13 | nmap                          |
| 80   | tcp      | http    | Apache httpd 2.4.7 ((Ubuntu))       | nmap                          |
| 53   | udp      | domain  | version not identified, CVE not searched | nmap                    |
| 123  | udp      | ntp     | version not identified, CVE not searched | nmap                    |
| 161  | udp      | snmp    | version not identified, CVE not searched | nmap                    |
| 500  | udp      | isakmp  | version not identified, CVE not searched | nmap                    |
| 1194 | udp      | openvpn | version not identified, CVE not searched | nmap                    |

## Whatweb
- Apache 2.4.7
- Country: RESERVED (ZZ)
- Google Analytics Universal UA-11009417-1
- HTML5
- HTTP Server: Ubuntu Linux running Apache/2.4.7 (Ubuntu)
- IP: 45.33.32.156
- Webpage Title: "Go ahead and ScanMe!"

## Gobuster
| Path          | Status Code | Notes                   |
|---------------|-------------|-------------------------|
| /.hta         | 403         | Forbidden               |
| /.htpasswd    | 403         | Forbidden               |
| /.htaccess    | 403         | Forbidden               |
| /.svn/entries | 403         | Forbidden               |
| /.svn         | 301         | Redirect to /.svn/       |
| /favicon.ico  | 403         | Forbidden               |
| /images       | 301         | Redirect to /images/      |
| /index        | 200         |                         |
| /index.html   | 200         |                         |
| /shared       | 301         | Redirect to /shared/      |

## WHOIS Information
- Domain Name: nmap.org
- Registrar: Dynadot Inc
- Creation Date: 1999-01-18
- Last Updated: 2026-04-10
- Expiry Date: 2029-01-18
- Registrar Abuse Contact Email: abuse@dynadot.com
- Registrar Abuse Contact Phone: +1.6502620100
- Domain Status: clientTransferProhibited
- Name Servers: ns1.linode.com, ns2.linode.com, ns3.linode.com, ns4.linode.com, ns5.linode.com
- DNSSEC: unsigned

## CVE Findings

| Service/Version        | CVE ID        | Severity | Source       |
|-----------------------|---------------|----------|--------------|
| Apache httpd 2.4.7    | CVE-2021-44224| Unknown  | NVD          |
| OpenSSH 6.6.1p1       | No CVEs found | N/A      | NVD          |

The CVE-2021-44224 for Apache httpd 2.4.7 describes a vulnerability where a crafted URI sent to an httpd server configured as a forward proxy (with ProxyRequests on) can cause a crash due to a NULL pointer dereference.

## Risk Assessment (Interpretation)
The presence of an outdated OpenSSH 6.6.1p1 and Apache 2.4.7 on the target indicates potential exposure to known vulnerabilities. The detected CVE in Apache suggests risk if the server is configured as a forward proxy, which may not be the case here, but still warrants verification. Several web directory paths are protected or redirect; attempts to access sensitive config files are met with 403 Forbidden, suggesting some access control but potential for misconfiguration remains. The UDP services mostly did not provide version info, impeding vulnerability assessment for those.

## Recommendations
1. Upgrade Apache httpd from 2.4.7 to a current supported version to mitigate CVE-2021-44224 and other vulnerabilities.
2. Upgrade OpenSSH to a recent supported version to increase security posture.
3. Review Apache server configuration, specifically ProxyRequests settings, to ensure no open proxy configuration.
4. Harden directory access controls, ensure sensitive files (.hta, .htpasswd, .htaccess) are not accessible even with redirects or misconfigurations.
5. Investigate UDP services for version and configuration to enable vulnerability assessment and apply corresponding patches or mitigation.
6. Regularly review WHOIS and DNS settings for security and compliance.

If you require further analysis or targeted testing, let me know.