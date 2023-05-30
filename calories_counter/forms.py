from django import forms
from .models import Food, Meal


class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = "__all__"


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ["meal", "name", "calories", "protein", "fat", "carbs"]
        labels = {
            "meal": "Meal",
            "name": "Name",
            "calories": "Calories",
            "protein": "Protein",
            "fat": "Fat",
            "carbs": "Carbs",
        }


class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = "__all__"
        labels = {
            "meal_name": "Meal Name",
            "foods": "Foods",
            "quantity": "Quantity",
        }


# class MealFoodForm(forms.ModelForm):
#     class Meta:
#         model = MealFood
#         fields = ["meal", "food", "quantity"]
#         labels = {
#             "meal": "Meal",
#             "food": "Food",
#             "quantity": "Quantity",
#         }
#
#
# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ["user", "meals"]
#         labels = {
#             "user": "User",
#             "meals": "Meals",
#         }
