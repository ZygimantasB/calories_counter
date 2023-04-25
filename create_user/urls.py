from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path("", views.start_page, name="start_page"),
    path("login/", views.sign_in, name="login"),
    path("logout/", views.sign_out, name="logout"),
    path("register/", views.register, name="register"),
]
