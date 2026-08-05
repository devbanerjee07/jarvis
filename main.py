from brain.brain import think
from rich.console import Console

console = Console()

console.print("[bold cyan]====================================[/bold cyan]")
console.print("[bold green]         JARVIS AI[/bold green]")
console.print("[bold cyan]====================================[/bold cyan]")

while True:
    command = input("You: ")

    if command.lower() == "exit":
        break

    think(command)