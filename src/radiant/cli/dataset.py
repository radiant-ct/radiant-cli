import typer

from radiant.backend_api import Client   
from radiant.backend_api.api.dataset_controller.get_all_datasets import sync as get_all_datasets

from radiant.config.config import load_config
from radiant.utils.files.files import  is_file_upwards

from radiant.dataset.dataset_metadata_schema import DatasetMetadataSchema
from radiant.dataset.dataset_metadata_service import create_dataset_metadata

from pathlib import Path
from rich import print

app = typer.Typer()
config = load_config()
client = Client(base_url=config.remote)

@app.command()
def init(
    name: str = typer.Option(None, "--name", help="Name of the dataset"),
    description: str = typer.Option(None, "--description", help="Description of the dataset"),
    credits: str = typer.Option(None, "--credits", help="Credits of the dataset"),
):

    if is_file_upwards(Path.cwd(), ".dataset"):
        print("[red]Error: Already in a dataset folder[/red]")
        raise typer.Exit()

    if name is None:
        name = typer.prompt("Name")

    if description is None:
        description = typer.prompt("Description")

    if credits is None:
        credits = typer.prompt("Credits")

    metadata = DatasetMetadataSchema(name=name, description=description, credits=credits)

    create_dataset_metadata(Path.cwd() / ".dataset", metadata)

    print("Dataset created [green]succesfully[/green]")

@app.command()
def push():
    pass

@app.command(name="list")
def list_remote():
    res = get_all_datasets(client=client)
    print(res)

@app.command()
def show():
    pass