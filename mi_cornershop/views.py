#Django
from django.shortcuts import render

def index(request):
    """
    Home
    :param request ():
    :return ():
    """
    # template's data
    data = {
        'title': 'Home',
    }

    return render(request, 'index.html', data)