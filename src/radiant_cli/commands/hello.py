from rich.console import Console
from radiant_cli.services.health_service import get_hello_health
import asyncio

console = Console()

def hello():
    """Pings to your remote repository."""
    asyncio.run(async_hello())

async def async_hello():
    try:
      data = await get_hello_health()
      console.print(data["message"], style="bold green")
    except:
       console.print("Cannot connect to the server", style="bold red")
