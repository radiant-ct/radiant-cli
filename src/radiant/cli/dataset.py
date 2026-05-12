import typer

from dataclasses import asdict

from radiant.backend_api import Client   
from radiant.backend_api.api.dataset_controller.get_all_datasets import sync as get_all_datasets

from radiant.config.config import load_config
from radiant.utils.files.files import  is_file_upwards, find_file_upwards

from radiant.dataset.dataset_metadata_schema import DatasetMetadataSchema
from radiant.dataset.dataset_metadata_service import create_dataset_metadata, load_dataset_metadata

from pathlib import Path
from rich import print
from rich.console import Console
from rich.table import Table

app = typer.Typer()
config = load_config()
client = Client(base_url=config.remote)
console = Console()

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
    dataset_path = find_file_upwards(Path.cwd(), ".dataset")

    if dataset_path is None:
        print("[red]Error: not in a dataset folder, try: \r [bold]radiant dataset init[/bold][/red]")
        raise typer.Exit()
    
    metadata = load_dataset_metadata(dataset_path)
    _pretty_print_dataset_metadata(metadata)



def _pretty_print_dataset_metadata(metadata: DatasetMetadataSchema):
    table = Table(title="Dataset Metadata")

    table.add_column("Field", style="cyan bold")
    table.add_column("Value", style="white")

    for key, value in asdict(metadata).items():
        table.add_row(key, str(value))

    console.print(table)