from __future__ import annotations

import json
from collections.abc import Mapping
from io import BytesIO
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import File

if TYPE_CHECKING:
    from ..models.dataset_creation_dto import DatasetCreationDTO


T = TypeVar("T", bound="CreateDatasetBody")


@_attrs_define
class CreateDatasetBody:
    """
    Attributes:
        data (DatasetCreationDTO):
        file (File):
    """

    data: DatasetCreationDTO
    file: File
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        file = self.file.to_tuple()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "file": file,
            }
        )

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("data", (None, json.dumps(self.data.to_dict()).encode(), "application/json")))

        files.append(("file", self.file.to_tuple()))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataset_creation_dto import DatasetCreationDTO

        d = dict(src_dict)
        data = DatasetCreationDTO.from_dict(d.pop("data"))

        file = File(payload=BytesIO(d.pop("file")))

        create_dataset_body = cls(
            data=data,
            file=file,
        )

        create_dataset_body.additional_properties = d
        return create_dataset_body

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
