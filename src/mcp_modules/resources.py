import httpx
import json
from ..api import digi_client

async def get_digimon_data(name: str) -> str:
    """
    Fetches raw Digimon JSON data for programmatic access.
    Resource URI format: digimon://{name}
    """
    try:
        data = await digi_client.get_digimon(name)
        return json.dumps(data, indent=2)
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            return json.dumps({"error": f"Digimon '{name}' not found."})
        return json.dumps({"error": f"API Error: {str(e)}"})
    except Exception as e:
        return json.dumps({"error": f"Unexpected Error: {str(e)}"})
