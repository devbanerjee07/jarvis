import webbrowser
import subprocess


def execute(command):
    command = command.strip().lower()

    print(f"Received command: {command}")

    if command == "calculator":
        print("Opening Calculator...")
        subprocess.run(["open", "-a", "Calculator"])
        return

    if command == "notes":
        print("Opening Notes...")
        subprocess.run(["open", "-a", "Notes"])
        return

    if command == "terminal":
        print("Opening Terminal...")
        subprocess.run(["open", "-a", "Terminal"])
        return

    if command == "youtube":
        print("Opening YouTube...")
        webbrowser.open("https://youtube.com")
        return

    if command == "google":
        print("Opening Google...")
        webbrowser.open("https://google.com")
        return

    print("I don't know that command yet.")