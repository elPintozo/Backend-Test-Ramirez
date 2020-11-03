# Django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Apps.menus
from apps.menus import forms
from apps.menus import models

@login_required()
def create_ingredient(request):
    """
    Function to create ingredients
    :param request (POST):
    :return ():
    """

    data = dict()

    if request.method == 'POST':
        form = forms.IngredientForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('menus:list-ingredient')
    else:
        form = forms.IngredientForm()

    data['form'] = form
    data['title'] = 'Add Ingredient'

    return render(request, 'menus/add_ingredient.html', data)

@login_required()
def list_ingredient(request):
    """
    Function to create ingredients
    :param request (POST):
    :return ():
    """

    data = dict()
    data['list_ingredients'] = models.Ingredient.objects.all()
    data['title'] = 'Ingredient List'

    return render(request, 'menus/list_ingredient.html', data)
