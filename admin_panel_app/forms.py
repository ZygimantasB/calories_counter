from django import forms


class UploadFoodInformationForm(forms.Form):
    file = forms.FileField()


class UploadQuotesForm(forms.Form):
    file = forms.FileField()
