# MCP Server Health Check Endpoint Documentation

## Overview

The MCP Server now includes a built-in `health_check()` tool that allows developers to verify server status and availability. This endpoint is essential for monitoring, load balancing, and automated health verification in production environments.

## Purpose

The health check endpoint provides:
- **Server Status**: Confirms the server is online and operational
- **Timestamps**: Returns ISO 8601 formatted UTC timestamp for monitoring
- **Service Metadata**: Includes service name and version information
- **Zero Dependencies**: No external calls required, minimal latency

## How to Use the Health Check Endpoint

### 1. Starting the Server

```bash
python src/servers/mcp_server/app.py
```

The server will start on `http://127.0.0.1:8000` with SSE transport enabled.

### 2. Checking Server Health via Python Client

```python
from mcp import Client

# Initialize client
client = Client("http://127.0.0.1:8000/sse")

# Call the health check tool
result = client.call_tool("health_check")

print(result)
# Output:
# {
#     "status": "healthy",
#     "timestamp": "2025-11-11T14:23:45.123456",
#     "service": "MCP Server",
#     "version": "1.0.0"
# }
```

### 3. Response Format

The health check returns a JSON object with the following fields:

| Field | Type | Description |
|-------|------|-------------|
| `status` | string | Server health status ("healthy" or "unhealthy") |
| `timestamp` | string | ISO 8601 formatted UTC timestamp |
| `service` | string | Service name identifier |
| `version` | string | Server version number |

## Use Cases

1. **Monitoring**: Periodic health checks in monitoring systems (Prometheus, DataDog)
2. **Load Balancing**: Health checks before routing requests
3. **Service Discovery**: Automatic detection of online MCP servers
4. **Orchestration**: Container and Kubernetes health probes
5. **Alerting**: Automated alerts when server becomes unavailable

## Implementation Details

The health check tool is implemented as a simple FastMCP tool that requires no parameters and completes in milliseconds. It follows the same conventions as other tools in the MCP server.

- **Location**: `app.py`, lines 19-30
- **Tool Name**: `health_check`
- **Parameters**: None
- **Return Type**: Dictionary with status information

## Error Handling

If the server is offline or unreachable, the client will receive a connection error. Implement retry logic for production scenarios:

```python
import time
from mcp import Client

def check_server_health(max_retries=3):
    client = Client("http://127.0.0.1:8000/sse")
    
    for attempt in range(max_retries):
        try:
            result = client.call_tool("health_check")
            return result["status"] == "healthy"
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                time.sleep(2)  # Wait before retry
    
    return False
```

## Integration with Monitoring Systems

The health check endpoint can be integrated into monitoring systems by periodically calling `health_check()` and alerting if the response indicates an unhealthy status or connection timeout.
