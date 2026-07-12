# Skopos Recon Report
**Target:** testphp.vulnweb.com
**Date:** 2026-07-12 17:53:35

---

### Executive Summary
A comprehensive scan of testphp.vulnweb.com was conducted including port scanning, web technology fingerprinting, directory brute forcing, WHOIS lookup, and CVE searching for identified services. No open TCP ports on the target were detected using Nmap. WhatWeb did not identify technologies, and Gobuster failed to connect to the target web server. WHOIS information about the root domain vulnweb.com was successfully retrieved. CVE searching could not be meaningfully performed due to lack of version information from the scans.

### Open Ports & Services

| Port | Protocol | Service | Version | Source |
|-------|----------|----------|---------|--------|
| None detected | N/A | N/A | N/A | nmap |

_No open TCP ports were detected on testphp.vulnweb.com, so no service versions are available._

### Whatweb
No technologies identified.

### Gobuster
Could not run directory enumeration; unable to connect to http://testphp.vulnweb.com/.

### WHOIS Information
```
Domain Name: VULNWEB.COM
Registry Domain ID: 1602006391_DOMAIN_COM-VRSN
Registrar WHOIS Server: whois.gandi.net
Registrar URL: http://www.gandi.net
Updated Date: 2026-06-01T05:28:12Z
Creation Date: 2010-06-14T07:50:29Z
Registry Expiry Date: 2027-06-14T07:50:29Z
Registrar: Gandi SAS
Registrar IANA ID: 81
Registrar Abuse Contact Email: abuse@support.gandi.net
Registrar Abuse Contact Phone: +33.170377661
Domain Status: clientTransferProhibited https://icann.org/epp#clientTransferProhibited
Name Server: NS-136.AWSDNS-17.COM
Name Server: NS-1450.AWSDNS-53.ORG
Name Server: NS-1588.AWSDNS-06.CO.UK
Name Server: NS-557.AWSDNS-05.NET
DNSSEC: unsigned
```

### CVE Findings

| Service/Version | CVE ID | Severity | Source |
|-----------------|---------|----------|--------|
| No service versions identified | N/A | N/A | No CVEs searched |

_No service versions were identified; therefore, CVE search was not applicable._

### Risk Assessment (Interpretation)
The absence of open ports indicates the host may be effectively filtering inbound connections or the scanned IP does not currently host publicly accessible services. The failure to detect web technologies and inability to enumerate directories suggest either network access restrictions or the target web service is not exposed at the scanned IP. WHOIS information confirms the domain is valid and currently registered with standard domain protection status. Without detected services, no direct vulnerabilities can be assessed.

### Recommendations
- Verify network accessibility and firewall settings for the target to confirm if port restrictions or network blocking is in place that limits scanning.
- Confirm the correct IP address or hostname for the web services if the target is expected to serve web content.
- If authorized, conduct scans from different vantage points or use alternative scanning methods (e.g., UDP, ICMP, or authenticated scanning) to bypass network filtering.
- Regularly monitor the domain registration status and DNS records to detect changes that might expose new services.
- If access to the web application is restored, rerun gobuster and WhatWeb to identify directories and technology stack for further vulnerability assessment.

If you require further testing or specific scans within scope, please advise.