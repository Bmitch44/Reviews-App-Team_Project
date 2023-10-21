import os
from unittest import TestCase
from src.app_logic.app_logic import User
from src.app_logic.app_logic import Topic
from src.app_logic.app_logic import Review
from src.app_logic.app_logic import Session

class TestAppLogic(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.user = User('Martha','email@gmail.com','password',1)
        cls.topic = Topic('Stocks','They are going up',1,1)
        cls.review = Review('this is a test',1,1,"draft",1)
        cls.session = Session(1,)

    def test_user(self):
        user_data = {
            "id": 1,
            "username": 'Martha',
            "hashed_password": 'password',
            "email": 'email@gmail.com',
        }

        self.assertEqual(self.user.data, user_data)

    def test_topic(self):
        topic_data = {
            "id" : 1,
            "name" : 'Stocks',
            "description" : 'They are going up',
            "user_id" : 1
        }

        self.assertEqual(self.topic.data, topic_data)

    def test_review(self):
        review_data = {
            "id" : 1,
            "review_text" : 'this is a test',
            "user_id" : 1,
            "topic_id" : 1,
            "status" : "draft"
        }

        self.assertEqual(self.review.data, review_data)

    def test_session(self):
        review_data = {
            "id" : 1,
            "user_id" : self.user_id,
            "created_at" : self.created_at,
            "expires_at" : self.expires_at,
            "last_activity_at" : self.last_activity_at,
            "is_active" : self.is_active,
        }

        self.assertEqual(self.session.data, review_data)