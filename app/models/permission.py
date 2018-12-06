from app.db import get_db
from flask import Blueprint

columns = ['permission']


def all_permissions():
    db = get_db()
    query = "SELECT permission FROM permission"
    result = db.execute(query).fetchall()
    return result


def get_roles(permission):
    db = get_db()
    query = "SELECT role.* FROM role " \
            "inner join role_permission rp on role.role = rp.role " \
            "inner join permission p on rp.permission = p.permission where p.permission=?"
    result = db.execute(query, (permission,)).fetchone()
    return result
