from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class UserRegistrationForm(UserCreationForm):
    class Meta:
        phone_number = forms.CharField()
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)