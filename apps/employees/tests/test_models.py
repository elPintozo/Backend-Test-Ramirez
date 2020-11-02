# Django
from django.test import TestCase
from datetime import datetime

# App.Employee
from apps.employees import models

# App.Menu
from apps.menus import models as model_menu

# App.Employee
from apps.employees import models

class TestModels(TestCase):

    def setUp(self):
        self.employee1 = models.Employee.objects.create(
            name = 'Pepe',
            phone = 981275085,
            email = 'ricardo@correo.com',
            nationality = '46'
        )
        self.ingredient1 = model_menu.Ingredient.objects.create(
            name = 'Apple',
            type = '1',
        )

        self.plate1 = model_menu.Plate.objects.create(
            name='Fruit mix',
            type='3',
        )

        self.menu1 = model_menu.Menu.objects.create(
            name='Sin carne',
            day=datetime.now()
        )

        self.employeepreferences1 = models.EmployeePreferences.objects.create(
            type = '1',
            employee = self.employee1,
            plate = self.plate1,
            ingredient = self.ingredient1
        )

    def test_employee_created(self):
        print('\n',models.Employee.objects.all())
        self.assertTrue(models.Employee.objects.filter(name='Pepe').exists())

    def test_employeepreferences_created(self):
        print('\n',models.EmployeePreferences.objects.all())
        self.assertTrue(models.EmployeePreferences.objects.filter(employee=self.employee1).exists())


"""
Recomended command:
$ python manage.py test apps.employees --keepdb
"""