import asyncio
import os

from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

async def main():
    # You can configure the client to talk to your local MCP server or the deployed one.
    client = MultiServerMCPClient(
        {
            "digimon_local": {
                "command": "uv",
                "args": ["run", "-m", "src.main"],
                "transport": "stdio",
            },
            # "digimon_remote": {
            #     # Replace with your actual deployed FastMCP Horizon App URL (append /sse)
            #     "url": "https://mcp-digimon-testian.fastmcp.app/sse",
            #     "transport": "sse",
            # },
        }
    )
    tools = await client.get_tools()

    # Use a supported model for the agent. GPT-4o-mini is a common choice.
    # Note: Ensure you have OPENAI_API_KEY in your .env file
    agent = create_agent(
        model="gpt-4o-mini",
        tools=tools,
        system_prompt="You are a helpful assistant who uses tools to answer questions about Digimon.",
    )
    
    response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "Tell me about the digimon Agumon and suggest a good team for him."}]}
    )
    
    print(response["messages"][-1].content)

if __name__ == "__main__":
    asyncio.run(main())
