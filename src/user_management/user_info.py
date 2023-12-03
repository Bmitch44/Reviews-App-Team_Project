import hashlib
import os
from src.app_logic.app_logic import User, Review, Topic
from src.user_management.session_management import SessionManager
from src.data_management.object_mapper import ObjectMapper

class UserInfo:
    def __init__(self, db_path: str):
        """
        Initializes a UserInfo instance.

        Args:
            db_path (str): The path to the database where user information is stored.
        """
        self.db_path = db_path
        self.object_mapper = ObjectMapper(self.db_path)
        self.session_manager = SessionManager(self.db_path)

    def register(self, username, email, password):
        """
        Registers a new user with the provided username, email, and password.

        Args:
            username (str): The username of the user to be registered.
            email (str): The email address of the user to be registered.
            password (str): The password of the user to be registered.

        Returns:
            User: The User object representing the registered user.
        
        Raises:
        ValueError: If the username or email already exists.
        """
        existing_users = self.object_mapper.get(User)
        for user in existing_users:
            if user.username == username:
                raise ValueError("Username is already taken.")
            if user.email == email:
                raise ValueError("A user already exists with this email.")
        #register the user
        hashed_password = self._hash_password(password)
        user = User(username, email, hashed_password)
        result = self.object_mapper.add(user)
        self.session_manager.create_session(user.id, is_active=0)
        return result

    def login(self, username, password):
        """
        Logs in a user with the provided username and password.

        Args:
            username (str): The username of the user trying to log in.
            password (str): The password of the user trying to log in.

        Returns:
            SessionManager: The SessionManager id if login is successful
        
        Raises:
        ValueError: If the user does not exist or the password is incorrect.
        """
        users = self.object_mapper.get(User)
        user_found = None
        for user in users:
            if user.username == username:
                user_found = user
                break

        if not user_found:
            raise ValueError("User does not exist.")

        if self._verify_password(user_found.hashed_password, password):
            return self.session_manager.get_user_session(user_found.id).id
        else:
            raise ValueError("Incorrect password.")

    def logout(self, id):
        """
        Logs out a user by invalidating the session with the given session ID.

        Args:
            id (str): The ID of the session to be invalidated.
        """
        session = self.session_manager.get_session(id)
        if session:
            session.is_active = 0
            self.session_manager.update_session(session)

    def _hash_password(self, password, salt=None):
        """
        Hashes the provided password using a salt.

        Args:
            password (str): The password to be hashed.
            salt (bytes, optional): The salt to be used for hashing (default is None).

        Returns:
            str: The hashed password.
        """
        if salt is None:
            salt = os.urandom(16)
        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        return salt + hashed_password

    def _verify_password(self, stored_password, provided_password):
        """
        Verifies if the provided password matches the stored (hashed) password.

        Args:
            stored_password (str): The stored (hashed) password.
            provided_password (str): The password provided for verification.

        Returns:
            bool: True if the provided password matches the stored password, False otherwise.
        """
        salt = stored_password[:16]
        return stored_password == self._hash_password(provided_password, salt)

    def search_review(self, query):
        """
        Search for reviews based on query.

        Args:
            Query made for a topic or username

        Returns:
            A list of Review objects that match the search criteria.
        """
        if not query:
            raise ValueError("Query cannot be empty.")

        result = []
        all_reviews = self.object_mapper.get(Review)  # This retrieves all reviews.
        all_topics = self.object_mapper.get(Topic)  # This retrieves all topics.
        all_users = self.object_mapper.get(User)  # This retrieves all users

        for review in all_reviews:
            for user in all_users:
                if user.id == review.user_id and query in user.username:
                    result.append(review)
            for topic in all_topics:
                if topic.id == review.topic_id and query in topic.name:
                    result.append(review)
        return result
