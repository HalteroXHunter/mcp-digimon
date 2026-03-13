import pytest
import os
from src.mcp_modules import tools, resources

@pytest.mark.asyncio
async def test_get_digimon_success():
    result = await tools.get_digimon("agumon")
    assert "Agumon" in result
    assert "Description" in result
    assert "Levels: Child" in result

@pytest.mark.asyncio
async def test_search_digimon():
    result = await tools.search_digimon(query="agu", exact=False)
    assert "Found" in result
    assert "Agumon" in result

@pytest.mark.asyncio
async def test_get_skill():
    result = await tools.get_skill("1")
    assert "Description" in result
    assert "Skill:" in result

@pytest.mark.asyncio
async def test_get_digimon_data_resource():
    result = await resources.get_digimon_data("agumon")
    assert "{" in result # Should be JSON
    assert '"name": "Agumon"' in result
