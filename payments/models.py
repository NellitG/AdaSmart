from django.db import models
from users.models import User

# Create your models here.
# Create a fee payment model
class FeePayment(models.Model):
    parent = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'parent'})
    student_name = models.CharField(max_length=100)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    payment_date = models.DateTimeField(auto_now_add=True)
    receipt_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.student_name} - {self.amount_paid} KES"

class FeeBalance(models.Model):
    parent = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'role': 'parent'})
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)