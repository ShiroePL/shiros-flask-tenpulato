from flask import Blueprint, render_template

# Create a blueprint for about-related routes
about_bp = Blueprint('about', __name__, url_prefix='/about')

@about_bp.route('/')
def about():
    """
    Route handler for the about page.
    
    Returns:
        Rendered about/about.html template
    """
    # Information to pass to the template
    about_info = {
        "title": "About This Demo",
        "description": "This is a demo Flask application showing best practices for organization and structure.",
        "features": {
            "Blueprints": "For modular route organization",
            "Templates": "With inheritance for DRY HTML",
            "Static Files": "Organized CSS, JS, and images",
            "Configuration": "Centralized application settings"
        }
    }
    
    return render_template('about/about.html', info=about_info) 