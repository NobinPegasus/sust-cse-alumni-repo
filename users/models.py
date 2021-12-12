from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db import models
# from django.contrib.auth.models import User
from PIL import Image


from .managers import CustomUserManager

from django.contrib import admin




#
# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     name = models.CharField(max_length=200)
#     email = models.EmailField(_('email address'), unique=True)
#     registration = models.IntegerField(_('registration'),blank=True,unique=True)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     date_joined = models.DateTimeField(default=timezone.now)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['registration']
#
#     objects = CustomUserManager()
#
#     def __str__(self):
#         return self.email

from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class CustomUser(AbstractUser):
    username = None
    first_name = models.CharField('Name',max_length=200,unique=True)
    email = models.EmailField(_('email address'), unique=True)
    registration = models.IntegerField()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email



class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
