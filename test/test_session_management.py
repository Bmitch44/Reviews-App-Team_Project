import os
import unittest
from src.data_management.object_mapper import ObjectMapper
from src.user_management.session_management import SessionManager
from src.app_logic.app_logic import Session


class TestSessionManager(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db_path = "test.db"
        cls.object_mapper = ObjectMapper(cls.db_path)
        cls.session_management = SessionManager(cls.db_path)

    def setUp(self):
        self.object_mapper.data_store.clear_tables()
         
    def test_create_session(self):
        user_id = 1
        session = self.session_management.create_session(user_id)
        self.assertIsInstance(session, Session)

    def test_get_session(self):
        user_id = 1
        session = self.session_management.create_session(user_id)
        retrieved_session = self.session_management.get_user_session(user_id)
        self.assertIsNotNone(retrieved_session)
 
    def test_get_user_session(self):
        user_id = 1
        session = self.session_management.create_session(user_id)
        retrieved_session = self.session_management.get_user_session(user_id)
        self.assertEqual(retrieved_session.user_id, user_id)

    def test_update_session(self):
        user_id = 1
        session = self.session_management.create_session(user_id)
        session.is_active = 0
        self.session_management.update_session(session)
        retrieved_session = self.session_management.get_user_session(user_id)
        self.assertEqual(retrieved_session.is_active, 0)

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.db_path)

if __name__ == '__main__':
    unittest.main()
