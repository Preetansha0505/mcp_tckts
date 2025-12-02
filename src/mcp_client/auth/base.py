"""Base authentication strategy interface."""

from abc import ABC, abstractmethod
from typing import Optional, Dict


class Auth(ABC):
    """
    Abstract base class for authentication strategies.

    This class defines the interface for all authentication implementations,
    enabling pluggable authentication in the MCP Client.
    """

    @abstractmethod
    def get_token(self) -> Optional[str]:
        """
        Retrieve an authentication token.

        Returns:
            Optional[str]: Authentication token string, or None if no token.

        Raises:
            AuthenticationError: If token retrieval fails.
        """
        pass

    @abstractmethod
    def get_headers(self) -> Dict[str, str]:
        """
        Generate authentication headers for HTTP requests.

        Returns:
            Dict[str, str]: Dictionary of headers to include in requests.
        """
        pass
