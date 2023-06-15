from django import forms
from .models import Food

from datetime import date
from CONSTATNS.meal import THEN_EATEN


class FoodForm(forms.ModelForm):
    then_eaten = forms.ChoiceField(choices=THEN_EATEN)
    date = forms.DateField(
        input_formats=['%Y-%m-%d'],
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'value': date.today()})
    )

    class Meta:
        model = Food
        fields = ['then_eaten', 'food_name', 'calories', 'protein', 'fat', 'carbs', 'weight_measure', 'date']


class UpdateWeightForm(forms.Form):
    new_weight = forms.DecimalField(max_digits=5, decimal_places=2)
