from dataclasses import dataclass, asdict, field, fields, is_dataclass
from pathlib import Path
import tomli
import tomli_w
from typing import Type, TypeVar, Dict, Any

T = TypeVar("T")

@dataclass
class DatasetConfiguration:
    name: str
    description: str = ""
    credits: str = ""


def get_dataset_folder(path: Path) -> Path:
    """Return the .dataset folder inside the given path."""
    return path / ".dataset"

def get_meta_path(path: Path) -> Path:
    """Return the path to meta.toml inside .dataset."""
    return get_dataset_folder(path) / "meta.toml"

def save_metadata(config: DatasetConfiguration, path: Path) -> None:
    """Save DatasetConfiguration to meta.toml."""
    dfolder: Path = get_dataset_folder(path)
    dfolder.mkdir(parents=True, exist_ok=True)
    mfile: Path = get_meta_path(path)
    with mfile.open("wb") as f:
        tomli_w.dump(asdict(config), f)

def load_metadata(path: Path) -> DatasetConfiguration:
    """Load DatasetConfiguration from meta.toml."""
    mfile: Path = get_meta_path(path)
    if not mfile.exists():
        raise FileNotFoundError(f"No dataset metadata found in {mfile}")

    with mfile.open("rb") as f:
        data: Dict[str, Any] = tomli.load(f)
    return _from_dict(DatasetConfiguration, data)

def is_dataset(path: Path) -> bool:
    """Check if folder contains a .dataset/meta.toml."""
    return get_meta_path(path).is_file()

def _from_dict(cls: Type[T], data: Dict[str, Any]) -> T:
    """Recursively convert dict to dataclass."""
    if not is_dataclass(cls):
        return data  # type: ignore

    kwargs: Dict[str, Any] = {}
    for f in fields(cls):
        value: Any = data.get(f.name, None)
        if value is not None and is_dataclass(f.type):
            value = _from_dict(f.type, value)
        kwargs[f.name] = value

    return cls(**kwargs)
