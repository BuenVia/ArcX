from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegistrationForm

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.is_superuser:  # Check if the user is a superuser
                login(request, user)
                return redirect('dashboard')  # Redirect to the dashboard
            else:
                # Display error message if the user is not a superuser
                messages.error(request, "You don't have sufficient privileges to access this page.")
                return redirect('admin_login')  # Stay on login page
        else:
            # Invalid credentials message
            messages.error(request, "Invalid username or password")
            return redirect('admin_login')
    
    return render(request, 'admin_app/login.html')  # Render the login page


def admin_logout(request):
    logout(request)
    return redirect('admin_login')  # Redirect to 'manager/' path after logout


@login_required
def dashboard(request):
    if request.user.is_superuser:
        return render(request, 'admin_app/dashboard.html')  # Render dashboard page for superuser
    return redirect('')  # If the user is not a superuser, redirect to home

@login_required
def clients_page(request):
    if request.user.is_superuser:
        users = User.objects.all()
        return render(request, 'admin_app/clients.html', { "users": users })  # Render dashboard page for superuser
    return redirect('')  # If the user is not a superuser, redirect to home

@login_required
def client_edit(request, id):
    if request.user.is_superuser:
        if request.method == "POST":
            user = get_object_or_404(User, id=id)
            user.first_name = request.POST.get('firstname')
            user.last_name = request.POST.get('lastname')
            user.email = request.POST.get('email')
            user.username = request.POST.get('username')
            user.save()
            return redirect('clients')
        else:
            user = User.objects.get(id=id)
            return render(request, 'admin_app/client_edit.html', { "user": user })  # Render dashboard page for superuser
    return redirect('')  # If the user is not a superuser, redirect to home

@login_required
def client_pw_edit(request, id):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                # Process the form data, save user, etc.
                return redirect('some_success_page')
        else:
            form = UserRegistrationForm()

        return render(request, 'admin_app/client_pw_edit.html', {'form': form})
    return redirect('')  # If the user is not a superuser, redirect to home