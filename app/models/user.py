from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app.models import db, login

class User(UserMixin, db.Model):
    """User model for authentication and user management"""
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Example relationship - a user can have many posts (one-to-many)
    # This demonstrates how relationships work in SQLAlchemy
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    
    def __repr__(self):
        """String representation of the User model"""
        return f'<User {self.username}>'
    
    def set_password(self, password):
        """Set a secure password hash"""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Verify password against stored hash"""
        return check_password_hash(self.password_hash, password)

# User loader function for Flask-Login
@login.user_loader
def load_user(id):
    """Load a user from the database"""
    return User.query.get(int(id))


# Post model as an example of a related model
class Post(db.Model):
    """Example Post model to demonstrate relationships"""
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __repr__(self):
        """String representation of the Post model"""
        return f'<Post {self.title}>' 