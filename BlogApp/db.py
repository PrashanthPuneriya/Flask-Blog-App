import psycopg2
import click

from flask import current_app, g
from flask.cli import with_appcontext

from .settings import DB_HOST, DB_NAME, DB_USERNAME, DB_PASSWORD


"""
Database:-
 - Connects to the db
 - Closes the db connection
 - Initializes the db table through schema.sql script file
"""


def get_db():
    # During a request, every call to get_db() will return the same connection
    if 'db' not in g:
        # if the db is not connected during this app context then connect
        g.db = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USERNAME,
            password=DB_PASSWORD,
        )
    return g.db


def close_db(err=None):
    # Remove the db connection from the global object(g) of this app context if it exists
    conn = g.pop('db', None)
    # If a connection to the db in this context exists then disconnect
    if conn is not None:
        conn.close()


def init_db():
    conn = get_db()
    cur = conn.cursor()

    with current_app.open_resource('schema.sql') as f:
        cur.execute(f.read().decode('utf8'))
    conn.commit()
    cur.close()


"""
 - Adds init-db command to the shell
 - Registers the init_db_command and close_db methods with the app instance
"""


# The below two decorators are similar to the flask's app cli decorator ==> @appname.cli.command('init-db')
@click.command('init-db')
@with_appcontext
def init_db_command():
    """
    @with_appcontext is required because:-
        We never told Flask what application(since, flask can have multiple apps) it should deal with
        when running init_db() method.

        Hence, we need to push the app context to it.
    """

    init_db()
    click.echo('Initialized the database!!!')


def init_app(app):

    # Registers the cli command with the flask app
    app.cli.add_command(init_db_command)

    # It tells Flask to call that close_db() when cleaning up after returning the response.
    # close_db() will be called only when the application context is popped.
    app.teardown_appcontext(close_db)
