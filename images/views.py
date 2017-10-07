from django.shortcuts import render
from . import models
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# Create your views here.


def like_image(request, image_id):

    try:
        existing_like = models.Like.objects.get(
            image__id=image_id, user__id=request.user.id)
        existing_like.delete()
        response = HttpResponse(status=204)
    except models.Like.DoesNotExist:
        found_image = models.Image.objects.get(id=image_id)
        new_like = models.Like.objects.create(
            user=request.user,
            image=found_image
        )
        new_like.save()
        response = HttpResponse(status=200)

    return response


@csrf_exempt
def comment_image(request, image_id):

    comment_to_save = request.POST.get('comment', None)

    if comment_to_save is not None:

        image = models.Image.objects.get(id=image_id)

        new_comment = models.Comment.objects.create(
            comment=comment_to_save,
            user=request.user,
            image=image
        )

        new_comment.save()

        response = JsonResponse({
            'comment': new_comment.comment,
            'user': new_comment.user.username
        })

    else:
        response = HttpResponse(status=406)

    return response
