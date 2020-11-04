# Django
from django.urls import path

# Apps.menus
from apps.menus import views

app_name='menus'

urlpatterns = [
    path('add/ingredient', views.create_ingredient, name='add-ingredient'),
    path('list/ingredient', views.list_ingredient, name='list-ingredient'),

    path('add/menu', views.create_menu, name='add-menu'),
    path('list/menu', views.list_menu, name='list-menu'),

    path('list/plate/<int:pk_menu>', views.list_plate_from_menu, name='list-plate-from-menu'),
    path('add/ingredient_to_plate/<int:pk_menu>/<str:type_plate>',
         views.add_ingredient_to_plate,
         name='add-ingredient-to-plate'),
]