from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from flaskdraft import db, bcrypt
from flaskdraft.models import UserInfo, Post, Feedback
from flaskdraft.users.forms import (RegisterForm, LoginForm, UpdateAccountForm,
                                   RequestResetForm, ResetPasswordForm, FeedbackForm)
from flaskdraft.users.utils import save_picture, send_reset_email
from flaskdraft.send_mail import send_mail


from flask import Blueprint

users = Blueprint('users', __name__)


#----------------------------REGISTER ENDPOINT----------------------------#


@users.route("/register", methods=['GET', 'POST'])
def register():
    
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = UserInfo(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)


#-------------------LOGIN------------------------#


@users.route("/login", methods=['GET', 'POST'])
def login():

    #redirect is user is authenicated

    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    
    #form template
    form = LoginForm()

    #if clicked 
    if form.validate_on_submit():

        #checks if there is a user with same email
        user = UserInfo.query.filter_by(email=form.email.data).first()
        
        #if email exists and password hash in database is the same hash as the login form submittion send user to home page and remember login
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            
            #from flask_login import #it remembers user
            login_user(user, remember=form.remember.data)
            #get next parameter(args is dictionary and get method is option so it is able to return none)
            #we are trying to redirect to page the user was on previous before accessing  blocked page
            next_page = request.args.get('next')
            #redirect if next page doesnt exist
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

#----------------------------LOGOUT ENDPOINT----------------------------#


@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))


#----------------------------ACCOUNT ENDPOINT----------------------------#

@users.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form)


#-------------------Select Specific User------------------#

@users.route("/user/<string:username>")
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = UserInfo.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=5)
    return render_template('user_posts.html', posts=posts, user=user)


    #--------------------------RESET PASSWORD-------------------#

@users.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = UserInfo.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password.', 'info')
        return redirect(url_for('users.login'))
    return render_template('reset_request.html', title='Reset Password', form=form)


#--------------------RESET TOKEN-------------------------#


@users.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    user = UserInfo.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('reset_token.html', title='Reset Password', form=form)


@users.route('/feedback', methods=['GET', 'POST'])
@login_required
def feedback():
    
        
    form = FeedbackForm()
    if form.validate_on_submit():

        username = form.username.data
        email = form.email.data
        comments = form.comments.data

        if username == '' or email == '':
            return render_template('feedback.html', message='Please enter required fields')
        
        if Feedback.query.filter(Feedback.email==email).count() < 5:
            data = Feedback(username, email, comments)
            db.session.add(data)
            db.session.commit()
            send_mail(username, email, comments)
            flash('Your Feedback has been sent! Thank You!', 'success')
            return render_template('success.html')
        return render_template('feedback.html', message='The 5 feedback submission limit has been exceeded', form=form)
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template('feedback.html', title='Feedback', form = form)
