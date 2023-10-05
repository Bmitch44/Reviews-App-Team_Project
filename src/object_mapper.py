class BaseMapper:
    """
    A base mapper that provides shared logic and interface for all mappers.
    """

    def to_database(self, obj):
        """
        Convert an object to its database representation.
        
        Args:
            obj (object): The object to be mapped.

        Returns:
            dict: A dictionary representation for the database.

        Raises:
            NotImplementedError: This function should be implemented by child classes.
        """
        raise NotImplementedError("This function has not been implemented yet.")

    def from_database(self, data):
        """
        Convert a database record to an object.
        
        Args:
            data (dict): The data from the database.

        Returns:
            object: The mapped object.

        Raises:
            NotImplementedError: This function should be implemented by child classes.
        """
        raise NotImplementedError("This function has not been implemented yet.")


class UserMapper(BaseMapper):
    """
    Maps the User object to and from its database representation.
    """

    def to_database(self, user):
        # Implement the specific logic for mapping a User object to database representation.
        pass

    def from_database(self, data):
        # Implement the specific logic for mapping database data to a User object.
        pass


class ReviewMapper(BaseMapper):
    """
    Maps the Review object to and from its database representation.
    """

    def to_database(self, review):
        # Implement the specific logic for mapping a Review object to database representation.
        pass

    def from_database(self, data):
        # Implement the specific logic for mapping database data to a Review object.
        pass


class TopicMapper(BaseMapper):
    """
    Maps the Topic object to and from its database representation.
    """

    def to_database(self, topic):
        # Implement the specific logic for mapping a Topic object to database representation.
        pass

    def from_database(self, data):
        # Implement the specific logic for mapping database data to a Topic object.
        pass