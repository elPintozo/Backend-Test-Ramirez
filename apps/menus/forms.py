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