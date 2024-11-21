#!/usr/bin/env python3
"""A module for authentication-related routines.
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    returns bytes is a salted hash of the input password.
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
