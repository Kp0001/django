from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

# Set up form field for user registration
class SignUpForm(UserCreationForm):
    class Meta:
        model = Employee
        fields = ('username', 'email', 'sin', 'phone', 'password1', 'password2')


# class CompanyForm(UserCreationForm):
#     class Meta:
#         model = Company
#         fields = 'name'
