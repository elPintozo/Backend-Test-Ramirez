# Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib import messages

def index(request):
    """
    Index
    :param request ():
    :return ():
    """
    # template's data
    data = {
        'title': 'Index',
    }

    return render(request, 'index.html', data)

def home(request):
    """
    Home
    :param request ():
    :return ():
    """
    # template's data
    data = {
        'title': 'Home',
    }

    return render(request, 'home.html', data)

def login_custom(request):
    """
    Function that help us to login in the page
    :param request (POST): username and password
    :return (render/redirect):
    """

    ## valido para evitar ingresar por URL
    if request.user.is_authenticated:
        return redirect('index')

    # template's data
    data = dict()

    if request.method == 'POST':

        ##obtengo los datos del formulario
        username = request.POST.get('username')
        password = request.POST.get('password')

        ## Function that to check if exists the user
        user = authenticate(username=username, password=password)

        #check if data is valid
        if user is not None:
            ##login user in the page
            login(request, user)

            #I send a success message
            messages.success(request, 'Welcome {}.'.format(username))

            # If send me a next variable(it has a url), I redirect you to the solicit variable
            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET.get('next'))

            #If doesn't send me a next variable(it has a url), I redirect you to home page
            return redirect('home')
        else:
            messages.error(request, 'Username or password invalid.')

    data={
        'title':'Login'
    }
    return render(request, 'users/login.html', data)

def logout_custom(request):
    """
    Function that help us to logout in the page
    :param request (None):
    :return (redirect):
    """
    logout(request)
    messages.success(request, 'Goodbye')
    return redirect('login')