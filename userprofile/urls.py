from django.urls import path, include
from . import views

urlpatterns = [
    path('accounts/', views.auth_user_profile, name='user_profile')
]