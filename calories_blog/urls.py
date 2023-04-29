from django.urls import path
from . import views

urlpatterns = [
    path("calories_blog/", views.start_page_cal, name="start_page_cal"),
    path("calories_blog/posts/", views.posts, name="posts"),
    path("calories_blog/posts/<slug:slug>/", views.post_detail, name="post-detail-page"),
    ]
