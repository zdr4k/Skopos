import sys
from datetime import datetime
import os
from dotenv import load_dotenv
from config import client, MODEL
from tools.nmap_tool import run_nmap, TOOL_DEFINITION as NMAP_TOOL
from tools.whois_tool import run_whois, TOOL_DEFINITION as WHOIS_TOOL
from tools.nvd_tool import search_cves, TOOL_DEFINITION as NVD_TOOL
from tools.whatweb_tool import run_whatweb, TOOL_DEFINITION as WHATWEB_TOOL
from tools.gobuster_tool import run_gobuster, TOOL_DEFINITION as GOBUSTER_TOOL
from tools.allowed_domains import is_allowed


available_tools = {
    "run_nmap": run_nmap,
    "search_cves": search_cves,
    "search_whois":run_whois,
    "run_whatweb":run_whatweb,
    "run_gobuster":run_gobuster
}

tools = [NMAP_TOOL, WHOIS_TOOL, NVD_TOOL, WHATWEB_TOOL, GOBUSTER_TOOL]

target = sys.argv[1]


if not is_allowed(target):
    print(f"[!] Target {target} is not in the allowed domains list. Aborting.")
    exit(1)



system_prompt = open("prompts/system.txt").read()
user_prompt = open("prompts/user.txt").read().replace("{target}", target)

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt}
]

while True:
    response = client.chat.completions.create(
        model="openai/gpt-4.1-mini",
        messages=messages,
        tools=tools,
    )

    message = response.choices[0].message

    if not message.tool_calls:
        os.makedirs("reports", exist_ok=True)
        date_str = datetime.now().strftime("%Y%m%d-%H%M%S")
        report_filename = f"reports/{target}-{date_str}.md"
        
        with open(report_filename, "w") as f:
            f.write(f"# Skopos Recon Report\n")
            f.write(f"**Target:** {target}\n")
            f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write("---\n\n")
            f.write(message.content)
        
        print(f"[*] Report saved to {report_filename}")
        print(f"REPORT_FILE={report_filename}", flush=True) 
        break

    messages.append(message)

    for tool_call in message.tool_calls:
        tool_name = tool_call.function.name
        tool_args = eval(tool_call.function.arguments)

        print(f"[*] Agent calling: {tool_name}({tool_args})")
        result = available_tools[tool_name](**tool_args)
        print(f"[*] Result received ({len(result)} chars)")

        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": result
        })
