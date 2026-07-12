import subprocess

def run_whatweb(target: str) -> str:
    result = subprocess.run(
     ["sudo","whatweb",target],
     capture_output=True, text=True, timeout=60 
    )

    return result.stdout

TOOL_DEFINITION = {
    "type":"function",
    "function":{
        "name":"run_whatweb",
        "description":"Runs whatweb against a target",
        "parameters": {
            "type": "object",
            "properties": {
                "target": {"type": "string"}
            },
            "required": ["target"]
        }
    }
}