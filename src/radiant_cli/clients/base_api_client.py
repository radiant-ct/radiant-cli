import httpx
from radiant_cli.utils.config_util import load_config

class BaseAPIClient:
    def __init__(self):
        config = load_config()
        self.base_url = config.remote.base_url
        self.timeout = 10.0

    async def _get(self, path: str):
        url = f"{self.base_url}{path}"
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            try:
                resp = await client.get(url)
                resp.raise_for_status()
                return resp.json()

            except httpx.RequestError as e:
                return {"error": f"Request error: {str(e)}"}

            except httpx.HTTPStatusError as e:
                return {
                    "error": f"HTTP {e.response.status_code}",
                    "details": e.response.text,
                }

    async def _post(self, path: str, data: dict):
        url = f"{self.base_url}{path}"
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            try:
                resp = await client.post(url, json=data)
                resp.raise_for_status()
                return resp.json()

            except httpx.RequestError as e:
                return {"error": f"Request error: {str(e)}"}

            except httpx.HTTPStatusError as e:
                return {
                    "error": f"HTTP {e.response.status_code}",
                    "details": e.response.text,
                }
