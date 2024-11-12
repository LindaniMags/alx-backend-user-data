#!/usr/bin/env python3
""" Auth class
"""
from typing import List, TypeVar
from flask import request


class Auth:
    """ Initialize Auth class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Require Auth
        """
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Authorization header
        """
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ Current user
        """
        return None
