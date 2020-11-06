# Django
from django.shortcuts import render, redirect

# Apps.employees
from apps.employees import models

# Apps.menus
from apps.menus import models as models_menu

def search_employee(request):
    """

    :param request (POST/GET):
    :return:
    """
    data = dict()

    if request.method == 'POST':
        if 'number' in request.POST:
            if models.Employee.objects.filter(phone=int(request.POST['number'])).exists():
                return redirect('employees:list-menu')

    data['title'] = "My prefences"

    return render(request, 'employees/search_employee.html', data)


def list_menu(request):
    """
    Function for lists the menus
    :param request ():
    :return ():
    """

    data = dict()
    data['list_menus'] = models_menu.Menu.objects.all()
    data['title'] = 'Menu List'

    return render(request, 'employees/menu/list_menu.html', data)

def list_plate_from_menu(request, identifier):
    """

    :param request ():
    :param pk_menu (int):
    :return:
    """

    data = dict()

    my_plates = models_menu.PlateIngredients.objects.filter(menu__identifier=identifier)
    data['my_plates_lunch'] = my_plates.filter(plate__type='1')
    data['my_plates_salad'] = my_plates.filter(plate__type='2')
    data['my_plates_dessert'] = my_plates.filter(plate__type='3')

    data['title'] = "Menu's plates"
    data['identifier'] = identifier

    return render(request, 'employees/plate/list_plate_from_menu.html', data)