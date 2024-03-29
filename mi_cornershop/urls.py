"""mi_cornershop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#Django
from django.contrib import admin
from django.urls import path, include

#Project
from mi_cornershop import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('users/login', views.login_custom, name='login'),
    path('users/logout', views.logout_custom, name='logout'),
    path('menus/', include('apps.menus.urls')),
    path('employees/', include('apps.employees.urls')),
]
