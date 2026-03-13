import sys
import os

# Horizon runs the app from /app. Add the current working directory to sys.path
sys.path.insert(0, os.getcwd())

from mcp.server.fastmcp import FastMCP
from src.mcp_modules import tools, resources, prompts

# Initialize the global FastMCP server attached to the module
mcp = FastMCP("Digimon Server")

# -----------------
# Register Tools
# -----------------
mcp.tool()(tools.get_digimon)
mcp.tool()(tools.search_digimon)
mcp.tool()(tools.get_skill)

# -----------------
# Register Resources
# -----------------
mcp.resource("digimon://{name}")(resources.get_digimon_data)

# -----------------
# Register Prompts
# -----------------
mcp.prompt()(prompts.compare_digimon)
mcp.prompt()(prompts.suggest_team)

# ASGI App Export (Handle internally by Horizon)
# -----------------

if __name__ == "__main__":
    # Provides fallback local standard I/O running if invoked directly via `mcp dev`
    mcp.run()
