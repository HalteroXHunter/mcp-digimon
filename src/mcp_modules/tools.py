import httpx
from typing import Any, Dict, List, Optional
from ..api import digi_client

async def get_digimon(name_or_id: str) -> str:
    """
    Fetches full details of a specific Digimon including attacks, levels, fields, and descriptions.
    
    Args:
        name_or_id: The unique ID or exact name of the Digimon (e.g., 'agumon', '271').
    """
    try:
        data = await digi_client.get_digimon(name_or_id)
        
        # Format the output nicely for the LLM
        name = data.get("name", "Unknown")
        digimon_id = data.get("id", "Unknown")
        
        # Extract descriptions
        descriptions = [d.get("description", "") for d in data.get("descriptions", []) if d.get("language") == "en-us"]
        description = descriptions[0] if descriptions else "No English description available."
        
        # Extract attributes, levels, types
        attributes = ", ".join([a.get("attribute", "") for a in data.get("attributes", [])])
        levels = ", ".join([l.get("level", "") for l in data.get("levels", [])])
        types = ", ".join([t.get("type", "") for t in data.get("types", [])])
        
        # Extract skills
        skills = "\n".join([f"- {s.get('skill', '')}: {s.get('description', '')}" for s in data.get("skills", [])])
        
        return f"""
Digimon: {name} (ID: {digimon_id})
Levels: {levels}
Types: {types}
Attributes: {attributes}

Description:
{description}

Skills:
{skills}
"""
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            return f"Digimon '{name_or_id}' not found."
        return f"API Error: {str(e)}"
    except Exception as e:
        return f"Unexpected Error: {str(e)}"

async def search_digimon(
    query: str = "",
    exact: bool = False,
    attribute: Optional[str] = None,
    level: Optional[str] = None
) -> str:
    """
    Searches for a list of Digimon matching criteria. If no exact query is given, it performs a fuzzy search.
    
    Args:
        query: The name or partial name to search for.
        exact: If true, will search for the exact string passed in the query.
        attribute: Filter by attribute (e.g., 'Vaccine', 'Virus', 'Data').
        level: Filter by level (e.g., 'Rookie', 'Champion', 'Ultimate').
    """
    try:
        data = await digi_client.search_digimon(
            name=query if query else None,
            exact=exact,
            attribute=attribute,
            level=level
        )
        
        content = data.get("content", [])
        if not content:
            return f"No Digimon found matching query: '{query}', Attribute: {attribute}, Level: {level}"
            
        # Format results
        results = []
        for d in content:
            results.append(f"- {d.get('name')} (ID: {d.get('id')}) - URL: {d.get('href')}")
            
        pageable = data.get("pageable", {})
        total_elements = pageable.get("totalElements", 0)
        
        header = f"Found {total_elements} Digimon (showing up to {len(results)}):\n"
        return header + "\n".join(results)
        
    except httpx.HTTPStatusError as e:
        return f"API Error: {str(e)}"
    except Exception as e:
        return f"Unexpected Error: {str(e)}"

async def get_skill(name_or_id: str) -> str:
    """
    Fetches information about a specific Digimon skill/attack.
    
    Args:
        name_or_id: The unique ID or exact name of the skill.
    """
    try:
        data = await digi_client.get_skill(name_or_id)
        
        name = data.get("name", "Unknown")
        skill_id = data.get("id", "Unknown")
        description = data.get("description", "No description available.")
        
        return f"Skill: {name} (ID: {skill_id})\nDescription: {description}"
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            return f"Skill '{name_or_id}' not found."
        return f"API Error: {str(e)}"
    except Exception as e:
        return f"Unexpected Error: {str(e)}"
