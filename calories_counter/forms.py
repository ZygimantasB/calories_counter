from django import forms
from .models import Food, Meal, MealFood, UserProfile


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ["User", "food_name", "calories"]
        labels = {
            "user": "User",
            "food_name": "Food Name",
            "calories": "Calories",
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


class MealFoodForm(forms.ModelForm):
    class Meta:
        model = MealFood
        fields = ["meal", "food", "quantity"]
        labels = {
            "meal": "Meal",
            "food": "Food",
            "quantity": "Quantity",
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["user", "meals"]
        labels = {
            "user": "User",
            "meals": "Meals",
        }
