import uuid

import bcrypt
from flask import Blueprint, redirect, url_for, request, render_template, flash
from flask_login import login_user, login_required, logout_user, current_user

from forms import RegisterForm, LoginForm
from models import User, db

guest_blueprint = Blueprint('guest_views', __name__, template_folder='templates')


def redirect_if_authenticated(username=None):
    if current_user.is_authenticated:
        return redirect(url_for('user_views.dashboard', username=username or current_user.username))


@guest_blueprint.route('/')
def redir():
    return redirect(url_for('guest_views.login'))


@guest_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    # if user is already logged in, redirect to dashboard
    redirect_response = redirect_if_authenticated()
    if redirect_response:
        return redirect_response

    # if user presses login button
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        # check if user exists
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            # check if password matches
            if bcrypt.checkpw(form.password.data.encode('utf-8'), user.password.encode('utf-8')):
                login_user(user)
                flash("Logged in", category='success')
                return redirect(url_for('user_views.dashboard', username=user.username))
            # if password does not match, flash error and redirect to login page
            else:
                flash("Incorrect Password", category='error')
                return render_template('guest/login.html', form=form, error="Invalid email or password")
        # if user does not exist, flash error and redirect to login page
        else:
            flash("The account does not exist.", category='error')
            return render_template('guest/login.html', form=form, error="The account does not exist.")

    return render_template('guest/login.html', form=form)


@guest_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    # if user is already logged in, redirect to dashboard
    redirect_response = redirect_if_authenticated()
    if redirect_response:
        return redirect_response

    # if user presses register button
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        # check if user exists
        user = User.query.filter_by(username=form.username.data).first()
        email = User.query.filter_by(email=form.email.data).first()
        if user or email:
            # if user exists, flash error and redirect to register page
            flash("Account already exists", category='error')
            return render_template('guest/register.html', form=form, error="Account already exists")
        else:
            # if user does not exist, create user and redirect to login page
            new_user = User(
                id=str(uuid.uuid4()),
                username=form.username.data,
                email=form.email.data,
                password=bcrypt.hashpw(form.password.data.encode('utf-8'), bcrypt.gensalt()),
                role='user'
            )
            db.session.add(new_user)
            db.session.commit()
            flash("Account created successfully.", category='success')
            return redirect(url_for('guest_views.login'))
    return render_template('guest/register.html', form=form)


@guest_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logged out", category='success')
    return redirect('/')
