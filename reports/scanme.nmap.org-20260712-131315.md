# Skopos Recon Report
**Target:** scanme.nmap.org
**Date:** 2026-07-12 13:13:15

---

# Security Reconnaissance Report: scanme.nmap.org

---

## Executive Summary
The target scanme.nmap.org has several open UDP ports detected by Nmap, including DNS (port 53), NTP (port 123) with version NTP v4, SNMP (port 161), ISAKMP (port 500), and OpenVPN (port 1194). Web technology fingerprinting reveals an Apache HTTP server version 2.4.7 running on Ubuntu Linux. Directory enumeration on the web server found several directories and files responding with HTTP status codes 200, 301, and 403. The root domain nmap.org is registered with Dynadot Inc and is in good standing. CVE searches found multiple vulnerabilities associated with Apache 2.4.7 and NTP version 4, with no CVEs identified for OpenVPN, SNMP, and ISAKMP due to version information being missing or no CVEs.

---

## Open Ports & Services

| Port  | Protocol | Service  | Version    | Source (Nmap)            |
|-------|----------|----------|------------|--------------------------|
| 53    | UDP      | domain   | version not identified | Nmap                   |
| 123   | UDP      | ntp      | NTP v4     | Nmap                     |
| 161   | UDP      | snmp     | version not identified | Nmap                   |
| 500   | UDP      | isakmp   | version not identified | Nmap                   |
| 1194  | UDP      | openvpn  | version not identified | Nmap                   |

---

## Whatweb

- Apache 2.4.7 (Ubuntu)
- Country: RESERVED (ZZ)
- Google Analytics Universal (UA-11009417-1)
- HTML5
- HTTP Server: Ubuntu Linux (Apache/2.4.7)
- IP: 45.33.32.156
- Title: "Go ahead and ScanMe!"

---

## Gobuster

| Path         | Status Code |
|--------------|-------------|
| /.htaccess   | 403         |
| /.hta        | 403         |
| /.htpasswd   | 403         |
| /.svn        | 301         |
| /.svn/entries| 403         |
| /favicon.ico | 403         |
| /images      | 301         |
| /index.html  | 200         |
| /index       | 200         |
| /shared      | 301         |

---

## WHOIS Information

- Domain Name: nmap.org
- Registrar: Dynadot Inc
- Registrar IANA ID: 472
- Updated Date: 2026-04-10
- Creation Date: 1999-01-18
- Registry Expiry Date: 2029-01-18
- Domain Status: clientTransferProhibited
- Name Servers: ns1.linode.com, ns2.linode.com, ns3.linode.com, ns4.linode.com, ns5.linode.com
- DNSSEC: unsigned
- Registrar Abuse Contact Email: abuse@dynadot.com
- Registrar Abuse Contact Phone: +1.6502620100

---

## CVE Findings

| Service / Version  | CVE ID       | Severity | Source                |
|--------------------|--------------|----------|-----------------------|
| Apache 2.4.7       | CVE-2012-2378| Not stated | NVD                   |
|                    | CVE-2016-6814| Not stated | NVD                   |
|                    | CVE-2021-44224| Not stated | NVD                   |
|                    | CVE-2025-66200| Not stated | NVD                   |
| NTP 4              | CVE-2001-0414| Not stated | NVD                   |
|                    | CVE-2004-0657| Not stated | NVD                   |
|                    | CVE-2005-2496| Not stated | NVD                   |
|                    | CVE-2006-7160| Not stated | NVD                   |
|                    | CVE-2008-3081| Not stated | NVD                   |
| SNMP (version unknown) | CVE-2013-3634 | Not stated | NVD                |
|                      | CVE-2022-26380| Not stated | NVD                |
|                      | CVE-2024-37992| Not stated | NVD                |
|                      | CVE-2024-54015| Not stated | NVD                |
|                      | CVE-2025-27394| Not stated | NVD                |
| OpenVPN (version unknown) | No CVEs found | N/A      | NVD                   |
| ISAKMP (version unknown) | No CVEs found | N/A      | NVD                   |

---

## Risk Assessment (Interpretation)

The Apache 2.4.7 server running publicly has multiple known CVEs including ones related to security policy enforcement and forwarding proxy issues, which can expose the server to web-based attacks or denial of service. The presence of multiple sensitive HTTP directories and files protected with 403 status codes indicates some security controls but also the presence of potentially sensitive paths worth further review. The NTP server version 4 also exhibits multiple historical vulnerabilities linked to denial of service and buffer overflows, posing risks of disruption or exploitation in network time services.

The lack of version information for some UDP services (domain, SNMP, ISAKMP, OpenVPN) limits precise vulnerability assessment. However, missing version info itself may suggest conservative scanning or service obfuscation.

---

## Recommendations

1. Upgrade Apache HTTP Server to the latest supported stable version to mitigate known CVEs.
2. Review and secure web server configurations to limit exposure of sensitive directories such as .htaccess, .htpasswd, and .svn.
3. Harden NTP server configuration or upgrade to an actively maintained version to address known vulnerabilities.
4. Identify and document precise versions for SNMP, ISAKMP, and OpenVPN services to allow for targeted vulnerability assessments.
5. Conduct periodic vulnerability scans and audits to detect and mitigate emerging threats.
6. Consider enabling DNSSEC for the domain for improving DNS security posture.