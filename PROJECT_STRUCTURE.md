# MCP Client - Pluggable Authentication

A Python client for the Model Context Protocol (MCP) with modular, pluggable authentication.

## Overview

This project refactors the MCP Client to support multiple authentication strategies while maintaining backward compatibility. The client no longer depends on Databricks-specific authentication but instead uses an abstract authentication interface that can be extended.

## Features

- **Pluggable Authentication**: Support for multiple auth strategies through a common interface
- **No Auth Support**: Clients can connect without any authentication (default)
- **Databricks Auth**: Databricks-specific token-based authentication
- **Extensible Design**: Easy to add new authentication strategies
- **Fully Typed**: Complete type hints for better IDE support and type checking
- **Well Documented**: Comprehensive docstrings following Ruff standards

## Project Structure

```
src/mcp_client/
├── __init__.py              # Main package exports
├── client.py                # MCPClient implementation
└── auth/
    ├── __init__.py          # Auth module exports
    ├── base.py              # Abstract Auth interface
    ├── no_auth.py           # NoAuth implementation
    └── databricks_auth.py   # Databricks auth implementation

tests/
├── conftest.py              # Pytest configuration
├── unit/
│   ├── test_no_auth.py      # NoAuth unit tests
│   ├── test_databricks_auth.py  # DatabricksAuth unit tests
│   └── test_mcp_client.py   # MCPClient unit tests
└── integration/
    └── test_mcp_client_integration.py  # Integration tests
```

## Installation

```bash
# Clone the repository
git clone <repo-url>
cd mcp_tckts

# Install in development mode with dev dependencies
pip install -e ".[dev]"
```

## Usage

### No Authentication (Default)

```python
from src.mcp_client import MCPClient

# Create client with no authentication
client = MCPClient(endpoint="tcp://127.0.0.1:3456")

# Or explicitly pass None
client = MCPClient(endpoint="tcp://127.0.0.1:3456", auth=None)
```

### Databricks Authentication

```python
from src.mcp_client import MCPClient, DatabricksAuth

# Create Databricks auth
auth = DatabricksAuth(token="your-databricks-token")

# Create client with Databricks auth
client = MCPClient(endpoint="tcp://127.0.0.1:3456", auth=auth)

# Get headers for requests
headers = client.get_auth_headers()
# Output: {'Authorization': 'Bearer your-databricks-token', 'Content-Type': 'application/json'}
```

## Testing

### Run All Tests

```bash
pytest
```

### Run Unit Tests Only

```bash
pytest tests/unit
```

### Run Integration Tests Only

```bash
pytest tests/integration
```

### Run with Coverage

```bash
pytest --cov=src tests/
```

## Code Quality

### Ruff Formatting

```bash
# Check code style
ruff check src/ tests/

# Format code
ruff format src/ tests/
```

### Type Checking

```bash
mypy src/
```

## Authentication Strategies

### Auth Base Class

All authentication strategies inherit from `Auth` and must implement:

- `get_token() -> Optional[str]`: Return authentication token
- `get_headers() -> Dict[str, str]`: Return HTTP headers for requests

### Creating Custom Auth Strategy

```python
from src.mcp_client.auth.base import Auth
from typing import Dict, Optional

class CustomAuth(Auth):
    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_token(self) -> Optional[str]:
        return self.api_key

    def get_headers(self) -> Dict[str, str]:
        return {"X-API-Key": self.api_key}

# Use it with MCPClient
client = MCPClient(endpoint="tcp://127.0.0.1:3456", auth=CustomAuth("key123"))
```

## Acceptance Criteria

✅ **Dependency of MCPClient on Databricks auth removed**
- Databricks auth is now optional and pluggable
- No hard dependency on Databricks-specific libraries

✅ **Auth supports no auth as well (make default argument for Auth=None)**
- Default auth is `NoAuth` (no authentication)
- Can explicitly pass `auth=None`
- Clients can connect without any authentication

✅ **Unit tests added for No Auth, Dbx auth**
- `tests/unit/test_no_auth.py`: Tests for NoAuth strategy
- `tests/unit/test_databricks_auth.py`: Tests for DatabricksAuth strategy
- `tests/unit/test_mcp_client.py`: Tests for MCPClient with both strategies

✅ **Ruff formatted doc strings added**
- All functions and classes have docstrings
- Following Google-style format compatible with Ruff
- All docstrings are type-hinted and descriptive

## Contributing

1. Create a feature branch: `git checkout -b feature/auth-strategy`
2. Make your changes with Ruff formatting: `ruff format .`
3. Add tests for new functionality
4. Submit a pull request to `dev` branch

## License

See LICENSE file for details.
