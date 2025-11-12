"""
MCP Server with Health Check Endpoint

This module provides an MCP server with a built-in health check tool
to verify server availability and status.
"""

from mcp.server.fastmcp import FastMCP
from datetime import datetime
import logging

# Setup logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Create an MCP server
mcp = FastMCP("MCP Health Check Server")


@mcp.tool()
def health_check() -> dict:
    """
    Health check tool to verify server is online and operational.
    
    Returns:
        dict: Server status information including timestamp
    """
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "service": "MCP Server",
        "version": "1.0.0"
    }


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together"""
    return a + b


if __name__ == "__main__":
    print("Starting MCP server...", flush=True)
    
    try:
        mcp.run()
    except Exception as exc:
        logger.error(f"Server error: {exc}")
        raise
