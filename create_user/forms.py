from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=150, widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
