from src.data_management.object_mapper import ObjectMapper
from src.app_logic.logic import Session

class SessionManager:
    def __init__(self, db_path: str):
        """
        Initializes a new SessionManager instance.

        Args:
            db_path (str): The path to the database where session data is stored.
        """
        self.db_path = db_path
        self.sessions = []
        

    def create_session(self, user_id: int, is_active: int = 1):
        """
        Creates a new session for a user.

        Args:
            user_id (int): The ID of the user for whom the session is created.
            is_active (int, optional): A flag indicating whether the session is active (default is 1).

        Returns:
            Session: The created session object.
        """
        session = Session(user_id, is_active)
        self.sessions.append(session)  # Add the session to your sessions data structure
        return session
        

    def get_session(self, session_id: str):
        """
        Retrieves a session by its ID.

        Args:
            session_id (str): The ID of the session to retrieve.

        Returns:
            Session: The session object if found, None otherwise.
        """
        for session in self.sessions:
            if session.session_id == session_id:
                return session
        return None
        

    def get_user_session(self, user_id: int):
        """
        Retrieves the session associated with a user.

        Args:
            user_id (int): The ID of the user.

        Returns:
            Session: The session object if found, None otherwise.
        """
        for session in self.sessions:
            if session.user_id == user_id:
                return session
        return None
        

    def update_session(self, session):
        """
        Updates a session.

        Args:
            session (Session): The session object to update.
        """
        for i, existing_session in enumerate(self.sessions):
            if existing_session.session_id == session.session_id:
                self.sessions[i] = session
                return
        
