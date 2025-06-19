from django.db.models.signals import post_save, post_delete, pre_save
from .models import UserProfile
from django.contrib.auth.models import User
from django.dispatch import receiver
import os

# Signal 1: Automatically create a UserProfile when a new User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


# Signal 2: Save the UserProfile whenever the User is saved 
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
    
    
    
# Delete profile image from disk when profile is deleted
@receiver(post_delete, sender=UserProfile)
def delete_profile_image_on_delete(sender, instance, **kwargs):
    if instance.image_link and instance.image_link.path:
        if os.path.isfile(instance.image_link.path):
            os.remove(instance.image_link.path)


# Delete old image from disk when image is replaced
@receiver(pre_save, sender=UserProfile)
def delete_old_image_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return  # It's a new profile

    try:
        old_instance = UserProfile.objects.get(pk=instance.pk)
    except UserProfile.DoesNotExist:
        return

    old_file = old_instance.image_link
    new_file = instance.image_link

    if old_file and old_file != new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)