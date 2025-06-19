from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import UserProfile
from django.contrib.auth import logout
from django.views.decorators.cache import never_cache





# Genral way
# @login_required
# def user_profile(request):
#     profile = request.user.userprofile
#     return render(request, 'accounts/profile.html', {'profile': profile})


# Best way
@login_required
@never_cache
def user_profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request, 'accounts/profile.html', {'profile': profile})


@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect('login')



def register(request):
    pass