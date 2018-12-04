import sqlite3

import click
from flask import g, current_app
from flask.cli import with_appcontext

true, false, null = True, False, None


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=null):
    db = g.pop('db', null)

    if db is not null:
        db.close()


def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as schema:
        db.executescript(schema.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """
    Clears existing data and create new tables
    :return: None
    """
    init_db()
    click.echo("Initialized the database")


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
