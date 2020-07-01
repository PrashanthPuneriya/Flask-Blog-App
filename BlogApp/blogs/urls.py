from flask import Blueprint

from .views import (
    PostAllView,
    PostDetailView,
    PostUserView,
)

blogs = Blueprint(
    'blogs',
    __name__,
    url_prefix='/'
)

blogs.add_url_rule('<int:post_id>/', view_func=PostDetailView.as_view('post-detail'))
blogs.add_url_rule('all-posts/', view_func=PostAllView.as_view('post-all'))
blogs.add_url_rule('user-posts/', view_func=PostUserView.as_view('post-user'))