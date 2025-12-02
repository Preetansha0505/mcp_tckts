"""MCP Client with pluggable authentication."""

from .client import MCPClient
from .auth.base import Auth

__version__ = "0.1.0"
__all__ = ["MCPClient", "Auth"]
