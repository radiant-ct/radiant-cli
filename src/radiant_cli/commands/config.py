import typer
from radiant_cli.utils.config_util import save_config, load_config, RadiantCLIConfiguration

app = typer.Typer(help="Configuration commands")

@app.command()
def remote(url: str):
    """Config the url of the remote repository."""
    config : RadiantCLIConfiguration = load_config()
    config.remote.base_url = url
    save_config(config)
