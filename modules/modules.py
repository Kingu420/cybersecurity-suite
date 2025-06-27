# This script can be run to generate all module files with consistent layout and banner
import os

MODULES = [
    "wordlist_generator",
    "web_attack",
    "post_exploitation",
    "forensic",
    "payload_creation",
    "exploit_framework",
    "reverse_engineering",
    "ddos",
    "rat",
    "xss",
    "steganography",
    "other",
    "anonymity",
    "update_uninstall"
]

BANNER_TEMPLATE = """
import os
from pyfiglet import Figlet
from rich.console import Console

def banner():
    fig = Figlet(font='slant')
    console = Console()
    os.system('clear')
    console.print(fig.renderText("{name}"), style="bold blue")

def run():
    banner()
    print("[+] {name} module loaded.")
    input("\n[✔] Press Enter to return to menu...")
"""

# Ensure modules directory exists
os.makedirs("modules", exist_ok=True)

for name in MODULES:
    path = f"modules/{name}.py"
    content = BANNER_TEMPLATE.format(name=name.replace("_", " ").title())
    with open(path, "w") as f:
        f.write(content)

print("✅ All module templates created successfully in /modules")

