import tarfile
import typer

from pathlib import Path
from rich import print
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, Confirm
from rich.progress import (
    Progress, SpinnerColumn, TextColumn,
    BarColumn, DownloadColumn, TransferSpeedColumn, TimeRemainingColumn,
)

from radiant.bundle.bundle_metadata_schema import BundleMetadataSchema
from radiant.bundle.bundle_metadata_service import (
    create_bundle_metadata,
    load_bundle_metadata,
    save_bundle_metadata,
)
from radiant.backend_api.models.image_filter import ImageFilter
from radiant.backend_api.api.image_controller.search_images import sync as search_images
from radiant.utils.files.files import find_file_upwards
from radiant.cli.dataset import get_client

from typing import Any

import httpx

app = typer.Typer()
console = Console()

BUNDLE_FILE = ".bundle"
MEDIA_DIR   = "media"
BACKEND_PORT = 7777

# ─────────────────────────────────────────────────────────────────────────────
# Filter field definitions — single source of truth for the TUI
# Each entry: (human label, ImageFilter snake_case attr, camelCase YAML key, type)
# ─────────────────────────────────────────────────────────────────────────────

_CATEGORICAL_FIELDS = [
    # (label,                ImageFilter attr,      camelCase key)
    ("Sex",                  "sex",                 "sex"),
    ("Convolution Kernel",   "convolution_kernel",  "convolutionKernel"),
    ("Manufacturer",         "manufacturer",        "manufacturer"),
    ("Manufacturer Model",   "manufacturer_model",  "manufacturerModel"),
    ("Software Version",     "software_version",    "softwareVersion"),
]

_RANGE_FIELDS = [
    # (label,                          base attr,                                    type)
    ("Age (years)",                    "age_years",                                  int),
    ("Study Date (YYYY-MM-DD)",        "study_date",                                 str),
    ("KVP",                            "kvp",                                        float),
    ("Exposure mAs",                   "exposure_mas",                               float),
    ("Slice Thickness (mm)",           "slice_thickness_mm",                         float),
    ("Pixel Spacing (mm)",             "pixel_spacing_mm",                           float),
    ("Rows",                           "rows",                                       int),
    ("Columns",                        "columns",                                    int),
    ("N Slices",                       "n_slices",                                   int),
    # Shape
    ("Shape Mesh Volume",              "shape_mesh_volume",                          float),
    ("Shape Voxel Volume",             "shape_voxel_volume",                         float),
    ("Shape Surface Area",             "shape_surface_area",                         float),
    ("Shape Sphericity",               "shape_sphericity",                           float),
    ("Shape Compactness 1",            "shape_compactness_1",                        float),
    ("Shape Compactness 2",            "shape_compactness_2",                        float),
    ("Shape Max 3D Diameter",          "shape_maximum_3_d_diameter",                 float),
    ("Shape Major Axis Length",        "shape_major_axis_length",                    float),
    ("Shape Minor Axis Length",        "shape_minor_axis_length",                    float),
    ("Shape Least Axis Length",        "shape_least_axis_length",                    float),
    ("Shape Elongation",               "shape_elongation",                           float),
    ("Shape Flatness",                 "shape_flatness",                             float),
    # First order
    ("First Energy",                   "first_energy",                               float),
    ("First Total Energy",             "first_total_energy",                         float),
    ("First Entropy",                  "first_entropy",                              float),
    ("First Minimum",                  "first_minimum",                              float),
    ("First 10th Percentile",          "first_10_th_percentile",                     float),
    ("First 90th Percentile",          "first_90_th_percentile",                     float),
    ("First Maximum",                  "first_maximum",                              float),
    ("First Mean",                     "first_mean",                                 float),
    ("First Median",                   "first_median",                               float),
    ("First IQR",                      "first_interquartile_range",                  float),
    ("First Range",                    "first_range",                                float),
    ("First Mean Abs Deviation",       "first_mean_absolute_deviation",              float),
    ("First Robust MAD",               "first_robust_mean_absolute_deviation",       float),
    ("First RMS",                      "first_root_mean_squared",                    float),
    ("First Skewness",                 "first_skewness",                             float),
    ("First Kurtosis",                 "first_kurtosis",                             float),
    ("First Variance",                 "first_variance",                             float),
    ("First Uniformity",               "first_uniformity",                           float),
    # GLCM
    ("GLCM Autocorrelation",           "glcm_autocorrelation",                       float),
    ("GLCM Cluster Prominence",        "glcm_cluster_prominence",                    float),
    ("GLCM Cluster Shade",             "glcm_cluster_shade",                         float),
    ("GLCM Cluster Tendency",          "glcm_cluster_tendency",                      float),
    ("GLCM Contrast",                  "glcm_contrast",                              float),
    ("GLCM Correlation",               "glcm_correlation",                           float),
    ("GLCM Difference Average",        "glcm_difference_average",                    float),
    ("GLCM Difference Entropy",        "glcm_difference_entropy",                    float),
    ("GLCM Difference Variance",       "glcm_difference_variance",                   float),
    ("GLCM ID",                        "glcm_id",                                    float),
    ("GLCM IDM",                       "glcm_idm",                                   float),
    ("GLCM IDMN",                      "glcm_idmn",                                  float),
    ("GLCM IDN",                       "glcm_idn",                                   float),
    ("GLCM IMC1",                      "glcm_imc_1",                                 float),
    ("GLCM IMC2",                      "glcm_imc_2",                                 float),
    ("GLCM Inverse Variance",          "glcm_inverse_variance",                      float),
    ("GLCM Joint Average",             "glcm_joint_average",                         float),
    ("GLCM Joint Energy",              "glcm_joint_energy",                          float),
    ("GLCM Joint Entropy",             "glcm_joint_entropy",                         float),
    ("GLCM Max Probabilities",         "glcm_max_probabilities",                     float),
    ("GLCM Sum Average",               "glcm_sum_average",                           float),
    ("GLCM Sum Entropy",               "glcm_sum_entropy",                           float),
    ("GLCM Sum Squares",               "glcm_sum_squares",                           float),
    # GLRLM
    ("GLRLM GL Non-Uniformity",        "glrlm_gray_level_non_uniformity",            float),
    ("GLRLM GLNU Normalized",          "glrlm_gray_level_non_uniformity_normalized", float),
    ("GLRLM GL Variance",              "glrlm_gray_level_variance",                  float),
    ("GLRLM High GL Run Emphasis",     "glrlm_high_gray_level_run_emphasis",         float),
    ("GLRLM Long Run Emphasis",        "glrlm_long_run_emphasis",                    float),
    ("GLRLM Long Run High GL",         "glrlm_long_run_high_gray_level_emphasis",    float),
    ("GLRLM Long Run Low GL",          "glrlm_long_run_low_gray_level_emphasis",     float),
    ("GLRLM Low GL Run Emphasis",      "glrlm_low_gray_level_run_emphasis",          float),
    ("GLRLM Run Entropy",              "glrlm_run_entropy",                          float),
    ("GLRLM Run Length Non-Unif.",     "glrlm_run_length_non_uniformity",            float),
    ("GLRLM RLNU Normalized",          "glrlm_run_length_non_uniformity_normalized", float),
    ("GLRLM Run Percentage",           "glrlm_run_percentage",                       float),
    ("GLRLM Run Variance",             "glrlm_run_variance",                         float),
    ("GLRLM Short Run Emphasis",       "glrlm_short_run_emphasis",                   float),
    ("GLRLM Short Run High GL",        "glrlm_short_run_high_gray_level_emphasis",   float),
    ("GLRLM Short Run Low GL",         "glrlm_short_run_low_gray_level_emphasis",    float),
    # GLSZM
    ("GLSZM GL Non-Uniformity",        "glszm_gray_level_non_uniformity",            float),
    ("GLSZM GLNU Normalized",          "glszm_gray_level_non_uniformity_normalized", float),
    ("GLSZM GL Variance",              "glszm_gray_level_variance",                  float),
    ("GLSZM High GL Zone Emphasis",    "glszm_high_gray_level_zone_emphasis",        float),
    ("GLSZM Large Area Emphasis",      "glszm_large_area_emphasis",                  float),
    ("GLSZM Large Area High GL",       "glszm_large_area_high_gray_level_emphasis",  float),
    ("GLSZM Large Area Low GL",        "glszm_large_area_low_gray_level_emphasis",   float),
    ("GLSZM Low GL Zone Emphasis",     "glszm_low_gray_level_zone_emphasis",         float),
    ("GLSZM Size Zone Non-Unif.",      "glszm_size_zone_non_uniformity",             float),
    ("GLSZM SZNU Normalized",          "glszm_size_zone_non_uniformity_normalized",  float),
    ("GLSZM Small Area Emphasis",      "glszm_small_area_emphasis",                  float),
    ("GLSZM Small Area High GL",       "glszm_small_area_high_gray_level_emphasis",  float),
    ("GLSZM Small Area Low GL",        "glszm_small_area_low_gray_level_emphasis",   float),
    ("GLSZM Zone Entropy",             "glszm_zone_entropy",                         float),
    ("GLSZM Zone Percentage",          "glszm_zone_percentage",                      float),
    ("GLSZM Zone Variance",            "glszm_zone_variance",                        float),
    # NGTDM
    ("NGTDM Busyness",                 "ngtdm_busyness",                             float),
    ("NGTDM Coarseness",               "ngtdm_coarseness",                           float),
    ("NGTDM Complexity",               "ngtdm_complexity",                           float),
    ("NGTDM Contrast",                 "ngtdm_contrast",                             float),
    ("NGTDM Strength",                 "ngtdm_strength",                             float),
    # GLDM
    ("GLDM Dependence Entropy",        "gldm_dependence_entropy",                    float),
    ("GLDM Dependence Non-Unif.",      "gldm_dependence_non_uniformity",             float),
    ("GLDM Dep. Non-Unif. Norm.",      "gldm_dependence_non_uniformity_normalized",  float),
    ("GLDM Dependence Variance",       "gldm_dependence_variance",                   float),
    ("GLDM GL Non-Uniformity",         "gldm_gray_level_non_uniformity",             float),
    ("GLDM GL Variance",               "gldm_gray_level_variance",                   float),
    ("GLDM High GL Emphasis",          "gldm_high_gray_level_emphasis",              float),
    ("GLDM Large Dep. Emphasis",       "gldm_large_dependence_emphasis",             float),
    ("GLDM Large Dep. High GL",        "gldm_large_dependence_high_gray_level_emphasis", float),
    ("GLDM Large Dep. Low GL",         "gldm_large_dependence_low_gray_level_emphasis",  float),
    ("GLDM Low GL Emphasis",           "gldm_low_gray_level_emphasis",               float),
    ("GLDM Small Dep. Emphasis",       "gldm_small_dependence_emphasis",             float),
    ("GLDM Small Dep. High GL",        "gldm_small_dependence_high_gray_level_emphasis", float),
    ("GLDM Small Dep. Low GL",         "gldm_small_dependence_low_gray_level_emphasis",  float),
]


# ─────────────────────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────────────────────

def _require_bundle_file() -> Path:
    path = find_file_upwards(Path.cwd(), BUNDLE_FILE)
    if path is None:
        print("[red]Error: not in a bundle folder, try:\n [bold]radiant bundle init <name>[/bold][/red]")
        raise typer.Exit()
    return path


def _prompt_range(label: str, cast: type) -> tuple[Any, Any]:
    """Prompt for an optional min/max pair. Returns (min|None, max|None)."""
    console.print(f"  [cyan]{label}[/cyan]")
    raw_min = Prompt.ask("    min", default="").strip()
    raw_max = Prompt.ask("    max", default="").strip()
    try:
        v_min = cast(raw_min) if raw_min else None
    except ValueError:
        console.print(f"    [yellow]Invalid min, skipping[/yellow]")
        v_min = None
    try:
        v_max = cast(raw_max) if raw_max else None
    except ValueError:
        console.print(f"    [yellow]Invalid max, skipping[/yellow]")
        v_max = None
    return v_min, v_max


def _build_filter(collected: dict) -> ImageFilter:
    """Build an ImageFilter from the flat camelCase dict the TUI collects."""
    return ImageFilter.from_dict(collected)


# ─────────────────────────────────────────────────────────────────────────────
# Commands
# ─────────────────────────────────────────────────────────────────────────────

@app.command()
def init(name: str = typer.Argument(..., help="Name of the bundle")):
    """Create a new bundle folder."""
    bundle_dir  = Path.cwd() / name
    bundle_file = bundle_dir / BUNDLE_FILE

    if bundle_dir.exists():
        print(f"[red]Error: folder [bold]{name}[/bold] already exists[/red]")
        raise typer.Exit()

    bundle_dir.mkdir()
    create_bundle_metadata(bundle_file, BundleMetadataSchema(name=name))

    console.rule(f"[bold cyan]Bundle '{name}' initialised[/bold cyan]")
    print(f"  [dim]{bundle_file}[/dim]\n")
    print("Next steps:")
    print(f"  [cyan]cd {name}[/cyan]")
    print(f"  [cyan]radiant bundle add[/cyan]   ← query images and store their IDs")
    print(f"  [cyan]radiant bundle pull[/cyan]  ← download the images")


"""
Replace the `add` command in radiant/cli/bundle.py with this.
Everything else (init, pull, show) stays identical.
"""

from radiant.cli.bundle_tui import run_filter_tui

@app.command()
def add():
    """Interactively filter images and save their IDs into the bundle."""
    bundle_file = _require_bundle_file()
    metadata    = load_bundle_metadata(bundle_file)

    results = run_filter_tui(
        bundle_name=metadata.name,
        search_fn=lambda f: search_images(client=get_client(), filter_=f),
    )

    if not results:
        print("[yellow]No images saved — bundle unchanged.[/yellow]")
        raise typer.Exit()

    new_ids      = [str(img.id) for img in results]
    existing_set = set(metadata.image_ids)
    added        = [i for i in new_ids if i not in existing_set]
    metadata.image_ids = list(existing_set | set(new_ids))
    save_bundle_metadata(bundle_file, metadata)

    from rich.console import Console
    Console().print(
        f"[green]{len(added)} new ID(s) added.[/green] "
        f"Bundle [bold]{metadata.name}[/bold] now has "
        f"[bold]{len(metadata.image_ids)}[/bold] image(s)."
    )

@app.command()
def pull():
    """Download all images in the bundle into ./media/<id>.tar.gz (decompressed)."""
    bundle_file = _require_bundle_file()
    metadata    = load_bundle_metadata(bundle_file)

    if not metadata.image_ids:
        print("[yellow]Bundle has no image IDs. Run [bold]radiant bundle add[/bold] first.[/yellow]")
        raise typer.Exit()

    media_dir = bundle_file.parent / MEDIA_DIR
    media_dir.mkdir(exist_ok=True)

    config      = _load_config()
    # Replace whatever port the config has with 8888 for media downloads
    from urllib.parse import urlparse, urlunparse
    parsed      = urlparse(config.remote)
    base_url    = urlunparse(parsed._replace(netloc=f"{parsed.hostname}:{BACKEND_PORT}"))

    console.rule(f"[bold cyan]Pulling {len(metadata.image_ids)} image(s)[/bold cyan]")

    with Progress(
        SpinnerColumn(),
        TextColumn("[cyan]{task.description:<30}"),
        BarColumn(bar_width=28),
        DownloadColumn(),
        TransferSpeedColumn(),
        TimeRemainingColumn(),
        console=console,
        transient=False,
    ) as progress:

        for image_id in metadata.image_ids:
            archive_path = media_dir / f"{image_id}.tar.gz"
            extract_path = media_dir / image_id
            url          = f"{base_url}/media/{image_id}.tar.gz"

            task = progress.add_task(f"{image_id[:8]}…", total=None)

            try:
                with httpx.stream("GET", url, timeout=120) as r:
                    r.raise_for_status()
                    total = int(r.headers.get("content-length", 0)) or None
                    progress.update(task, total=total)

                    with open(archive_path, "wb") as f:
                        for chunk in r.iter_bytes(chunk_size=65536):
                            f.write(chunk)
                            progress.update(task, advance=len(chunk))

            except httpx.HTTPError as e:
                progress.update(task, description=f"[red]{image_id[:8]}… FAILED[/red]")
                console.print(f"  [red]✗ {image_id}: {e}[/red]")
                continue

            # Decompress
            progress.update(task, description=f"{image_id[:8]}… extracting")
            extract_path.mkdir(exist_ok=True)
            with tarfile.open(archive_path, "r:gz") as tar:
                tar.extractall(path=extract_path)
            archive_path.unlink()

            progress.update(task, description=f"[green]{image_id[:8]}… ✓[/green]")

    console.rule("[bold green]Done[/bold green]")
    print(f"  Images saved to [dim]{media_dir}[/dim]")


@app.command()
def show():
    """Show the current bundle contents."""
    bundle_file = _require_bundle_file()
    metadata    = load_bundle_metadata(bundle_file)

    console.rule(f"[bold cyan]Bundle: {metadata.name}[/bold cyan]")

    if not metadata.image_ids:
        print("[yellow]No images yet. Run [bold]radiant bundle add[/bold].[/yellow]")
        return

    table = Table(border_style="cyan", header_style="bold cyan")
    table.add_column("#",   style="dim", justify="right")
    table.add_column("Image ID")

    for i, image_id in enumerate(metadata.image_ids, 1):
        table.add_row(str(i), image_id)

    console.print(table)
    print(f"\nTotal: [bold]{len(metadata.image_ids)}[/bold] image(s)")


def _load_config():
    from radiant.config.config import load_config
    return load_config()