from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, username, is_admin=False, is_staff=True,
                    is_active=True, password=None, *args, **kwargs):
        if not email:
            raise ValueError("User must have an email")

        if not username:
            raise ValueError("User must have a full name")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.username = username
        user.set_password(password)  # change password to hash
        user.admin = is_admin
        user.staff = is_staff
        user.active = is_active
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, *args, **kwargs):
        if not email:
            raise ValueError("User must have an email")

        if not username:
            raise ValueError("User must have a full name")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.username = username
        user.set_password(password)
        user.admin = True
        user.staff = True
        user.is_superuser = True
        user.active = True
        user.save(using=self._db)
        return user


#         return self.get(email_)


# Create your models here.
class Employee(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True, primary_key=True)
    username = models.TextField(max_length=100, unique=True)
    sin = models.CharField(max_length=15)
    phone = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'username'
    is_anonymous = False
    default = ''
    is_authenticated = True

    def __str__(self):
        return self.username + ' ---- ' + self.email


class Company(models.Model):
    name = models.CharField(max_length=50)
    jobName = models.CharField(max_length=200)
    pay = models.FloatField()
    maxNeeded = models.IntegerField()

    def __str__(self):
        return '{} {}'.format(self.name, self.jobName)


class Request(models.Model):
    name = models.ForeignKey(Company, blank=True, null=True, on_delete=models.CASCADE)

    username = models.OneToOneField(Employee, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.name, self.username)
