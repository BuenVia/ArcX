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
        return f"{self.role}: {self.qualification_name}"
    

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

# Repo of all equipment, regardless of ueser
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

# Euipment linked to a user
class EquipmentUser(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "equipment_user"

    def __str__(self):
        return f"{self.equipment} {self.user}"

class EquipmentTest(models.Model):
    calibrate_date = models.DateField(blank=True, null=True)
    calibrate_freq = models.IntegerField(blank=True, null=True)
    service_date = models.DateField(blank=True, null=True)
    servcice_freq = models.IntegerField(blank=True, null=True)
    inspection_date = models.DateField(blank=True, null=True)
    inspection_freq = models.IntegerField(blank=True, null=True)
    test_date = models.DateField(blank=True, null=True)
    test_freq = models.IntegerField(blank=True, null=True)
    equipmentuser = models.ForeignKey(EquipmentUser, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "equipment_test"

    def __str__(self):
        return f"{self.equipmentuser} Test Data"

    