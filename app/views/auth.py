from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user, login_required
from urllib.parse import urlparse

from app.forms.auth import LoginForm, RegistrationForm
from app.models.user import User
from app.models import db

# Create a blueprint for authentication
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Handle user login"""
    
    # If user is already logged in, redirect to home page
    if current_user.is_authenticated:
        return redirect(url_for('home.index'))
    
    # Create login form
    form = LoginForm()
    
    # Process form submission
    if form.validate_on_submit():
        # Find the user by username
        user = User.query.filter_by(username=form.username.data).first()
        
        # Check if user exists and password is correct
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password', 'danger')
            return redirect(url_for('auth.login'))
        
        # Log the user in
        login_user(user, remember=form.remember_me.data)
        
        # Redirect to the page the user was trying to access or to the home page
        next_page = request.args.get('next')
        if not next_page or urlparse(next_page).netloc != '':
            next_page = url_for('home.index')
            
        flash('You are now logged in!', 'success')
        return redirect(next_page)
    
    # Render the login template
    return render_template('auth/login.html', title='Sign In', form=form)


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """Handle user registration"""
    
    # If user is already logged in, redirect to home page
    if current_user.is_authenticated:
        return redirect(url_for('home.index'))
    
    # Create registration form
    form = RegistrationForm()
    
    # Process form submission
    if form.validate_on_submit():
        # Create new user
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        
        # Add to database
        db.session.add(user)
        db.session.commit()
        
        flash('Congratulations, you are now a registered user!', 'success')
        return redirect(url_for('auth.login'))
    
    # Render the registration template
    return render_template('auth/register.html', title='Register', form=form)


@auth_bp.route('/logout')
def logout():
    """Handle user logout"""
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('home.index')) 