import subprocess

def run_nmap(target: str) -> str:
    result = subprocess.run(
        [
            "sudo", "nmap",
            "-sSV",
            "--top-ports", "1000",
            "-Pn",
            "-T4",
            "--version-intensity", "7",
            target
        ],
        capture_output=True, text=True, timeout=240
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