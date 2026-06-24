import os

from integrations.base import MCPClientABC


class GithubClient(MCPClientABC):
    _SERVERS = {
        "github": {
            "transport": "streamable_http",
            "url": "https://api.githubcopilot.com/mcp/",
            "headers": {
                "Authorization": os.getenv("GITHUB_MCP_TOKEN")
            }
        }
    }

    _NEEDED_TOOLS = (
        "get_file_contents",
        "create_or_update_file",
        "pull_request_read"
    )
