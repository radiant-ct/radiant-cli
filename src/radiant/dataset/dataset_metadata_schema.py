from dataclasses import dataclass, asdict
from pathlib import Path
import yaml


CONFIG_FILE = ".dataset"


@dataclass
class DatasetMetadataSchema:
    name: str = "New dataset"
    description: str = "This is a dataset"
    credits: str = "Anonymous"


DEFAULT_CONFIG = DatasetMetadataSchema()


def default_config_dict() -> dict:
    return asdict(DEFAULT_CONFIG)


def config_path(path: Path | None = None) -> Path:
    return (path or Path.cwd()) / CONFIG_FILE