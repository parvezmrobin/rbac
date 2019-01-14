from werkzeug.security import generate_password_hash

from app.db import get_db

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
    :return: user.id
    :rtype: int
    """
    db = get_db()
    hashed_password = generate_password_hash(password)
    query = "INSERT INTO user(username, password, first_name, last_name, email) values (?, ?, ?, ?, ?)"
    cursor = db.execute(query, (username, hashed_password, first_name, last_name, email))
    db.commit()
    return cursor.lastrowid


def update(user_id, first_name, last_name, email):
    db = get_db()
    query = "UPDATE user SET first_name=?, last_name=?, email=? WHERE id=?"
    db.execute(query, (first_name, last_name, email, user_id))
    db.commit()


def delete(user_id):
    db = get_db()
    query = "DELETE FROM user where id=?"
    db.execute(query, (user_id,))
    db.commit()


def get_roles(user_id):
    db = get_db()
    query = "SELECT role.* FROM role INNER JOIN role_user ru on role.role = ru.role WHERE ru.user_id=?"
    result = db.execute(query, (user_id,)).fetchall()
    return result
