import os

def find_radiant_root(start_path=None):
    """
    Recursively searches upward from start_path (or current dir)
    to find the nearest '.radiant' directory.
    Returns the absolute path to the folder containing '.radiant',
    or None if not found.
    """
    if start_path is None:
        start_path = os.getcwd()

    current_dir = os.path.abspath(start_path)

    while True:
        radiant_path = os.path.join(current_dir, ".radiant")
        if os.path.isdir(radiant_path):
            return current_dir

        parent_dir = os.path.dirname(current_dir)
        if parent_dir == current_dir:
            return None

        current_dir = parent_dir


def create_radiant_folder():
    """
    Creates an empty '.radiant' folder in the current working directory.
    If it already exists, does nothing.
    """
    path = os.path.join(os.getcwd(), ".radiant")
    os.makedirs(path, exist_ok=True)
    return path
