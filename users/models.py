from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('not-specified', 'Not specified')
    )

    profile_photo = models.ImageField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    gender = models.CharField(
        max_length=100, choices=GENDER_CHOICES, default='male')
