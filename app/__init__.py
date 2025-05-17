from flask import Flask
from flask_migrate import Migrate

from app.config import Config
from app.models import db, login
from app.commands import init_db_command, seed_db_command

def create_app(config_class=Config):
    """
    Create and configure the Flask application instance.
    
    Args:
        config_class: Configuration class to use for app configuration
        
    Returns:
        Configured Flask application instance
    """
    # Initialize the Flask application
    app = Flask(__name__)
    
    # Load configuration from config class
    app.config.from_object(config_class)
    
    # Initialize extensions
    db.init_app(app)
    login.init_app(app)
    
    # Initialize database migrations
    migrate = Migrate(app, db)
    
    # Register blueprints
    from app.views.home import home_bp
    from app.views.about import about_bp
    from app.views.auth import auth_bp
    from app.views.posts import posts_bp
    
    app.register_blueprint(home_bp)
    app.register_blueprint(about_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(posts_bp)
    
    # Register CLI commands
    app.cli.add_command(init_db_command)
    app.cli.add_command(seed_db_command)
    
    # Create database tables within application context
    with app.app_context():
        db.create_all()
        # Additional database initialization can go here
        
    return app 