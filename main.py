import os
import sys
from colorama import init, Fore, Style
from modules import info_gathering, wireless_attack, sql_injection, phishing
from modules import (
    info_gathering,
    wireless_attack,
    sql_injection,
    phishing,
    wordlist_generator,
    web_attack,
    post_exploitation,
    forensic,
    payload_creation,
    exploit_framework,
    reverse_engineering,
    ddos,
    rat,
    xss,
    steganography,
    other,
    anonymity,
    update_uninstall
)

# Initialize colorama
init(autoreset=True)

def load_banner():
    print("\033[92m" + r"""\        ██████╗██╗   ██╗██████╗ ███████╗██████╗        ███████╗███████╗ ██████╗██╗   ██╗██████╗ ██╗████████╗██╗   ██╗""")                        
    print("\033[96m" + r"""\       ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗       ██╔════╝██╔════╝██╔════╝██║   ██║██╔══██╗██║╚══██╔══╝╚██╗ ██╔╝""")
    print("\033[94m" + r"""\       ██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝ ████╗ ███████╗█████╗  ██║     ██║   ██║██████╔╝██║   ██║    ╚████╔╝ """)
    print("\033[95m" + r"""\       ██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗ ╚═══╝ ╚════██║██╔══╝  ██║     ██║   ██║██╔══██╗██║   ██║     ╚██╔╝  """)
    print("\033[92m" + r"""\╚       ██████╗   ██║   ██████╔╝███████╗██║  ██║       ███████║███████╗╚██████╗╚██████╔╝██║  ██║██║   ██║      ██║   """)
    print("\033[91m" + r"""\        ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝       ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝   ╚═╝      ╚═╝                                """)

    
    print("\033[96m" + "   [✔] https://github.com/YourName/cybersecurity-suite")
    print("\033[92m" + "   [✔] Cybersecurity Toolkit - Ethical Hacking Lab v1.0")
    print("\033[91m" + "   [X] For Educational and Authorized Use Only\n" + "\033[0m")



def main_menu():
    tools = {
        "0": ("Anonymously Hiding Tools", lambda: anonymity.AnonymouslyHidingTools().show_options()),
        "1": ("Information Gathering Tools", lambda: info_gathering.InformationGatheringTools().show_options()),
        "2": ("Wordlist Generator", lambda: wordlist_generator.WordlistGeneratorTools().show_options()),
        "3": ("Wireless Attack Tools", lambda: wireless_attack.WirelessAttackTools().show_options()),
        "4": ("SQL Injection Tools", lambda: sql_injection.SQLInjectionTools().show_options()),
        "5": ("Phishing Attack Tools", lambda: phishing.PhishingAttackTools().show_options()),
        "6": ("Web Attack Tools", lambda: web_attack.WebAttackTools().show_options()),
        "7": ("Post Exploitation Tools", lambda: post_exploitation.PostExploitationTools().show_options()),
        "8": ("Forensic Tools", lambda: forensic.ForensicTools().show_options()),
        "9": ("Payload Creation Tools", lambda: payload_creation.PayloadCreationTools().show_options()),
        "10": ("Exploit Framework", lambda: exploit_framework.ExploitFrameworkTools().show_options()),
        "11": ("Reverse Engineering Tools", lambda: reverse_engineering.ReverseEngineeringTools().show_options()),
        "12": ("DDOS Attack Tools", lambda: ddos.DDOSAttackTools().show_options()),
        "13": ("Remote Administrator Tools (RAT)", lambda: rat.RATTools().show_options()),
        "14": ("XSS Attack Tools", lambda: xss.XSSAttackTools().show_options()),
        "15": ("Steganography Tools", lambda: steganography.SteganographyTools().show_options()),
        "16": ("Other Tools", lambda: other.OtherTools().show_options()),
        "17": ("Update or Uninstall | Hackingtool", lambda: update_uninstall.UpdateUninstallTools().show_options()),
        "00": ("Exit", sys.exit)

    }

    while True:
        os.system("clear")  # or use 'cls' for Windows
        load_banner()

        print(Fore.YELLOW + "\nSelect a category:\n")
        for key, (name, _) in tools.items():
            print(Fore.GREEN + f"[{key}] " + Fore.WHITE + name)

        choice = input(Fore.MAGENTA + "\nChoose a tool to proceed: ").strip()

        if choice in tools:
            _, action = tools[choice]
            try:
                action()
            except KeyboardInterrupt:
                print(Fore.RED + "\n[!] Interrupted. Returning to menu...")
                time.sleep(1)
        else:
            print(Fore.RED + "Invalid choice.")
            input(Fore.CYAN + "Press Enter to continue...")

if __name__ == "__main__":
    main_menu()


