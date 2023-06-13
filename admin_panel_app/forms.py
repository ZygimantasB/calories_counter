from django import forms


class UploadFoodInformationForm(forms.Form):
    file = forms.FileField()
