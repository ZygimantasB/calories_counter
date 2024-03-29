from django import forms

from CONSTATNS.gender import GENDER
from CONSTATNS.activity_level import ACTIVITY
from CONSTATNS.burned_calories import CALORIES_BURNED


class BMIForm(forms.Form):
    weight_kg = forms.FloatField(label='Weight in kg')
    height_cm = forms.FloatField(label="Height in cm")


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


class BurnedCaloriesForm(forms.Form):
    weight_kg = forms.FloatField(label='Weight in kg')
    duration_minutes = forms.IntegerField(label="Duration in min", help_text='Duration in minutes')
    activity = forms.ChoiceField(choices=CALORIES_BURNED, label='Activity Level')


class BasalMetabolicRateForm(forms.Form):
    weight_kg = forms.FloatField(label='Weight in kg')
    height_cm = forms.FloatField(label="Height in cm")
    age = forms.IntegerField(label='Age')
    gender = forms.ChoiceField(choices=GENDER, widget=forms.RadioSelect, label='Gender')


class BodyFatForm(forms.Form):
    weight_kg = forms.FloatField(label='Weight in kg')
    height_cm = forms.FloatField(label="Height in cm")
    waist_cm = forms.FloatField(label="Waist in cm")
    neck_cm = forms.FloatField(label="Neck in cm")
    hip_cm = forms.FloatField(label="Hip in cm", initial=1, required=True)
    gender = forms.ChoiceField(choices=GENDER, widget=forms.RadioSelect, label='Gender')
