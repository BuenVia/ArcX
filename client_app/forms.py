# forms.py
from django import forms
from django.contrib.auth.forms import PasswordChangeForm
# from .models import ClientUserPDF


# forms.py
class CustomPasswordChangeForm(PasswordChangeForm):
    # Add customizations if necessary, like additional validation or styling
    def __init__(self, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(*args, **kwargs)
        # Adding CSS classes to the form fields
        self.fields['old_password'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control'})


# class ClientUserPDFForm(forms.ModelForm):
#     class Meta:
#         model = ClientUserPDF
#         fields = ['pdf']  # Only include the file upload field




class DocumentUploadForm(forms.Form):
    document_file = forms.FileField(
        label='Select a PDF file',
        required=True,
        max_length=5 * 1024 * 1024  # 5MB limit
    )
