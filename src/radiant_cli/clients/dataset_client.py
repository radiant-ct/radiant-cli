from typing import List, Callable
from radiant_cli.clients.base_api_client import BaseAPIClient
from radiant_cli.clients.models.dataset_models import DatasetCreate, DatasetRead
import json

class DatasetClient(BaseAPIClient):

    async def create_dataset(self, dataset: DatasetCreate, file_path: str, progress_cb: Callable[[int], None] | None = None):
        data = {"data": json.dumps(dataset.dict())}

        class _ProgressReader:
            def __init__(self, fp, cb: Callable[[int], None] | None):
                self._fp = fp
                self._cb = cb

            def read(self, size=-1):
                chunk = self._fp.read(size)
                if chunk and self._cb:
                    self._cb(len(chunk))
                return chunk

            def __getattr__(self, name):
                return getattr(self._fp, name)

        f = open(file_path, "rb")
        reader = _ProgressReader(f, progress_cb)

        files = {
            "file": (
                "dataset.tar.gz",
                reader,
                "application/gzip",
            )
        }

        resp = await self._post_multipart("/datasets/", data=data, files=files)

        if isinstance(resp, dict) and "error" in resp:
            try:
                f.close()
            except Exception:
                pass
            return resp

        try:
            f.close()
        except Exception:
            pass

        return DatasetRead(**resp)
