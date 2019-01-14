from flask import Blueprint, jsonify
from flask_jwt import jwt_required, current_identity
from werkzeug.security import check_password_hash

from api.user import create as create_user
from app.models.user import where_first, read, columns

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
    return create_user()
