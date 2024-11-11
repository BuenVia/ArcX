from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Equipment, Staff, StaffRole, RoleNames, StaffQualification, UserProfile
from django.forms import inlineformset_factory


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

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
    

class AddUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    repeat_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    # Override the clean method to validate the passwords
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        repeat_password = cleaned_data.get('repeat_password')

        if password != repeat_password:
            raise ValidationError("Passwords do not match.")

        return cleaned_data

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["business_name", "address_one", "address_two", "town", "county", "postcode", "telephone"]


class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name', 'item_number', 'make', 'model', 'serial_number', 'equipment_group']

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['first_name', 'last_name', 'staff_id']

class StaffRoleForm(forms.ModelForm):
    role = forms.ModelChoiceField(
        queryset=RoleNames.objects.all(),
        empty_label="Select Role",
        widget=forms.Select
    )

    class Meta:
        model = StaffRole
        fields = ['role']

class StaffQualificationForm(forms.ModelForm):
    class Meta:
        model = StaffQualification
        fields = ['qualification', 'qualification_date']

# Create formsets for inline use
StaffRoleFormSet = inlineformset_factory(
    Staff, StaffRole, form=StaffRoleForm, extra=1, can_delete=True
)
StaffQualificationFormSet = inlineformset_factory(
    Staff, StaffQualification, form=StaffQualificationForm, extra=1, can_delete=True
)