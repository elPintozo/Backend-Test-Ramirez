# Django
from datetime import datetime, timedelta
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

    return render(request, 'menus/ingredient/add_ingredient.html', data)

@login_required()
def list_ingredient(request):
    """
    Function for lists the ingredients
    :param request (POST):
    :return ():
    """

    data = dict()
    data['list_ingredients'] = models.Ingredient.objects.all()
    data['title'] = 'Ingredient List'

    return render(request, 'menus/ingredient/list_ingredient.html', data)

@login_required()
def create_menu(request):
    """
    Function to create ingredients with particular date
    :param request:
    :return:
    """
    data = dict()

    if request.method == 'POST':
        form = forms.MenuForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('menus:list-menu')
    else:
        form = forms.MenuForm()
        tomorrow = datetime.now() + timedelta(days=1)
        tomorrow_formatted = tomorrow.strftime('%Y-%m-%d')
        form.fields['day'].initial = tomorrow_formatted

    data['form'] = form
    data['title'] = ' Menu'

    return render(request, 'menus/menu/add_menu.html', data)

@login_required()
def list_menu(request):
    """
    Function for lists the menus
    :param request ():
    :return ():
    """

    data = dict()
    data['list_menus'] = models.Menu.objects.all()
    data['title'] = 'Menu List'

    return render(request, 'menus/menu/list_menu.html', data)

@login_required()
def list_plate_from_menu(request, pk_menu):
    """

    :param request ():
    :param pk_menu (int):
    :return:
    """

    data = dict()

    my_plates = models.PlateIngredients.objects.filter(menu=pk_menu)
    data['my_plates_lunch'] = my_plates.filter(plate__type='1')
    data['my_plates_salad'] = my_plates.filter(plate__type='2')
    data['my_plates_dessert'] = my_plates.filter(plate__type='3')

    data['title'] = "Menu's plates"
    data['pk_menu'] = pk_menu

    return render(request, 'menus/plate/list_plate_from_menu.html', data)

@login_required()
def add_ingredient_to_plate(request, pk_menu, type_plate):
    """

    :param request ():
    :param pk_menu (int):
    :param type_plate (string):
    :return:
    """

    data = dict()

    if request.method == 'POST':
        form = forms.PlateIngredientsForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('menus:list-plate-from-menu', pk_menu)
    else:
        form = forms.PlateIngredientsForm()

        if models.Menu.objects.filter(pk=pk_menu).exists():
            my_menu = models.Menu.objects.get(pk=pk_menu)
            form.fields['menu'].initial = my_menu
            my_plate = my_menu.get_or_create_plate(type_plate)
            form.fields['plate'].initial = my_plate
        else:
            return redirect('menus:list-menu')

    data['form'] = form
    data['title'] = 'Add ingredient to plate'
    data['pk_menu'] = pk_menu
    data['type_plate'] = type_plate

    return render(request, 'menus/plate/add_ingredient_to_plate.html', data)

