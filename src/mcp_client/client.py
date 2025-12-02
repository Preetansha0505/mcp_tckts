"""MCP Client with pluggable authentication."""

from typing import Optional, Dict, Any
# from .auth.base import Auth
# from .auth.no_auth import NoAuth

from .auth.base_prac import Auth
from .auth.basic_auth import BasicAuth

class MCPClient:
    """
    MCP (Model Context Protocol) Client with pluggable authentication.

    This client supports multiple authentication strategies and can operate
    without authentication. The authentication method is determined at
    connection time and is decoupled from the client implementation.

    Attributes:
        auth: Authentication strategy instance (defaults to NoAuth).
        endpoint: Server endpoint URL.
    """

    def __init__(
        self,
        endpoint: Optional[str] = None,
        auth: Optional[Auth] = None,
    ) -> None:
        """
        Initialize the MCP Client.

        Args:
            endpoint: MCP server endpoint URL (optional).
            auth: Authentication strategy (defaults to NoAuth if None).

        Example:
            >>> client = MCPClient(auth=None)  # No authentication
            >>> client = MCPClient(auth=DatabricksAuth("token123"))
        """
        self.endpoint = endpoint
        # self.auth = auth if auth is not None else NoAuth()
        self.auth = auth
        

    async def connect(self) -> None:
        """
        Establish connection to the MCP server.

        Uses the configured authentication method to prepare headers.
        Future implementations will extend this with actual transport logic.
        """
        if not self.endpoint:
            raise ValueError("Endpoint must be set before connecting.")

        # 1️⃣ Step: authentication header construction
        headers = {}
        if self.auth:
            headers.update(self.auth.get_headers())

        # 2️⃣ Step: Placeholder for future transport logic
        # Example:
        # if self.endpoint.startswith("http://") or self.endpoint.startswith("https://"):
        #     self.connection = await self._connect_http(self.endpoint, headers)
        # elif self.endpoint.startswith("sse://"):
        #     self.connection = await self._connect_sse(self.endpoint, headers)
        # elif self.endpoint.startswith("tcp://"):
        #     self.connection = await self._connect_tcp(self.endpoint)
        # else:
        #     raise ValueError(f"Unsupported endpoint: {self.endpoint}")

        # 3️⃣ For now: just store headers for testing
        self._debug_headers = headers
        return
    
    

    async def disconnect(self) -> None:
        """
        Close the connection to the MCP server.

        This method safely closes the active connection and cleans up resources.
        """
        # Cleanup logic would go here
        pass

    def get_auth_headers(self) -> Dict[str, str]:
        """
        Get authentication headers for requests.

        Returns:
            Dict[str, str]: Headers dict with authentication information.

        Example:
            >>> headers = client.get_auth_headers()
            >>> # headers will be empty for NoAuth, or include Bearer token for DatabricksAuth
        """
        return self.auth.get_headers()

    async def call_tool(self, tool_name: str, **kwargs: Any) -> Any:
        """
        Call a tool on the remote MCP server.

        Args:
            tool_name: Name of the tool to invoke.
            **kwargs: Tool-specific arguments.

        Returns:
            The result from the tool execution.

        Raises:
            ConnectionError: If not connected to the server.
            ValueError: If tool_name is invalid.
        """
        if not self.endpoint:
            raise ConnectionError("Not connected to MCP server.")

        headers = self.get_auth_headers()
        # Tool invocation logic would go here
        pass

    async def get_resource(self, resource_uri: str) -> Any:
        """
        Fetch a resource from the remote MCP server.

        Args:
            resource_uri: URI of the resource to fetch.

        Returns:
            The resource data.

        Raises:
            ConnectionError: If not connected to the server.
            ValueError: If resource_uri is invalid.
        """
        if not self.endpoint:
            raise ConnectionError("Not connected to MCP server.")

        headers = self.get_auth_headers()
        # Resource fetch logic would go here
        pass
