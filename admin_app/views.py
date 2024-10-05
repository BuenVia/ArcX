from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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


@login_required
def dashboard(request):
    if request.user.is_superuser:
        return render(request, 'admin_app/dashboard.html')  # Render dashboard page for superuser
    return redirect('')  # If the user is not a superuser, redirect to home


def admin_logout(request):
    logout(request)
    return redirect('admin_login')  # Redirect to 'manager/' path after logout