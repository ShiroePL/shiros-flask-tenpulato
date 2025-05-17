from flask import Blueprint, render_template
from app.models.user import Post

# Create a blueprint for home-related routes
# The first argument is the blueprint name
# The second argument is the import name (usually __name__)
# The url_prefix will be prepended to all routes in this blueprint
home_bp = Blueprint('home', __name__, url_prefix='/')

@home_bp.route('/')
def index():
    """
    Route handler for the homepage.
    
    Returns:
        Rendered home/index.html template
    """
    # Example of passing data to a template
    page_title = "Welcome to Flask Demo"
    features = [
        "Modular Structure with Blueprints",
        "Template Inheritance",
        "Static File Organization",
        "Clean Configuration",
        "Database with SQLAlchemy",
        "User Authentication with Flask-Login",
        "Forms with Flask-WTF",
        "Environment Management with python-dotenv"
    ]
    
    # Get recent posts to display on homepage
    recent_posts = Post.query.order_by(Post.created_at.desc()).limit(3).all()
    
    # render_template renders an HTML template with the provided variables
    return render_template('home/index.html', 
                           title=page_title, 
                           features=features,
                           recent_posts=recent_posts) 