from flask import Blueprint, jsonify, request
from flask_jwt import jwt_required

from api.validation import required
from app.models.user import index as index_users, columns

bp = Blueprint('api.v1.user', __name__, url_prefix='/api/v1/user')


@bp.route('/', methods=["GET"])
@jwt_required()
def index():
    rows = index_users()
    results = []
    for row in rows:
        results.append(dict(zip(columns, row)))
    return jsonify(results), 200


@bp.route("/", methods=["POST"])
@jwt_required()
def create():
    data = request.get_json()
    errors = required(['user'], data)
    if errors:
        return jsonify(errors), 400
    # TODO: Check already exists