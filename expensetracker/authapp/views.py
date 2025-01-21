from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth import authenticate, login as auth_login  # Renamed to avoid conflict
# from .models import CustomUser
# from django.utils import timezone  # Add this import at the top


def signup(request):
    if request.method == 'POST':
        register_number= request.POST['user_id']
        name= request.POST['username']
        email= request.POST['email']
        phone= request.POST['contact_number']
        password= request.POST['password']
        user = User.objects.create(username=email, email=email, first_name=name, last_name=register_number)
        user.set_password(password)
        user.save()

        userProfile = UserProfile.objects.create(user=user, contact_number=phone)
        userProfile.save()
            # Create a UserProfile instance for the registered user
            # UserProfile.objects.create(user=user)
        return redirect('login')  # Replace 'home' with your actual homepage URL name
    else:
        return render(request, 'authenticate/signup.html')
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import login  # Correct import

def user_login(request):
    if request.method == 'POST':
        # Get the email and password from the login form
        email = request.POST.get('user_id')  # Here 'user_id' corresponds to email in the signup view
        password = request.POST.get('password')

        # Authenticate the user using email as the username
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')  # Replace 'dashboard' with your post-login redirect view
            else:
                messages.error(request, 'Your account is inactive. Please contact support.')
        else:
            messages.error(request, 'Invalid email or password.')

        # Re-render the login page with error messages
        return render(request, 'authenticate/login.html')

    return render(request, 'authenticate/login.html')



# @login_required(login_url='login')from django.shortcuts import render

def home(request):
    return render(request, 'users/home.html')  # Replace 'home.html' with the correct template
