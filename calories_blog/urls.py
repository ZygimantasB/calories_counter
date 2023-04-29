from django.urls import path
from . import views

urlpatterns = [
    path("calories_blog/", views.start_page, name="start_page"),
    path("calories_blog/posts/", views.posts, name="posts"),
    path("calories_blog/posts/<slug:slug>/", views.single_post, name="single_post"),
    ]
