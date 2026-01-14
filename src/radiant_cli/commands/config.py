import typer
from radiant_cli.utils.config_util import save_config, load_config, RadiantCLIConfiguration

app = typer.Typer(help="Configuration commands")

from typing import Optional, Callable

def get_or_set(
    value: Optional[str],
    getter: Callable[[], str],
    setter: Callable[[str], None],
    save: Callable[[], None],
    label: str = "Value",
):
    if value is None:
        typer.echo(getter())
    else:
        setter(value)
        save()
        typer.echo(f"{label} set to: {value}")

@app.command()
def remote(url: Optional[str] = typer.Argument(
        None,
        help="Remote repository URL"
    )):
    """Get or set the remote repository URL."""
    config: RadiantCLIConfiguration = load_config()

    get_or_set(
        value=url,
        getter=lambda: config.remote.base_url,
        setter=lambda v: setattr(config.remote, "base_url", v),
        save=lambda: save_config(config),
        label="Remote URL",
    )
