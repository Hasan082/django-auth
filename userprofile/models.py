from django.db import models
from django.contrib.auth.models import User


class authUserProfile(User):
    phone = models.CharField(max_length=15, null=True, blank=True)
    image_link = models.ImageField(upload_to='user-image', blank=True, null=True)
    