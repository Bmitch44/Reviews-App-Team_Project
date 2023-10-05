from unittest import TestCase
from src.object_mapper import UserMapper, ReviewMapper, TopicMapper


class TestUserMapper(TestCase):
    def test_to_database(self):
        # Arrange
        mapper = UserMapper()
        user = None

        # Act
        result = mapper.to_database(user)

        # Assert
        self.assertRaises(NotImplementedError)

    def test_from_database(self):
        # Arrange
        mapper = UserMapper()
        data = None

        # Act
        result = mapper.from_database(data)

        # Assert
        self.assertRaises(NotImplementedError)


class TestReviewMapper(TestCase):
    def test_to_database(self):
        # Arrange
        mapper = ReviewMapper()
        review = None

        # Act
        result = mapper.to_database(review)

        # Assert
        self.assertRaises(NotImplementedError)

    def test_from_database(self):
        # Arrange
        mapper = ReviewMapper()
        data = None

        # Act
        result = mapper.from_database(data)

        # Assert
        self.assertRaises(NotImplementedError)


class TestTopicMapper(TestCase):
    def test_to_database(self):
        # Arrange
        mapper = TopicMapper()
        topic = None

        # Act
        result = mapper.to_database(topic)

        # Assert
        self.assertRaises(NotImplementedError)

    def test_from_database(self):
        # Arrange
        mapper = TopicMapper()
        data = None

        # Act
        result = mapper.from_database(data)

        # Assert
        self.assertRaises(NotImplementedError)