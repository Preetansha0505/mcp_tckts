"""Unit tests for NoAuth strategy."""

import pytest
from src.mcp_client.auth.no_auth import NoAuth


class TestNoAuth:
    """Test suite for NoAuth authentication strategy."""

    def test_no_auth_initialization(self) -> None:
        """Test NoAuth can be instantiated."""
        auth = NoAuth()
        assert auth is not None

    def test_get_token_returns_none(self) -> None:
        """Test that get_token returns None for NoAuth."""
        auth = NoAuth()
        token = auth.get_token()
        assert token is None

    def test_get_headers_returns_empty_dict(self) -> None:
        """Test that get_headers returns empty dictionary for NoAuth."""
        auth = NoAuth()
        headers = auth.get_headers()
        assert headers == {}
        assert isinstance(headers, dict)

    def test_multiple_instances_are_independent(self) -> None:
        """Test that multiple NoAuth instances work independently."""
        auth1 = NoAuth()
        auth2 = NoAuth()

        assert auth1.get_token() == auth2.get_token()
        assert auth1.get_headers() == auth2.get_headers()
