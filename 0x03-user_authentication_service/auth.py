#!/usr/bin/env python3
"""
Register user
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """
    returns bytes is a salted hash of the input password.
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


class Auth:
    """
    Auth class to interact with the authentication database.
    """

    def __init__(self):
        """
        Initialize a new Auth instance.
        """

        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register user
        """

        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            pass

        hashed_password = _hash_password(password)

        user = self._db.add_user(email, hashed_password)
        return user
