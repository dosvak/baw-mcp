"""Minimal Python client (pip install mcp): lists the tools and runs one search."""
import asyncio
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

async def main():
    async with streamablehttp_client("https://bawmcp.dosvak.com/mcp") as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()
            print([t.name for t in (await session.list_tools()).tools])
            result = await session.call_tool("search_knowledge", {"query": "how do timers behave on CP4BA"})
            print(result.content[0].text)

asyncio.run(main())
