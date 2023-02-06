from flask import Blueprint, render_template, flash, redirect, url_for, request
from .forms import SignupForm, LoginForm
from flask_login import login_user, current_user, logout_user
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    cur_user = current_user
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')
    return render_template('login.html', form=form, cur_user = cur_user)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    cur_user = current_user
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        password2 = form.password2.data

        user = User.query.filter_by(email = email).first()
        if user:
            flash('The user has already been created', category='error')
            return redirect(url_for('auth.signup'))
        elif len(name) < 2:
            flash('The name should be greater than 2 characters', category='error')
            return redirect(url_for('auth.signup'))
        elif len(email) < 3:
            flash('Email should be greater than 3 characters', category='error')
            return redirect(url_for('auth.signup'))
        elif password != password2:
            flash('Password should be the same', category='error')
            return redirect(url_for('auth.signup'))
        else:
            new_user = User( name = name, email = email, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()

            login_user(new_user, remember=True)
            flash('New user has been created', category='success')
            return redirect(url_for('auth.login'))


    return render_template('signup.html', form=form, cur_user = cur_user)


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))