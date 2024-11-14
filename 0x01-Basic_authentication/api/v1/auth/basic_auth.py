#!/usr/bin/env python3
""" Basic auth
"""
import re
import base64
import binascii
from typing import Tuple, TypeVar

from .auth import Auth
from models.user import User


class BasicAuth(Auth):
    """Initialize BasicAuth class
    """

    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:
        """Extracts the Base64 part of the Authorization header
        """
        if isinstance(authorization_header, str):
            pattern = r'Basic (?P<token>.+)'
            match = re.fullmatch(pattern, authorization_header.strip())
            if match is not None:
                return match.group('token')
        return None

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str,
    ) -> str:
        """Decodes the Base64 part of the Authorization header
        into a string
        """
        if isinstance(base64_authorization_header, str):
            try:
                is_b64 = base64.b64decode(
                    base64_authorization_header,
                    validate=True,
                )
                return is_b64.decode('utf-8')
            except (binascii.Error, UnicodeDecodeError):
                return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """Extracts the user credentials from the Base64 decoded value"""
        if isinstance(decoded_base64_authorization_header, str):
            pattern = r'(?P<user>\w+)\:(?P<pwd>\w+)'
            match = re.fullmatch(pattern, decoded_base64_authorization_header)
            if match is not None:
                return match.group('user'), match.group('pwd')
        return None, None
