from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from . import models
from images import models as image_models


def index(request):
    if request.user.is_authenticated:
        images = image_models.Image.objects.all()
        context = {
            'images': images
        }
        return render(request, 'feed.html', context)
    else:
        response = HttpResponseRedirect(reverse('login'))
    return response


def login(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    else:
        response = HttpResponseRedirect(reverse('index'))
    return response


def explore(request):
    if request.user.is_authenticated:
        users = models.User.objects.exclude(id=request.user.id)
        context = {
            'users': users
        }
        return render(request, 'explore.html', context)
    else:
        response = HttpResponseRedirect(reverse('login'))
    return response


def profile(request, username_from_url):
    if request.user.is_authenticated:
        profile_user = models.User.objects.get(username=username_from_url)
        context = {
            'profile_user': profile_user
        }
        return render(request, 'profile.html', context)
    else:
        response = HttpResponseRedirect(reverse('login'))
    return response
