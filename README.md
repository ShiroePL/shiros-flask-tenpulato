# Flask Demo Project

A complete Flask application template designed to demonstrate Flask project structure and best practices for C# developers learning Python, featuring SQLAlchemy, Flask-Login, WTForms, and Bootstrap 5 with a dark theme.

## Project Overview

This project serves as a comprehensive template/example for Flask web applications, highlighting:

- Modular code organization using Flask Blueprints
- HTML templating with Jinja2 inheritance
- Structured static file organization (CSS, JavaScript)
- Python package and module structure
- Database integration with SQLAlchemy and SQLite
- User authentication with Flask-Login
- Form handling with WTForms
- Environment configuration with python-dotenv
- **Modern UI with Bootstrap 5 (dark theme)**

## Project Structure

```
flask_demo/
├── app/                    # Application package
│   ├── __init__.py         # Application factory
│   ├── config.py           # Configuration settings
│   ├── models/             # Database models
│   │   ├── __init__.py     # DB initialization
│   │   └── user.py         # User and Post models
│   ├── forms/              # WTForms forms
│   │   ├── __init__.py     # Package initialization
│   │   ├── auth.py         # Authentication forms
│   │   └── post.py         # Post forms
│   ├── static/             # Static files (CSS, JS, images)
│   │   ├── css/            # CSS files
│   │   ├── js/             # JavaScript files
│   │   └── img/            # Image files
│   ├── templates/          # HTML templates
│   │   ├── base.html       # Base template
│   │   ├── home/           # Home page templates
│   │   ├── about/          # About page templates
│   │   ├── auth/           # Authentication templates
│   │   └── posts/          # Blog post templates
│   └── views/              # Blueprint modules
│       ├── __init__.py     # Package initialization
│       ├── home.py         # Home routes
│       ├── about.py        # About routes
│       ├── auth.py         # Authentication routes
│       └── posts.py        # Blog post routes
├── .env                    # Environment variables (create from env_example.txt)
├── env_example.txt         # Example environment file
├── app.db                  # SQLite database (created at runtime)
├── requirements.txt        # Python dependencies
├── run.py                  # Application entry point
└── README.md               # Project documentation
```

## Key Concepts for C# Developers

### Flask Blueprints vs. ASP.NET Controllers

In Flask, Blueprints serve a similar purpose to Controllers in ASP.NET MVC. They organize routes into logical groups, allowing you to:

- Split your application into modular components
- Register URL routes with specific prefixes
- Apply middleware to specific groups of routes

Example in `app/views/home.py`:

```python
# Create a blueprint for home-related routes
home_bp = Blueprint('home', __name__, url_prefix='/')

@home_bp.route('/')
def index():
    # Route handler for the homepage
    recent_posts = Post.query.order_by(Post.created_at.desc()).limit(3).all()
    return render_template('home/index.html', recent_posts=recent_posts)
```

### SQLAlchemy vs. Entity Framework

SQLAlchemy is a Python ORM similar to Entity Framework in C#:

```python
# Define a model (similar to EF entity classes)
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    
    # Relationships (similar to navigation properties in EF)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    
# Query the database (similar to LINQ in C#)
users = User.query.filter_by(username='john').first()
recent_posts = Post.query.order_by(Post.created_at.desc()).all()
```

### Flask-Login vs. ASP.NET Identity

Flask-Login provides user authentication similar to ASP.NET Identity:

```python
# Login a user
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('home.index'))
    return render_template('auth/login.html', form=form)

# Protect routes with login_required decorator
@posts_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    # Only authenticated users can access this route
    # ...
```

### WTForms vs. ASP.NET MVC Forms

WTForms provides form handling and validation similar to MVC model binding:

```python
# Form definition (similar to ASP.NET MVC model)
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    
# Form validation and processing
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Form is valid, create new user
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)
```

### Bootstrap 5 Integration

This project uses Bootstrap 5 with a dark theme, similar to how you might use Bootstrap in ASP.NET MVC projects:

```html
<!-- Bootstrap 5 via CDN in base.html -->
<html lang="en" data-bs-theme="dark">
<head>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Bootstrap Icons -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css" rel="stylesheet">
</head>

<!-- Bootstrap JavaScript -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
```

The project demonstrates:

- Responsive layouts with Bootstrap's grid system
- Dark theme with `data-bs-theme="dark"` attribute 
- UI components like cards, modals, navbars, and forms
- Bootstrap Icons for enhanced UI
- JavaScript interactions with Bootstrap components

This approach is similar to how you would include Bootstrap in an ASP.NET MVC project by referencing it via CDN or through the LibMan/NPM package manager.

### Templates vs. Razor Views

Flask uses Jinja2 templating, which is similar to Razor in ASP.NET:

```html
<!-- Template inheritance (like Razor layouts) -->
{% extends "base.html" %}

<!-- Variable rendering (like Razor's @Model.Property) -->
<h1>{{ post.title }}</h1>

<!-- Conditional blocks (like Razor's @if statements) -->
{% if current_user.is_authenticated %}
    <a href="{{ url_for('posts.create') }}">Create Post</a>
{% endif %}

<!-- Loops (like Razor's @foreach) -->
{% for post in posts %}
    <div class="post">{{ post.title }}</div>
{% endfor %}

<!-- Form rendering with WTForms -->
<form method="POST">
    {{ form.hidden_tag() }}
    {{ form.username.label }}
    {{ form.username(class="form-control") }}
    {{ form.submit(class="btn") }}
</form>
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone or download this repository

2. Create a virtual environment:
   ```
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```
   # Rename env_example.txt to .env or create a new .env file
   # You can modify the values as needed
   ```

5. Run the application:
   ```
   python run.py
   ```

6. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

7. Register a new user account to access all features

## Key Features Demonstrated

### User Authentication

- User registration with validation
- Login with session management
- Protected routes with @login_required
- Password hashing for security

### Database Operations (CRUD)

- Create: Adding new users and posts
- Read: Displaying users and posts
- Update: Editing existing posts
- Delete: Removing posts

### Forms with Validation

- Client-side and server-side validation
- CSRF protection
- Custom validators
- Flash messages for user feedback

### Modern UI with Bootstrap 5

- Dark theme via the `data-bs-theme="dark"` attribute
- Responsive design with Bootstrap's grid system
- Interactive components:
  - Modal dialogs for confirmations
  - Cards for content display
  - Navbar with dropdown menus
  - Form validation and styling
  - Alert messages
- Bootstrap Icons for enhanced UI
- Custom animations and transitions

### Environment Configuration

- Using python-dotenv for environment variables
- Separating development and production settings

## Learning Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Flask-Login Documentation](https://flask-login.readthedocs.io/)
- [Flask-WTF Documentation](https://flask-wtf.readthedocs.io/)
- [Bootstrap 5 Documentation](https://getbootstrap.com/docs/5.3/)
- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [Jinja2 Template Documentation](https://jinja.palletsprojects.com/) 