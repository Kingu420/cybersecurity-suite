# coding=utf-8
import os
from core.hackingtool import HackingTool, HackingToolsCollection
from rich.console import Console
from pyfiglet import Figlet

def wireless_banner():
    fig = Figlet(font="slant")
    banner = fig.renderText("Wireless Attacks")
    console = Console()
    os.system("clear")
    console.print(f"[bold cyan]{banner}[/bold cyan]")

def wireless_setup_sequence():
    os.system("clear")
    print("\n\033[96m[*] Step 1: Stopping NetworkManager and wpa_supplicant...\033[0m")
    os.system("sudo systemctl stop NetworkManager")
    os.system("sudo systemctl stop wpa_supplicant")
    input("\n\033[92m[✔] Done. Press Enter to continue to Step 2...\033[0m")

    print("\n\033[96m[*] Step 2: Checking USB Wi-Fi adapters (lsusb)...\033[0m")
    os.system("lsusb")
    input("\n\033[92m[✔] Done. Press Enter to continue to Step 3...\033[0m")

    print("\n\033[96m[*] Step 3: Checking wireless interfaces (iwconfig)...\033[0m")
    os.system("iwconfig")
    input("\n\033[92m[✔] Done. Press Enter to continue to Step 4...\033[0m")

    print("\n\033[96m[*] Step 4: Checking monitor mode support (airmon-ng)...\033[0m")
    os.system("sudo airmon-ng")
    input("\n\033[93m[!] If interface name found (like wlan0), continue.\n[✔] Press Enter to kill interfering processes...\033[0m")

    os.system("sudo airmon-ng check kill")
    input("\n\033[92m[✔] Done. Press Enter to enable monitor mode...\033[0m")

    interface = input("\n\033[96m[?] Enter your wireless interface (e.g., wlan0): \033[0m").strip()
    if interface:
        os.system(f"sudo airmon-ng start {interface}")
        input("\n\033[92m[✔] Monitor mode enabled (likely wlan0mon). Press Enter to launch Wireless Tools menu...\033[0m")
    else:
        print("\033[91m[!] No interface entered. Skipping monitor mode setup.\033[0m")
        input("Press Enter to continue...")

    print("\n\033[96m[✔] Setup complete. Loading wireless attack tools...\033[0m")

class WIFIPumpkin(HackingTool):
    TITLE = "WiFi-Pumpkin"
    DESCRIPTION = (
        "Simple rogue AP framework."
    )
    INSTALL_COMMANDS = [
        "cd /home/hp/hp-tools/cybersecurity-suite/tools && "
        "git clone https://github.com/P0cL4bs/wifipumpkin3.git",
        "cd wifipumpkin3 && sudo python3 setup.py install"
    ]
    RUN_COMMANDS = ["cd /home/hp/hp-tools/cybersecurity-suite/tools/wifipumpkin3 && sudo wifipumpkin3"]
    PROJECT_URL = "https://github.com/P0cL4bs/wifipumpkin3"

class pixiewps(HackingTool):
    TITLE = "pixiewps"
    DESCRIPTION = (
        "Bruteforcing WPS with Pixie Dust."
    )
    INSTALL_COMMANDS = [
        "cd /home/hp/hp-tools/cybersecurity-suite/tools && "
        "git clone https://github.com/wiire/pixiewps.git && sudo apt-get -y install build-essential",
        "cd pixiewps && make && sudo make install"
    ]
    RUN_COMMANDS = ["pixiewps -h"]
    PROJECT_URL = "https://github.com/wiire/pixiewps"
    def run(self):
        os.system('clear')
        print(
            "1. Put your interface into monitor mode using: airmon-ng start wlan0\n"
            "2. Find routers using: wash -i wlan0mon\n"
            "3. Use reaver with Pixie Dust: reaver -i wlan0mon -b <BSSID> -c <channel> -K 1 -f"
        )
        input("\n[✔] Press Enter to return...")

class BluePot(HackingTool):
    TITLE = "BluePot (Bluetooth Honeypot)"
    DESCRIPTION = "Bluetooth honeypot GUI to analyze nearby BT devices."
    INSTALL_COMMANDS = [
        "cd /home/hp/hp-tools/cybersecurity-suite/tools && "
        "wget https://raw.githubusercontent.com/andrewmichaelsmith/bluepot/master/bin/bluepot-0.2.tar.gz",
        "tar -xzf bluepot-0.2.tar.gz && rm bluepot-0.2.tar.gz"
    ]
    RUN_COMMANDS = ["cd /home/hp/hp-tools/cybersecurity-suite/tools/bluepot && sudo java -jar bluepot.jar"]
    PROJECT_URL = "https://github.com/andrewmichaelsmith/bluepot"

class Fluxion(HackingTool):
    TITLE = "Fluxion"
    DESCRIPTION = "Fake AP + phishing = strong attack vector."
    INSTALL_COMMANDS = [
        "cd /home/hp/hp-tools/cybersecurity-suite/tools && "
        "git clone https://github.com/FluxionNetwork/fluxion.git",
        "cd fluxion && sudo chmod +x fluxion.sh"
    ]
    RUN_COMMANDS = ["cd /home/hp/hp-tools/cybersecurity-suite/tools/fluxion && sudo bash fluxion.sh -i"]
    PROJECT_URL = "https://github.com/FluxionNetwork/fluxion"

class Wifiphisher(HackingTool):
    TITLE = "Wifiphisher"
    DESCRIPTION = (
        "Captures credentials via phishing."
    )
    INSTALL_COMMANDS = [
        "cd /home/hp/hp-tools/cybersecurity-suite/tools && "
        "git clone https://github.com/wifiphisher/wifiphisher.git",
        "cd wifiphisher && sudo python3 setup.py install"
    ]
    RUN_COMMANDS = ["cd /home/hp/hp-tools/cybersecurity-suite/tools/wifiphisher && sudo wifiphisher"]
    PROJECT_URL = "https://github.com/wifiphisher/wifiphisher"

class Wifite(HackingTool):
    TITLE = "Wifite"
    DESCRIPTION = "Easy, automated attack framework."
    INSTALL_COMMANDS = [
        "cd /home/hp/hp-tools/cybersecurity-suite/tools && "
        "git clone https://github.com/derv82/wifite2.git",
        "cd wifite2 && sudo python3 setup.py install"
    ]
    RUN_COMMANDS = ["cd /home/hp/hp-tools/cybersecurity-suite/tools/wifite2 && sudo python3 Wifite.py"]
    PROJECT_URL = "https://github.com/derv82/wifite2"

class EvilTwin(HackingTool):
    TITLE = "EvilTwin"
    DESCRIPTION = "FakeAP attack script using phishing and fake login portals."
    INSTALL_COMMANDS = [
        "cd /home/hp/hp-tools/cybersecurity-suite/tools && "
        "git clone https://github.com/Z4nzu/fakeap.git"
    ]
    RUN_COMMANDS = ["cd /home/hp/hp-tools/cybersecurity-suite/tools/fakeap && sudo bash fakeap.sh"]
    PROJECT_URL = "https://github.com/Z4nzu/fakeap"

class Fastssh(HackingTool):
    TITLE = "Fastssh"
    DESCRIPTION = "Fast, multi-threaded SSH brute force scanner." "Used after gaining wireless access to SSH targets."
    INSTALL_COMMANDS = [
        "cd /home/hp/hp-tools/cybersecurity-suite/tools && "
        "git clone https://github.com/Z4nzu/fastssh.git",
        "cd fastssh && sudo chmod +x fastssh.sh",
        "sudo apt-get install -y sshpass netcat"
    ]
    RUN_COMMANDS = ["cd /home/hp/hp-tools/cybersecurity-suite/tools/fastssh && sudo bash fastssh.sh --scan"]
    PROJECT_URL = "https://github.com/Z4nzu/fastssh"

class Howmanypeople(HackingTool):
    TITLE = "Howmanypeople"
    DESCRIPTION = (
        "Count number of people around using WiFi signal strength.\n"
        "[!] Requires compatible Wi-Fi adapter.\n"
        "[!] May be illegal depending on country laws."
    )
    INSTALL_COMMANDS = [
        "sudo apt-get install -y tshark",
        "sudo python3 -m pip install howmanypeoplearearound"
    ]
    RUN_COMMANDS = ["howmanypeoplearearound"]
    PROJECT_URL = "https://github.com/schollz/howmanypeoplearearound"

class WirelessAttackTools(HackingToolsCollection):
    TITLE = "Wireless attack tools"
    DESCRIPTION = "Wi-Fi hacking tools: rogue APs, MITM, phishing, and analysis."
    TOOLS = [
        WIFIPumpkin(),
        pixiewps(),
        BluePot(),
        Fluxion(),
        Wifiphisher(),
        Wifite(),
        EvilTwin(),
        Fastssh(),
        Howmanypeople()
    ]
    def show_options(self):
        wireless_setup_sequence()
        wireless_banner()
        print("\033[93m[+] Wireless Hacking Tools — Rogue APs, WPS attacks, and sniffing.\033[0m\n")
        super().show_options()

