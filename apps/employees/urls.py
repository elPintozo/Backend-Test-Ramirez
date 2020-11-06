# Django
from django.urls import path

# Apps.Employees
from apps.employees import views

app_name='employees'

urlpatterns = [
    path('search/', views.search_employee, name='search-employee'),
    path('list/menu/<int:phone>', views.list_menu, name='list-menu'),
    path('list/plate/<str:identifier>/<int:phone>', views.list_plate_from_menu, name='list-plate-from-menu'),
    path('add/preference/<str:identifier>/<int:phone>/<str:type_plate>', views.add_preference_of_employee, name='add-preference-of-employee'),
]