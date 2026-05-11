from pathlib import Path
from dataclasses import asdict
from radiant.utils.files.files import find_file_upwards
import yaml

import typer
from rich import print



from .schema import (
    ConfigSchema,
    DEFAULT_CONFIG,
    default_config_dict,
)


def get_config_path() -> Path:
    path = find_file_upwards(Path.cwd(), ".radiant")

    if path == None:
        print("[red]Error: not in a workspace, try:\n[bold]radiant workspace init[/bold][/red]")
        raise typer.Exit()

    return path


def create_config(path: Path) -> None:
    save_config(DEFAULT_CONFIG, path)


def load_config(path: Path | None = None) -> ConfigSchema:
    
    if path is None:
      path = get_config_path()


    with open(path, "r") as file:
        data = yaml.safe_load(file) or {}

    defaults = default_config_dict()
    defaults.update(data)

    return ConfigSchema(**defaults)


def save_config(config: ConfigSchema, path: Path | None = None ) -> None:


    if path is None:
        path = get_config_path()


    with open(path, "w") as file:
        yaml.safe_dump(asdict(config), file, sort_keys=False)

def get_config(key: str):
    config = load_config()

    if not hasattr(config, key):
        print(f"[red]Error: Unknown config key [bold]{key}[/bold][/red]")
        raise typer.Exit()


    return getattr(config, key)


def set_config(key: str, value):
    config = load_config()

    if not hasattr(config, key):
        print(f"[red]Error: Unknown config key [bold]{key}[/bold][/red]")
        raise typer.Exit()

    setattr(config, key, value)

    save_config(config)