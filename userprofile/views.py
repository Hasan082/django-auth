from django.contrib.auth.decorators import login_required
from django.shortcuts import render







@login_required
def user_profile(request):
    profile = request.user.userprofile
    return render(request, 'accounts/profile.html', {'profile': profile})


def register(request):
    pass