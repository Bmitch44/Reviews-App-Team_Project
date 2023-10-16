

class User:
    """s
    """
    def __init__(self, username: str, email:str, hashed_passowrd: str, 
                 id: int=None):
        pass
    
        

class Reviews:
    """
    """

    def __init__(self, review_text: str, user_id: int, topic_id: int, 
                 status: str = "draft", id: int = None):
        pass

class Topic:
    """"""
    
    def __init__(self, name: str, description: str, user_id: int, 
                 id: int = None):
        pass

class Session:
    """"""

    def __init__(self, user_id, created_at = None, expires_at = None, 
                 last_activity  = None, is_active = 0, session_id = None):
        pass

