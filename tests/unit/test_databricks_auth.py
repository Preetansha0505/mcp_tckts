"""Unit tests for Databricks authentication strategy."""

import pytest
from src.mcp_client.auth.databricks_auth import DatabricksAuth


class TestDatabricksAuth:
    """Test suite for Databricks authentication strategy."""

    def test_databricks_auth_initialization(self) -> None:
        """Test DatabricksAuth can be instantiated with valid token."""
        token = "test_token_123"
        auth = DatabricksAuth(token)
        assert auth is not None

    def test_databricks_auth_raises_on_empty_token(self) -> None:
        """Test DatabricksAuth raises ValueError for empty token."""
        with pytest.raises(ValueError, match="token cannot be empty"):
            DatabricksAuth("")

    def test_databricks_auth_raises_on_none_token(self) -> None:
        """Test DatabricksAuth raises ValueError for None token."""
        with pytest.raises(ValueError, match="token cannot be empty"):
            DatabricksAuth(None)  # type: ignore

    def test_get_token_returns_provided_token(self) -> None:
        """Test that get_token returns the provided token."""
        expected_token = "databricks_token_xyz"
        auth = DatabricksAuth(expected_token)
        token = auth.get_token()
        assert token == expected_token

    def test_get_headers_includes_bearer_token(self) -> None:
        """Test that get_headers includes Bearer token."""
        token = "my_token_123"
        auth = DatabricksAuth(token)
        headers = auth.get_headers()

        assert "Authorization" in headers
        assert headers["Authorization"] == f"Bearer {token}"

    def test_get_headers_includes_content_type(self) -> None:
        """Test that get_headers includes Content-Type header."""
        auth = DatabricksAuth("token_123")
        headers = auth.get_headers()

        assert "Content-Type" in headers
        assert headers["Content-Type"] == "application/json"

    def test_get_headers_format(self) -> None:
        """Test the complete format of returned headers."""
        token = "test_token"
        auth = DatabricksAuth(token)
        headers = auth.get_headers()

        expected_headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }
        assert headers == expected_headers
