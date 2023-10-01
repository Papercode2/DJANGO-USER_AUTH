from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser  # Import the CustomUser model from models.py

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text="Required. Enter a valid email address.")
    phone = forms.CharField(max_length=15, required=False, help_text="Optional. Enter your phone number.")

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
