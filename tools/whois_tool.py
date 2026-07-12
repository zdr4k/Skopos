import subprocess

def run_whois(target: str) -> str:
    result = subprocess.run(
        ["whois", target],
        capture_output=True, text=True, timeout=30
    )
    return result.stdout[:2000]


TOOL_DEFINITION = {
    "type": "function",
    "function": {
        "name": "search_whois",
        "description": "Run WHOIS lookup to get domain registration and ownership information",
        "parameters": {
            "type": "object",
            "properties": {
                "target": {"type": "string", "description": "Domain or IP to lookup"}
            },
            "required": ["target"]
        }
    }
}