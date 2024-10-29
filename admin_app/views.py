import os
from collections import defaultdict
from datetime import date
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Prefetch, Min
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistrationForm, AddUserForm, EquipmentForm
from .models import DocumentClient, DocumentTitle, Staff, StaffRole, StaffQualification,  Equipment, EquipmentGroup, EquipmentUser

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
            password = request.POST.get('password')
            repeat_password = request.POST.get('repeat_password')
            print(request.POST.get('password'))
            print(request.POST.get('repeat_password'))
            if password == repeat_password:
                if form.is_valid():
                    user = user_form.save()
                    user.set_password('unencrypted_password')  # replace with your real password
                    user.save()
                    # Process the form data, save user, etc.
                    return redirect('clients')
        else:
            form = UserRegistrationForm()

        return render(request, 'admin_app/client_pw_edit.html', {'form': form})
    return redirect('')  # If the user is not a superuser, redirect to home

@login_required
def client_new(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = AddUserForm(request.POST)
            if form.is_valid():
                # Create the user object without saving it yet
                user = form.save(commit=False)

                # Set the password using set_password() to hash it securely
                password = form.cleaned_data['password']
                user.set_password(password)

                # Save the user object with the password
                user.save()

                return redirect('clients')  # Redirect after successful user creation
        else:
            form = AddUserForm()

        return render(request, 'admin_app/client_new.html', {'form': form})

# Documentation
@login_required
def client_document_view(request, id):
    if request.user.is_superuser:
        user_pdfs = DocumentClient.objects.filter(user=id)
        return render(request, 'admin_app/client_docs.html', {"user_pdfs": user_pdfs})

@login_required
def document_view(request):
    if request.user.is_superuser:
        user_pdfs = DocumentClient.objects.all()
        return render(request, 'admin_app/documents.html', {"user_pdfs": user_pdfs})

@login_required
def delete_pdf(request, pdf_id):
    # Find the PDF object by its ID
    pdf = get_object_or_404(DocumentClient, id=pdf_id)
    print(pdf)
    # Delete the file from the file system
    if pdf.pdf:
        print(pdf.pdf)
        # Construct the full file path
        file_path = os.path.join(settings.MEDIA_ROOT, str(pdf.pdf))
        # Check if the file exists before attempting to delete it
        print(file_path)
        if os.path.exists(file_path):
            os.remove(file_path)

    # Delete the record from the database
    pdf.delete()

    # Redirect to some page after deletion (e.g., PDF list or success page)
    return redirect('admin_documents')  # Replace with your desired redirect

# Equipment
@login_required
def admin_all_equipment(request):
    equipment_items = Equipment.objects.select_related('equipment_group').all()

    # Initialize a dictionary to hold the grouped data
    grouped_equipment = defaultdict(list)

    # Group equipment by EquipmentGroup
    for equipment in equipment_items:
        group_name = equipment.equipment_group.name
        grouped_equipment[group_name].append(equipment)

    # Transform the grouped data into the desired structure
    equipment_list = [
        {
            "group": group,
            "items": items,
        }
        for group, items in grouped_equipment.items()
    ]
    context = {'equipment_list': equipment_list}
    return render(request, 'admin_app/admin_add_equipment.html', context=context)

@login_required
def admin_all_equipment_new(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_all_equipment')  # Redirect to the equipment list or another appropriate page
    else:
        form = EquipmentForm()
    
    return render(request, 'admin_app/admin_equipment_add_edit.html', {'form': form, 'is_edit': False})

@login_required
def admin_all_equipment_edit(request, id):
    equipment = get_object_or_404(Equipment, id=id)
    if request.method == 'POST':
        form = EquipmentForm(request.POST, instance=equipment)
        if form.is_valid():
            form.save()
            return redirect('admin_all_equipment')  # Redirect to the equipment list or another appropriate page
    else:
        form = EquipmentForm(instance=equipment)
    
    return render(request, 'admin_app/admin_equipment_add_edit.html', {'form': form, 'is_edit': True})

@login_required
def admin_all_equipment_delete(request, id):
    equipment = get_object_or_404(Equipment, id=id)
    if request.method == 'POST':
        equipment.delete()
        return redirect('admin_all_equipment')  # Redirect to the list view after deletion

    return render(request, 'admin_app/admin_delete_equipment.html', {'equipment': equipment})

@login_required
def admin_client_equipment(request, id):
        # Fetch EquipmentUser instances for the specified user and prefetch related data
    # equipment_list = EquipmentUser.objects.filter(user_id=id)\
    #     .select_related('equipment__equipment_group')\
    #     .prefetch_related(Prefetch('equipmenttest_set'))\
    #     .order_by('equipment__equipment_group_id')  # Order by EquipmentGroup ID

    # context = {
    #     'equipment_list': equipment_list,
    # }
    equipment_list = (
        EquipmentUser.objects.filter(user_id=id)
        .select_related('equipment__equipment_group')
        .prefetch_related(Prefetch('equipmenttest_set'))
        .order_by('equipment__equipment_group_id')
    )

    # Group equipment by EquipmentGroup
    grouped_equipment = {}
    for equipment_user in equipment_list:
        group_name = equipment_user.equipment.equipment_group.name

        # Initialize group if it doesn't exist
        if group_name not in grouped_equipment:
            grouped_equipment[group_name] = []

        # Gather equipment and related test data
        item_data = {
            "id": equipment_user.equipment.id,
            "name": equipment_user.equipment.name,
            "item_number": equipment_user.equipment.item_number,
            "make": equipment_user.equipment.make,
            "model": equipment_user.equipment.model,
            "serial_number": equipment_user.equipment.serial_number,
            "tests": list(equipment_user.equipmenttest_set.all())  # Access tests from equipment_user
        }

        # Add item data to the appropriate group
        grouped_equipment[group_name].append(item_data)

    # Convert grouped data to desired structure
    context = {
        "equipment_list": [
            {"group": group_name, "items": items}
            for group_name, items in grouped_equipment.items()
        ]
    }
    return render(request, 'admin_app/client_equipment.html', context=context)

# Competenecy
@login_required
def admin_competency(request, id):
    staff_list = Staff.objects.filter(user_id=id)\
        .select_related('user')\
        .prefetch_related(
            Prefetch('staffrole_set', queryset=StaffRole.objects.select_related('role')),
            Prefetch('staffqualification_set', queryset=StaffQualification.objects.select_related('qualification'))
        )\
        .annotate(min_role_id=Min('staffrole__role_id'))\
        .order_by('min_role_id')
    today = date.today()
    return render(request, 'admin_app/client_competency.html', {'staff_list': staff_list, 'today': today})
