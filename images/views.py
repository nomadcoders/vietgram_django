from django.shortcuts import render
from . import models
from django.http import HttpResponse
# Create your views here.


def like_image(request, image_id):

    try:
        existing_like = models.Like.objects.get(
            image__id=image_id, user__id=request.user.id)
        existing_like.delete()
        response = HttpResponse(status=202)
    except models.Like.DoesNotExist:
        image = models.Image.objects.get(id=image_id)
        new_like = models.Like.objects.create(
            user=request.user,
            image=image
        )
        new_like.save()
        response = HttpResponse(status=200)

    return response
