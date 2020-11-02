# Django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Apps.menus
from apps.menus import forms

#@login_required()
def create_ingredient(request):
    """

    :param request ():
    :return ():
    """

    data = dict()

    if request.method == 'POST':
        form = forms.IngredientForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = forms.IngredientForm()

    data['form'] = form

    return render(request, 'menus/add_ingredient.html', data)
