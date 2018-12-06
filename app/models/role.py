from app.db import get_db
from flask import Blueprint

bp = Blueprint('model.role', __name__)

columns = ['role']


def all_roles():
    db = get_db()
    query = "SELECT role FROM role"
    result = db.execute(query).fetchall()
    return result


def get_users(role):
    db = get_db()
    query = "SELECT user.id, first_name, last_name, email, username FROM role " \
            "inner join role_user on role.role = role_user.role " \
            "inner join user on role_user.user_id = user.id where role.role=?"
    result = db.execute(query, (role,)).fetchone()
    return result
