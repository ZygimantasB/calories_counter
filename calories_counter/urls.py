from django.urls import path
from . import views

urlpatterns = [
    path("", views.start_page, name="start_page"),
    path("food/", views.FoodView.as_view(), name="foods"),
    path("food/create/", views.FoodCreate.as_view(), name="food_create"),
]
