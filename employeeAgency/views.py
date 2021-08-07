import numpy
import scipy
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from scipy import stats

# Views
from .models import Company
from .utils import get_plot


@login_required
def profile(request):
    return render(request, "registration/success.html", {})


# Function to render register page
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


# Function to render about page
def about(request):
    return render(request, 'registration/about.html', {})


# Function to tender contact page
def contact(request):
    return render(request, 'registration/contact.html', {})


# Function to render home page
def home(request):
    return render(request, 'registration/home.html', {})


# Function to render stat page
def stat(request, stats=None):
    qs = Company.objects.all()
    x = [x.name for x in qs]
    y = [y.pay for y in qs]

    chart = get_plot(x, y)
    m3 = numpy.mean(y)
    x1 = numpy.median(y)
    x2 = scipy.stats.mode(y)

    x3 = numpy.std(y)
    return render(request, "registration/stat.html", {'chart': chart, 'avgPay': m3, 'median': x1, 'mode': x2,  'std': x3})


# Function to render jobs page
@login_required
def employer(request):
    company = Company.objects.all()
    message_name = request.user.username
    message_email = request.user.email
    message = 'Hello, my name is ' + message_name + ' my registered email is ' + message_email + ' and i want to work at  ' + request.POST.get(
        "name", "") + ' in ' + request.POST.get("job", "")
    print(request.POST)
    if request.method == 'POST':
        send_mail(message_name, message, message_email, ['kpsingh@yopmail.com'])
        return render(request, 'registration/employer.html', {'company': company, 'message_name': message_name})
    else:
        return render(request, 'registration/employer.html', {'company': company})
