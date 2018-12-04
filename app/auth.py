import functools

from flask import Blueprint, flash, redirect, render_template, request, url_for, session, g
from werkzeug.security import check_password_hash, generate_password_hash

from app.db import get_db

true, false, null = True, False, None

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = null

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif db.execute(
                'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not null:
            error = f'Username {username} is already taken.'

        if error is null:
            db.execute(
                'INSERT INTO user (username, password) VALUES (?, ?)',
                (username, generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for('auth.login'))

        flash(error)
    return render_template('/auth/register.html')


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
