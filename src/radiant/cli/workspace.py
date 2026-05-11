from pathlib import Path
from radiant.utils.files.files import is_file_upwards
import typer
from rich import print
from radiant.config.config import *

app = typer.Typer()

@app.command()
def init():
    """
    Initializes a new workspace in the current directory
    """
    pwd = Path.cwd()
    if is_file_upwards(pwd, ".radiant"):
        print("[red]Error: already in a radiant workspace[/red]")
        raise typer.Exit()
    
    create_config(pwd / ".radiant") 
    print("Workspace created [green]succesfully[/green]")

@app.command()
def set(key, value):
    """
    Sets a config to a value
    """
    set_config(key,value)

    print(f"[bold]{key}[/bold] was set to [green]{value}[/green]")

@app.command()
def get(key):
    """
    Shows the value of a config
    """
    value = get_config(key)
    print(f"[bold]{key}[/bold] has a value of [green]{value}[/green]")

