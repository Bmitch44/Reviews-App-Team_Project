import os
from unittest import TestCase
from src.data_management.data_store import DataStore

class TestDataStore(TestCase):

    @classmethod
    def setUpClass(cls):
        # Create a new test database for this test suite
        cls.data_store = DataStore("test.db")

    def setUp(self):
        # Before each test, clear all tables to ensure there's no leftover data
        self.data_store.clear_tables()

    def test_save_success(self):
        user_data = {
            "id": "1",
            "username": "test_user_1",
            "hashed_password": "test_password_1",
            "email": "test_email_1@example.com",
        }
        self.assertTrue(self.data_store.save(user_data, "user"))

    def test_save_failure(self):
        user_data = {
            "id": "1",
            "username": "test_user_1",
            "hashed_password": "test_password_1",
            "email": "test_email_1@example.com",
        }
        self.assertTrue(self.data_store.save(user_data, "user"))
        user_data["invalid_column"] = "invalid_value"
        self.assertTrue(self.data_store.save(user_data, "user"))

    def test_load_success(self):
        user_data = {
            "id": "1",
            "username": "test_user_1",
            "hashed_password": "test_password_1",
            "email": "test_email_1@example.com",
        }
        self.assertTrue(self.data_store.save(user_data, "user"))
        loaded_users = self.data_store.load("user")
        self.assertIn(user_data, loaded_users)

    def test_load_failure(self):
        user_data = {
            "id": "1",
            "username": "test_user_1",
            "hashed_password": "test_password_1",
            "email": "test_email_1@example.com",
        }
        self.assertTrue(self.data_store.save(user_data, "user"))
        loaded_users = self.data_store.load("invalid_table")
        self.assertEqual(loaded_users, None)

    def test_clear_tables(self):
        user_data = {
            "id": "1",
            "username": "test_user_1",
            "hashed_password": "test_password_1",
            "email": "test_email_1@example.com",
        }
        self.assertTrue(self.data_store.save(user_data, "user"))
        self.data_store.clear_tables()
        loaded_users = self.data_store.load("user")
        self.assertEqual(loaded_users, None)

    def test_delete_success(self):
        user_data = {
            "id": "1",
            "username": "test_user_1",
            "hashed_password": "test_password_1",
            "email": "test_email_1@example.com",
        }
        self.assertTrue(self.data_store.save(user_data, "user"))
        self.assertTrue(self.data_store.delete(1, "user"))
    
    def test_delete_failure(self):
        self.assertFalse(self.data_store.delete(1, "user"))

    @classmethod
    def tearDownClass(cls):
        os.remove("src/database/test.db")
