import click
from flask.cli import with_appcontext
from app.models import db
from app.models.user import User, Post

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Create database tables from models"""
    db.create_all()
    click.echo('Initialized the database.')

@click.command('seed-db')
@with_appcontext
def seed_db_command():
    """Seed the database with sample data"""
    # Check if we already have users
    if User.query.count() > 0:
        click.echo('Database already contains data. Skipping seed.')
        return
    
    # Create sample users
    admin = User(username='admin', email='admin@example.com')
    admin.set_password('password')
    
    john = User(username='john', email='john@example.com')
    john.set_password('password')
    
    jane = User(username='jane', email='jane@example.com')
    jane.set_password('password')
    
    db.session.add_all([admin, john, jane])
    db.session.commit()
    
    # Create sample posts
    post1 = Post(
        title='Welcome to Flask Demo',
        content='This is the first post in our Flask blog demo. This demonstrates how to use SQLAlchemy models with relationships.',
        user_id=admin.id
    )
    
    post2 = Post(
        title='Working with SQLAlchemy',
        content='SQLAlchemy is a powerful ORM for Python that allows you to work with databases in an object-oriented way, similar to Entity Framework in C#.',
        user_id=john.id
    )
    
    post3 = Post(
        title='Authentication with Flask-Login',
        content='Flask-Login provides user session management for Flask. It handles the common tasks of logging in, logging out, and remembering users\' sessions over extended periods of time.',
        user_id=jane.id
    )
    
    post4 = Post(
        title='Forms with Flask-WTF',
        content='Flask-WTF integrates WTForms with Flask, providing form validation, CSRF protection, and more. It\'s similar to how form validation works in ASP.NET MVC.',
        user_id=admin.id
    )
    
    db.session.add_all([post1, post2, post3, post4])
    db.session.commit()
    
    click.echo('Added sample users and posts to the database.') 