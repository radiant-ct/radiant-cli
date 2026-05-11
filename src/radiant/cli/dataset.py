import typer

from radiant.backend_api import Client   
from radiant.backend_api.api.dataset_controller.get_all_datasets import sync as get_all_datasets

from radiant.config.config import load_config

app = typer.Typer()
config = load_config()
client = Client(base_url=config.remote)

@app.command()
def init():
    pass


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