from flask.views import MethodView
from flask import make_response
from .. import db
import json


class PostAllView(MethodView):
    def get(self):
        connection = db.get_db()
        cursor = connection.cursor()
        cursor.execute(
            "SELECT title, content, users.email FROM blogs, users;"
        )

        """
        cursor.execute(
            "INSERT INTO blogs VALUES (%s, %s, %s, %s)",
            (2, "user1-title2", "user1-content2", 1)
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
        connection = db.get_db()
        cursor = connection.cursor()
        cursor.execute(
            "DELETE FROM blogs;"
        )
        connection.commit()
        data = {'Success': 'Deleted all posts successfully'}
        response = make_response(data, 200)
        return response


class PostUserView(MethodView):
    def get(self):
        # Lists all the posts of the user
        pass

    def post(self):
        # Create a post under the user
        pass

    def delete(self):
        # Delete all the user posts
        pass


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
