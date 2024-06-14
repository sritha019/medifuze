from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
        ('agent', 'Agent'),
        ('technician', 'Technician'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='patient')
    address = models.TextField()
    mobile_number = models.CharField(max_length=15)

class TestCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Test(models.Model):
    category = models.ForeignKey(TestCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    department = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    address = models.TextField()
    position = models.CharField(max_length=255)
    fees = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    date_booked = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.doctor.name}"

class Report(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    file = models.FileField(upload_to='reports/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.file.name}"
