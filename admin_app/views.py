import os
from collections import defaultdict
from datetime import date
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Prefetch, Min
from django.forms import modelformset_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm, UserRegistrationForm, AddUserForm, UserProfileForm, EquipmentForm, StaffForm, StaffRoleForm, StaffQualificationForm
from .models import UserProfile, DocumentClient, DocumentTitle, Staff, StaffRole, RoleNames, Qualifications, StaffQualification, Equipment, EquipmentGroup, EquipmentUser, EquipmentTest

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.is_superuser:  # Check if the user is a superuser
                login(request, user)
                return redirect('aa_dashboard')  # Redirect to the dashboard
            else:
                # Display error message if the user is not a superuser
                messages.error(request, "You don't have sufficient privileges to access this page.")
                return redirect('aa_login')  # Stay on login page
        else:
            # Invalid credentials message
            messages.error(request, "Invalid username or password")
            return redirect('aa_login')
    
    return render(request, 'admin_app/aa_login.html')  # Render the login page

def admin_logout(request):
    logout(request)
    return redirect('aa_login')  # Redirect to 'manager/' path after logout

@login_required
def aa_dashboard(request):
    if request.user.is_superuser:
        return render(request, 'admin_app/aa_dashboard.html')  # Render dashboard page for superuser
    return redirect('')  # If the user is not a superuser, redirect to home

# Client Controll
@login_required
def aa_clients_list(request):
    if request.user.is_superuser:
        users = User.objects.all()
        return render(request, 'admin_app/clients/aa_clients.html', { "users": users })  # Render dashboard page for superuser
    return redirect('')  # If the user is not a superuser, redirect to home

@login_required
def aa_client_create(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            user_form = AddUserForm(request.POST)
            profile_form = UserProfileForm(request.POST)

            if user_form.is_valid() and profile_form.is_valid():
                # Create the user object without saving it yet
                user = user_form.save(commit=False)

                # Set the password using set_password() to hash it securely
                password = user_form.cleaned_data['password']
                user.set_password(password)

                # Save the user object
                user.save()

                # Create the profile object and link it to the user
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()

                return redirect('aa_clients')  # Redirect after successful user creation
        else:
            user_form = AddUserForm()
            profile_form = UserProfileForm()

        return render(
            request,
            'admin_app/clients/aa_client_create.html',
            {
                'user_form': user_form,
                'profile_form': profile_form,
            },
        )

@login_required
def aa_client_read(request, id):
    user = User.objects.filter(id=id).first()
    user_profile = UserProfile.objects.filter(user_id=id).first()
    context = {'user': user, 'user_profile': user_profile}
    return render(request, 'admin_app/clients/aa_client_read.html', context)

@login_required
def aa_client_update(request, id):
    if request.user.is_superuser:
        user = get_object_or_404(User, id=id)
        profile = get_object_or_404(UserProfile, user=user)

        if request.method == 'POST':
            user_form = UserForm(request.POST, instance=user)
            profile_form = UserProfileForm(request.POST, instance=profile)

            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                return redirect('aa_client_read', id=id)  # Redirect to a success page or user dashboard
        else:
            user_form = UserForm(instance=user)
            profile_form = UserProfileForm(instance=profile)

        context = {
            'user_form': user_form,
            'profile_form': profile_form,
            'id': id
        }
        return render(request, 'admin_app/clients/aa_client_update.html', context)
    return redirect('')  # If the user is not a superuser, redirect to home

@login_required
def aa_client_update_pw(request, id):
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

        return render(request, 'admin_app/aa_client_update_pw.html', {'form': form})
    return redirect('')  # If the user is not a superuser, redirect to home

@login_required
def aa_client_delete(request, id):
    user = User.objects.filter(id=id).first()
    if request.method == "POST":
        if request.POST.get('name') == user.username:
            user.delete()
            return redirect('aa_clients')
        else:
            print("huh?")
            return redirect('aa_client_update', id=user.id)
            
    context = {'user': user}
    return render(request, 'admin_app/clients/aa_client_delete.html', context)






# Documentation
@login_required
def client_document_view(request, id):
    if request.user.is_superuser:
        user = User.objects.filter(id=id).first()
        documents = DocumentClient.objects.filter(user=id)
        print(documents[0].file)
        return render(request, 'admin_app/documentation/aa_client_docs.html', {"documents": documents, 'user': user})

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
    return render(request, 'admin_app/equipment/aa_equipment_add.html', context=context)

@login_required
def admin_all_equipment_new(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_all_equipment')  # Redirect to the equipment list or another appropriate page
    else:
        form = EquipmentForm()
    
    return render(request, 'admin_app/equipment/aa_equipment_add.html', {'form': form, 'is_edit': False})

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
    
    return render(request, 'admin_app/equipement/aa_equipment_edit.html', {'form': form, 'is_edit': True})

@login_required
def admin_all_equipment_delete(request, id):
    equipment = get_object_or_404(Equipment, id=id)
    if request.method == 'POST':
        equipment.delete()
        return redirect('admin_all_equipment')  # Redirect to the list view after deletion

    return render(request, 'admin_app/equipment/aa_equipment_delete.html', {'equipment': equipment})

@login_required
def admin_client_equipment(request, id):
    # Fetch EquipmentUser instances for the specified user and prefetch related data
    equipment_list = (
        EquipmentUser.objects.filter(user_id=id)
        .select_related('equipment__equipment_group')
        .prefetch_related(Prefetch('equipmenttest_set'))
        .order_by('equipment__equipment_group_id')
    )

    # Group equipment by EquipmentGroup
    # Prepare the result structure
    grouped_equipment = {}
    for equipment_user in equipment_list:
        group_name = equipment_user.equipment.equipment_group.name

        # Initialize group if it doesn't exist
        if group_name not in grouped_equipment:
            grouped_equipment[group_name] = []

        # Gather equipment and latest test data
        try:
            latest_test = equipment_user.equipmenttest_set.latest('test_date')  # Order by 'test_date' or another date field
            test_data = {
                "calibrate_date": latest_test.calibrate_date,
                "calibrate_freq": latest_test.calibrate_freq,
                "service_date": latest_test.service_date,
                "service_freq": latest_test.servcice_freq,
                "inspection_date": latest_test.inspection_date,
                "inspection_freq": latest_test.inspection_freq,
                "test_date": latest_test.test_date,
                "test_freq": latest_test.test_freq,
            }
        except EquipmentTest.DoesNotExist:
            test_data = None  # Handle cases where no tests exist

        item_data = {
            "id": equipment_user.equipment.id,
            "name": equipment_user.equipment.name,
            "item_number": equipment_user.equipment.item_number,
            "make": equipment_user.equipment.make,
            "model": equipment_user.equipment.model,
            "serial_number": equipment_user.equipment.serial_number,
            "latest_test": test_data,  # Add only the latest test
        }

        # Add item data to the appropriate group
        grouped_equipment[group_name].append(item_data)

    user = User.objects.filter(id=id)
    print(user)
    # Convert grouped data to desired structure
    context = {
        "equipment_list": [
            {"group": group_name, "items": items}
            for group_name, items in grouped_equipment.items()
        ],
        'user': user[0]
    }

    return render(request, 'admin_app/equipment/aa_equipment.html', context=context)

# Competenecy
@login_required
def admin_competency(request, id):
    # Fetch all roles
    roles = RoleNames.objects.all()
    
    data = {}
    
    for role in roles:
        # Get qualifications for this role
        qualifications = Qualifications.objects.filter(role=role)
        
        # Get all staff for this role and their qualifications
        staff_roles = StaffRole.objects.filter(role=role, staff__user_id=id)
        
        staff_data = []
        
        for staff_role in staff_roles:
            # Get qualifications for this specific staff member
            staff_qualifications = StaffQualification.objects.filter(staff=staff_role.staff, qualification__in=qualifications)
            
            # Structure staff qualification data for this role
            qualification_data = {q.qualification_name: None for q in qualifications}  # initialize with None
            for sq in staff_qualifications:
                qualification_data[sq.qualification.qualification_name] = sq.qualification_date
            
            staff_data.append({
                "staff_name": f"{staff_role.staff.first_name} {staff_role.staff.last_name}",
                "staff_id": staff_role.staff.id,
                "qualifications": qualification_data
            })

        
        # Prepare the role data for the template
        data[role.role_name] = {
            "qualifications": [q.qualification_name for q in qualifications],
            "staff_data": staff_data
        }
        print(staff_data)

    context = {
        'data': data,
        'user': id
    }
    print(context)
    # context = {'roles_data': roles_data, 'today': today}
    return render(request, 'admin_app/competency/aa_competency.html', context)

@login_required
def admin_competency_staff(request, id):
    staff = Staff.objects.filter(id=id).first()
    staff_qualification = StaffQualification.objects.filter(staff=id)
    staff_role = StaffRole.objects.filter(staff=id).first()
    context = {
        "staff": staff,
        "staff_qualification": staff_qualification,
        "staff_role": staff_role
    }
    print(context)
    return render(request, 'admin_app/competency/aa_competency_staff.html', context=context)

@login_required
def admin_competency_staff_add(request, user_id):
    user = get_object_or_404(User, id=user_id)  # Fetch the User based on the passed user_id
    StaffQualificationFormSet = modelformset_factory(
        StaffQualification,
        form=StaffQualificationForm,
        extra=1,  # Adjust extra forms as needed
    )
    if request.method == 'POST':
        staff_form = StaffForm(request.POST)
        role_form = StaffRoleForm(request.POST)
        qualification_formset = StaffQualificationFormSet(request.POST, prefix='qualification')

        if all([staff_form.is_valid(), role_form.is_valid(), qualification_formset.is_valid()]):
            staff = staff_form.save(commit=False)
            staff.user = user
            staff.save()

            role = role_form.save(commit=False)
            role.staff = staff
            role.save()

            for qualification_form in qualification_formset:
                qualification = qualification_form.save(commit=False)
                qualification.staff = staff
                qualification.save()

            return redirect('staff_list')  # Redirect to a relevant page
    else:
        staff_form = StaffForm()
        role_form = StaffRoleForm()
        qualification_formset = StaffQualificationFormSet(prefix='qualification')

    context = {
        'staff_form': staff_form,
        'role_form': role_form,
        'qualification_formset': qualification_formset,
        'user': user,
    }
    return render(request, 'admin_app/competency/aa_competency_staff_add_edit.html', context=context)

@login_required
def add_or_edit_staff(request, user_id, staff_id=None):
    user = get_object_or_404(User, id=user_id)
    StaffRoleFormSet = modelformset_factory(StaffRole, form=StaffRoleForm, extra=1, can_delete=True)
    StaffQualificationFormSet = modelformset_factory(StaffQualification, form=StaffQualificationForm, extra=1, can_delete=True)

    if staff_id:
        staff = get_object_or_404(Staff, id=staff_id, user=user)
        staff_form = StaffForm(request.POST or None, instance=staff)
        role_formset = StaffRoleFormSet(request.POST or None, queryset=staff.staffrole_set.all())
        qualification_formset = StaffQualificationFormSet(request.POST or None, queryset=staff.staffqualification_set.all())
    else:
        staff_form = StaffForm(request.POST or None)
        role_formset = StaffRoleFormSet(request.POST or None, queryset=StaffRole.objects.none())
        qualification_formset = StaffQualificationFormSet(request.POST or None, queryset=StaffQualification.objects.none())

    if request.method == 'POST':
        if staff_form.is_valid() and role_formset.is_valid() and qualification_formset.is_valid():
            # Save staff
            new_staff = staff_form.save(commit=False)
            new_staff.user = user
            new_staff.save()

            # Save roles
            for form in role_formset:
                role = form.save(commit=False)
                role.staff = new_staff
                role.save()
                form.save_m2m()

            # Save qualifications
            for form in qualification_formset:
                qualification = form.save(commit=False)
                qualification.staff = new_staff
                qualification.save()
                form.save_m2m()

            return redirect('success_page')  # Change to appropriate redirect

    context = {
        'staff_form': staff_form,
        'role_formset': role_formset,
        'qualification_formset': qualification_formset,
    }
    return render(request, 'admin_app/competency/aa_competency_staff_add_edit.html', context=context)