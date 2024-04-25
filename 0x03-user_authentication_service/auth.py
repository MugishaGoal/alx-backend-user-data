#!/usr/bin/env python3
"""Auth module"""


import bcrypt
from sqlalchemy.orm.exc import NoResultFound

from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """A method that takes in a password string arguments and returns bytes"""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user"""
        try:
            # Check if user already exists with the provided email
            self._db.find_user_by(email=email)
            # If user exists, raise ValueError
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            # If user does not exist, hash the password
            hashed_password = _hash_password(password)
            # Create a new user object
            user = User(email=email, hashed_password=hashed_password)
            # Add the user to the database
            self._db.add_user(email=email, hashed_password=hashed_password)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """Validates login credentials"""
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(
                    password.encode('utf-8'),
                    user.hashed_password)
        except NoResultFound:
            return False
