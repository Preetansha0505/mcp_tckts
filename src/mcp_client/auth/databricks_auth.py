"""Databricks authentication strategy."""

from typing import Dict, Optional
from .base import Auth


class DatabricksAuth(Auth):
    """
    Databricks-specific authentication strategy.

    This implementation handles Databricks workspace authentication
    using bearer tokens.
    """

    def __init__(self, token: str) -> None:
        """
        Initialize Databricks authentication.

        Args:
            token: Databricks authentication token (e.g., PAT or workspace token).

        Raises:
            ValueError: If token is empty or None.
        """
        if not token:
            raise ValueError("Databricks token cannot be empty.")
        self.token = token

    def get_token(self) -> Optional[str]:
        """
        Retrieve the Databricks authentication token.

        Returns:
            str: The Databricks token.
        """
        return self.token

    def get_headers(self) -> Dict[str, str]:
        """
        Generate authentication headers for Databricks requests.

        Returns:
            Dict[str, str]: Dictionary containing Authorization header.
        """
        return {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }
