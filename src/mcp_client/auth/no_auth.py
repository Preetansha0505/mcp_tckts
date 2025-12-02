"""No authentication strategy."""

from typing import Dict, Optional
from .base import Auth


class NoAuth(Auth):
    """
    No-authentication strategy.

    This implementation allows connections without any authentication.
    No tokens or headers are provided.
    """

    def get_token(self) -> Optional[str]:
        """
        Retrieve an authentication token.

        Returns:
            None: No token is provided for unauthenticated connections.
        """
        return None

    def get_headers(self) -> Dict[str, str]:
        """
        Generate authentication headers for HTTP requests.

        Returns:
            Dict[str, str]: Empty dictionary (no auth headers needed).
        """
        return {}
