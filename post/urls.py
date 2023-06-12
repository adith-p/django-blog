from django.urls import path
from . import views

app_name = "post"
urlpatterns = [
    path("", views.index, name="home"),
    path("add_post", views.add_post, name="add_post"),
    path("posts", views.posts, name="posts"),
    path("post/<int:id>", views.post_details, name="details"),
    path("edit_post/<int:id>", views.edit_post, name="edit_post"),
    path("delete_post/<int:id>", views.delete_post, name="delete_post")
]
