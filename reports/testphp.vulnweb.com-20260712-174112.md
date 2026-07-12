# Skopos Recon Report
**Target:** testphp.vulnweb.com
**Date:** 2026-07-12 17:41:12

---

# Security Reconnaissance Report for testphp.vulnweb.com

## Executive Summary
- Nmap scan detected no open or responsive ports on testphp.vulnweb.com.
- Whatweb did not return any technology fingerprinting results.
- Gobuster directory enumeration could not connect to the target and returned no paths.
- WHOIS lookup for the root domain vulnweb.com reveals registration details including registrar Gandi SAS and expiration date in June 2027.
- No exact service versions were identified to allow specific CVE searches; generic searches for HTTP and TCP did return some unrelated historical CVEs.

## Open Ports & Services

| Port | Protocol | Service | Version | Source |
|------|----------|---------|---------|--------|
| None detected | N/A | N/A | N/A | nmap |

## Whatweb
No technologies identified or returned by the tool.

## Gobuster
Gobuster scan failed to connect to http://testphp.vulnweb.com/. No directory paths enumerated.

## WHOIS Information
- Domain Name: vulnweb.com
- Registry Domain ID: 1602006391_DOMAIN_COM-VRSN
- Registrar WHOIS Server: whois.gandi.net
- Registrar URL: http://www.gandi.net
- Updated Date: 2026-06-01T05:28:12Z
- Creation Date: 2010-06-14T07:50:29Z
- Registry Expiry Date: 2027-06-14T07:50:29Z
- Registrar: Gandi SAS
- Registrar IANA ID: 81
- Registrar Abuse Contact Email: abuse@support.gandi.net
- Registrar Abuse Contact Phone: +33.170377661
- Domain Status: clientTransferProhibited
- Name Servers:
  - NS-136.AWSDNS-17.COM
  - NS-1450.AWSDNS-53.ORG
  - NS-1588.AWSDNS-06.CO.UK
  - NS-557.AWSDNS-05.NET
- DNSSEC: unsigned

## CVE Findings

| Service / Version | CVE ID | Severity | Source |
|-------------------|--------|----------|--------|
| HTTP / unknown version | CVE-2002-2012 | Unknown | NVD Search |
| HTTP / unknown version | CVE-2002-2317 | Unknown | NVD Search |
| HTTP / unknown version | CVE-2003-0249 | Unknown | NVD Search |
| HTTP / unknown version | CVE-2004-2208 | Unknown | NVD Search |
| HTTP / unknown version | CVE-2004-2424 | Unknown | NVD Search |
| TCP / unknown version | CVE-2002-1585 | Unknown | NVD Search |
| TCP / unknown version | CVE-2003-0145 | Unknown | NVD Search |
| TCP / unknown version | CVE-2002-1474 | Unknown | NVD Search |
| TCP / unknown version | CVE-2003-0845 | Unknown | NVD Search |
| TCP / unknown version | CVE-2003-0905 | Unknown | NVD Search |

*Note: Versions were not identified by nmap or whatweb to perform precise CVE searches. The above CVEs are from generic product searches and may not apply.*

## Risk Assessment (Interpretation)
Due to all scanned TCP ports being filtered or non-responsive, no definitive open services or versions were identified on testphp.vulnweb.com. This significantly limits the ability to assess risk or vulnerability exposure based on live service data. The inability to connect with the web server to perform directory enumeration and technology fingerprinting further indicates there may be network controls or service disruptions preventing external reconnaissance. Without precise software versions or open ports, risk assessment relies heavily on assumptions which are not supported by collected data.

## Recommendations
- Verify network accessibility and firewall policies that may be blocking remote scans or connections to testphp.vulnweb.com.
- Perform internal scanning or testing from a location within the trusted network perimeter if external reconnaissance is restricted.
- Enable service banners or version disclosures cautiously to aid vulnerability assessment while balancing security considerations.
- Investigate other methods or credentials to obtain application and infrastructure details to augment external reconnaissance limitations.
- Maintain updated asset inventories and monitor for configuration changes that affect network visibility during assessments.