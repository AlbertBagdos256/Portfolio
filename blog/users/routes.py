# custom
from blog.models import User, Post
from blog import db,bcrypt
from blog.users.forms import RegistrationForm, LoginForm, UpdateAccountForm
from blog.users.utils import Pics_to_db
# system
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required

users = Blueprint('users', __name__)

@users.route("/register", methods = ['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title = 'Register', form = form)
    

@users.route("/login", methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember = form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.index'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form = form)


@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@users.route("/account", methods = ['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = Pics_to_db(form.picture.data)
            current_user.image_file = picture_file
            
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename = 'images/users_avatars/' + current_user.image_file)
    return render_template('profile.html', title = 'Account',
                           image_file = image_file, form = form)


@users.route("/user/<username>", methods = ['GET','POST'])

def user(username):
    user_data = User.query.filter_by(username = username).all()
    user = User.query.filter_by(username = username).first()
    for content in  user_data:
        username = content.username
        email    = content.email
        img_file = content.image_file
        
    posts_list = user.posts
    image_path = url_for('static', filename = 'images/users_avatars/' + img_file)
    return render_template('user.html', username = username, email = email, image_path = image_path,
                           posts_list = posts_list)
      
