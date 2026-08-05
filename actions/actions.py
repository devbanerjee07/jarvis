import webbrowser
import subprocess
import urllib.parse

# Mac application names
APPS = {
    "calculator": "Calculator",
    "notes": "Notes",
    "terminal": "Terminal",
    "vscode": "Visual Studio Code",
    "visual studio code": "Visual Studio Code",
    "safari": "Safari",
}


def execute(command):
    command = command.strip().lower()

    print(f"Received command: {command}")

    # ---------- Open Installed Apps ----------
    if command in APPS:
        app_name = APPS[command]

        print(f"Opening {app_name}...")

        subprocess.run(["open", "-a", app_name])

        return

    # ---------- Open Any App ----------
    if command.startswith("open "):
        app = command.replace("open ", "").strip()

        print(f"Opening {app}...")

        subprocess.run(["open", "-a", app])

        return

    # ---------- Google Search ----------
    if command.startswith("search google for "):
        query = command.replace("search google for ", "").strip()

        url = "https://www.google.com/search?q=" + urllib.parse.quote(query)

        print(f"Searching Google for: {query}")

        webbrowser.open(url)

        return

    # ---------- YouTube Search ----------
    if command.startswith("search youtube for "):
        query = command.replace("search youtube for ", "").strip()

        url = (
            "https://www.youtube.com/results?search_query="
            + urllib.parse.quote(query)
        )

        print(f"Searching YouTube for: {query}")

        webbrowser.open(url)

        return

    # ---------- Websites ----------
    if command == "youtube":
        print("Opening YouTube...")
        webbrowser.open("https://youtube.com")
        return

    if command == "google":
        print("Opening Google...")
        webbrowser.open("https://google.com")
        return

    if command == "chatgpt":
        print("Opening ChatGPT...")
        webbrowser.open("https://chatgpt.com")
        return

    print("Sorry, I don't understand that command yet.")