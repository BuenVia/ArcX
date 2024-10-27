from datetime import date
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch, Min
from django.shortcuts import render, redirect, get_object_or_404
# from .forms import ClientUserPDFForm
# from .models import ClientUserPDF
from django.utils import timezone
from admin_app.models import DocumentClient, DocumentTitle, Staff, StaffRole, StaffQualification
from .forms import DocumentUploadForm

# Login/ Logout/ Dashboard
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
    # Documents
    documents = DocumentClient.objects.filter(user=request.user)
    complete = 0
    for doc in documents:
        if doc.uploaded:
            complete += 1
    all_docs = len(documents)
    #Staff
    staff = Staff.objects.filter(user=request.user)
    print(staff)
    staff_num = len(staff)
    #Equipment

    context = {
        'complete': complete, 
        'all_docs': all_docs,
        'staff_num': staff_num
        }
    return render(request, 'client_app/dashboard.html', context=context)
    # return render(request, 'client_app/dashboard.html', {'documents': [], 'complete': 0, 'all_docs': 0})


### DOCUMENTATION
@login_required
def document_review(request):
    user_documents = DocumentClient.objects.filter(user=request.user)
    return render(request, 'client_app/documents.html', {'user_documents': user_documents})

@login_required
def upload_document(request, id):
    document_title = get_object_or_404(DocumentTitle, id=id)

    if request.method == 'POST':
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Clean the filename
            original_file_name = request.FILES['document_file'].name
            cleaned_filename = f"{request.user.username.replace('.', '_').replace(' ', '_')}_{document_title.title.replace('.', '_').replace(' ', '_')}.pdf"

            # Save the file
            document_client = DocumentClient.objects.get(user=request.user, document=document_title)
            document_client.file.save(cleaned_filename, request.FILES['document_file'])

            # Update upload status and date
            document_client.uploaded = True
            document_client.created_date = timezone.now()
            document_client.save()

            return redirect('document_review')  # Redirect after successful upload

    else:
        form = DocumentUploadForm()

    return render(request, 'client_app/upload_document.html', {'form': form, 'document_title': document_title})


@login_required
def client_staff(request):
    staff_list = Staff.objects.filter(user_id=request.user)\
        .select_related('user')\
        .prefetch_related(
            Prefetch('staffrole_set', queryset=StaffRole.objects.select_related('role')),
            Prefetch('staffqualification_set', queryset=StaffQualification.objects.select_related('qualification'))
        )\
        .annotate(min_role_id=Min('staffrole__role_id'))\
        .order_by('min_role_id')
    today = date.today()
    return render(request, 'client_app/client_staff.html', {'staff_list': staff_list, 'today': today})
"""
- Create chapter model (for the 11 chapters) - will need title, upload date, due date
- Create model for tools and competency
- Create calendar model for the tools and competency

- Front page showing how many documents uploaded and access to calendar
- Document page showing details of each of the 11 chapters - including what has been uploaded and what is out standing.
- Calendar/Date page showing the schedule for:
-   - Equipment/Tool checks
-   - Competency/Acreditation expiry dates
- Front page should show warnings for:
-   - Pending due date of documents
-   - Pending expiry dates of tools/ competency.


"""