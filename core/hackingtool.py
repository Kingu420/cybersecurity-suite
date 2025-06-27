# core/hackingtool.py
import os
import time
import shutil

class HackingTool:
    def __init__(self):
        self.title = self.TITLE
        self.description = getattr(self, "DESCRIPTION", "")
        self.install_commands = getattr(self, "INSTALL_COMMANDS", [])
        self.run_commands = getattr(self, "RUN_COMMANDS", [])
        self.project_url = getattr(self, "PROJECT_URL", "")
        self.notes = getattr(self, "NOTES", "")

    def is_installed(self):
        """Check if the main run command executable exists."""
        if not self.run_commands:
            return False
        cmd = self.run_commands[0].split()[0]
        return shutil.which(cmd) is not None

    def install(self):
        for command in self.install_commands:
            print(f"[+] Executing: {command}")
            os.system(command)

    def run(self):
        os.system("clear")
        for command in self.run_commands:
            print(f"[+] Running: {command}")
            os.system(command)
        input("\n\033[96m[✔] Press Enter to return to menu...\033[0m")

    def show_info(self):
        print(f"\n{self.title}\n{'-' * len(self.title)}")
        print(self.description)
        if self.project_url:
            print(f"Repo: {self.project_url}")
        if self.notes:
            print(f"\n📌 Notes:\n{self.notes}")


class HackingToolsCollection:
    def __init__(self):
        self.title = self.TITLE
        self.tools = self.TOOLS

    def show_options(self):
        while True:
            os.system("clear")
            print(f"\n{self.title}\n{'=' * len(self.title)}")

            for index, tool in enumerate(self.tools, start=1):
                status = "✅" if tool.is_installed() else "❌"
                print(f"{index}. {tool.title} {status}")
                if tool.description:
                    print(f"    └─ Note: {tool.description.split('.')[0]}.")

            print("0. Back")

            choice = input("\nChoose a tool: ").strip()

            if choice == "0":
                break
            elif choice.isdigit() and 1 <= int(choice) <= len(self.tools):
                selected_tool = self.tools[int(choice) - 1]

                os.system("clear")
                print(f"[+] Selected: {selected_tool.title}")
                print(f"[i] {selected_tool.description}\n")

                if not selected_tool.is_installed():
                    confirm = input("[!] Tool not found. Install now? (y/n): ").strip().lower()
                    if confirm == "y":
                        selected_tool.install()

                selected_tool.run()
            else:
                print("[!] Invalid choice.")
                time.sleep(1)

