# Django and Python
import uuid
from django.db import models
from django.db.models.signals import pre_save

class Ingredient(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)

class Plate(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)

class Menu(models.Model):
    menu_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.menu_id

def set_menu_id(sender, instance, *args, **kwargs):
    """
    Function that help me to create diffucult ID for the menu instance
    :param sender (Class): Menu class
    :param instance (Object): Menu instace
    :param args (list): other paramethers
    :param kwargs (list): other paramethers
    :return (None):
    """
    #valid if menu has id
    if not instance.menu_id:
        #add strong id
        instance.menu_id = str(uuid.uuid4())

#I notific that before create menu new, must pass for particular function
pre_save.connect(set_menu_id, sender=Menu)