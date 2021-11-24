import datetime

from django.db import models

# Create your models here.
from django.utils import timezone


class Account(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=225)
    first_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=150, null=True)
    user_name = models.CharField(max_length=30, unique=True, null=True)
    date_registered = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.email
