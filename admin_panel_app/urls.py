from django.urls import path
from . import views

urlpatterns = [
    path("upload_food_information/", views.UploadInformationView.as_view(), name="upload_information"),
    ]
