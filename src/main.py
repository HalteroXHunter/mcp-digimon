from mcp.server.fastmcp import FastMCP
from src.mcp_modules import tools, resources, prompts

# Initialize the global FastMCP server attached to the module
mcp = FastMCP("Digimon Server")

# -----------------
# Register Tools
# -----------------
# FastMCP uses the docstrings and type hints of these functions
# to auto-generate the JSON Schema arguments for the client.
mcp.add_tool(tools.get_digimon)
mcp.add_tool(tools.search_digimon)
mcp.add_tool(tools.get_skill)

# -----------------
# Register Resources
# -----------------
mcp.add_resource(resources.get_digimon_data, "digimon://{name}")

# -----------------
# Register Prompts
# -----------------
mcp.add_prompt(prompts.compare_digimon)
mcp.add_prompt(prompts.suggest_team)

# -----------------
# ASGI App Export
# -----------------
# Extract the ASGI app for use with SSE via a deployment server (e.g. uvicorn)
app = mcp.get_asgi_app()

if __name__ == "__main__":
    # Provides fallback local standard I/O running if invoked directly via `mcp dev`
    mcp.run()
