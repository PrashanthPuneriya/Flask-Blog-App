from flask.views import MethodView
from flask import make_response, request
from .. import db
import json


class PostAllView(MethodView):
    def get(self):
        # Get all posts
        connection = db.get_db()
        cursor = connection.cursor()
        cursor.execute(
            "SELECT title, content, users.email FROM blogs, users;"
        )

        """
        cursor.execute(
            "INSERT INTO blogs (title, content, user_id) VALUES (%s, %s, %s)",
            ("user1-title2", "user1-content2", 1)
        )
        connection.commit()

        print(cursor.description) # tuple of tuples
        print(cursor.fetchall()) # list of tuples

        for col in cursor.description:
            print(col[0]) # Column names   
        """

        rows = cursor.fetchall()
        column_names = [col[0] for col in cursor.description]
        posts = [dict(zip(column_names, row)) for row in rows]

        """
        posts = []
        for row in rows:
            dict_obj = dict(zip(column_names, row))
            posts.append(dict_obj)
        """

        """
        json.dumps() serializes the data i.e. encodes the python data
        
        json.loads() deserializes the data i.e. decodes the json data or string of json formatted data into python data type
        """

        response = make_response(json.dumps(posts), 200)
        return response

    def delete(self):
        # Delete all posts
        connection = db.get_db()
        cursor = connection.cursor()
        cursor.execute(
            "DELETE FROM blogs;"
        )
        connection.commit()
        return ({'Success': 'Deleted all the user posts successfully'})


class PostUserView(MethodView):
    # User ID must be obtained via auth for the following methods. For now included a dummy user_id
    def get(self):
        # List all the posts of the user

        user = 1

        connection = db.get_db()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT title, content FROM blogs WHERE blogs.user_id = %s;", str(user)
        )

        rows = cursor.fetchall()
        print(rows)
        print(cursor.description)
        column_names = [col[0] for col in cursor.description]
        posts = [dict(zip(column_names, row)) for row in rows]

        response = make_response(json.dumps(posts), 200)
        return response

    def post(self):
        # Create a post under the user

        user = 1

        connection = db.get_db()
        cursor = connection.cursor()

        data = request.get_json()
        post_title = data['title']
        post_content = data['content']

        cursor.execute(
            "INSERT INTO blogs (title, content, user_id) VALUES (%s, %s, %s);",
            (post_title, post_content, user)
        )

        cursor.execute(
            "SELECT email FROM users WHERE id = %s;", str(user)
        )

        user_email = cursor.fetchone()

        connection.commit()

        return ({'Success': 'Post saved successfully', 'title': post_title, 'content': post_content, 'user': user_email[0]})

    def delete(self):
        # Delete all the user posts

        user = 1

        connection = db.get_db()
        cursor = connection.cursor()
        cursor.execute(
            "DELETE FROM blogs WHERE user_id = %s;", str(user)
        )
        connection.commit()
        return ({'Success': 'Deleted all the user posts successfully'})


class PostDetailView(MethodView):
    def get(self, post_id):
        # Detail view of the post
        pass

    def patch(self, post_id):
        # PATCH -> Because we are updating only certain fields of the post but not the entire entity
        pass

    def delete(self, post_id):
        # Delete a single post
        pass
