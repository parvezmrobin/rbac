from flask import Blueprint, request, jsonify
from flask_jwt import jwt_required, current_identity
from werkzeug.security import check_password_hash

from app.models.user import where_first, create, read, columns

bp = Blueprint('api.v1.auth', __name__, url_prefix="/api/v1/auth")


class UserPayload:
    def __init__(self, user):
        self.id = user['id']


def verify(username, password):
    if not (username and password):
        return None
    user = where_first(username=username)
    if check_password_hash(user['password'], password):
        return UserPayload(user)


def identity(payload):
    user_id = payload['identity']
    return {'user_id': user_id}


@bp.route("/user", methods=["GET"])
@jwt_required()
def user():
    user_id = current_identity['user_id']
    user = read(user_id)
    response = dict(zip(columns, user))
    return jsonify(response)


@bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    errors = {}

    if not (('first_name' in data) and data['first_name']):
        errors['first_name'] = 'First name is required.'
    if not (('last_name' in data) and data['last_name']):
        errors['last_name'] = 'Last name is required.'
    if not (('email' in data) and data['email']):
        errors['email'] = 'Email is required.'
    if not (('username' in data) and data['username']):
        errors['username'] = 'Username is required.'
    if not (('password' in data) and data['password']):
        errors['password'] = 'Password is required.'
    if not (('confirm_password' in data) and data['confirm_password']):
        errors['confirm_password'] = 'Confirm password is required.'
    elif 'password' in data and data['password'] and data['password'] != data['confirm_password']:
        errors['confirm_password'] = "Confirm password doesn't match."
    if not errors:
        username_match = where_first(username=data['username'])
        email_match = where_first(email=data['email'])
        if username_match:
            errors['username'] = f"Username {data['username']} is already taken."
        if email_match:
            errors['email'] = f"Email {data['email']} is already taken."

    if not errors:
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        username = data['username']
        password = data['password']
        user_id = create(username, password, first_name, last_name, email)

        response = {'user_id': user_id}
        return jsonify(response), 201

    return jsonify(errors), 400
