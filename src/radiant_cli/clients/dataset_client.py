from typing import List
from radiant_cli.clients.base_api_client import BaseAPIClient
from radiant_cli.clients.models.dataset_models import DatasetCreate, DatasetRead
import json

class DatasetClient(BaseAPIClient):

    async def create_dataset(self, dataset: DatasetCreate, file_path: str):
        data = {"data": json.dumps(dataset.dict())}

        files = {
            "file": (
                "dataset.tar.gz",
                open(file_path, "rb"),
                "application/gzip"
            )
        }

        resp = await self._post_multipart("/datasets/", data=data, files=files)

        if isinstance(resp, dict) and "error" in resp:
            return resp

        return DatasetRead(**resp)
