import datetime
import uuid

class User:
    """
    A user in the system
    """

    def __init__(self, username: str, email:str, hashed_password: str, 
                 id: int=None):
        self.username = username
        self.email = email
        self.hashed_password = hashed_password
        self.id = id or uuid.uuid4().hex
    
    @property
    def data(self):
        """
        Allows you to access class data as a dictionary
        
        This function creates an empty dictionary and if it is the first time
        this class is initialized assigns the id a key in the dictionary. 
        Then updates all other entries to their current states.
        In all updates after the first the id will remain the same.

        Returns: 
            the class variables as a dictionary
        """
        data = {}
        if self.id:
            data["id"] = self.id

        data.update({
            "username" : self.username,
            "email" : self.email,
            "hashed_password" : self.hashed_password 
            })

        return data

    
class Review:
    """
    A review in the system
    """

    def __init__(self, review_text: str, user_id: int, topic_id: int, 
                 status: str = "draft", id: int = None):
        self.review_text = review_text
        self.user_id = user_id
        self.topic_id = topic_id
        self.status = status
        self.id = id or uuid.uuid4().hex

    @property
    def data(self):
        """
        Allows you to access class data as a dictionary
        
        This function creates an empty dictionary and if it is the first time
        this class is initialized assigns the id a key in the dictionary. 
        Then updates all other entries to their current states.
        In all updates after the first the id will remain the same.

        Returns: 
            the class variables as a dictionary
        """
        data = {}
        if self.id:
            data["id"] = self.id

        data.update({
            "review_text" : self.review_text,
            "user_id" : self.user_id,
            "topic_id" : self.topic_id,
            "status" : self.status
        })

        return data


class Topic:
    """
    a topic in the system 
    """
    
    def __init__(self, name: str, description: str, user_id: int, 
                 id: int = None):
        self.name = name
        self.description = description
        self.user_id = user_id
        self.id = id or uuid.uuid4().hex

    @property
    def data(self):
        """
        Allows you to access class data as a dictionary
        
        This function creates an empty dictionary and if it is the first time
        this class is initialized assigns the id a key in the dictionary. 
        Then updates all other entries to their current states.
        In all updates after the first the id will remain the same.

        Returns: 
            the class variables as a dictionary
        """
        data = {}
        if self.id:
            data["id"] = self.id

        data.update({
            "name" : self.name,
            "description" : self.description,
            "user_id" : self.user_id
            })

        return data


class Session:
    """
    A session with the server 
    """

    def __init__(self, user_id, created_at = None, expires_at = None, 
                 last_activity_at  = None, is_active = 0, session_id = None):
        self.user_id = user_id
        self.created_at = created_at or datetime.datetime.now()
        self.expires_at = expires_at or (self.created_at 
                                         + datetime.timedelta(hours=1))
        self.last_activity_at = last_activity_at or datetime.datetime.now()
        self.is_active = is_active
        self.session_id = session_id or uuid.uuid4().hex

    @property
    def data(self):
        """
        Allows you to access class data as a dictionary
        
        This function creates an empty dictionary and if it is the first time
        this class is initialized assigns the session_id a key in the dictionary. 
        Then updates all other entries to their current states. 
        In all updates after the first the session_id will remain the same.

        Returns: 
            the class variables as a dictionary
        """
        data = {}
        if self.session_id:
            data["session_id"] = self.session_id

        data.update({"user_id" : self.user_id,
            "created_at" : self.created_at,
            "expires_at" : self.expires_at,
            "last_activity_at" : self.last_activity_at,
            "is_active" : self.is_active,
        })

        return data