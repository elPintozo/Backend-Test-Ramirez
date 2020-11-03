# Django
from django.test import SimpleTestCase
from django.urls import reverse, resolve

# Apps.menus
from apps.menus import views

class TestUrls(SimpleTestCase):

    def test_create_ingredient_url_resolves(self):
        url = reverse('menus:add-ingredient')
        self.assertEquals(resolve(url).func, views.create_ingredient)

    def test_list_ingredient_url_resolves(self):
        url = reverse('menus:list-ingredient')
        self.assertEquals(resolve(url).func, views.list_ingredient)

"""
Recomended command:
$ python manage.py test apps.menus --keepdb
"""