from django import forms
from .models import Food, BodyCircumferenceMeasurements

from datetime import date
from CONSTATNS.meal import THEN_EATEN


class FoodForm(forms.ModelForm):
    """
    Form for adding food to database
    """
    then_eaten = forms.ChoiceField(choices=THEN_EATEN)
    date = forms.DateField(
        input_formats=['%Y-%m-%d'],
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'value': date.today()})
    )

    class Meta:
        model = Food
        fields = ['then_eaten', 'food_name', 'calories', 'protein', 'fat', 'carbs', 'weight_measure', 'date']


class UpdateWeightForm(forms.Form):
    """
    Form for updating weight
    """
    new_weight = forms.DecimalField(max_digits=5, decimal_places=2)


class BodyCircumferenceMeasurementsForm(forms.ModelForm):
    """
    Form for adding body circumference measurements
    """
    class Meta:
        model = BodyCircumferenceMeasurements
        fields = ['neck_size', 'chest_size', 'waist_size', 'left_bicep_size', 'right_bicep_size', 'left_forearm_size',
                  'right_forearm_size', 'left_thigh_size', 'right_thigh_size', 'left_calf_size', 'right_calf_size']
        labels = {
            'neck_size': 'Neck size',
            'chest_size': 'Chest size',
            'waist_size': 'Waist size',
            'left_bicep_size': 'Left bicep size',
            'right_bicep_size': 'Right bicep size',
            'left_forearm_size': 'Left forearm size',
            'right_forearm_size': 'Right forearm size',
            'left_thigh_size': 'Left thigh size',
            'right_thigh_size': 'Right thigh size',
            'left_calf_size': 'Left calf size',
            'right_calf_size': 'Right calf size',
        }
