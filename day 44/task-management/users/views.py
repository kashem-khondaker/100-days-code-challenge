from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from users.forms import RegistrationForm,CustomRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def sign_up(request):
    if request.method == "POST":
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Welcome {user.username}! Your account has been created.')
            return redirect('sign-in')  # সাইন আপ হয়ে গেলে সাইন ইন পেজে পাঠাবে
        else:
            messages.error(request, "Form submission failed! Please check the errors below.")
    else:
        form = CustomRegistrationForm()  # GET request এ ফাঁকা form যাবে

    return render(request, 'registration/signUp.html', {'form': form})


def sign_in(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'registration/login.html')


def user_logout(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "You have successfully logged out.")  # Logout success message
        return redirect('sign-in')

    return redirect('home')