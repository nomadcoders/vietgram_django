from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# 0) Play some music
# 1) Create 'partials' folder inside of 'templates' folder
# 2) Move <nav> and <footer> to nav.html and footer.html (dont forget to load static)
# 3) Create base.html and include nav and footer and create title block and content block
# 4) Create feed.html and then extend from 'base.html' and put the <main id="feed"> inside of the content block
# 5) Enjoy :)


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
