import urllib.request
import urllib.parse
import json
import time

def search_cves(product: str, version: str) -> str:
    time.sleep(1)
    query = urllib.parse.quote(f"{product} {version}")
    url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch={query}&resultsPerPage=5"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
        cves = []
        for item in data.get("vulnerabilities", []):
            cve = item["cve"]
            desc = next((d["value"] for d in cve["descriptions"] if d["lang"] == "en"), "")
            cves.append(f"{cve['id']}: {desc[:150]}")
        return "\n".join(cves) if cves else "No CVEs found"
    except Exception as e:
        return f"Error: {e}"


TOOL_DEFINITION = {
    "type": "function",
    "function": {
        "name": "search_cves",
        "description": "Search NVD for known CVEs for a specific product and version",
        "parameters": {
            "type": "object",
            "properties": {
                "product": {"type": "string", "description": "Product name, e.g. openssh"},
                "version": {"type": "string", "description": "Version number, e.g. 6.6.1"}
            },
            "required": ["product", "version"]
        }
    }
}