from rich.console import Console
from radiant_cli.clients.health_service import get_hello_health
import asyncio

console = Console()

def hello():
    """Pings to your remote repository."""
    asyncio.run(_hello())

async def _hello():
    try:
      data = await get_hello_health()
      console.print(data["message"], style="bold green")
    except:
       console.print("Cannot connect to the server", style="bold red")
