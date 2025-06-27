# coding=utf-8
import os
from core.hackingtool import HackingTool, HackingToolsCollection
from rich.console import Console
from rich.text import Text
from pyfiglet import Figlet

def wordlist_banner():
    fig = Figlet(font='slant')
    raw_banner = fig.renderText("Wordlist Generator")

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


class Cupp(HackingTool):
    TITLE = "Cupp (Common User Password Profiler)"
    DESCRIPTION = "Generate wordlists based on personal information (name, DOB, etc)."
    INSTALL_COMMANDS = [
        "cd /home/hp/hp-tools/cybersecurity-suite/tools && git clone https://github.com/Mebus/cupp.git"
    ]
    RUN_COMMANDS = ["cd /home/hp/hp-tools/cybersecurity-suite/tools/cupp && python3 cupp.py -i"]
    PROJECT_URL = "https://github.com/Mebus/cupp"
    NOTES = "Best for custom wordlists in targeted attacks. Ask for victim details to generate context-aware lists."


class WordlistCreator(HackingTool):
    TITLE = "WordlistCreator (Brute Pattern List Maker)"
    DESCRIPTION = "Create wordlists using brute force and user-defined patterns."
    INSTALL_COMMANDS = [
        "cd /home/hp/hp-tools/cybersecurity-suite/tools && git clone https://github.com/zanyarjamal/wordlistcreator.git"
    ]
    RUN_COMMANDS = ["cd /home/hp/hp-tools/cybersecurity-suite/tools/wordlistcreator && python3 wordlistcreator.py"]
    PROJECT_URL = "https://github.com/zanyarjamal/wordlistcreator"
    NOTES = "Useful for generating huge raw combinations quickly based on character sets and lengths."


class Goblin(HackingTool):
    TITLE = "Goblin (Wordlist from URL or File)"
    DESCRIPTION = "Create wordlists by parsing words from URLs, files or raw text."
    INSTALL_COMMANDS = [
        "cd /home/hp/hp-tools/cybersecurity-suite/tools && git clone https://github.com/UndeadSec/GoblinWordGenerator.git goblin"
    ]
    RUN_COMMANDS = ["cd /home/hp/hp-tools/cybersecurity-suite/tools/goblin && python3 goblin.py -h"]
    PROJECT_URL = "https://github.com/UndeadSec/GoblinWordGenerator"
    NOTES = "Good for passive reconnaissance, creating lists from websites or dumps."


class OneBillionWordlist(HackingTool):
    TITLE = "1.4 Billion Password Wordlist"
    DESCRIPTION = "Precompiled list of 1.4B real-world passwords leaked in past breaches."
    INSTALL_COMMANDS = [
        "cd /home/hp/hp-tools/cybersecurity-suite/tools && wget https://github.com/berzerk0/Probable-Wordlists/releases/download/v2.1/Real-Passwords-Large.lst.zip",
        "unzip Real-Passwords-Large.lst.zip"
    ]
    RUN_COMMANDS = ["echo 'Use with cracking tools like Hydra, John, Hashcat, etc.'"]
    PROJECT_URL = "https://github.com/berzerk0/Probable-Wordlists"
    NOTES = "Use only if you're targeting common and reused passwords at scale. Not ideal for specific targets."


class WordlistGeneratorTools(HackingToolsCollection):
    TITLE = "Wordlist Generator"
    DESCRIPTION = "Tools to generate password lists for cracking or guessing."
    TOOLS = [
        Cupp(),
        WordlistCreator(),
        Goblin(),
        OneBillionWordlist()
    ]

    def show_options(self):
        wordlist_banner()
        print("\033[93m[+] Generate custom or large-scale wordlists for brute force, phishing, or auditing.\033[0m\n")
        super().show_options()

