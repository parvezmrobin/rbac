from flask import Blueprint, render_template

from app.models.user import all_users

bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/', methods=["GET"])
def index():
    users = all_users()
    return render_template('user.html', users=users)
