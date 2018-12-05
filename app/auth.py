import functools

from flask import Blueprint, flash, redirect, render_template, request, url_for, session, g
from werkzeug.security import check_password_hash, generate_password_hash

from app.db import get_db

true, false, null = True, False, None

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        errors = {}

        if not first_name:
            errors['first_name'] = 'First name is required.'
        if not last_name:
            errors['last_name'] = 'Last name is required.'
        if not email:
            errors['email'] = 'Email is required.'
        if not username:
            errors['username'] = 'Username is required.'
        if not password:
            errors['password'] = 'Password is required.'
        if not errors:
            user = db.execute(
                'SELECT id FROM user WHERE username = ?', (username,)
             ).fetchone()
            if user is not null:
                errors['username'] = f'Username {username} is already taken.'
            user = db.execute(
                'SELECT id FROM user WHERE email = ?', (email,)
            ).fetchone()
            if user is not null:
                errors['email'] = f'Email {email} is already taken.'

        if not errors:
            db.execute(
                'INSERT INTO user (first_name, last_name, email, username, password) VALUES (?, ?, ?, ?, ?)',
                (first_name, last_name, email, username, generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for('auth.login'))

        flash(errors)
    return render_template('auth/register.html')


@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = user = null

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        else:
            user = db.execute(
                'SELECT * FROM user WHERE username = ?', (username,)
            ).fetchone()

            if user is null:
                error = 'Incorrect username.'
            elif not check_password_hash(user['password'], password):
                error = 'Incorrect password.'

        if error is null:
            session.clear()
            session['user_id'] = user['id']

            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is null:
        g.user = null
    else:
        db = get_db()
        g.user = db.execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**keyargs):
        if g.user is null:
            return redirect(url_for('auth.login'))
        return view(**keyargs)

    return wrapped_view
