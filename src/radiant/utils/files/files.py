from pathlib import Path

def is_file_upwards(start_path: str, file_name: str) -> bool:
    path = Path(start_path).resolve()

    if path.is_file():
        path = path.parent

    for parent in [path, *path.parents]:
        if (parent / file_name).exists():
            return True

    return False

def find_file_upwards(start_path: str, file_name: str) -> Path | None:
    path = Path(start_path).resolve()

    if path.is_file():
        path = path.parent

    for parent in [path, *path.parents]:
        candidate = parent / file_name
        if candidate.exists():
            return candidate

    return None
