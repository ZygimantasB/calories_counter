from django.urls import path
from . import views

urlpatterns = [
    path("calories_blog/", views.StartingPageView.as_view(), name="start_page_cal"),
    path("calories_blog/posts/", views.AllPostsView.as_view(), name="posts"),
    path("calories_blog/posts/<slug:slug>/", views.SinglePostView.as_view(), name="post-detail-page"),
    ]
