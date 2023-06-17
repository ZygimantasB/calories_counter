from django import forms

from CONSTATNS.gender import GENDER
from CONSTATNS.activity_level import ACTIVITY


class BMIForm(forms.Form):
    weight = forms.FloatField(label='Weight in kg')
    height = forms.FloatField(label="Height in cm")

    class Meta:
        fields = ['weight', 'height']
        labels = {'weight': 'Weight in kg', 'height': 'Height in cm'}


class WaitHipRatioForm(forms.Form):
    waist = forms.FloatField(label='Waist in cm')
    hip = forms.FloatField(label="Hip in cm")
    gender = forms.ChoiceField(choices=GENDER, widget=forms.RadioSelect, label='Gender')


class DailyCaloriesForm(forms.Form):
    weight_kg = forms.FloatField(label='Weight in kg')
    height_cm = forms.FloatField(label="Height in cm")
    age = forms.IntegerField(label='Age')
    gender = forms.ChoiceField(choices=GENDER, widget=forms.RadioSelect, label='Gender')
    activity_level = forms.ChoiceField(choices=ACTIVITY, widget=forms.RadioSelect, label='Activity Level')
