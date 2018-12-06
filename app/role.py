from flask import Blueprint, render_template

bp = Blueprint('role', __name__, url_prefix='/role')


@bp.route('/', methods=["GET"])
def index():
    return render_template('role.html')
