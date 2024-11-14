#!/usr/bin/env python3
""" Basic auth
"""
from typing import Tuple, TypeVar

from .auth import Auth
from models.user import User


class BasicAuth(Auth):
    """Initialize BasicAuth class
    """

    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:
        """ Extract base64 authorization header
        """
        pass
