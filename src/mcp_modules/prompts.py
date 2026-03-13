from mcp.types import PromptMessage, TextContent
from typing import Optional

def compare_digimon(digimon1: str, digimon2: str) -> list[PromptMessage]:
    """
    Prompt template to compare two Digimon.
    
    Args:
        digimon1: The first Digimon to compare
        digimon2: The second Digimon to compare
    """
    return [
        PromptMessage(
            role="user",
            content=TextContent(
                type="text",
                text=f"""Please compare the Digimon '{digimon1}' and '{digimon2}'. 

Use the `get_digimon` tool to fetch their data.
1. Compare their types, attributes, and levels.
2. Discuss their unique skills and how they might fare against one another in battle.
3. Determine who might have an elemental or type advantage.
"""
            )
        )
    ]

def suggest_team(
    preferred_level: Optional[str] = None, 
    preferred_attribute: Optional[str] = None
) -> list[PromptMessage]:
    """
    Prompt template to suggest a cohesive Digimon team.
    
    Args:
        preferred_level: The preferred Digimon level (e.g., 'Ultimate', 'Mega')
        preferred_attribute: The preferred Digimon attribute (e.g., 'Data', 'Vaccine', 'Virus')
    """
    return [
        PromptMessage(
            role="user",
            content=TextContent(
                type="text",
                text=f"""Please suggest a cohesive team of 3 Digimon.

Use the `search_digimon` tool to find potential candidates.
Focus constraints:
- Preferred Level: {preferred_level if preferred_level else 'Any'}
- Preferred Attribute: {preferred_attribute if preferred_attribute else 'Any'}

Use the `get_digimon` tool to gather details on your top 3 picks and explain:
1. Why this team works well together.
2. The team's overall battle strategy based on their skills.
"""
            )
        )
    ]
