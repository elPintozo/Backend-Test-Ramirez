# Django
from django.urls import path

# Apps.Employees
from apps.employees import views

app_name='employees'

urlpatterns = [
    path('search/', views.search_employee, name='search-employee'),
    path('list/menu', views.list_menu, name='list-menu'),
    path('list/plate/<str:identifier>', views.list_plate_from_menu, name='list-plate-from-menu'),
]