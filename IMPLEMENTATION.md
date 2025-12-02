# Project Ticket - MCP Client Authentication Refactor

## Ticket Information

**Ticket ID**: TKT-XX  
**Title**: Remove Databricks Auth Dependency & Implement Pluggable Authentication  
**Status**: In Development  
**Priority**: High  

## Description

As a user/developer of the MCP client repo, I want the client to handle determining what authentication to use based on inputs when the client connection is made so that the code is more modular.

## Acceptance Criteria

- [x] Dependency of the MCPClient on Databricks auth removed
- [x] The auth supports no auth as well (make default argument for Auth=None)
- [x] Unit tests added for No Auth, Dbx auth
- [x] Ruff formatted doc strings added
- [ ] Code PR'd and merged

## Implementation Details

### Changes Made

#### 1. **Authentication Architecture**
- Created abstract `Auth` base class in `src/mcp_client/auth/base.py`
- Implemented `NoAuth` strategy (default) in `src/mcp_client/auth/no_auth.py`
- Implemented `DatabricksAuth` strategy in `src/mcp_client/auth/databricks_auth.py`

#### 2. **MCPClient Refactor**
- Updated `MCPClient.__init__()` to accept optional `auth` parameter
- Default authentication is `NoAuth` (no credentials required)
- Removed hard dependency on Databricks-specific libraries
- Added `get_auth_headers()` method to retrieve authentication headers

#### 3. **Test Coverage**
- **NoAuth Tests** (`tests/unit/test_no_auth.py`):
  - Initialization
  - Returns None for token
  - Returns empty headers dict
  - Multiple instances work independently

- **DatabricksAuth Tests** (`tests/unit/test_databricks_auth.py`):
  - Valid token initialization
  - Raises ValueError on empty/None token
  - Returns correct Bearer token
  - Returns proper headers with Authorization and Content-Type

- **MCPClient Tests** (`tests/unit/test_mcp_client.py`):
  - Initialization with NoAuth (default)
  - Initialization with explicit None auth
  - Initialization with DatabricksAuth
  - Correct header generation for each auth type
  - Connect/disconnect lifecycle
  - Tool calling and resource fetching

- **Integration Tests** (`tests/integration/test_mcp_client_integration.py`):
  - NoAuth and DatabricksAuth work independently
  - Auth strategy switching on same endpoint

#### 4. **Documentation**
- Comprehensive docstrings on all classes and methods
- Ruff-compliant formatting with type hints
- Added example usage in docstrings

## File Structure

```
src/mcp_client/
├── __init__.py
├── client.py
└── auth/
    ├── __init__.py
    ├── base.py
    ├── no_auth.py
    └── databricks_auth.py

tests/
├── conftest.py
├── unit/
│   ├── test_no_auth.py
│   ├── test_databricks_auth.py
│   └── test_mcp_client.py
└── integration/
    └── test_mcp_client_integration.py

pyproject.toml              # Project configuration
PROJECT_STRUCTURE.md        # This file
```

## Key Design Decisions

1. **Strategy Pattern**: Used for pluggable authentication to support multiple strategies
2. **Default NoAuth**: Encourages secure defaults while allowing optional authentication
3. **Type Safety**: Full type hints for better IDE support and error detection
4. **Async Ready**: Methods designed for async operations (connection lifecycle)
5. **Extensible**: Easy to add new auth strategies by subclassing `Auth`

## How to Use

### No Authentication
```python
client = MCPClient(endpoint="tcp://localhost:3456")
```

### Databricks Authentication
```python
auth = DatabricksAuth(token="dbx_token_123")
client = MCPClient(endpoint="tcp://localhost:3456", auth=auth)
```

### Custom Authentication
```python
class CustomAuth(Auth):
    def get_token(self) -> Optional[str]:
        return "custom_token"
    
    def get_headers(self) -> Dict[str, str]:
        return {"X-Custom-Auth": "custom_token"}

auth = CustomAuth()
client = MCPClient(endpoint="tcp://localhost:3456", auth=auth)
```

## Testing Commands

```bash
# Run all tests
pytest

# Run unit tests only
pytest tests/unit

# Run with coverage
pytest --cov=src tests/

# Run integration tests
pytest tests/integration

# Format with ruff
ruff format src/ tests/

# Check with ruff
ruff check src/ tests/
```

## Next Steps

1. Run all tests to verify implementation
2. Format code with ruff
3. Create pull request to `dev` branch
4. Code review and merge

## Notes

- No external Databricks SDK required for MCPClient initialization
- Backward compatible with existing code that uses DatabricksAuth
- Flexible enough to support future auth strategies (OAuth, API keys, etc.)
- All code follows Ruff formatting standards
