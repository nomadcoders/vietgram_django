from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def index(request):
    if request.user.is_authenticated():
        response = HttpResponse('Feed')
    else:
        response = HttpResponseRedirect(reverse('login'))
    return response


def login(request):
    if not request.user.is_authenticated():
        response = HttpResponse('Log in.')
    else:
        response = HttpResponseRedirect(reverse('index'))
    return response
