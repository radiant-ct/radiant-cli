import httpx


async def get_hello_health() -> dict:
    base_url = "http://localhost:8000"
    url = f"{base_url}/health/hello"
    async with httpx.AsyncClient(timeout=5.0) as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            return response.json()
        except httpx.RequestError as e:
            return {"error": f"Request error: {str(e)}"}
        except httpx.HTTPStatusError as e:
            return {"error": f"HTTP error {e.response.status_code}: {e.response.text}"}
