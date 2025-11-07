import typer
from rich.console import Console

console = Console()

def hello():
    """Pings to your remote repository."""
    console.print("Hello", "World!", style="bold red")
