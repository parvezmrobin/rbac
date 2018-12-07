from flask import Blueprint, jsonify, request

from app.models.role import columns as role_columns
from models.permission import index as index_permission, columns, get_roles, create as create_permission

bp = Blueprint('api.permission', __name__, url_prefix='/api/permission')


@bp.route('/all', methods=["GET"])
def index():
    rows = index_permission()
    results = []
    for row in rows:
        results.append(dict(zip(columns, row)))
    return jsonify(results), 200


@bp.route("/roles", methods=["GET"])
def get_users():
    permission = request.args.get('permission')
    roles = get_roles(permission)
    result = []
    for role in roles:
        result.append(dict(zip(role_columns, role)))
    return jsonify(result), 200


@bp.route('/create', methods=["POST"])
def create():
    data = request.get_json()
    name = data['name']
    entity = data['entity']
    operation = data['operation']
    # TODO: Validate

    permission_id = create_permission(name, entity, operation)
    response = {'permission_id': permission_id}
    return jsonify(response), 201