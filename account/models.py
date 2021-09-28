from account import ACCOUNT
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from .managers import CustomUserManager
from django.utils.safestring import mark_safe

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    url_username = models.CharField(max_length=200, unique=True, help_text="harvardlampoon/@<YOUR_URL_USERNAME>/")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    graduation_year = models.CharField(max_length=50)
    display_name = models.CharField(max_length=200)
    bio = models.TextField(max_length=5000, null=True, blank=True)

    profile_picture = models.ImageField(upload_to="profiles/", null=True, blank=True)

    board = models.CharField(choices=ACCOUNT.BOARD_CHOICES, max_length=20)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'display_name', 'url_username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def profile_picture_preview(self):
        if self.profile_picture:
            return mark_safe(u"<a href='{}'><img height='300' style='border-radius: 50%;' src='{}'/></a>".format(self.profile_picture.url, self.profile_picture.url))
        else:
            return 'No Image'
    profile_picture_preview.short_description = 'Image'

    def get_name(self):
        return f"{self.first_name} {self.last_name}"
