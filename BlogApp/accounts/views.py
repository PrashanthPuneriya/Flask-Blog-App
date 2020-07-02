from flask import make_response, request, redirect, url_for, session
from flask.views import MethodView
from werkzeug.security import generate_password_hash, check_password_hash
from .. import db


def login_required(f):
    def wrapped_view(self, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('accounts.login'))

        # check the session data here then only return the f()
        return f(self, **kwargs)

    return wrapped_view


class RegisterView(MethodView):
    def get(self):
        return "Register by providing details"

    def post(self):
        data = request.json
        email = data['email']
        first_name = data['first_name']
        last_name = data['last_name']
        password = data['password']
        # have to sanitize the data and do all the other stuff

        connection = db.get_db()
        cursor = connection.cursor()

        if email == "" or first_name == "" or password == "":
            return ({'Error': 'Something is wrong with your data'})

        cursor.execute(
            "select id from users where email = %s;",
            (email, )
        )
        user = cursor.fetchone()

        if user is not None:
            return ({'Error': 'Email is already used by someone'})

        cursor.execute(
            "insert into users (first_name, last_name, email, password) values (%s, %s, %s, %s);",
            (first_name, last_name, email, generate_password_hash(password))
        )
        connection.commit()

        return ({"Success": "Registered successfully"})


class LoginView(MethodView):
    def get(self):
        return "Login by providing details"

    def post(self):
        data = request.json
        email = data['email']
        password = data['password']
        # have to sanitize the data
        error = None

        connection = db.get_db()
        cursor = connection.cursor()

        cursor.execute("select * from users where email=%s;", (email, ))
        user = cursor.fetchone()

        if user is None:
            error = 'Incorrect email address'
        elif not check_password_hash(user[4], password):
            error = 'Incorrect password'

        if error is None:
            session.clear()
            session['user_id'] = user[0]
            return ({"Success": "Logged in successfully"})

        else:
            return ({"Error": error})


def logoutView():
    session.clear()
    return ({"Success": "Logged out successfully"})
