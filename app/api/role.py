from flask import Blueprint, jsonify, request
from flask_jwt import jwt_required

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


@bp.route("/<string:role>/permissions", methods=["GET"])
@jwt_required()
def get_permissions(role):
    permissions = role_model.get_permissions(role)
    result = []
    for permission in permissions:
        result.append(dict(zip(permission_columns, permission)))
    return jsonify(result), 200
