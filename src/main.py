import sys
from pathlib import Path

# Add the parent directory of `src` to sys.path to allow `src.*` absolute imports.
# This prevents "attempted relative import with no known parent package" errors.
root_dir = Path(__file__).resolve().parent.parent
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

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
