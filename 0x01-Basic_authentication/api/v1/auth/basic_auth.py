#!/usr/bin/env python3
""" Basic auth
"""
import base64
from typing import Tuple, TypeVar

from .auth import Auth
from models.user import User


class BasicAuth(Auth):
    """Initialize BasicAuth class
    """


def extract_base64_authorization_header(self,
                                        authorization_header: str) -> str:
    """
    Extracts the Base64 part of the Authorization
    header for Basic Authentication
    """
    if authorization_header is None:
        return None
    if not authorization_header.startswith("Basic "):
        return None
    return authorization_header.split(" ")[1]


def decode_base64_authorization_header(
        self, base64_authorization_header: str) -> str:
    """Decodes a Base64 string to a string
    """
    if isinstance(base64_authorization_header, str):
        if base64_authorization_header is None:
            return None
        try:
            return base64.b64decode(base64_authorization_header).decode("utf-8")
        except Exception:
            return None


def extract_user_credentials(
        self, decoded_base64_authorization_header: str) -> Tuple(str, str):
    """Extracts the user email and password from the Base64 decoded value
    """
    if decoded_base64_authorization_header is None:
        return (None, None)
    if ":" not in decoded_base64_authorization_header:
        return (None, None)
    return (decoded_base64_authorization_header.split(":", 1))


def user_object_from_credentials(
        self,
        user_email: str,
        user_pwd: str) -> TypeVar('User'):
    """Retrieves the User instance based on email and password.
    """
    if isinstance(user_email, str) and isinstance(user_pwd, str):
        try:
            users = User.search({'email': user_email})
        except Exception:
            return None
        if len(users) <= 0:
            return None
        if users[0].is_valid_password(user_pwd):
            return users[0]
    return None


def current_user(self, request=None) -> TypeVar('User'):
    """Retrieves the user from a request.
    """
    auth_header = self.authorization_header(request)
    b64_auth_token = self.extract_base64_authorization_header(auth_header)
    auth_token = self.decode_base64_authorization_header(b64_auth_token)
    email, password = self.extract_user_credentials(auth_token)
    return self.user_object_from_credentials(email, password)
