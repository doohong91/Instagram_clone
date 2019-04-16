from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('root')
    else:
        form = UserCreationForm()
        return render(request, 'accounts/signup.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('root')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('root')
    

def profile(request, username):
    # User모델을 가져오는 방법
    # 1. from django.contrib.auth.models import User (비추)
    # 2. from django.conf import settings -> settings.AUTH_USER_MODEL (string형식)
    # 3. from django.contrib.auth import get_user_model 
    profile = get_object_or_404(get_user_model(), username=username)
    return render(request, 'accounts/profile.html', {'profile': profile})
