from django import forms

from CONSTATNS.gender import GENDER


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
