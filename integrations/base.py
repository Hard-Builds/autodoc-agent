from abc import ABC

from langchain_mcp_adapters.client import MultiServerMCPClient


class MCPClientABC(ABC):
    _SERVERS = None
    _NEEDED_TOOLS = None

    _client = None
    _tools = None

    @classmethod
    async def get_client(cls):
        if cls._client is None:
            cls._client = MultiServerMCPClient(cls._SERVERS)
        return cls._client

    @classmethod
    async def get_tools(cls):
        client = await cls.get_client()
        if cls._tools is None:
            tools = await client.get_tools()
            tools = [t for t in tools if t.name in cls._NEEDED_TOOLS]
            cls._tools = tools
        return cls._tools
