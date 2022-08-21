from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(blank=False, max_length=255)
    last_name = models.CharField(blank=False, max_length=255)
    email = models.EmailField(_('Email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email