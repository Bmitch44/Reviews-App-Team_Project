import os
import unittest
import uuid
import json

# Local imports
from src.user_management.session_management import SessionManager
from src.data_management.object_mapper import ObjectMapper
from src.user_management.user_info import UserInfo
from src.app_logic.app_logic import Review, User 

class TestUserInfo(unittest.TestCase):
    """
    Test cases for user information management functionalities.
    """
    
    @classmethod
    def setUpClass(cls):
        """
        Set up the class for UserInfo tests by initializing paths and mappers.
        """
        cls.db_path = "test.db"
        cls.object_mapper = ObjectMapper(cls.db_path)
        cls.session_manager = SessionManager(cls.db_path)
        cls.user_info = UserInfo(cls.db_path)

    def setUp(self):
        """
        Prepare the database for each test by clearing tables.
        """
        self.object_mapper.data_store.clear_tables()

    def test_register(self):
        """
        Test the user registration process.
        """
        username = "test_user"
        email = "test_user@example.com"
        password = "test_password"
        user = self.user_info.register(username, email, password)
        self.assertTrue(user)

    def test_login(self):
        """
        Test the user login process.
        """
        username = "test_user"
        email = "test_user@example.com"
        password = "test_password"
        result = self.user_info.register(username, email, password)
        self.assertTrue(result)

    def test_logout(self):
        """
        Test the user logout process and validate session deactivation.
        """
        username = "test_user"
        email = "test_user@example.com"
        password = "test_password"
        self.user_info.register(username, email, password)
        id = self.user_info.login(username, password)
        self.user_info.logout(id)
        retrieved_session = self.session_manager.get_session(id)
        self.assertFalse(retrieved_session.is_active)
        
    def test_search_review(self):
        """
        Test the search_review() function from user_info by creating a user and a review,
        and then searching for the review by username.
        """
        # Setup for the test
        # Create a UserInfo instance and any other necessary setup steps
        self.user_info = UserInfo(self.object_mapper)

        # Create a user
        test_user = User(
            username="testuser123", email = "test_user@example.com",
            hashed_password="test_password")  # Add other required attributes
        self.object_mapper.add(test_user)

        # Create a review written by the user
        test_review = Review(
            review_text="This is a test review.",
            user_id=test_user.id,
            topic_id=str(uuid.uuid4()),  # Random UUID for the topic_id
            status="draft",
            review_ratings=json.dumps([]),  # JSON representation of an empty ratings list
            id=str(uuid.uuid4())  # Random UUID for the review ID
        )
        # You will need to implement a method to add a review in your data store or mock database
        self.object_mapper.add(test_review)

        # Test with username as query
        query = test_user.username
        actual_results = self.user_info.search_review(query)

        # Check if the actual results contain the expected review
        self.assertTrue(any(review.id == test_review.id for review in actual_results))

    @classmethod
    def tearDownClass(cls):
        """
        Clean up after tests by removing the test database file.
        """
        os.remove("src/database/test.db")

if __name__ == '__main__':
    unittest.main()

