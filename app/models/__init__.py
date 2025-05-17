# This file makes the models directory a Python package
# It serves as a central point for database initialization and models imports

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize SQLAlchemy for database management
db = SQLAlchemy()

# Initialize LoginManager for user authentication
login = LoginManager()
login.login_view = 'auth.login'  # Specify the endpoint for the login page
login.login_message = 'Please log in to access this page.'
login.login_message_category = 'info'

# Import models so they are registered with SQLAlchemy
from app.models.user import User 