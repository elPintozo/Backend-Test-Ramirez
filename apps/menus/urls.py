# Django
from django.urls import path

# Apps.menus
from apps.menus import views

app_name='menus'

urlpatterns = [
    path('add/ingredient', views.create_ingredient, name='add-ingredient'),
    path('list/ingredient', views.list_ingredient, name='list-ingredient')
]