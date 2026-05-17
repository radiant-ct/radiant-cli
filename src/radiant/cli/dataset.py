import typer

from dataclasses import asdict

from radiant.backend_api.models import DatasetCreationDTO
from radiant.backend_api import Client
from radiant.backend_api.models.create_dataset_body import CreateDatasetBody
from radiant.backend_api.api.dataset_controller.get_all_datasets import sync as get_all_datasets
from radiant.backend_api.api.dataset_controller.create_dataset import sync as create_dataset
from radiant.backend_api.api.dataset_controller.create_dataset import sync_detailed as create_dataset_detailed
from radiant.backend_api.types import File

from radiant.config.config import load_config
from radiant.utils.files.files import  is_file_upwards, find_file_upwards

from radiant.dataset.dataset_metadata_schema import DatasetMetadataSchema
from radiant.dataset.dataset_metadata_service import create_dataset_metadata, load_dataset_metadata

from radiant.utils.files.compression import compress_dataset_folder

from pathlib import Path
from rich import print
from rich.console import Console
from rich.table import Table

import io
from rich.progress import (
    Progress, SpinnerColumn, TextColumn,
    BarColumn, FileSizeColumn, TransferSpeedColumn, TimeRemainingColumn,
)

app = typer.Typer()
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
    metadata_path = find_file_upwards(Path.cwd(), ".dataset")
    if metadata_path is None:
        print("[red]Error: not in a dataset folder, try:\n [bold]radiant dataset init[/bold][/red]")
        raise typer.Exit()

    if not is_file_upwards(Path.cwd(), ".radiant"):
        print("[red]Error: not in a workspace, try:\n[bold]radiant workspace init[/bold][/red]")
        raise typer.Exit()


    metadata = load_dataset_metadata(metadata_path)
    console.rule("[bold cyan]Pushing dataset[/bold cyan]")

    with Progress(
        SpinnerColumn(),
        TextColumn("[cyan]{task.description:<25}"),
        BarColumn(bar_width=32),
        FileSizeColumn(),
        TransferSpeedColumn(),
        TimeRemainingColumn(),
        console=console,
        transient=False,
    ) as progress:

        # ── Step 1: compress ──────────────────────────────────────────────
        compress_task = progress.add_task("Compressing…", total=None)
        archive_path = compress_dataset_folder(
            metadata_path.parent,
            progress=progress,
            task_id=compress_task,
        )
        progress.update(compress_task, description="[green]Compressed ✓")

        # ── Step 2: upload ────────────────────────────────────────────────
        file_size = archive_path.stat().st_size
        upload_task = progress.add_task("Uploading…", total=file_size)

        class _TrackedFile(io.RawIOBase):
            def __init__(self, path: Path):
                self._fh = path.open("rb")
            def read(self, n=-1):
                chunk = self._fh.read(n)
                if chunk:
                    progress.update(upload_task, advance=len(chunk))
                return chunk
            def readinto(self, b):
                n = self._fh.readinto(b)
                if n:
                    progress.update(upload_task, advance=n)
                return n
            def readable(self): return True
            def close(self):
                self._fh.close()
                super().close()

        with _TrackedFile(archive_path) as tracked:
            body = CreateDatasetBody(
                data=DatasetCreationDTO(
                    name=metadata.name,
                    description=metadata.description,
                    credits_=metadata.credits,
                ),
                file=File(
                    payload=tracked,
                    file_name=archive_path.name,
                    mime_type="application/gzip",
                ),
            )
            response = create_dataset(client=get_client(), body=body)

        progress.update(upload_task, description="[green]Uploaded ✓")

    archive_path.unlink(missing_ok=True)

    if response is None:
        print("[red]Upload failed — check your remote URL.[/red]")
        raise typer.Exit(1)

    console.rule("[bold green]Done[/bold green]")
    print(f"[green]Dataset pushed![/green] Remote ID: [bold]{response.id}[/bold]")
    

@app.command(name="list")
def list_remote():
    res = get_all_datasets(client=get_client())
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



def get_client():
    config = load_config()
    return Client(base_url=config.remote)