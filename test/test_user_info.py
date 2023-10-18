import os
import unittest
from src.app_logic.app_logic import User
from src.user_management.session_management import SessionManager
from src.data_management.object_mapper import ObjectMapper
from src.user_management.user_info import UserInfo

class TestUserInfo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db_path = "test.db"
        cls.object_mapper = ObjectMapper(cls.db_path)
        cls.session_manager = SessionManager(cls.db_path)
        cls.user_info = UserInfo(cls.db_path)

    def setUp(self):
        self.object_mapper.clear_tables()

    def test_register(self):
        username = "test_user"
        email = "test_user@example.com"
        password = "test_password"
        user = self.user_info.register(username, email, password)
        self.assertIsInstance(user, User)

    def test_login_success(self):
        username = "test_user"
        email = "test_user@example.com"
        password = "test_password"
        self.user_info.register(username, email, password)
        session_manager = self.user_info.login(username, password)
        self.assertIsInstance(session_manager, SessionManager)

    def test_login_failure(self):
        username = "test_user"
        email = "test_user@example.com"
        password = "test_password"
        self.user_info.register(username, email, password)
        incorrect_password = "incorrect_password"
        session_manager = self.user_info.login(username, incorrect_password)
        self.assertIsNone(session_manager)

    def test_logout(self):
        username = "test_user"
        email = "test_user@example.com"
        password = "test_password"
        user = self.user_info.register(username, email, password)
        session = self.session_manager.create_session(user.id)
        self.user_info.logout(session.id)
        retrieved_session = self.session_manager.get_session(session.id)
        self.assertTrue(retrieved_session.is_terminated)

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.db_path)

if __name__ == '__main__':
    unittest.main()