import os
import time 
from pyfiglet import Figlet
from rich.console import Console
from rich.text import Text

from core.hackingtool import HackingTool, HackingToolsCollection

def info_banner():
    fig = Figlet(font='standard')
    raw_banner = fig.renderText("Information Gathering")

    gradient_colors = ["bright_cyan", "bright_magenta", "bright_blue", "bright_green"]
    styled = Text()
    color_index = 0

    for char in raw_banner:
        if char != '\n':
            styled.append(char, style=gradient_colors[color_index % len(gradient_colors)])
            color_index += 1
        else:
            styled.append('\n')

    console = Console()
    os.system("clear")
    console.print(styled)


class WhoisLookup(HackingTool):
    TITLE = "Whois Lookup"
    DESCRIPTION = "Perform Whois lookup to gather domain information."
    INSTALL_COMMANDS = ["sudo apt install whois"]
    RUN_COMMANDS = ["whois example.com"]


class DNSenum(HackingTool):
    TITLE = "DNS Enum"
    DESCRIPTION = "Enumerate DNS records of a target domain."
    INSTALL_COMMANDS = ["sudo apt install dnsutils"]
    RUN_COMMANDS = ["dig example.com any"]


class NmapScan(HackingTool):
    TITLE = "Nmap Scan"
    DESCRIPTION = "Perform Nmap scan on target IP."
    INSTALL_COMMANDS = ["sudo apt install nmap"]
    RUN_COMMANDS = ["/home/hp/hp-tools/cybersecurity-suite/tools/nmap/nmap -A 127.0.0.1"]
    NOTES = "Performs an aggressive scan with OS detection, version detection, and more."

    def run(self):
        try:
            os.system("clear")
            print(f"[+] Selected: {self.TITLE}")
            print(self.DESCRIPTION)

            mode = input("\nChoose mode: [1] Auto Scan  [2] Manual Options  > ").strip()

            if mode == "1":
                command = f"/home/hp/hp-tools/cybersecurity-suite/tools/nmap/nmap -A 127.0.0.1"
            elif mode == "2":
                print("📘 Common Nmap Options Explained:")
                print("  -A    : Aggressive scan (includes OS detection, version detection, script scanning, and traceroute)")
                print("  -sV   : Service version detection (find out what version of service is running on a port)")
                print("  -sS   : Stealth scan (SYN scan; faster and less detectable)")
                print("  -O    : OS detection (tries to guess the operating system of the target)")
                print("  -Pn   : No ping (skip host discovery, useful if ping is blocked)")
                print("  -p    : Specify ports (e.g., -p 80,443 for HTTP/HTTPS)")
                print("  -T4   : Set timing to faster (T0–T5, where T4 is faster but more detectable)")
                print("  -v    : Verbose mode (shows more details during the scan)")
                print("  -sU   : UDP scan (scan UDP ports, which are often ignored)")


                target = input("\nEnter target IP or domain (e.g., 192.168.1.1 or example.com): ").strip()
                if not target:
                    print("[!] Target is required!")
                    return
                options = input("Enter Nmap options (e.g., -A, -sV, -p 80): ").strip()
                command = f"/home/hp/hp-tools/cybersecurity-suite/tools/nmap/nmap {options} {target}"
            else:
                print("[!] Invalid option.")
                return

            print(f"\n[+] Running: {command}\n")
            os.system(command)
        except KeyboardInterrupt:
            print("\n[!] Scan cancelled by user.")
        finally:
            input("\n\033[96m[✔] Press Enter to return to menu...\033[0m")


class InformationGatheringTools(HackingToolsCollection):
    TITLE = "Information Gathering"
    DESCRIPTION = "Tools to collect reconnaissance info: Whois, DNS, Nmap, etc."
    TOOLS = [
        NmapScan(),
        WhoisLookup(),
        DNSenum()
    ]

    def show_options(self):
        info_banner()  # ✅ show banner
        print("\033[93m[+] Reconnaissance Tools — Domain, IP, Port, and DNS analysis.\033[0m\n")
        super().show_options()  # ✅ render tool list

