from fastmcp import FastMCP
from database.db import init_db
import mcp_app.tools_voiture as tools_voitures
import asyncio

# Create the MCP server with a name
mcp_server = FastMCP("Automobiles MCP Server")

# Register all car tools
tools_voitures.register_tools(mcp_server)


async def main():
    # Connect to MongoDB first
    await init_db()
    print("✅ MongoDB connected")

    # Start the MCP server
    # It runs on port 8002, separate from the FastAPI server (port 8000)
    await mcp_server.run_async(
        transport="streamable-http",
        host="127.0.0.1",
        port=8002,
        path="/mcp",
    )


if __name__ == "__main__":
    asyncio.run(main())