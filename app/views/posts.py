from flask import Blueprint, render_template, redirect, url_for, flash, request, abort
from flask_login import current_user, login_required

from app.forms.post import PostForm
from app.models.user import Post
from app.models import db

# Create a blueprint for post management
posts_bp = Blueprint('posts', __name__, url_prefix='/posts')

@posts_bp.route('/')
def index():
    """Display all posts"""
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template('posts/index.html', title='All Posts', posts=posts)


@posts_bp.route('/<int:id>')
def view(id):
    """Display a single post"""
    post = Post.query.get_or_404(id)
    return render_template('posts/view.html', title=post.title, post=post)


@posts_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    """Create a new post"""
    form = PostForm()
    
    if form.validate_on_submit():
        post = Post(
            title=form.title.data,
            content=form.content.data,
            author=current_user
        )
        db.session.add(post)
        db.session.commit()
        
        flash('Your post has been created!', 'success')
        return redirect(url_for('posts.view', id=post.id))
    
    return render_template('posts/editor.html', title='Create Post', form=form)


@posts_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    """Edit an existing post"""
    post = Post.query.get_or_404(id)
    
    # Check if the current user is the author
    if post.author != current_user:
        abort(403)  # Forbidden
    
    form = PostForm()
    
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.view', id=post.id))
    elif request.method == 'GET':
        # Pre-populate form with existing data
        form.title.data = post.title
        form.content.data = post.content
    
    return render_template('posts/editor.html', title='Edit Post', form=form)


@posts_bp.route('/delete/<int:id>', methods=['POST'])
@login_required
def delete(id):
    """Delete a post"""
    post = Post.query.get_or_404(id)
    
    # Check if the current user is the author
    if post.author != current_user:
        abort(403)  # Forbidden
    
    db.session.delete(post)
    db.session.commit()
    
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('posts.index')) 