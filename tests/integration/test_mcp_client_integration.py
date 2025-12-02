"""Integration tests for MCP Client."""

import pytest
from src.mcp_client.client import MCPClient
from src.mcp_client.auth.no_auth import NoAuth
from src.mcp_client.auth.databricks_auth import DatabricksAuth


class TestMCPClientIntegration:
    """Integration test suite for MCPClient with different auth strategies."""

    def test_client_with_no_auth_and_databricks_auth_independently(
        self,
    ) -> None:
        """Test that NoAuth and DatabricksAuth work independently."""
        client_no_auth = MCPClient(
            endpoint="tcp://127.0.0.1:3456",
            auth=NoAuth(),
        )
        client_dbx = MCPClient(
            endpoint="tcp://127.0.0.1:3456",
            auth=DatabricksAuth("token_123"),
        )

        # Verify they have different auth headers
        assert client_no_auth.get_auth_headers() == {}
        assert "Authorization" in client_dbx.get_auth_headers()

    def test_switching_auth_strategy_on_same_endpoint(self) -> None:
        """Test creating clients with same endpoint but different auth."""
        endpoint = "tcp://127.0.0.1:3456"

        client1 = MCPClient(endpoint=endpoint, auth=NoAuth())
        client2 = MCPClient(endpoint=endpoint, auth=DatabricksAuth("token"))

        # Both should share endpoint
        assert client1.endpoint == client2.endpoint
        # But have different auth
        assert client1.get_auth_headers() != client2.get_auth_headers()
