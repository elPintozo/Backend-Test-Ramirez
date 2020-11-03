# Django
from django.test import TestCase, Client
from django.urls import reverse, resolve

# Apps.Menu
from apps.menus import models

class TestViews(TestCase):

    def setUp(self):
        # el usuario que se usa para hacer el test
        self.client = Client()

        # indico variables necesarias para cargar la view
        self.VAR_USER = 'ricardo'
        self.VAR_PASS = '12345678q'

        # hago el login con el usuario indicado
        self.client.login(username=self.VAR_USER, password=self.VAR_PASS)

    def test_create_ingredient_GET(self):
        response = self.client.get(reverse('menus:add-ingredient'))

        # I valid status code after get request
        self.assertEquals(response.status_code, 200)

        # I valid use of asigned template
        self.assertTemplateUsed(response, 'menus/add_ingredient.html')

    def test_create_ingredient_POST(self):
        response = self.client.post(reverse('menus:add-ingredient'), {
            'name': 'pineapple',
            'type': '1',
        })

        # I valid status code after get request
        self.assertEquals(response.status_code, 302)

        # I valid ingredient created
        self.assertEquals(models.Ingredient.objects.filter(name='pineapple').exists(), True)

    def test_create_ingredient_POST_no_data(self):
        response = self.client.post(reverse('menus:add-ingredient'), {})

        # I valid status code after get request
        self.assertEquals(response.status_code, 200)

        # I valid ingredient created
        self.assertEquals(models.Ingredient.objects.filter(name='pineapple').exists(), False)

    def test_list_ingredient_GET(self):
        response = self.client.get(reverse('menus:list-ingredient'))

        # I valid status code after get request
        self.assertEquals(response.status_code, 200)

        # I valid use of asigned template
        self.assertTemplateUsed(response, 'menus/list_ingredient.html')

"""
Recomended command:
$ python manage.py test apps.menus --keepdb
"""