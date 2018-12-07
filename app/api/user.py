from flask import Blueprint, jsonify

from app.models.user import index as index_users, columns

bp = Blueprint('api.user', __name__, url_prefix='/api/user')


@bp.route('/all', methods=["GET"])
def index():
    rows = index_users()
    results = []
    for row in rows:
        results.append(dict(zip(columns, row)))
    return jsonify(results), 200