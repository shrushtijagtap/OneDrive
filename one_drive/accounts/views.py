from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.utils import timezone

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password_last_changed = timezone.now()
            user.save()
            login(request, user)
            return redirect('home') 
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to a homepage or dashboard
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'accounts/login.html')

# main/views.py
@login_required
def home(request):
    return render(request, 'home.html')


def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    return render(request, 'profile.html')