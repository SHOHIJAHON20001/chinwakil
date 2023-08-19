from django.shortcuts import render, redirect
from account.forms import CustomRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

def register_user(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('app:home')
        messages.error(request, 'malumotlar notogri')
    else:
        form = CustomRegisterForm()
    return render(request, 'registration.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('app:home')
        else: 
            messages.error(request, 'Invalid username or password')
            
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('app:home')

def logout_page(request):
    return render(request, 'logout.html')
