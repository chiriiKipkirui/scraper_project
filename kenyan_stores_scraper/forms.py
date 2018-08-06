from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User


class RegistrationForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password =forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.CharField(widget=forms.EmailInput)

    class Meta:
        model = User
        fields = ['username', 'password','confirm_password','first_name', 'last_name', 'email']

