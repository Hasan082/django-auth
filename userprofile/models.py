from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, null=True, blank=True)
    image_link = models.ImageField(upload_to='user_image', blank=True, null=True)
    
    def __str__(self):
        return self.user.username
    
    
    

    