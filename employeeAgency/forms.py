from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    sin = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ('username', 'email', 'sin','phone', 'password1', 'password2')





