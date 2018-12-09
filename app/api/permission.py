from flask import Blueprint, jsonify, request
from flask_jwt import jwt_required

from app.api.validation import required
from app.models.role import columns as role_columns
from models.permission import index as index_permission, columns, get_roles
from models.permission import create as create_permission, edit as edit_permission, delete as delete_permission

bp = Blueprint('api.v1.permission', __name__, url_prefix='/api/v1/permission')

entities = ('user', 'role', 'permission')
operations = ('index', 'create', 'read', 'update', 'delete')


@bp.route('/all', methods=["GET"])
@jwt_required()
def index():
    rows = index_permission()
    results = []
    for row in rows:
        results.append(dict(zip(columns, row)))
    return jsonify(results), 200


@bp.route("/roles", methods=["GET"])
@jwt_required()
def get_users():
    permission = request.args.get('permission')
    roles = get_roles(permission)
    result = []
    for role in roles:
        result.append(dict(zip(role_columns, role)))
    return jsonify(result), 200


@bp.route('/create', methods=["POST"])
@jwt_required()
def create():
    data = request.get_json()
    errors = _validate(data)

    if errors:
        return jsonify(errors), 400

    name = data['name']
    entity = data['entity']
    operation = data['operation']

    permission_id = create_permission(name, entity, operation)
    response = {'permission_id': permission_id}
    return jsonify(response), 201


def _validate(data):
    errors = required(['name', 'entity', 'operation'], data)
    if 'entity' not in errors and data['entity'] not in entities:
        errors['entity'] = 'Entity is invalid.'
    if 'operation' not in errors and data['operation'] not in operations:
        errors['operation'] = 'Operation is invalid.'
    return errors


@bp.route('/<int:permission_id>', methods=["PUT"])
@jwt_required()
def update(permission_id):
    data = request.get_json()
    errors = _validate(data)

    if errors:
        return jsonify(errors), 400

    name = data['name']
    entity = data['entity']
    operation = data['operation']

    edit_permission(permission_id, name, entity, operation)
    response = {'message': 'updated'}
    return jsonify(response), 202


@bp.route('/<int:permission_id>', methods=["DELETE"])
@jwt_required()
def delete(permission_id):
    delete_permission(permission_id)
    response = {'message': 'deleted'}
    return jsonify(response), 202
