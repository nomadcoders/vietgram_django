from django.db import models
from users import models as user_models


class Image(models.Model):

    author = models.ForeignKey(user_models.User, related_name='images')
    description = models.TextField()
    file = models.ImageField()
    date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=100)

    @property
    def is_liked(self, user):
        return True

    def __str__(self):
        return self.location

    class Meta:
        ordering = ["-date", ]


class Like(models.Model):

    user = models.ForeignKey(user_models.User)
    image = models.ForeignKey(Image, related_name='likes')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.location


class Comment(models.Model):

    comment = models.TextField()
    user = models.ForeignKey(user_models.User)
    image = models.ForeignKey(Image,  related_name='comments')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
