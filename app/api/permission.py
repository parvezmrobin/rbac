from flask import Blueprint, jsonify, request

from app.models.role import columns as role_columns
from models.permission import all_permissions, columns, get_roles

bp = Blueprint('api.permission', __name__, url_prefix='/api/permission')


@bp.route('/all', methods=["GET"])
def index():
    rows = all_permissions()
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
