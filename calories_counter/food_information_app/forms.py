from django import forms


class ProductSearch(forms.Form):
    """
    This class is responsible for searching for a product.
    """
    name_search = forms.CharField(max_length=255, required=False, label="Search for a product")
