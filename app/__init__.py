from flask import Flask

true, false, null = True, False, None


def create_app(test_config=null):
    # Create and configure the application
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE='rbac.sqlite'
    )

    if test_config is null:
        app.config.from_pyfile('config.py', silent=true)
    else:
        app.config.from_mapping(test_config)

    from .db import init_app
    init_app(app)

    from . import auth, blog
    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app
