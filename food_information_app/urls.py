from django.urls import path
from .views import ProductInformationView

urlpatterns = [
    path("product_information", ProductInformationView.as_view(), name="product_information_food"),
]