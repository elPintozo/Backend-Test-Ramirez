# Django and Python
import uuid
from datetime import datetime
from django.db import models
from django.db.models.signals import pre_save

class Ingredient(models.Model):
    type_options = (
        ('1', 'Simple'),
        ('2', 'Prepared'),
    )
    name = models.CharField(max_length=100, null=False, default='')
    type = models.CharField(max_length=1, choices=type_options, default='1')
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Plate(models.Model):
    type_options = (
        ('1', 'Lunch'),
        ('2', 'Salad'),
        ('3', 'Dessert'),
    )
    name = models.CharField(max_length=100, null=False, default='')
    type = models.CharField(max_length=1, choices=type_options, default='1')
    ingredients = models.ManyToManyField(Ingredient, through='PlateIngredients')
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.get_type_display()

class Menu(models.Model):
    name = models.CharField(max_length=100, null=False, default='')
    day = models.DateTimeField(default=datetime.now, blank=False)
    identifier = models.CharField(max_length=100, null=False, blank=False, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.identifier

    def get_or_create_plate(self, type_plate):
        """

        :param type_plate (string):
        :return (Plate):
        """
        if not PlateIngredients.objects.filter(menu=self, plate__type=type_plate).count():
            return Plate.objects.create(name=' ', type=type_plate)
        else:
            return PlateIngredients.objects.filter(menu=self, plate__type=type_plate).first().plate

class PlateIngredients(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    plate = models.ForeignKey(Plate, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [['plate', 'ingredient']]

def set_menu_identifier(sender, instance, *args, **kwargs):
    """
    Function that help me to create diffucult ID for the menu instance
    :param sender (Class): Menu class
    :param instance (Object): Menu instace
    :param args (list): other paramethers
    :param kwargs (list): other paramethers
    :return (None):
    """
    #valid if menu has id
    if not instance.identifier:
        #add strong id
        instance.identifier = str(uuid.uuid4())

#I notific that before create menu new, must pass for particular function
pre_save.connect(set_menu_identifier, sender=Menu)

"""
Tips to load data: 

** You can use this command for load data 
$ python3 manage.py loaddata ingredients_03112020.json
"""




