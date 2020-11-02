# Django
from django.test import SimpleTestCase

# Apps.menus
from apps.menus import forms
class TestForms(SimpleTestCase):

    def test_ingredient_form_valid_data(self):
        """

        :return:
        """
        form  = forms.IngredientForm(data={
            'name':'tomato',
            'type': '1'
        })
        self.assertTrue(form.is_valid())

    def test_ingredient_form_no_data(self):
        """

        :return:
        """
        form  = forms.IngredientForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)