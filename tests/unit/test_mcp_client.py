"""Unit tests for MCPClient."""

import pytest
import pytest_asyncio
from src.mcp_client.client import MCPClient
from src.mcp_client.auth.no_auth import NoAuth
from src.mcp_client.auth.databricks_auth import DatabricksAuth


class TestMCPClientInitialization:
    """Test suite for MCPClient initialization."""

    def test_mcp_client_initialization_with_no_auth(self) -> None:
        """Test MCPClient initialization without authentication."""
        client = MCPClient()
        assert client is not None
        assert isinstance(client.auth, NoAuth)

    def test_mcp_client_initialization_with_none_auth(self) -> None:
        """Test MCPClient initialization with explicit None auth."""
        client = MCPClient(auth=None)
        assert isinstance(client.auth, NoAuth)

    def test_mcp_client_initialization_with_databricks_auth(self) -> None:
        """Test MCPClient initialization with Databricks auth."""
        token = "test_token"
        auth = DatabricksAuth(token)
        client = MCPClient(auth=auth)
        assert client.auth == auth

    def test_mcp_client_initialization_with_endpoint(self) -> None:
        """Test MCPClient initialization with endpoint."""
        endpoint = "tcp://127.0.0.1:3456"
        client = MCPClient(endpoint=endpoint)
        assert client.endpoint == endpoint

    def test_mcp_client_initialization_with_endpoint_and_auth(self) -> None:
        """Test MCPClient initialization with both endpoint and auth."""
        endpoint = "tcp://127.0.0.1:3456"
        auth = DatabricksAuth("token_123")
        client = MCPClient(endpoint=endpoint, auth=auth)
        assert client.endpoint == endpoint
        assert client.auth == auth


class TestMCPClientAuthHeaders:
    """Test suite for MCPClient authentication headers."""

    def test_get_auth_headers_with_no_auth(self) -> None:
        """Test that get_auth_headers returns empty dict for NoAuth."""
        client = MCPClient()
        headers = client.get_auth_headers()
        assert headers == {}

    def test_get_auth_headers_with_databricks_auth(self) -> None:
        """Test that get_auth_headers returns Bearer token for DatabricksAuth."""
        token = "dbx_token_123"
        auth = DatabricksAuth(token)
        client = MCPClient(auth=auth)
        headers = client.get_auth_headers()

        assert "Authorization" in headers
        assert headers["Authorization"] == f"Bearer {token}"
        assert "Content-Type" in headers


class TestMCPClientConnectDisconnect:
    """Test suite for MCPClient connect/disconnect methods."""

    @pytest.mark.asyncio
    async def test_connect_without_endpoint_raises_error(self) -> None:
        """Test that connect raises error when endpoint is not set."""
        client = MCPClient()
        with pytest.raises(ValueError, match="Endpoint must be set"):
            await client.connect()

    @pytest.mark.asyncio
    async def test_connect_with_endpoint_and_no_auth(self) -> None:
        """Test that connect succeeds with endpoint and NoAuth."""
        client = MCPClient(endpoint="tcp://127.0.0.1:3456")
        # Should not raise an error
        await client.connect()

    @pytest.mark.asyncio
    async def test_connect_with_endpoint_and_databricks_auth(self) -> None:
        """Test that connect succeeds with endpoint and DatabricksAuth."""
        auth = DatabricksAuth("token_123")
        client = MCPClient(endpoint="tcp://127.0.0.1:3456", auth=auth)
        # Should not raise an error
        await client.connect()

    @pytest.mark.asyncio
    async def test_disconnect_succeeds(self) -> None:
        """Test that disconnect completes without error."""
        client = MCPClient()
        # Should not raise an error
        await client.disconnect()


class TestMCPClientToolCalling:
    """Test suite for MCPClient tool calling."""

    @pytest.mark.asyncio
    async def test_call_tool_without_endpoint_raises_error(self) -> None:
        """Test that call_tool raises error when not connected."""
        client = MCPClient()
        with pytest.raises(ConnectionError, match="Not connected"):
            await client.call_tool("test_tool")

    @pytest.mark.asyncio
    async def test_call_tool_with_endpoint(self) -> None:
        """Test that call_tool succeeds with endpoint."""
        client = MCPClient(endpoint="tcp://127.0.0.1:3456")
        # Should not raise an error
        await client.call_tool("test_tool", param1="value1")


class TestMCPClientResourceFetching:
    """Test suite for MCPClient resource fetching."""

    @pytest.mark.asyncio
    async def test_get_resource_without_endpoint_raises_error(self) -> None:
        """Test that get_resource raises error when not connected."""
        client = MCPClient()
        with pytest.raises(ConnectionError, match="Not connected"):
            await client.get_resource("resource://test")

    @pytest.mark.asyncio
    async def test_get_resource_with_endpoint(self) -> None:
        """Test that get_resource succeeds with endpoint."""
        client = MCPClient(endpoint="tcp://127.0.0.1:3456")
        # Should not raise an error
        await client.get_resource("resource://test")
