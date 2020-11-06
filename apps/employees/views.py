# Django
from django.shortcuts import render, redirect
from django.contrib import messages

# Apps.employees
from apps.employees import models
from apps.employees import forms

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
                return redirect('employees:list-menu', int(request.POST['number']) )

    data['title'] = "My prefences"

    return render(request, 'employees/search_employee.html', data)


def list_menu(request, phone):
    """
    Function for lists the menus
    :param request ():
    :param phone (int):
    :return ():
    """

    data = dict()
    my_employe = models.Employee.objects.filter(phone=int(phone))
    if my_employe.count() != 0:
        data['list_menus'] = models_menu.Menu.objects.all()
        data['title'] = 'Menu List'
        data['phone_employee'] = my_employe[0].phone
        data['email_employee'] = my_employe[0].email
    else:
        return redirect('employees:search-employee')

    return render(request, 'employees/menu/list_menu.html', data)

def list_plate_from_menu(request, identifier, phone):
    """

    :param request ():
    :param identifier (str):
    :param phone (int):
    :return:
    """
    data = dict()

    my_plates = models_menu.PlateIngredients.objects.filter(menu__identifier=identifier)
    my_employe = models.Employee.objects.filter(phone=int(phone))

    if my_plates.count()!=0 and my_employe.count()!=0:

        # menu data
        data['my_plates_lunch'] = my_plates.filter(plate__type='1')
        data['my_plates_salad'] = my_plates.filter(plate__type='2')
        data['my_plates_dessert'] = my_plates.filter(plate__type='3')

        # preference data
        my_preference = models.EmployeePreferences.objects.filter(employee__phone=phone)
        if my_preference.count()!=0:
            data['my_prefence_lunch'] = my_preference.filter(plate__type='1')
            data['my_prefence_salad'] = my_preference.filter(plate__type='2')
            data['my_prefence_dessert'] = my_preference.filter(plate__type='3')

        data['title'] = "Menu's plates"
        data['identifier'] = identifier
        data['phone'] = phone
        data['menu'] = my_plates[0].menu

    else:
        return redirect('employees:list-menu', phone)

    return render(request, 'employees/plate/list_plate_from_menu.html', data)

def add_preference_of_employee(request, identifier, phone, type_plate):
    """

    :param request (GET/POST):
    :param identifier (str):
    :param phone (int):
    :return ():
    """

    data = dict()

    if request.method == 'POST':
        form = forms.EmployeePreferencesForm(request.POST)

        if form.is_valid():
            form.save()

            # I send a success message
            messages.success(request, 'Ingredient was add to the preference')

            return redirect('employees:list-plate-from-menu', identifier, phone)
    else:
        form = forms.EmployeePreferencesForm()

        my_employe = models.Employee.objects.filter(phone=int(phone))
        my_plate = my_employe[0].get_or_create_plate(type_plate)

        form.fields['plate'].initial = my_plate
        form.fields['employee'].initial = my_employe[0]

    data['form'] = form
    data['title'] = 'Add preference of employee'
    data['identifier'] = identifier
    data['phone'] = phone
    data['type_plate'] = type_plate

    return render(request, 'employees/plate/add_preference_of_employee.html', data)