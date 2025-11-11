from rich.console import Console
from radiant_cli.utils.radiant_folder_util import create_radiant_folder, find_radiant_root
from radiant_cli.utils.config_util import generate_default_config
from pathlib import Path

console = Console()


class RadiantInitializationError(Exception):
    """Raised when trying to initialize inside an existing Radiant project."""
    def __init__(self, root_path: str):
        message = (
            "Failed initialization, already inside a Radiant project.\n"
            "There is a .radiant folder in a parent directory.\n"
            f".radiant folder at: {root_path}"
        )
        super().__init__(message)

def init():
    """Initializes a new Radiant project."""
    console.print("Initializing a new Radiant!", style="bold green")

    root = find_radiant_root()
    if root is not None:
        raise RadiantInitializationError(root)

    path = create_radiant_folder()

    generate_default_config()

    console.print(f"Created new .radiant folder at: [cyan]{path}[/cyan]", style="bold green")
