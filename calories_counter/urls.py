from django.urls import path
from . import views

urlpatterns = [
    path("", views.start_page, name="start_page"),
    path("foods/", views.FoodsView.as_view(), name="foods"),
    path('food/update/<int:pk>', views.FoodUpdate.as_view(), name='food_update'),
    path('food/delete/<int:pk>', views.FoodDelete.as_view(), name='food_delete'),
    path("food/create/", views.FoodCreate.as_view(), name="food_create"),

    path("user_information/", views.UserInformationView.as_view(), name="user_information"),
    path("user_information/enter_information/", views.UserInformationCreate.as_view(), name="create_user_information"),
    path("user_information/update_information/", views.UserInformationUpdate.as_view(), name="update_user_information"),

    path("user_information/enter_body_volumes/", views.CreateBodyVolumes.as_view(), name="create_body_volumes"),

    # path("user_information/body_volumes/", views.BodyVolumes.as_view(), name="body_volumes"),
]
