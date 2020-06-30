from flask.views import MethodView
# from 

class PostAllView(MethodView):
    def get(self):
        
        pass

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
