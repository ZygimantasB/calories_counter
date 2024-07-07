from django import forms


class UploadFoodInformationForm(forms.Form):
    """
    This class is responsible for uploading food information.
    """
    file = forms.FileField()


class UploadQuotesForm(forms.Form):
    """
    This class is responsible for uploading quotes.
    """
    file = forms.FileField()
