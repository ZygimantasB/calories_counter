from django import forms
from .models import Food


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['then_eaten', 'food_name', 'calories', 'protein', 'fat', 'carbs', 'weight_measure', 'date']

