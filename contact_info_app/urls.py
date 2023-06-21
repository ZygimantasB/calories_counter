from django.urls import path
from . import views

urlpatterns = [
    path("contact_info/", views.contact_info, name="about_project"),
]
