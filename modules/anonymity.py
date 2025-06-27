# anonymity.py
import os
from core.hackingtool import HackingTool, HackingToolsCollection
from pyfiglet import Figlet
from rich.console import Console
from rich.text import Text

def anonymity_banner():
    fig = Figlet(font='slant')
    banner = fig.renderText("Anonymity Tools")
    console = Console()
    os.system("clear")
    console.print(f"[bold cyan]{banner}[/bold cyan]")

class TorProxy(HackingTool):
    TITLE = "Tor Proxy Setup"
    DESCRIPTION = "Route your traffic through the Tor network for anonymity."
    INSTALL_COMMANDS = [
        "sudo apt update",
        "sudo apt install tor -y"
    ]
    RUN_COMMANDS = [
        "sudo service tor start",
        "proxychains curl https://check.torproject.org"
    ]
    PROJECT_URL = "https://www.torproject.org/"

class MacChanger(HackingTool):
    TITLE = "MAC Address Changer"
    DESCRIPTION = "Change your MAC address to anonymize your device on networks."
    INSTALL_COMMANDS = ["sudo apt install macchanger"]
    RUN_COMMANDS = ["sudo macchanger -r wlan0"]
    PROJECT_URL = "https://github.com/alobbs/macchanger"

class AnonymityTools(HackingToolsCollection):
    TITLE = "Anonymously Hiding Tools"
    DESCRIPTION = "Tools to anonymize your identity like Tor and MAC changers."
    TOOLS = [
        TorProxy(),
        MacChanger()
    ]

    def show_options(self):
        anonymity_banner()
        print("\033[93m[+] Tools to route traffic anonymously and hide identity.\033[0m\n")
        super().show_options()

