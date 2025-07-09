from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('student', 'Student'),
        ('parent', 'Parent'),
    )
    name = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        full_name = f"{self.first_name} {self.last_name}".strip()
        return full_name if full_name else self.username

class Student(models.Model):
    full_name = models.CharField(max_length=100)
    parent = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'parent'})
    admission_number = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField()
    fee_payment = models.IntegerField(default=0)
    fee_balance = models.IntegerField(default=0)

    def __str__(self):
        return self.full_name
    
class Parent(models.Model):
    full_name = models.CharField(max_length=100)
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'student'}, related_name='parent')
    phone_number = models.CharField(max_length=15, blank=True, null=True)


    def __str__(self):
        return self.full_name
    
    # Git commit message to changes made in users/models.py
# Added User model with role choices, phone number, and custom string representation.
