import os
from unittest import TestCase
from src.data_management.object_mapper import ObjectMapper

# to be implemented when logic is implemented:
# from src.app_logic.logic import User, Review, Topic

class TestUserMapper(TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Create a new test database for this test suite
        cls.object_mapper = ObjectMapper("test.db")

    def setUp(self):
        # Before each test, clear all tables to ensure there's no leftover data
        self.object_mapper.data_store.clear_tables()

    def test_add_success(self):
        # to be implemented when logic is implemented:
        # user = User("testuser", "testpassword", "testemail")
        # self.assertTrue(self.object_mapper.add(user))
        pass

    def test_add_failure(self):
        # to be implemented when logic is implemented:
        # user = "testuser"
        # self.assertRaises(ValueError, self.object_mapper.add, user)
        pass

    def test_get_success(self):
        # to be implemented when logic is implemented:
        # user = User("testuser", "testpassword", "testemail")
        # self.object_mapper.add(user)
        # self.assertEqual(self.object_mapper.get(user, id=1), user)
        pass

    def test_get_failure(self):
        # to be implemented when logic is implemented:
        # user = User("testuser", "testpassword", "testemail")
        # self.object_mapper.add(user)
        # self.assertRaises(ValueError, self.object_mapper.get, user, id=2)
        pass

    def test_remove_success(self):
        # to be implemented when logic is implemented:
        # user = User("testuser", "testpassword", "testemail")
        # self.object_mapper.add(user)
        # self.assertTrue(self.object_mapper.remove(user))
        pass

    def test_remove_failure(self):
        # to be implemented when logic is implemented:
        # user = User("testuser", "testpassword", "testemail")
        # self.object_mapper.add(user)
        # self.object_mapper.remove(user)
        # self.assertRaises(ValueError, self.object_mapper.remove, user)
        pass

    @classmethod
    def tearDownClass(cls):
        # After all tests, delete the test database
        os.remove("src/database/test.db")