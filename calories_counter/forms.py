from django import forms
from .models import Food, Meal


class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = "__all__"


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['food_name', 'calories', 'protein', 'fat', 'carbs', 'weight_measure']
