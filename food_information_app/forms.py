from django import forms


class ProductSearch(forms.Form):
    name_search = forms.CharField(max_length=255, required=False, label="Search for a product")
