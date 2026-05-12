from pathlib import Path
from dataclasses import asdict
from radiant.utils.files.files import find_file_upwards
import yaml

import typer
from rich import print



from .dataset_metadata_schema import (
    DatasetMetadataSchema,
    DEFAULT_CONFIG,
    default_config_dict,
)


def get_config_path() -> Path:
    path = find_file_upwards(Path.cwd(), ".dataset")

    if path == None:
        print("[red]Error: not in a dataset, try:\n[bold]radiant dataset init[/bold][/red]")
        raise typer.Exit()

    return path


def create_dataset_metadata(path: Path, metadata: DatasetMetadataSchema) -> None:
    save_dataset_metadata(metadata, path)


def load_dataset_metadata(path: Path | None = None) -> DatasetMetadataSchema:
    
    if path is None:
      path = get_config_path()


    with open(path, "r") as file:
        data = yaml.safe_load(file) or {}

    defaults = default_config_dict()
    defaults.update(data)

    return DatasetMetadataSchema(**defaults)


def save_dataset_metadata(config: DatasetMetadataSchema, path: Path | None = None ) -> None:


    if path is None:
        path = get_config_path()


    with open(path, "w") as file:
        yaml.safe_dump(asdict(config), file, sort_keys=False)
