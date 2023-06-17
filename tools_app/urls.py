from django.urls import path
from .views import CalculateBMI, CalculateWaistHipRatio, CalculateDailyCalories

urlpatterns = [
    path("tool/calculate_bmi/", CalculateBMI.as_view(), name="calculate_bmi"),
    path("tool/calculate_waist_hip_ratio/", CalculateWaistHipRatio.as_view(), name="calculate_waist_hip_ratio"),
    path("tool/calculate_daily_calories/", CalculateDailyCalories.as_view(), name="calculate_daily_calories"),
]
