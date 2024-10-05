from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

def client_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('client_dashboard')  # Redirect to a client dashboard or homepage
        else:
            messages.error(request, "Invalid username or password")
            return redirect('client_login')
    
    return render(request, 'client_app/login.html')


@login_required
def client_dashboard(request):
    return render(request, 'client_app/dashboard.html')


def client_logout(request):
    logout(request)
    return redirect('client_login')  # Redirect to the login page after logging out
