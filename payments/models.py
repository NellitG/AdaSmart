from django.db import models
from users.models import User


# Create your models here.

class FeePayment(models.Model):
    parent = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'parent'},
        related_name='payments_as_parent'
    )
    student_name = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'student'},
        related_name='payments_as_student'
    )
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20)
    payment_date = models.DateField()
    receipt_url = models.URLField(blank=True, null=True)


    def __str__(self):
        return f"{self.student_name} - {self.amount_paid} KES"

class FeeBalance(models.Model):
    parent = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'role': 'parent'})
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)