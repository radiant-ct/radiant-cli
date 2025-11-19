import typer
from pathlib import Path
from rich.console import Console
from typing import Optional
from radiant_cli.utils.dataset.dataset_config_util import (
    DatasetConfiguration,
    save_metadata,
    load_metadata,
    is_dataset,
)
from rich.panel import Panel
from rich.markdown import Markdown

console: Console = Console()
app: typer.Typer = typer.Typer(help="Dataset Management Commands")


@app.command()
def init(
    path: Optional[str] = typer.Argument(None, help="Path to initialize dataset in (defaults to current directory)"),
    name: Optional[str] = typer.Option(None, "--name", "-n", help="Name of the dataset"),
    description: Optional[str] = typer.Option(None, "--description", "-d", help="Description of the dataset"),
    credits: Optional[str] = typer.Option(None, "--credits", "-c", help="Credits for the dataset"),
) -> None:
    """
    Initialize a folder as a dataset by creating a .dataset folder with meta.toml.
    """
    target: Path = Path(path) if path else Path.cwd()

    if not target.exists() or not target.is_dir():
        console.print(f"[bold red]Error:[/bold red] Path does not exist or is not a directory: {target}")
        raise typer.Exit(code=1)

    if not name:
        console.print("[bold blue]Interactive mode:[/bold blue] No dataset name provided. Please enter the details.")
        name = typer.prompt("Enter dataset name", type=str)
        description = typer.prompt("Enter dataset description (optional)", default="")
        credits = typer.prompt("Enter dataset credits (optional)", default="")
    else:
        description = description or ""
        credits = credits or ""

    if is_dataset(target):
        console.print(f"[bold yellow]Warning:[/bold yellow] Dataset already exists in {target}")
        raise typer.Exit(code=1)

    config: DatasetConfiguration = DatasetConfiguration(name=name, description=description, credits=credits)
    save_metadata(config, target)
    console.print(f"[bold green]Dataset initialized successfully at {target / '.dataset'}[/bold green]")


@app.command()
def show(path: Optional[str] = typer.Argument(None, help="Folder to show dataset info from (defaults to current directory)")) -> None:
    """
    Show dataset metadata if the folder is a dataset (contains .dataset/meta.toml).
    """
    target: Path = Path(path) if path else Path.cwd()

    if not target.exists() or not target.is_dir():
        console.print(f"[bold red]Error:[/bold red] Path does not exist or is not a directory: {target}")
        raise typer.Exit(code=1)

    if not is_dataset(target):
        console.print(f"[bold yellow]No dataset found in {target}[/bold yellow]")
        raise typer.Exit()

    metadata: DatasetConfiguration = load_metadata(target)

    files_count = 0
    folders_count = 0
    for item in target.iterdir():
        if item.name == ".dataset":
            continue
        if item.is_file():
            files_count += 1
        elif item.is_dir():
            folders_count += 1

    md_lines = [
        f"**Dataset**: {metadata.name}",
        f"**Folder:** {target}",
        f"**Description:** {metadata.description or 'N/A'}",
        f"**Credits:** {metadata.credits or 'N/A'}",
        f"**Contents:** {folders_count} folder(s), {files_count} file(s)",
    ]

    md_text = "\n\n".join(md_lines)

    console.print(Panel(Markdown(md_text), title="Dataset Info", border_style="green"))
