from django.urls import path
from . import views

urlpatterns = [
    path("upload_food_information/", views.UploadFoodInformationView.as_view(), name="upload_food_information"),
    path("count_inforamtion/", views.DetailDatabaseInformation.as_view(), name="count_information"),

    ]
