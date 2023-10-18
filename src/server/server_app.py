
"""
server_app.py - Web Application

This file contains the logic and routing for a web application built using Bottle. 
The application handles user registration, login, dashboard, topic management,
and review creation/editing. It interfaces with a user information system, a logic system and
uses templates to render HTML views for various user interactions.

Author:
- Cody Cribb

Date:
- Oct. 17, 2023

Version:
- 1.0
"""

import random
import os
from bottle import Bottle, run, template, request, redirect, response, static_file, TEMPLATE_PATH
from src.user_management.user_info import UserInfo
from src.app_logic.app_logic import Topic, Reviews

TEMPLATE_PATH.insert(0, './src/templates/')

class WebServer(Bottle):
    """
    WebServer class to handle web application routing and functionality, uses Bottle.
    """
    def __init__(self):
        """
        Initialize the WebServer instance.
        """
        super().__init__()
        self.TEMPLATES_PATH = os.path.join(os.path.dirname(__file__), '../../templates')
        self.database_path = 'database_path'

        # Route definitions
        self.route('/', callback=self.home)
        self.route('/login', callback=self.login)
        self.route('/login', method='POST', callback=self.do_login)
        self.route('/register', callback=self.register)
        self.route('/register', method='POST', callback=self.do_register)
        self.route('/dashboard', callback=self.dashboard)
        self.route('/dashboard', method='POST', callback=self.create_review)
        self.route('/topics', callback=self.list_topics)
        self.route('/topics/add', callback=self.show_create_topic_form)
        self.route('/topics/create', method='POST', callback=self.create_topic)
        self.route('/topics/<topic_id>', callback=self.view_topic)
        self.route('/topics/<topic_id>/edit/<review_id>', callback=self.show_edit_review_form)
        self.route('/topics/<topic_id>/edit/<review_id>', method='POST', callback=self.edit_review)

    def home(self):
        """
        Callback for the home route.

        Returns:
            str: Response for the home route. (base template)
        """
        return template('base.tpl', title='Home Page', base='<h1>Welcome to the home page!</h1>')

    def dashboard(self):
        """
        Callback for the dashboard route.

        Returns:
            str: Response for the dashboard route. (logged_in template)
        """
        return template('base_logged_in.tpl', title="Dashboard", base="Welcome to the dashboard!")

    def login(self):
        """
        Callback for the login route.

        Returns:
            str: Response for the login route. (login template)
        """
        return template('login')

    def do_login(self):
        """
        Implements the login itself, requests username and password from user, checks validity.

        Returns:
            str: Redirection to the dashboard if log in is successful, else returns an error message.
        """
        username = request.forms.get('username')
        password = request.forms.get('password')
        login_check = UserInfo(self.database_path).login(username, password)

        if login_check:
            self.logged_in_user = username
            return redirect('/dashboard')
        else:
            return("No user with this username and password found.") #Should also redirect to login or home

          

    def register(self):
        """
        Callback for the registration route.

        Returns:
            str: Response for the login route (registration template).
        """
        return template('register')

    def do_register(self):
        """
        Handle the user registration process.

        Registers a new user using the provided username, email, and password.

        Returns:
            str: Redirect to login route.
        """
        username = request.forms.get('username')
        password = request.forms.get('password')
        email = request.forms.get('email')
        UserInfo(self.database_path).register(username, email, password)
        return redirect('/login')

    def create_review(self, topic_id):
        """
        Create a new review for a given topic.

        Args:
            topic_id (int): The ID of the topic for which the review is being created.

        Returns:
            str: Response indicating the success or failure of the review creation.
        """
        if self.logged_in_user:
            review_content = request.forms.get('review_text')
            topic = self.topics[topic_id]
            review = Reviews(self.logged_in_user, review_content)
            topic.add_review(review)
            return template(os.path.join(self.TEMPLATES_PATH, 'create_review.tpl'), topic_id=topic_id)
        else:
            return redirect('/login')
        
    def show_edit_review_form(self, topic_id, review_id):
        """
        Display the form for editing a review.

        Args:
            topic_id (int): The ID of the topic to which the review belongs.
            review_id (int): The ID of the review to be edited.

        Returns:
            str: Response displaying the review edit form.
        """
        return f"Editing review {review_id} for topic {topic_id}"

    def edit_review(self, topic_id, review_id):
        """
        Edit an existing review.

        Args:
            topic_id (int): The ID of the topic to which the review belongs.
            review_id (int): The ID of the review to be edited.

        Returns:
            str: Response indicating the success or failure of the review editing.
        """

        topic_id = int(topic_id)
        review_id = int(review_id)
        if 0 <= topic_id < len(self.topics) and 0 <= review_id < len(self.topics[topic_id].reviews):
            review_text = request.forms.get('review_text')
            if self.topics[topic_id].reviews[review_id].author == self.logged_in_user:
                self.topics[topic_id].reviews[review_id].content = review_text
                return f"Review edited: {review_text}"
            else:
                return "You can only edit your own reviews."
        else:
            return "Invalid topic ID or review ID."
        
    def list_topics(self):
        """
        List all topics available.

        Returns:
            str: HTML response displaying a list of topics.
        """
        topics = UserInfo(self.database_path).mapper.get(Topic)
        reviews = UserInfo(self.database_path).mapper.get(Reviews)
        return template('list_topics.tpl', title="Topics", topics=topics, reviews=reviews, base="base_logged_in.tpl")

    def show_create_topic_form(self):
        """
        Display the form for creating a new topic.

        Returns:
            str: HTML response displaying the topic creation form.
        """
        return template('create_topic')

    def create_topic(self):
        """
        Create a new topic based on the provided form data.

        Returns:
            str: HTML response indicating the success or failure of the topic creation.
        """
        if self.logged_in_user:
        
            topic_name = request.forms.get('name')
            topic_description = request.forms.get('description')
            user_id = UserInfo(self.database_path).session_manager.get_session().user_id
            topic = Topic(topic_name, topic_description, user_id)
            self.topics.append(topic)
        return redirect(f'/topics/{len(self.topics) - 1}')

    def view_topic(self, topic_id):
        """
        View details of a specific topic.

        Args:
            topic_id (int): The ID of the topic to be viewed.

        Returns:
            str: Response displaying the details of the specified topic.
        """
        return f"Viewing topic with ID {topic_id}"

if __name__ == "__main__":
    host_name = "localhost"
    server_port = 8080
    app = WebServer()

    TEMPLATE_PATH.insert(0, './src/templates/')

    app.run(host=host_name, port=server_port)
    print("Server stopped.")