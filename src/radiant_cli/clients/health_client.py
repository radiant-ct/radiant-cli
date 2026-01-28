from radiant_cli.clients.base_api_client import  BaseAPIClient

class HealthClient(BaseAPIClient):
    async def get_hello_health(self) -> dict:
        return await self._get("/health/hello")
