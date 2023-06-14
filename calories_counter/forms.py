from django import forms
from .models import Food


class FoodForm(forms.ModelForm):
    date = forms.DateField(
        input_formats=['%Y-%m-%d'],
        widget=forms.DateInput(format='%Y-%m-%d')
    )

    class Meta:
        model = Food
        fields = ['then_eaten', 'food_name', 'calories', 'protein', 'fat', 'carbs', 'weight_measure', 'date']


