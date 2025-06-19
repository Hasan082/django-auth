from django.urls import path
from . import views
from django.contrib.auth.views import LoginView



urlpatterns = [
    path('', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.user_profile, name='user_profile'),
    path('register/', views.register, name='register'),    
]