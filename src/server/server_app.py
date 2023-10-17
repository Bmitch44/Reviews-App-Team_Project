import random
import os
from bottle import Bottle, run, template, request, redirect, static_file, TEMPLATE_PATH
from src.user_management.user_info import UserInfo
from src.app_logic.app_logic import Topic, Reviews

class WebServer(Bottle):
    def __init__(self):
        super().__init__()
        self.TEMPLATES_PATH = os.path.join(os.path.dirname(__file__), 'templates')
        self.topics = []  # List to store topics
        self.reviews = {}  # Dictionary to store reviews

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
        return "Welcome to the home page!"

    def login(self):
        return template('login')

    def do_login(self):
        username = request.forms.get('username')
        password = request.forms.get('password')

        if UserInfo.login(username, password):
            self.logged_in_user = username
            return redirect('/dashboard')
        else:
            return redirect('/login')  

    def register(self):
        return template('register')

    def do_register(self):
        username = request.forms.get('username')
        password = request.forms.get('password')
        email = request.forms.get('email')

       # Check if the username already exists
        if username in UserInfo.users:
            return f"Username '{username}' is already taken. Please choose a different username.<br><a href='/'><button>Back to Home</button></a>"

        # Register the user
        UserInfo.register(username, email, password)
        return f"Registered user: {username} <br><a href='/'><button>Back to Home</button></a>"

    def dashboard(self):
        if self.logged_in_user:
            # Sample user reviews for demonstration
            user_reviews_data = [
                {'review_text': 'Review 1 for Topic 1', 'topic_id': 0, 'id': 0, 'user_id': 0},
                {'review_text': 'Review 2 for Topic 1', 'topic_id': 0, 'id': 1, 'user_id': 0}
            ]

            user_reviews = [Reviews(review_data['review_text'], review_data['user_id'], review_data['topic_id'], id=review_data['id']) for review_data in user_reviews_data]

            return template(os.path.join(self.TEMPLATES_PATH, 'base_logged_in.tpl'), username=self.logged_in_user, user_reviews=user_reviews)
        else:
            return redirect('/login')


    def create_review(self):
        if self.logged_in_user:
            review_content = request.forms.get('review_content')
            topic_id = int(request.forms.get('topic_id'))
            topic = self.topics[topic_id]
            review = Reviews(self.logged_in_user, review_content)
            topic.add_review(review)
            return template(os.path.join(self.TEMPLATES_PATH, 'create_review.tpl'), topic_id=topic_id)
        else:
            return redirect('/login')
        
    def list_topics(self):
        return "List of topics goes here!"

    def show_create_topic_form(self):
        return template('create_topic')

    def create_topic(self):
        
        topic_name = request.forms.get('name')
        topic_description = request.forms.get('description')

        topic_name = request.forms.get('name')
        topic_description = request.forms.get('description')
        topic = Topic(topic_name, topic_description)
        self.topics.append(topic)
        return redirect(f'/topics/{len(self.topics) - 1}')

    def view_topic(self, topic_id):
        return f"Viewing topic with ID {topic_id}"

    def show_edit_review_form(self, topic_id, review_id):
        return f"Editing review {review_id} for topic {topic_id}"

    def edit_review(self, topic_id, review_id):

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

if __name__ == "__main__":
    host_name = "localhost"
    server_port = 8080
    app = WebServer()

    TEMPLATE_PATH.append(app.TEMPLATES_PATH)

    app.run(host=host_name, port=server_port)
    print("Server stopped.")