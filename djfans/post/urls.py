from django.urls import path
from post.views import NewPost

urlpatterns = [
    path('newpost/', NewPost, name='newpost'),
]
