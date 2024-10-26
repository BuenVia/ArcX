# from django.db import models
# from django.contrib.auth.models import User

# class ClientUserPDF(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)  # Many-to-One relationship
#     pdf = models.FileField(upload_to='pdfs/')
#     uploaded_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.user.username}'s PDF uploaded at {self.uploaded_at}"