from dataclasses import dataclass, asdict
from pathlib import Path
import yaml


CONFIG_FILE = ".radiant"


@dataclass
class ConfigSchema:
    remote: str = "http://localhost:8080"


DEFAULT_CONFIG = ConfigSchema()


def default_config_dict() -> dict:
    return asdict(DEFAULT_CONFIG)


def config_path(path: Path | None = None) -> Path:
    return (path or Path.cwd()) / CONFIG_FILE