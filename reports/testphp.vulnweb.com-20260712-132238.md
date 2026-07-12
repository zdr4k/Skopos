# Skopos Recon Report
**Target:** testphp.vulnweb.com
**Date:** 2026-07-12 13:22:38

---

# Security Reconnaissance Report for testphp.vulnweb.com

## Executive Summary
Nmap port scan revealed several open/filtered UDP ports including DNS (53), NTP (123), SNMP (161), ISAKMP (500), and OpenVPN (1194) on testphp.vulnweb.com. Web technology fingerprinting with WhatWeb did not yield identifiable results. Directory enumeration using Gobuster failed due to a connection timeout. WHOIS information shows the domain vulnweb.com was registered on 2010-06-14 via Gandi SAS and currently has active nameservers on AWS. Searches for CVEs found issues associated with services matching the open ports, including several CVEs related to SNMP and ISAKMP, but no CVEs were found for NTP and OpenVPN.

## Open Ports & Services

| Port  | Protocol | Service | Version  | Source (nmap)     |
|-------|----------|---------|----------|-------------------|
| 53    | UDP      | domain  | version not identified, CVE not searched | nmap    |
| 123   | UDP      | ntp     | version not identified, CVE not searched | nmap    |
| 161   | UDP      | snmp    | version not identified* | nmap    |
| 500   | UDP      | isakmp  | version not identified* | nmap    |
| 1194  | UDP      | openvpn | version not identified, CVE not searched | nmap    |

*Version numbers here refer to the port number as returned by nmap for the UDP services; exact software version wasn't identified, CVE searches were done using service name and port number as proxy.

## Whatweb
WhatWeb scan returned no identifiable web technologies or versions.

## Gobuster
Gobuster directory enumeration failed to connect to http://testphp.vulnweb.com/, resulting in no results.

## WHOIS Information
```
Domain Name: VULNWEB.COM
Registrar: Gandi SAS
Creation Date: 2010-06-14
Updated Date: 2026-06-01
Expiry Date: 2027-06-14
Domain Status: clientTransferProhibited
Nameservers:
- NS-136.AWSDNS-17.COM
- NS-1450.AWSDNS-53.ORG
- NS-1588.AWSDNS-06.CO.UK
- NS-557.AWSDNS-05.NET
DNSSEC: unsigned
```

## CVE Findings

| Service/Version | CVE ID         | Severity | Source           |
|-----------------|----------------|----------|------------------|
| SNMP (161)      | CVE-2001-0566  | Not Provided | NVD             |
| SNMP (161)      | CVE-2013-2780  | Not Provided | NVD             |
| SNMP (161)      | CVE-2016-8562  | Not Provided | NVD             |
| SNMP (161)      | CVE-2019-6813  | Not Provided | NVD             |
| SNMP (161)      | CVE-2019-19276 | Not Provided | NVD             |
| ISAKMP (500)    | CVE-2003-0108  | Not Provided | NVD             |
| ISAKMP (500)    | CVE-2006-0718  | Not Provided | NVD             |

No CVEs found for NTP (123) or OpenVPN (1194).

## Risk Assessment (Interpretation)
The presence of open/filtered UDP ports used for common network services such as DNS, NTP, SNMP, ISAKMP, and OpenVPN indicates this host is potentially running a range of network services that could be attack vectors if not properly secured. The discoveries of multiple CVEs related to SNMP and ISAKMP emphasize the need to carefully configure and update these services, as vulnerabilities in them can lead to denial of service or unauthorized access. The lack of identified web technologies or directory listings due to connection issues means the web application surface could not be analyzed here, leaving unknown potential vulnerabilities. The domain is long-standing and actively maintained according to WHOIS records.

## Recommendations
- Verify and update SNMP and ISAKMP service implementations to versions that address the known CVEs listed above.
- Configure firewall rules to limit exposure of UDP services to only trusted networks, reducing attack surface.
- Investigate and remediate the connectivity issues preventing directory enumeration to better understand the web application.
- Implement monitoring and alerting on these UDP services to detect abnormal activity related to known CVEs.
- Consider enabling DNSSEC to enhance domain DNS security, since current DNSSEC is unsigned.