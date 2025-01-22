from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile

# Signup View
def signup(request):
    if request.method == 'POST':
        register_number = request.POST['user_id']
        name = request.POST['username']
        email = request.POST['email']
        phone = request.POST['contact_number']
        password = request.POST['password']

        # Create a new user
        user = User.objects.create(username=email, email=email, first_name=name, last_name=register_number)
        user.set_password(password)
        user.save()

        # Create a Profile instance for the new user
        profile = Profile.objects.create(user=user, contact_number=phone)
        profile.save()

        # Redirect to login page after successful signup
        return redirect('login')
    else:
        return render(request, 'authenticate/signup.html')


# Login View
def user_login(request):
    if request.method == 'POST':
        # Get email and password from the login form
        email = request.POST.get('user_id')  # 'user_id' is used as email
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')  # Redirect to home/dashboard after login
            else:
                messages.error(request, 'Your account is inactive. Please contact support.')
        else:
            messages.error(request, 'Invalid email or password.')

        # Re-render the login page with error messages
        return render(request, 'authenticate/login.html')

    return render(request, 'authenticate/login.html')


# Home View
@login_required(login_url='login')  # Ensure only logged-in users can access this view
def home(request):
    return render(request, 'users/home.html')  # Replace 'home.html' with your actual template


# User Profile View
@login_required
@login_required
def user_profile(request):
    try:
        # Fetch the Profile for the logged-in user
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = None  # Handle case where the profile doesn't exist

    # Pass user and profile details to the template
    context = {
        'user': request.user,  # User object (contains username, email, etc.)
        'profile': profile,    # Profile object (contains contact_number)
    }
    return render(request, 'users/profile.html', context)
