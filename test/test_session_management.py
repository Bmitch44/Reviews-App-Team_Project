import os
import unittest
from unittest.mock import patch, Mock
from src.data_management.object_mapper import ObjectMapper
from src.user_management.session_management import SessionManager
from src.app_logic.app_logic import Session


class TestSessionManager(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db_path = "test.db"
        cls.object_mapper = ObjectMapper(cls.db_path)
        cls.session_manager = SessionManager(cls.db_path)

    def setUp(self):
        self.object_mapper.data_store.clear_tables()
         
    def test_create_session(self):
        user_id = 1
        with patch.object(self.session_manager.object_mapper, 'add', return_value=True):
            session = self.session_manager.create_session(user_id)
            self.assertIsInstance(session, Session)

    def test_get_session(self):
        user_id = 1
        with patch.object(self.session_manager.object_mapper, 'add', return_value=True):
            created_session = self.session_manager.create_session(user_id)
        retrieved_session = self.session_manager.get_session(created_session.user_id)
        self.assertIsNotNone(retrieved_session)
 
    def mock_db_get_method(self, obj_class, id=None):
        user_id = 1
        session = Session(user_id=user_id, is_active=1)
        return [session]

    def test_get_user_session(self):
        user_id = 1

        with patch('src.user_management.session_management.ObjectMapper.get', side_effect=self.mock_db_get_method):
            with patch('src.user_management.session_management.SessionManager.update_session', return_value=True):
                retrieved_session = self.session_manager.get_user_session(user_id)

        self.assertIsNotNone(retrieved_session)
        self.assertEqual(retrieved_session.user_id, user_id)

    def test_update_session(self):
        user_id = 1
        mock_session = Mock()
        mock_session.user_id = user_id
        mock_session.is_active = 1
        
        with patch('src.user_management.session_management.SessionManager.create_session', return_value=mock_session):
            with patch.object(self.session_manager.object_mapper, 'add', return_value=True):
                session = self.session_manager.create_session(user_id)
                self.assertEqual(session.user_id, user_id)
                self.assertEqual(session.is_active, 1)
                session.is_active = 0
                with patch('src.user_management.session_management.SessionManager.get_user_session', return_value=mock_session):
                    self.session_manager.update_session(session)
                    retrieved_session = self.session_manager.get_user_session(user_id)
                    self.assertEqual(retrieved_session.is_active, 0)


    @classmethod
    def tearDownClass(cls):
        os.remove("src/database/test.db")

if __name__ == '__main__':
    unittest.main()
