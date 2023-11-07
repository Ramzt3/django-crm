from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

def home(request):
    # check if loggin
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # authenticate
        user = authenticate(request, username=username, password=password)
        if not user:
            messages.success(request, "invalid credential")
            return redirect('home')
        else:
            login(request, user)
            messages.success(request, "you have been logged in")
            return redirect('home')
    else:
        return render(request, "home.html")

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "you have been logged out...")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered welcome")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form}) 
    return render(request, 'register.html', {'form': form}) 
