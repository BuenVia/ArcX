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
    


# COMPETENCY MODEL
# Staff
class Staff(models.Model):
    first_name = models.CharField(max_length=90)
    last_name = models.CharField(max_length=90)
    staff_id = models.CharField(max_length=45)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "staff"

    def __str__(self):
        return f"{self.user.username}: {self.first_name} {self.last_name}"

class RoleNames(models.Model):
    role_name = models.CharField(max_length=90)
    
    class Meta:
        db_table = "role_names"

    def __str__(self):
        return self.role_name

class Qualifications(models.Model):
    qualification_name = models.CharField(max_length=90)
    role = models.ForeignKey(RoleNames, on_delete=models.CASCADE)
    duration = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "qualification"

    def __str__(self):
        return f"{self.role}: {self.qualifiation_name}"
    

class StaffRole(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    role = models.ForeignKey(RoleNames, on_delete=models.CASCADE)

    class Meta:
        db_table = "staff_role"

    def __str__(self):
        return f"{self.staff} {self.role}"
    
class StaffQualification(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    qualification = models.ForeignKey(Qualifications, on_delete=models.CASCADE)
    qualification_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "staff_qualification"

    def __str__(self):
        return f"{self.staff} {self.qualification}"

# TOOLING MODEL
class EquipmentGroup(models.Model):
    name = models.CharField(max_length=90)

    class Meta:
        db_table = "equipment_group"

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=255)
    item_number = models.CharField(max_length=90)
    make = models.CharField(max_length=90)
    model = models.CharField(max_length=90)
    serial_number = models.CharField(max_length=90)
    equipment_group = models.ForeignKey(EquipmentGroup, on_delete=models.CASCADE)

    class Meta:
        db_table = "equipment"

    def __str__(self):
        return self.name


class EquipmentTest(models.Model):
    calibrate_date = models.DateField()
    calibrate_freq = models.IntegerField()
    service_date = models.DateField()
    servcice_freq = models.IntegerField()
    inspection_date = models.DateField()
    inspection_freq = models.IntegerField()
    test_date = models.DateField()
    test_freq = models.IntegerField()
