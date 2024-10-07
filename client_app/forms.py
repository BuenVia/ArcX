# forms.py
from django import forms
from .models import ClientUserPDF

class ClientUserPDFForm(forms.ModelForm):
    class Meta:
        model = ClientUserPDF
        fields = ['pdf']  # Only include the file upload field
