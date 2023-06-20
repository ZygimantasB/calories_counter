from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

from CONSTATNS.gender import GENDER
from CONSTATNS.activity_level import ACTIVITY
from CONSTATNS.burned_calories import CALORIES_BURNED


class BMIForm(forms.Form):
    weight_kg = forms.FloatField(label='Weight in kg')
    height_cm = forms.FloatField(label="Height in cm")

    def clean_weight_kg(self):
        weight_kg = self.cleaned_data.get('weight_kg')
        if weight_kg is not None:
            if weight_kg <= 0:
                raise forms.ValidationError("Invalid input. Please enter a positive number for weight.")
            elif weight_kg > 635:
                raise forms.ValidationError("Enter realistic number. Heaviest person in the world was "
                                            "Jon Brower Minnoch 635 kg")
        return weight_kg

    def clean_height_cm(self):
        height_cm = self.cleaned_data.get('height_cm')
        if height_cm is not None:
            if height_cm <= 0:
                raise forms.ValidationError("Invalid input. Please enter a positive number for height.")
            elif height_cm > 272:
                raise forms.ValidationError("Enter realistic number. Tallest person in the world was "
                                            "Robert Wadlow 272 cm.")
        return height_cm


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
    hip_cm = forms.FloatField(label="Hip in cm", required=False)
    gender = forms.ChoiceField(choices=GENDER, widget=forms.RadioSelect, label='Gender')
