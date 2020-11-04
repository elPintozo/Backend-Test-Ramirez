# Django
from django import forms

# Apps.menus
from apps.menus import models

class IngredientForm(forms.ModelForm):
    class Meta:
        model = models.Ingredient
        exclude = ('create_at', )
        fields = ('name', 'type',)
        labels = {
            'name' : 'Name',
            'type' : 'Type',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
        }

class MenuForm(forms.ModelForm):
    class Meta:
        model = models.Menu
        exclude = ('menu_id', 'create_at', )
        fields = ('name', 'day',)
        labels = {
            'name' : 'Name',
            'day' : 'Publication date',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'day': forms.DateTimeInput(attrs={'class': 'form-control', 'type':'date'}),
        }

class PlateIngredientsForm(forms.ModelForm):
    class Meta:
        model = models.PlateIngredients
        exclude = ('create_at', )
        fields = ('menu', 'plate', 'ingredient',)
        labels = {
            'menu' : '',
            'plate' : '',
            'ingredient' : 'Ingredient'
        }
        widgets = {
            'menu': forms.HiddenInput(),
            'plate': forms.HiddenInput(),
            'ingredient': forms.Select(attrs={'class': 'form-control'}),
        }
        error_messages = {
            '__all__': {
                'unique_together': "This ingredient already exists in this plate.",
            }
        }