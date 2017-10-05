from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# 1) Create the views
# 2) Create the urls with the views
# 3) Test with admin user and anon user


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
