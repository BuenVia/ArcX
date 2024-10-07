# models.py
from django.db import models
from django.contrib.auth.models import User

class ClientUserPDF(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Associate each PDF with a single user
    pdf = models.FileField(upload_to='pdfs/')  # This field handles file uploads
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s PDF"
