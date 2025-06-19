from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import UserProfile





# Genral way
# @login_required
# def user_profile(request):
#     profile = request.user.userprofile
#     return render(request, 'accounts/profile.html', {'profile': profile})


# Best way
@login_required
def user_profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request, 'accounts/profile.html', {'profile': profile})


def register(request):
    pass