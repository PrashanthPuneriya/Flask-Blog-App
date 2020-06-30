from flask.views import MethodView
from flask import make_response, jsonify
from .. import db
from flask import json


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
            print(posts) # list of tuples

            for col in cursor.description:
                print(col[0]) # Column names   
        """

        rows = cursor.fetchall()
        column_names = [col[0] for col in cursor.description]
        # posts = [dict(zip(column_names, row)) for row in rows]
        posts = []
        for row in rows:
            obj = dict(zip(column_names, row))
            posts.append(obj)

        print(type(posts))

        response = make_response(jsonify(posts), 200)
        # response = response_class(
        #     response=json.dumps(posts),
        #     status=200,
        #     mimetype='application/json'
        # )

        return response

    def delete(self):
        # Delete all the posts
        pass


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
