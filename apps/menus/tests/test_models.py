# Django
from django.test import TestCase
from datetime import datetime

# App.Menu
from apps.menus import models

class TestModels(TestCase):

    def setUp(self):
        self.ingredient1 = models.Ingredient.objects.create(
            name = 'Apple',
            type = '1',
        )

        self.plate1 = models.Plate.objects.create(
            name='Fruit mix',
            type='3',
        )

        self.menu1 = models.Menu.objects.create(
            name='Sin carne',
            day=datetime.now()
        )

        self.plateingredients1 = models.PlateIngredients.objects.create(
            menu = self.menu1,
            plate = self.plate1,
            ingredient = self.ingredient1
        )

    def test_ingredient_created(self):
        print('\n',models.Ingredient.objects.all())
        self.assertTrue(models.Ingredient.objects.filter(name='Apple').exists())

    def test_plate_created(self):
        print('\n',models.Plate.objects.all())
        self.assertTrue(models.Plate.objects.filter(name='Fruit mix').exists())

    def test_menu_created(self):
        print('\n',models.Menu.objects.all())
        self.assertTrue(models.Menu.objects.filter(name='Sin carne').exists())

    def test_plateingredients_created(self):
        print('\n',models.PlateIngredients.objects.all())
        self.assertTrue(models.PlateIngredients.objects.filter(plate = self.plate1,
                                                               ingredient = self.ingredient1).exists())

"""
Recomended command:
$ python manage.py test apps.menus --keepdb
"""