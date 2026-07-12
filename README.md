# Skopos

AI-powered reconnaissance agent built on top of GitHub Actions and GitHub Models.

Open a GitHub issue with a target domain. Get a structured security recon report in minutes.

## How it works

The agent autonomously decides which reconnaissance tools to call, reasons over the results, and delivers a structured report.

```
Issue created (target: example.com)
        ↓
GitHub Actions triggers
        ↓
Agent runs: nmap → whatweb → gobuster → whois → CVE lookup
        ↓
LLM analyzes findings
        ↓
Report posted as issue comment
        ↓
Save the report
```

## Tools

| Tool | Purpose |
|------|---------|
| nmap | Port and service enumeration |
| whatweb | Web technology fingerprinting |
| gobuster | Directory enumeration |
| whois | Domain registration lookup |
| NVD API | CVE lookup by service and version |

## Stack

- GitHub Actions — workflow orchestration
- GitHub Models API — LLM inference (gpt-4.1-mini, free tier)
- Python — agent loop and tool execution

## Setup

**1. Fork this repository**

**2. Add a secret**
Create a Fine-grained personal access tokens `models` read-only permission.

**4. Add a secret**
Go to Settings → Secrets and variables → Actions → New repository secret
Name: `GH_MODELS_TOKEN`  
value: The personal access token.

**3. Create the recon label for the repo**
Go to **Issues → Labels → New Label**, name it `recon`.

**4. Add targets to the allowed list**
Edit `allowed_domains.txt` and add the domains you have authorization to scan.

**5. Run**
Create a new issue using the **Recon Request** template, add the `recon` label, and wait 2-3 minutes. The report will appear as a comment and be saved to `reports/`.

## Project structure

```
skopos/
├── agent.py                          # Agent loop — tool calling and report generation
├── config.py                         # Client and model configuration
├── allowed_domains.txt               # Authorized scan targets
├── requirements.txt
├── prompts/
│   ├── system.txt                    # Agent behavior and constraints
│   └── user.txt                      # Recon task definition
├── tools/
│   ├── nmap_tool.py
│   ├── whatweb_tool.py
│   ├── gobuster_tool.py
│   ├── whois_tool.py
│   ├── nvd_tool.py
│   └── allowed_domains.py
├── wordlists/
│   └── common.txt                    # Wordlist for directory enumeration
├── reports/                          # Generated reports (committed automatically)
└── .github/
    ├── workflows/
    │   └── recon.yml                 # GitHub Actions workflow
    └── ISSUE_TEMPLATE/
        └── recon.yml                 # Issue template
```

## ⚠️ Authorized use only

Only scan targets you own or have explicit written permission to test. Unauthorized scanning will violate laws and terms of service.

The `allowed_domains.txt` file is your first line of control — keep it updated.

## Notes

This is a proof of concept and study project. The goal was to understand how to build an autonomous agent using native tool calling, without frameworks like LangChain or CrewAI, and integrate it into a GitHub-native workflow.

## Part of The Big Rollback series

https://medium.com/@kelvinzdk