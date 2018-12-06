from flask import Blueprint, jsonify, request

from app.models.role import all_roles, columns
from app.models.user import columns as user_columns

bp = Blueprint('api.role', __name__, url_prefix='/api/role')


@bp.route('/all', methods=["GET"])
def index():
    rows = all_roles()
    results = []
    for row in rows:
        results.append(dict(zip(columns, row)))
    return jsonify(results), 200


@bp.route("/users", methods=["GET"])
def get_users():
    role = request.args.get('role')
    users = get_users(role)
    result = []
    for user in users:
        result.append(dict(zip(user_columns, user)))
    return jsonify(result), 200
