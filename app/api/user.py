from flask import Blueprint, jsonify, request
from flask_jwt import jwt_required

from api.validation import required
from models.role import columns as role_columns
import models.user as user_model

bp = Blueprint('api.v1.user', __name__, url_prefix='/api/v1/user')


@bp.route('/', methods=["GET"])
@jwt_required()
def index():
    rows = user_model.index()
    results = []
    for row in rows:
        results.append(dict(zip(user_model.columns, row)))
    return jsonify(results), 200


@bp.route("/", methods=["POST"])
@jwt_required()
def create():
    data = request.get_json()
    fields = [
        'first_name', 'last_name', 'email', 'username', 'password', 'confirm_password',
    ]
    errors = required(fields, data)

    if not errors:
        # Checking both username and email existence
        # to minimize the number of API calls
        username_match = user_model.where_first(username=data['username'])
        email_match = user_model.where_first(email=data['email'])
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
        user_id = user_model.create(username, password, first_name, last_name, email)

        response = {'user_id': user_id}
        return jsonify(response), 201

    return jsonify(errors), 400


@bp.route("/<int:user_id>", methods=["PUT"])
@jwt_required()
def edit(user_id):
    data = request.get_json()
    fields = ['first_name', 'last_name', 'email', ]
    errors = required(fields, data)

    if not errors:
        email_matches = user_model.where(email=data['email'])
        valid_id = False
        for email_match in email_matches:
            if email_match['id'] != user_id:
                errors['email'] = f"Email {data['email']} is already taken."
            else:
                valid_id = True  # there exists an user with given user_id
        if not (valid_id or user_model.where_first(id=user_id)):
            # search for an user with user_id
            errors['id'] = f"Invalid id '{user_id}'"

    if errors:
        return jsonify(errors), 400

    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']

    user_model.update(user_id, first_name, last_name, email)

    return jsonify(message='updated'), 204


@bp.route("/<int:user_id>", methods=["DELETE"])
@jwt_required()
def remove(user_id):
    if not user_model.where_first(id=user_id):
        return jsonify(id=f"Invalid id '{user_id}'"), 400
    user_model.delete(user_id)

    return jsonify(message='removed'), 204


@bp.route("/<int:user_id>/role", methods=["GET"])
@jwt_required()
def get_roles(user_id):
    if not user_model.where_first(id=user_id):
        return jsonify(id=f"Invalid id '{user_id}'"), 400
    roles = user_model.get_roles(user_id)
    result = []
    for role in roles:
        result.append(dict(zip(role_columns, role)))
    return jsonify(result), 200
