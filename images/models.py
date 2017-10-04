from django.db import models
from users import models as user_models


class Image(models.Model):

    author = models.ForeignKey(user_models.User)
    description = models.TextField()
    file = models.ImageField()
    date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.location


class Like(models.Model):

    user = models.ForeignKey(user_models.User)
    image = models.ForeignKey(Image)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.location


class Comment(models.Model):

    comment = models.TextField()
    user = models.ForeignKey(user_models.User)
    image = models.ForeignKey(Image)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
