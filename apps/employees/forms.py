# Django
from django import forms

# Apps.employees
from apps.employees import models

class EmployeePreferencesForm(forms.ModelForm):
    class Meta:
        model = models.EmployeePreferences
        exclude = ('create_at', )
        fields = ('type', 'employee', 'plate', 'ingredient',)
        labels = {
            'type' : 'Preference',
            'ingredient' : 'Ingredient',
        }
        widgets = {
            'type': forms.Select(attrs={'class': 'form-control'}),
            'employee': forms.HiddenInput(),
            'plate': forms.HiddenInput(),
            'ingredient': forms.Select(attrs={'class': 'form-control'}),
        }