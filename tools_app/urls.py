from django.urls import path
from . import views

urlpatterns = [
    path("tool/calculate_bmi/", views.CalculateBMI.as_view(), name="calculate_bmi"),
    path("tool/calculate_waist_hip_ratio/", views.CalculateWaistHipRatio.as_view(), name="calculate_waist_hip_ratio"),
    path("tool/calculate_daily_calories/", views.CalculateDailyCalories.as_view(), name="calculate_daily_calories"),
    path("tool/calculate_burned_calories/", views.CalculateBurnedCalories.as_view(), name="calculate_burned_calories"),
]
