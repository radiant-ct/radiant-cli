import typer
from rich import print
from importlib.metadata import version

from radiant.cli.workspace import app as workspace_app
from radiant.cli.dataset import app as dataset_app
from radiant.backend_api.api.health_controller.health import sync as health_check

from rich.console import Console
from radiant.config.config import load_config
from radiant.cli.dataset import app as dataset_app, get_client
from radiant.backend_api.api.health_controller.health import sync as health_check
from radiant.backend_api.client import Client
from radiant.cli.bundle import app as bundle_app
APP_VERSION = version("radiant-ct")

app = typer.Typer()

def version_callback(value: bool):
    if value:
        print("radiant " + APP_VERSION)
        raise typer.Exit()


@app.callback()
def main(
    version: bool = typer.Option(
        None,
        "--version",
        "-v",
        callback=version_callback,
        is_eager=True,
        help="Show version and exit.",
    )
):
    pass


@app.command()
def health():
    """Check connectivity to the configured remote."""
    config = load_config()
    client = Client(base_url=config.remote)
    print(f"Pinging [cyan]{config.remote}[/cyan]...")
    try:
        result = health_check(client=client)
        if result is not None:
            print(f"[green]✓ Remote is healthy[/green] — {result}")
        else:
            print("[red]✗ Remote returned an empty response[/red]")
            raise typer.Exit(1)
    except Exception as e:
        print(f"[red]✗ Could not reach remote:[/red] {e}")
        raise typer.Exit(1)




# Modules
app.add_typer(workspace_app, name="workspace", help="Commands related to workspaces and configuration.")
app.add_typer(dataset_app, name="dataset", help="Commands related to datasets management.")
app.add_typer(bundle_app, name="bundle", help="Commands for managing image bundles.")
