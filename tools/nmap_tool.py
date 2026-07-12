import subprocess

def run_nmap(target: str) -> str:
    result = subprocess.run(
        [
            "sudo", "nmap",
            "-sSV",              
            "-sU",               
            "--top-ports", "100",
            "-p", "U:53,161,123,500,1194",
            "-Pn",
            "-T4",
            "--version-intensity", "7",
            target
        ],
        capture_output=True, text=True, timeout=180
    )
    return result.stdout or result.stderr

TOOL_DEFINITION = {
    "type": "function",
    "function": {
        "name": "run_nmap",
        "description": "Runs nmap port scan against a target",
        "parameters": {
            "type": "object",
            "properties": {
                "target": {"type": "string"}
            },
            "required": ["target"]
        }
    }
}