from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/', views.user_profile, name='user_profile'),
    path('register/', views.register, name='register'),    
]