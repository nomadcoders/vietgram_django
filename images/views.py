from django.shortcuts import render
from . import models
# Create your views here.


def like_image(request, image_id):

    # 0) Create a url like: '/images/{ID_OF_IMAGE}/like/
    # 1) Find a Like that exists with the image_id and the user_id
    # 2) If the like doesnt exist, create a like
    # 3) If the like is create return an HttpResponse with the status of 200
    # 4) If it already exists don't creatie the like and return  an HttpResponse with the status of 400
