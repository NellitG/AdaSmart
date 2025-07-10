from django.contrib import admin
from .models import FeePayment, FeeBalance
from users.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Register your models here.
@admin.register(FeePayment)
class FeePaymentAdmin(admin.ModelAdmin):
    list_display = ('parent', 'amount_paid', 'payment_date', 'payment_method',)

    
@admin.register(FeeBalance)
class FeeBalanceAdmin(admin.ModelAdmin):
    list_display = ('parent', 'balance')
    search_fields = ('parent__name',)


