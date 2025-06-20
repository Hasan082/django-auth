from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import UserProfile
from django.contrib.auth import login, logout
from django.views.decorators.cache import never_cache

from django.contrib.auth.models import User
from .forms import UserRegistrationForm



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
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Create UserProfile
            # UserProfile.objects.create(
            #     user=user,
            #     phone=form.cleaned_data['phone'],
            #     image_link=form.cleaned_data['image_link']
            # )
            
            # Update auto-created UserProfile
            profile = user.userprofile
            profile.phone = form.cleaned_data['phone']
            profile.image_link = form.cleaned_data['image_link']
            profile.save()

            login(request, user)  # Log the user in after registering
            return redirect('user_profile')
    else:
        form = UserRegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})


