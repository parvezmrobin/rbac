from flask import Blueprint, jsonify, request
from flask_jwt import jwt_required

from api.validation import required
from app.models import role as role_model
from app.models.user import columns as user_columns
from app.models.permission import columns as permission_columns

bp = Blueprint('api.v1.role', __name__, url_prefix='/api/v1/role')


@bp.route('/all', methods=["GET"])
@jwt_required()
def index():
    rows = role_model.index()
    results = []
    for row in rows:
        results.append(dict(zip(role_model.columns, row)))
    return jsonify(results), 200


@bp.route("/<string:role>/users", methods=["GET"])
@jwt_required()
def get_users(role):
    users = role_model.get_users(role)
    result = []
    for user in users:
        result.append(dict(zip(user_columns, user)))
    return jsonify(result), 200


@bp.route("<string:role>/users/add", methods=["POST"])
@jwt_required()
def add_user(role):
    data = request.get_json()
    errors = required(['user_id'], data)
    # TODO: already exists check
    if errors:
        return jsonify(errors), 400
    role_model.add_user(role, data['user_id'])
    response = {'message': 'added'}
    return jsonify(response), 201


# TODO: implement bulk user add


@bp.route("/<string:role>/permissions", methods=["GET"])
@jwt_required()
def get_permissions(role):
    permissions = role_model.get_permissions(role)
    result = []
    for permission in permissions:
        result.append(dict(zip(permission_columns, permission)))
    return jsonify(result), 200


@bp.route("<string:role>/permissions/add", methods=["POST"])
@jwt_required()
def add_permission(role):
    data = request.get_json()
    errors = required(['permissions_id'], data)
    # TODO: already exists check
    if errors:
        return jsonify(errors), 400
    role_model.add_permission(role, data['permissions_id'])
    response = {'message': 'added'}
    return jsonify(response), 201


# TODO: implement bulk permission add

@bp.route('create', methods=["POST"])
@jwt_required()
def create():
    data = request.get_json()
    errors = {}
    if 'role' not in data or not data['role']:
        errors['role'] = 'Role is required.'
    if errors:
        return jsonify(errors), 400
    # TODO: Check Role Existence
    role_model.create(data['role'])
    response = {'role': data['role']}
    return jsonify(response), 201
