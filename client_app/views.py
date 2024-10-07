from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_list_or_404
from .forms import ClientUserPDFForm
from .models import ClientUserPDF

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


def client_logout(request):
    logout(request)
    return redirect('client_login')  # Redirect to the login page after logging out


@login_required
def client_dashboard(request):
    return render(request, 'client_app/dashboard.html')


@login_required
def upload_pdf(request):
    # Check if the user already has a PDF associated with their account
    user_pdf = ClientUserPDF.objects.filter(user=request.user).first()

    if request.method == 'POST':
        form = ClientUserPDFForm(request.POST, request.FILES, instance=user_pdf)
        if form.is_valid():
            user_pdf = form.save(commit=False)
            user_pdf.user = request.user  # Associate the PDF with the logged-in user
            user_pdf.save()
            return redirect('client_dashboard')  # Redirect after successful upload
    else:
        form = ClientUserPDFForm(instance=user_pdf)

    return render(request, 'client_app/upload_pdf.html', {'form': form})