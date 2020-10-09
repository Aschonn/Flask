from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskdraft import db
from flaskdraft.models import Post
from flaskdraft.posts.forms import AddPost 

posts = Blueprint('posts', __name__)

#----------------------POST-------------------------#

@posts.route('/post/add', methods=['GET', 'POST'])
@login_required
def add_post():
    form = AddPost()
    #on submit do this
    if form.validate_on_submit():
        #gather data from submitted form
        post = Post(title = form.title.data, content=form.content.data, author=current_user)
        #add to sesh
        db.session.add(post)
        #commit sesh
        db.session.commit()
        flash('Your post has been added!', 'success')
        #redirect home if successful
        return redirect(url_for('main.home'))
    #else return form template
    return render_template('add_post.html', title='Account', form=form, legend = 'New Post')

@posts.route("/post/<int:post_id>")
def post(post_id):
    #get post based on specific id
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)
    #will return 404 if null
    #could specify error if null to help developers


@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    #check post database crosscheck database
    post = Post.query.get_or_404(post_id)
    #abort 403 if author doesnt equal the current user
    if post.author != current_user:
        abort(403)
    form = AddPost()
    if form.validate_on_submit():
        #get submitted form data
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        #add users email and content to form fields
        form.title.data = post.title
        form.content.data = post.content
    return render_template('add_post.html', title='Update Post',
                           form=form, legend='Update Post')


@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    #gets id and if it's in database it will delete
    post = Post.query.get_or_404(post_id)
    #before deleting we check that user is the one deleting it
    if post.author != current_user:
        abort(403)
    #delete command
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))

