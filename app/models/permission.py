from app.db import get_db
from flask import Blueprint

columns = ['id', 'name', 'entity', 'operation', 'info']


def index():
    db = get_db()
    query = "SELECT * FROM permission"
    result = db.execute(query).fetchall()
    return result


def create(name, entity, operation):
    db = get_db()
    query = "INSERT INTO permission(name, entity, operation) values (?, ?, ?)"
    result = db.execute(query, (name, entity, operation, ))
    db.commit()
    return result.lastrowid


def edit(permission_id, name, entity, operation):
    db = get_db()
    query = "UPDATE permission SET name=?, entity=?, operation=? WHERE id=?"
    result = db.execute(query, (name, entity, operation, permission_id))
    db.commit()


def delete(permission_id):
    db = get_db()
    query = "DELETE FROM permission WHERE id=?"
    result = db.execute(query, (permission_id, ))
    db.commit()


def get_roles(permission_id):
    db = get_db()
    query = "SELECT role.* FROM role " \
            "inner join permission_role pr on role.role = pr.role " \
            "inner join permission p on pr.permission_id = p.id where p.id=?"
    result = db.execute(query, (permission_id,)).fetchone()
    return result
