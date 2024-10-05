from django import forms
from django.core.exceptions import ValidationError

class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    repeat_password = forms.CharField(widget=forms.PasswordInput)

    # Override the clean method to add custom validation
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        repeat_password = cleaned_data.get('repeat_password')

        # Check if the passwords match
        if password and repeat_password and password != repeat_password:
            raise ValidationError("Passwords do not match.")
        
        return cleaned_data
