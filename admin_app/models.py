from django.db import models
from django.contrib.auth.models import User

class DocumentTitle(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        db_table = "document_titles"

    def __str__(self):
        return self.title
    
class DocumentClient(models.Model):
    document = models.ForeignKey(DocumentTitle, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded = models.BooleanField(default=False)
    upload_date = models.DateTimeField(null=True, blank=True)
    file = models.FileField(upload_to='uploads/', null=True, blank=True)  # Add this line for file storage
    
    class Meta:
        db_table = "document_clients"

    def __str__(self):
        return f"{self.user} {self.document} - {self.uploaded}"