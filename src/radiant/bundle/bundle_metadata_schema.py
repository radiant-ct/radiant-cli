from dataclasses import dataclass, field
from typing import Any


@dataclass
class BundleMetadataSchema:
    name: str
    image_ids: list[str] = field(default_factory=list)