from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail

# Views
from .models import Company


@login_required
def home(request):
    return render(request, "registration/success.html", {})


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            sin = form.cleaned_data.get('sin')
            email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})


def about(request):
    return render(request, 'registration/about.html', {})


def contact(request):
    return render(request, 'registration/contact.html', {})


@login_required
def employer(request):
    company = Company.objects.all()
    message_name = request.user.username
    message_email = request.user.email
    message = 'Hello, my name is ' + message_name +' my registred email is ' + message_email + ' and i want to work in  ' + request.POST.get("name", "") + ' in ' + request.POST.get("job", "")
    print(request.POST)
    if request.method == 'POST':
        send_mail(message_name, message, message_email, ['kpsingh@yopmail.com'])
        return render(request, 'registration/employer.html', {'company': company, 'message_name': message_name})
    else:
        return render(request, 'registration/employer.html', {'company': company})
