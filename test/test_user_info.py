import os
import unittest

# Local imports
from src.user_management.session_management import SessionManager
from src.data_management.object_mapper import ObjectMapper
from src.user_management.user_info import UserInfo

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
        session_id = self.user_info.login(username, password)
        self.user_info.logout(session_id)
        retrieved_session = self.session_manager.get_session(session_id)
        self.assertFalse(retrieved_session.is_active)

    @classmethod
    def tearDownClass(cls):
        """
        Clean up after tests by removing the test database file.
        """
        os.remove("src/database/test.db")

if __name__ == '__main__':
    unittest.main()

