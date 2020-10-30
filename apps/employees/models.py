# Django
from django.db import models
from django.contrib.auth.models import AbstractUser

class Preference(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)

class Employee(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
