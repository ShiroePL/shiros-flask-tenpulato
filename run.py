"""
Flask Demo Application Entry Point
This file serves as the entry point to run the Flask application
"""

from app import create_app

# Create the application instance using the factory function
app = create_app()

if __name__ == '__main__':
    """
    Run the application only if this script is executed directly.
    
    In production, you would use a WSGI server like Gunicorn or uWSGI,
    but for development, the built-in Flask server works well.
    """
    # Run the Flask development server
    # debug=True enables debug mode, which shows detailed error messages
    # and automatically reloads the server when code changes
    app.run(debug=True) 