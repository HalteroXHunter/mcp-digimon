import httpx
from typing import Any, Dict, Optional

BASE_URL = "https://digi-api.com/api/v1"

async def _get(endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Helper method to make async GET requests to the Digi API."""
    async with httpx.AsyncClient() as client:
        url = f"{BASE_URL}/{endpoint.lstrip('/')}"
        response = await client.get(url, params=params)
        response.raise_for_status()
        return response.json()

async def get_digimon(name_or_id: str) -> Dict[str, Any]:
    """
    Fetches full details of a specific Digimon.
    Endpoint: /api/v1/digimon/{id_or_name}
    """
    return await _get(f"/digimon/{name_or_id}")

async def search_digimon(
    name: Optional[str] = None,
    exact: bool = False,
    attribute: Optional[str] = None,
    level: Optional[str] = None,
    page: int = 0
) -> Dict[str, Any]:
    """
    Searches for Digimon matching criteria.
    Endpoint: /api/v1/digimon
    """
    params = {}
    if name: params["name"] = name
    if exact: params["exact"] = "true"
    if attribute: params["attribute"] = attribute
    if level: params["level"] = level
    params["page"] = page
    
    return await _get("/digimon", params=params)

async def get_skill(name_or_id: str) -> Dict[str, Any]:
    """
    Fetches details of a specific skill.
    Endpoint: /api/v1/skill/{id_or_name}
    """
    return await _get(f"/skill/{name_or_id}")
