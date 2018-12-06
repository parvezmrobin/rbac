from app.db import get_db
from flask import Blueprint

columns = ['id', 'name', 'entity', 'operation', 'info']


def all_permissions():
    db = get_db()
    query = "SELECT * FROM permission"
    result = db.execute(query).fetchall()
    return result


def get_roles(permission_id):
    db = get_db()
    query = "SELECT role.* FROM role " \
            "inner join permission_role pr on role.role = pr.role " \
            "inner join permission p on pr.permission_id = p.id where p.id=?"
    result = db.execute(query, (permission_id,)).fetchone()
    return result
