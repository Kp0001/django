from django.db import models


# Create your models here.
class Employee(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    username = models.TextField(max_length=100, unique=True)
    sin = models.CharField(max_length=15)
    phone = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
