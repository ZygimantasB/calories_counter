from django.urls import path
from .views import CalculateBMI, CalculateWaistHipRatio

urlpatterns = [
    path("tool/calculate_bmi/", CalculateBMI.as_view(), name="calculate_bmi"),
    path("tool/calculate_waist_hip_ratio/", CalculateWaistHipRatio.as_view(), name="calculate_waist_hip_ratio"),
]
