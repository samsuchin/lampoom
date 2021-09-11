from account import ACCOUNT
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    graduation_year = models.CharField(max_length=50)
    display_name = models.CharField(max_length=200)

    board = models.CharField(choices=ACCOUNT.BOARD_CHOICES, max_length=20)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'display_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
