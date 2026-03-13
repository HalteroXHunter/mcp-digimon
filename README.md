# Digimon FastMCP Server

A production-ready [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server providing seamless integration with the public [Digi API](https://digi-api.com/).

This server exposes robust tools, resources, and templates to LLMs, enabling them to query detailed statistics, skills, attributes, descriptions, and game data for Digimon directly.

## Features

Built with [FastMCP](https://fastmcp.readthedocs.io/en/latest/), this server provides a modular architecture exposing the following MCP components:

### Tools
- `get_digimon(name_or_id)`: Retrieve detailed data about a specific Digimon, including its type, level, attributes, skills, and English description.
- `search_digimon(query, exact, attribute, level)`: Search the Digimon database with fuzzy matching and filtering (e.g., finding all 'Vaccine' 'Rookie' Digimon).
- `get_skill(name_or_id)`: Fetches descriptions for specific Digimon skills/attacks.

### Resources
- `digimon://{name}`: Provides the raw JSON schema data for immediate context access for any given Digimon.

### Prompts
- `compare_digimon`: Instructs the agent to carefully analyze and compare two Digimon, their skills, attributes, and potential type advantages.
- `suggest_team`: A structured prompt instructing the agent to suggest a cohesive 3-Digimon team based on user-provided constraints (e.g., "Mega" level "Virus" types).

## Architecture

The project is structured modularly for easy extension and maintainability.

```text
src/
├── main.py                 # FastMCP ASGI initialization and registry
├── api/
│   └── digi_client.py      # Async HTTP client wrapper (httpx) for Digi-API
└── mcp_modules/
    ├── tools.py            # Definition of @mcp.tool functions
    ├── resources.py        # Definition of @mcp.resource functions
    └── prompts.py          # Definition of @mcp.prompt template definitions
```

Instead of using decorators which can cause circular imports, plain async Python functions are defined in `mcp_modules` and then explicitly registered via `mcp.add_tool()`, `mcp.add_resource()`, etc. in `src/main.py`.

## Getting Started

### Prerequisites

You must have Python 3.12+ and [`uv`](https://github.com/astral-sh/uv) installed.

### Local Development (stdio)

During development, you can use the MCP CLI to test the server locally using standard I/O transport. FastMCP provides a beautiful local Inspector dashboard.

```bash
# Run locally with Inspector via the CLI
npx @modelcontextprotocol/inspector uv run src/main.py
```

### Running the Python Tests
```bash
uv run pytest test_components.py
```

## Deployment (SSE Integration)

This FastMCP server is pre-configured to export an ASGI application, making it trivial to deploy as a web service using Server-Sent Events (SSE).

### 1. Running Locally (ASGI/SSE)
Run using Uvicorn:
```bash
uv run uvicorn src.main:app --host 0.0.0.0 --port 8000
```

### 2. Docker
A `Dockerfile` is included using `uv` to efficiently package the server for deployment to platforms like Google Cloud Run, Render, or Railway.

Build and run the container:
```bash
docker build -t mcp-digimon .
docker run -p 8000:8000 mcp-digimon
```

### Client Connection
Once deployed over HTTP/HTTPS, agents (e.g., Langchain, Claude Desktop) connect to the server via Server-Sent Events (SSE) by pointing to the hosted endpoint instead of invoking a local shell process.
