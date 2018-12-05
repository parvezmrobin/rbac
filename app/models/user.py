from app.db import get_db
from flask import Blueprint

bp = Blueprint('model.user', __name__)


def all_users():
    db = get_db()
    query = "SELECT * FROM user"
    result = db.execute(query).fetchall()
    return result


def get_user(user_id):
    db = get_db()
    query = "SELECT * FROM user where id=?"
    result = db.execute(query, (user_id,)).fetchone()
    return result
