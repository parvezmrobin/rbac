from werkzeug.security import generate_password_hash

from app.db import get_db
from flask import Blueprint

bp = Blueprint('model.user', __name__)

columns = ['id', 'first_name', 'last_name', 'email', 'username']


def index():
    db = get_db()
    query = "SELECT id, first_name, last_name, email, username FROM user"
    result = db.execute(query).fetchall()
    return result


def read(user_id):
    db = get_db()
    query = "SELECT id, first_name, last_name, email, username FROM user where id=?"
    result = db.execute(query, (user_id,)).fetchone()
    return result


def _where(**kwargs):
    if len(kwargs) == 0:
        raise ValueError("No condition given")
    conditions = map(lambda k: f"{k}=?", kwargs)
    condition = ' AND '.join(conditions)
    db = get_db()
    query = f"SELECT * FROM user WHERE {condition}"
    cursor = db.execute(query, tuple(kwargs.values()))
    return cursor


def where(**kwargs):
    cursor = _where(**kwargs)
    result = cursor.fetchall()
    return result


def where_first(**kwargs):
    cursor = _where(**kwargs)
    result = cursor.fetchone()
    return result


def create(username, password, first_name, last_name, email):
    """
    Creates new user account
    :param username:
    :param password:
    :param first_name:
    :param last_name:
    :param email:
    :return: [int] user.id
    """
    db = get_db()
    hashed_password = generate_password_hash(password)
    query = "INSERT INTO user(username, password, first_name, last_name, email) values (?, ?, ?, ?, ?)"
    cursor = db.execute(query, (username, hashed_password, first_name, last_name, email))
    db.commit()
    return cursor.lastrowid
