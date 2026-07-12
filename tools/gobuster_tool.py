import subprocess
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORDLIST = os.path.join(BASE_DIR, "wordlists", "common.txt")

def run_gobuster(target: str) -> str:
    if not os.path.exists(WORDLIST):
        return f"Wordlist not found: {WORDLIST}"
    
    result = subprocess.run(
        ["gobuster", "dir", "-u", target, "-w", WORDLIST, "-t", "20", "--timeout", "10s", "-q"],
        capture_output=True, text=True, timeout=120
    )
    return result.stdout or result.stderr

TOOL_DEFINITION = {
    "type": "function",
    "function": {
        "name": "run_gobuster",
        "description": "Runs gobuster directory enumeration against a web target",
        "parameters": {
            "type": "object",
            "properties": {
                "target": {"type": "string", "description": "Full URL, e.g. http://scanme.nmap.org"}
            },
            "required": ["target"]
        }
    }
}