from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import UserRegistrationForm, UserLoginForm

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            form = UserRegistrationForm()
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserRegistrationForm()
        return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                print(user)
                login(request, user)
                return redirect('home')
        else:
            form = UserLoginForm()
            return render(request, 'login.html', {'form': form})
    else:
        form = UserLoginForm()
        return render(request, 'login.html', {'form': form})


@login_required
def profile_view(request):
    return render(request, 'profile.html')

def logout_view(request):
    logout(request)
    return redirect('home')