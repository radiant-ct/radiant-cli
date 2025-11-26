from pathlib import Path
import tarfile
from typing import Callable, Iterable


def iter_files(root: Path) -> Iterable[Path]:
    """Yield file paths under root, skipping the .dataset metadata folder.

    This keeps the logic in one place so callers can pre-count files, or
    iterate and add them to the tar while updating progress.
    """
    for p in root.rglob("*"):
        if any(part == ".dataset" for part in p.parts):
            continue
        if p.is_file():
            yield p


def make_tar_gz_with_progress(root: Path, output_file: Path, progress_callback: Callable[[int], None] | None = None) -> None:
    """Create a .tar.gz archive from `root` while calling `progress_callback(bytes_added)`.

    The function walks files deterministically and adds them into the tar.gz archive
    using file objects; after writing each file we call progress_callback with the number
    of bytes read from that file so callers can update a progress bar.
    """
    root = root.resolve()
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with tarfile.open(output_file, "w:gz") as tar:
        for file_path in iter_files(root):
            arcname = file_path.relative_to(root)
            with file_path.open("rb") as f:
                tarinfo = tar.gettarinfo(fileobj=f, arcname=arcname)
                tar.addfile(tarinfo, fileobj=f)
                if progress_callback:
                    progress_callback(tarinfo.size)
