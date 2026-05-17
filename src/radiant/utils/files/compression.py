from pathlib import Path
import tarfile
from rich.progress import Progress, TaskID

def compress_dataset_folder(
    folder: str | Path,
    output: str | Path | None = None,
    *,
    progress: Progress | None = None,
    task_id: TaskID | None = None,
) -> Path:
    folder = Path(folder)
    if output is None:
        output = folder.with_suffix(".tar.gz")
    output = Path(output)

    files = [
        path
        for path in folder.rglob("*")
        if path.is_file() and path.name != ".dataset"
    ]
    total_size = sum(path.stat().st_size for path in files)

    def _run(p: Progress, t: TaskID):
        p.update(t, total=total_size)
        with tarfile.open(output, "w:gz") as tar:
            for file in files:
                arcname = file.relative_to(folder)
                tar.add(file, arcname=arcname)
                p.update(t, advance=file.stat().st_size)

    if progress is not None and task_id is not None:
        # Use the caller's progress — no nested context manager
        _run(progress, task_id)
    else:
        # Standalone usage (backward-compatible)
        with Progress() as p:
            t = p.add_task("[cyan]Compressing...", total=total_size)
            _run(p, t)

    return output