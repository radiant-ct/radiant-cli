from pathlib import Path
from radiant.utils.files.files import is_file_upwards
import typer
from rich import print


app = typer.Typer()

@app.command()
def init():
    pwd = Path.cwd()
    if is_file_upwards(pwd, ".radiant"):
        print("[red]Error: already in a radiant workspace[/red]")
    

    with open(".radiant", "w") as file:
        file.write("Your text goes here")

    print("Workspace created [green]succesfully[/green]")

