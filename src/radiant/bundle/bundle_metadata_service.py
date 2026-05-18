from pathlib import Path
import yaml
from radiant.bundle.bundle_metadata_schema import BundleMetadataSchema


def create_bundle_metadata(path: Path, metadata: BundleMetadataSchema) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    _write(path, metadata)


def load_bundle_metadata(path: Path) -> BundleMetadataSchema:
    with open(path, "r") as f:
        data = yaml.safe_load(f) or {}
    return BundleMetadataSchema(
        name=data.get("name", ""),
        image_ids=data.get("image_ids", []),
    )


def save_bundle_metadata(path: Path, metadata: BundleMetadataSchema) -> None:
    _write(path, metadata)


def _write(path: Path, metadata: BundleMetadataSchema) -> None:
    with open(path, "w") as f:
        yaml.safe_dump(
            {"name": metadata.name, "image_ids": metadata.image_ids},
            f,
            sort_keys=False,
        )