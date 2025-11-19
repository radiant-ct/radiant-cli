from typing import List
from radiant_cli.clients.base_api_client import BaseAPIClient
from radiant_cli.clients.models.dataset_models import DatasetCreate, DatasetRead


class DatasetClient(BaseAPIClient):

    async def list_datasets(self) -> List[DatasetRead] | dict:
        data = await self._get("/datasets/")
        # If error, return raw dict
        if isinstance(data, dict) and "error" in data:
            return data
        return [DatasetRead(**item) for item in data]

    async def create_dataset(self, dataset: DatasetCreate) -> DatasetRead | dict:
        payload = dataset.dict()
        data = await self._post("/datasets/", payload)
        if isinstance(data, dict) and "error" in data:
            return data
        return DatasetRead(**data)
