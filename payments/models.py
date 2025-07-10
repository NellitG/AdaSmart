from django.db import models
from users.models import Student, User

class FeePayment(models.Model):
    parent = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'parent'}, related_name='payments_as_parent')
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20)
    payment_date = models.DateField()
    
    def __str__(self):
        return f"{self.student.full_name} paid {self.amount_paid} KES"

class FeeBalance(models.Model):
    parent = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'role': 'parent'})
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)