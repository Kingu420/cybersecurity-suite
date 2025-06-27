
import os
from pyfiglet import Figlet
from rich.console import Console

def banner():
    fig = Figlet(font='slant')
    console = Console()
    os.system('clear')
    console.print(fig.renderText("Reverse Engineering"), style="bold blue")

def run():
    banner()
    print("[+] Reverse Engineering module loaded.")
    input("[✔] Press Enter to return to menu...")
