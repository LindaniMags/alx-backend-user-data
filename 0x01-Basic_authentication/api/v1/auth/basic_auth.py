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

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """ Decode base64 authorization header
        """
        pass

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """ Extract user credentials
        """
        pass

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str) -> TypeVar('User'):
        """ User object from credentials
        """
        pass

    def current_user(self, request=None) -> TypeVar('User'):
        """ Current user
        """
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Require auth
        """
        pass

    def authorization_header(self, request=None) -> str:
        """ Authorization header
        """
        pass
