from flask import Blueprint, render_template

bp = Blueprint('permission', __name__, url_prefix='/permission')


@bp.route('/', methods=["GET"])
def index():
    return render_template('permission.html')
