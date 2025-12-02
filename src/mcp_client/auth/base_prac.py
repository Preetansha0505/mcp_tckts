class Auth:
    """Base interface for all authentication methods."""

    def get_headers(self) -> dict[str, str]:
        """Return HTTP headers required for authentication."""
        raise NotImplementedError

    
    