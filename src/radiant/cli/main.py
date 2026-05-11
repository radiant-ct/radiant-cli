import typer
from rich import print
from importlib.metadata import version

APP_VERSION = version("radiant")

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
