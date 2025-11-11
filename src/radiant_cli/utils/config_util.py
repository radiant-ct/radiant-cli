from dataclasses import dataclass, asdict, field, fields, is_dataclass
import tomli_w
import tomli
from radiant_cli.utils.radiant_folder_util import find_radiant_root
import os


@dataclass
class RemoteConfiguration:
    base_url: str = "http://localhost:8000"


@dataclass
class RadiantCLIConfiguration:
    app_name: str = "MyApp"
    remote: RemoteConfiguration = field(default_factory=RemoteConfiguration)


def generate_default_config():
    save_config(RadiantCLIConfiguration())


def save_config(config: RadiantCLIConfiguration):
    with open(get_config_path(), "wb") as f:
        f.write(tomli_w.dumps(asdict(config)).encode("utf-8"))


def load_config() -> RadiantCLIConfiguration:
    with open(get_config_path(), "rb") as f:
        data = tomli.load(f)
    return _from_dict(RadiantCLIConfiguration, data)


def get_config_path():
    return os.path.join(find_radiant_root(), ".radiant", "config.toml")


def _from_dict(cls, data: dict):
    if not is_dataclass(cls):
        return data

    kwargs = {}
    for f in fields(cls):
        value = data.get(f.name, None)
        if value is not None:
            if is_dataclass(f.type):
                value = _from_dict(f.type, value)
        kwargs[f.name] = value

    return cls(**kwargs)
