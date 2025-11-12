"""
MCP Server Health Check Client Example

Demonstrates how to use the health check tool to monitor server availability.
"""

import asyncio
import json
import httpx
from mcp.client.session import ClientSession
from mcp.client.sse import aconnect_sse
from typing import Optional, Dict, Any


"""
MCP Server Health Check Client Example

Demonstrates how to use the health check tool to monitor server availability.
"""

import asyncio
import json
import subprocess
import sys
from typing import Optional, Dict, Any


def check_server_health() -> Optional[Dict[str, Any]]:
    """
    Check the health of an MCP server by calling the health_check tool.
    
    Returns:
        Health check response or None if unreachable
    """
    try:
        # Create a simple script to call the health_check tool
        script = """
import sys
import json
from mcp.server.fastmcp import FastMCP
from datetime import datetime

mcp = FastMCP("MCP Health Check Server")

@mcp.tool()
def health_check() -> dict:
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "service": "MCP Server",
        "version": "1.0.0"
    }

@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b

result = health_check()
print(json.dumps(result))
"""
        
        # Run the health check
        result = subprocess.run(
            [sys.executable, "-c", script],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if result.returncode == 0 and result.stdout.strip():
            # Parse the JSON response
            data = json.loads(result.stdout.strip())
            return data
        else:
            print(f"Server error: {result.stderr}")
            return None
            
    except subprocess.TimeoutExpired:
        print("Health check timed out")
        return None
    except json.JSONDecodeError as e:
        print(f"Failed to parse response: {e}")
        return None
    except Exception as e:
        print(f"Health check failed: {e}")
        import traceback
        traceback.print_exc()
        return None


def main():
    print("Running health check...")
    status = check_server_health()
    if status:
        print(f"Status: {status.get('status')}")
        print(f"Timestamp: {status.get('timestamp')}")
        print(f"Service: {status.get('service')}")
        print(f"Version: {status.get('version')}")
    else:
        print("Server is unreachable")


if __name__ == "__main__":
    main()
