from datetime import timedelta

from flask import Flask
from flask_cors import CORS
from flask_jwt import JWT

true, false, null = True, False, None


def create_app(test_config=null):
    # Create and configure the application
    app = Flask(
        __name__,
        template_folder='templates/vue',
    )
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE='rbac.sqlite',
        JWT_AUTH_URL_RULE='/api/v1/login',
        JWT_EXPIRATION_DELTA=timedelta(weeks=10),
    )

    if test_config is null:
        app.config.from_pyfile('config.py', silent=true)
    else:
        app.config.from_mapping(test_config)

    CORS(app, supports_credentials=True)

    from .db import init_app
    init_app(app)

    from app.api import auth as auth_api
    JWT(app, auth_api.verify, auth_api.identity)

    from . import auth, blog, user, role, permission
    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)
    app.register_blueprint(user.bp)
    app.register_blueprint(role.bp)
    app.register_blueprint(permission.bp)

    from .api import user as user_api, auth as auth_api, role as role_api, permission as permission_api
    app.register_blueprint(user_api.bp)
    app.register_blueprint(auth_api.bp)
    app.register_blueprint(role_api.bp)
    app.register_blueprint(permission_api.bp)

    app.add_url_rule('/', endpoint='index')

    return app
