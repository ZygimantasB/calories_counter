from django.urls import path
from . import views

urlpatterns = [
    path("", views.start_page, name="start_page"),
    path("foods/", views.FoodsView.as_view(), name="foods"),
    path('food/update/<int:pk>', views.FoodUpdate.as_view(), name='food_update'),
    path('food/delete/<int:pk>', views.FoodDelete.as_view(), name='food_delete'),
    path("food/create/", views.FoodCreate.as_view(), name="food_create"),

    path("user_information/", views.UserInformationView.as_view(), name="user_information"),
    path("user_information/enter_information", views.UserInformationCreate.as_view(), name="create_user_information"),


    # path("food/", views.FoodView.as_view(), name="foods"),
    # path('food/update/<int:pk>', views.FoodUpdate.as_view(), name='food_update'),
    # path('food/delete/<int:pk>', views.FoodDelete.as_view(), name='food_delete'),
    # path("food/create/", views.FoodCreate.as_view(), name="food_create"),
    # path("meal_food/", views.MealFoodView.as_view(), name="meal_food"),
    # path("meal_food/create/", views.MealFoodCreate.as_view(), name="meal_food_create"),
    # path("meal_food/update/<int:pk>", views.MealFoodUpdate.as_view(), name="meal_food_update"),
    # path("meal_food/delete/<int:pk>", views.MealFoodDelete.as_view(), name="meal_food_delete"),
    # path("meal/create/", views.MealCreate.as_view(), name="meal_create"),
    # path("meal/", views.MealView.as_view(), name="meals"),
    # path("meal/update/<int:pk>", views.MealUpdate.as_view(), name="meal_update"),
    # path("meal/delete/<int:pk>", views.MealDelete.as_view(), name="meal_delete"),
    # path("users_calories/", views.UserProfileView.as_view(), name="users_calories"),
]
