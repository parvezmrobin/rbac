from app.db import get_db
from flask import Blueprint

bp = Blueprint('model.role', __name__)

columns = ['role']


def index():
    db = get_db()
    query = "SELECT role FROM role"
    result = db.execute(query).fetchall()
    return result


def create(role):
    db = get_db()
    query = "INSERT INTO role(role) values (?)"
    db.execute(query, (role,))
    db.commit()


def update(old_role, new_role):
    db = get_db()
    query = "UPDATE role SET role=? WHERE role=?"
    db.execute(query, (new_role, old_role, ))
    db.commit()


def delete(role):
    db = get_db()
    query = "DELETE FROM role where role=?"
    db.execute(query, (role, ))
    db.commit()


def get_users(role):
    db = get_db()
    query = "SELECT user.id, first_name, last_name, email, username FROM role " \
            "inner join role_user on role.role = role_user.role " \
            "inner join user on role_user.user_id = user.id where role.role=?"
    result = db.execute(query, (role,)).fetchone()
    return result


def get_permissions(role):
    db = get_db()
    query = "SELECT permission.* FROM permission " \
            "INNER JOIN permission_role pr on permission.id = pr.permission_id " \
            "INNER JOIN role r on pr.role = r.role " \
            "WHERE r.role=?"
    result = db.execute(query, (role, )).fetchall()
    return result


def add_permission(role, permission_id):
    db = get_db()
    query = "INSERT INTO permission_role(role, permission_id) VALUES (?, ?)"
    db.execute(query, (role, permission_id))
    db.commit()


def remove_permission(role, permission_id):
    db = get_db()
    query = "DELETE FROM permission_role WHERE role=? AND permission_id=?"
    db.execute(query, (role, permission_id, ))
    db.commit()