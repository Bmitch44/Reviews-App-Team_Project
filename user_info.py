import hashlib
import os
from src.app_logic.logic import User
from src.user_management.session_management import SessionManager
from src.data_management.object_mapper import ObjectMapper

class UserInfo:
    def __init__(self, db_path: str):
        """
        Initializes a UserInfo instance.

        Args:
            db_path (str): The path to the database where user information is stored.
        """
        pass

    def register(self, username, email, password):
        """
        Registers a new user with the provided username, email, and password.

        Args:
            username (str): The username of the user to be registered.
            email (str): The email address of the user to be registered.
            password (str): The password of the user to be registered.

        Returns:
            User: The User object representing the registered user.
        """
        pass

    def login(self, username, password):
        """
        Logs in a user with the provided username and password.

        Args:
            username (str): The username of the user trying to log in.
            password (str): The password of the user trying to log in.

        Returns:
            SessionManager: The SessionManager object if login is successful, None otherwise.
        """
        
        pass

    def logout(self, session_id):
        """
        Logs out a user by invalidating the session with the given session ID.

        Args:
            session_id (str): The ID of the session to be invalidated.
        """
        pass

    def _hash_password(self, password, salt=None):
        """
        Hashes the provided password using a salt.

        Args:
            password (str): The password to be hashed.
            salt (bytes, optional): The salt to be used for hashing (default is None).

        Returns:
            str: The hashed password.
        """
        pass

    def _verify_password(self, stored_password, provided_password):
        """
        Verifies if the provided password matches the stored (hashed) password.

        Args:
            stored_password (str): The stored (hashed) password.
            provided_password (str): The password provided for verification.

        Returns:
            bool: True if the provided password matches the stored password, False otherwise.
        """
        pass
