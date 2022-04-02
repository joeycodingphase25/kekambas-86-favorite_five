# from crypt import methods
from app import app
from flask import redirect, render_template, url_for, flash
from flask_login import login_user
from app.forms import SignUpForm, RegisterAddress, LoginForm
from app.models import User, Post, Address
from app.data import dicts

@app.route('/')
def index():
    title = 'Home'
    user = {'id': 1, 'username': 'These are my current favorite pianists -- jojo', 'email': 'brians@codingtemple.com'}
    posts = dicts
    return render_template('index.html', current_user=user, title=title, posts=posts)


@app.route('/signup', methods=["GET", "POST"])
def signup():
    title = 'Sign Up'
    form = SignUpForm()
    if form.validate_on_submit(): # check if post request AND post is valid
        email = form.email.data
        username = form.username.data
        password = form.password.data
        # Create User object
        users_with_that_info = User.query.filter((User.username==username)|(User.email==email)).all()
        if users_with_that_info:
            flash(f"There is already a user with that username and/or email. Please Try Again!", "danger")
            return redirect(url_for('signup'))
        
        new_user = User(email=email, username=username, password=password)
        # Flash new user message
        flash(f"{new_user.username} has successfully signed up.", "success")
        return redirect(url_for('index'))

    return render_template('signup.html', title=title, form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    title = 'Log In'
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        # Check if there is a user with that username
        user = User.query.filter_by(username=username).first()
        # Check if there is user and password is correct
        if user and user.check_password(password):
            # log the user in with flask-login
            login_user(user)
            # flash message that user has successfully logged in
            flash(f"{user} has successfully logged in", 'success')
            # redirect to homepage
            return redirect(url_for('index'))
        else:
            flash("Username and/or password is incorrect", "danger")
    return render_template('login.html', title=title, form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash('You have successfully logged out', 'primary')
    return redirect(url_for('index'))

@app.route('/phone-address', methods=['GET', 'POST'])
def phone_address():
    title = 'Please Register'
    form = RegisterAddress() #RegisterAdressForm?
    addresses = Address.query.all()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        address = form.address.data
        Address(first_name=first_name, last_name=last_name, address=address)
        return redirect(url_for('index'))
    return render_template('phone-address.html', title=title, form=form, addressess = addresses)