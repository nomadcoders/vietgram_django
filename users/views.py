from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# 1) Render the template with render function (line one)
# 2) Create a folder named 'static' and another named 'templates'
# 3) Add STATIC_DIRS to settings.py (look on github)
# 4) Modifie TEMPLATE DIRS on settings.py (look on github)
# 5) Add template tags to your html (look on github)


def index(request):
    if request.user.is_authenticated:
        return render(request, 'feed.html')
    else:
        response = HttpResponseRedirect(reverse('login'))
    return response


def login(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    else:
        response = HttpResponseRedirect(reverse('index'))
    return response
