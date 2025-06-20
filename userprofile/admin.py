from django.contrib import admin
from .models import UserProfile

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'image_link')
    ordering = ('user',)
    search_fields = ('user__username', 'phone')
    
    
admin.site.register(UserProfile, UserProfileAdmin)