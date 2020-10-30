# Django
from django.db import models
from django.contrib.auth.models import AbstractUser

class Preference(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)

# class User(AbstractUser):
#
#     def get_full_name(self):
#         return '{} {}'.format(self.first_name, self.last_name)
#
# class Employee(User):
#     create_at = models.DateTimeField(auto_now_add=True)
#
#     #Indico que será un proxy model
#     class Meta:
#         proxy = True
