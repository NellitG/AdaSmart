from django.contrib import admin
from .models import FeePayment
from django.utils.html import format_html

# Register your models here.
@admin.register(FeePayment)
class FeePaymentAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'amount_paid', 'payment_date', 'payment_method', 'view_receipt')

    def view_receipt(self, obj):
        if obj.receipt_url:
            return format_html(f'<a href="{obj.receipt_url}" target="_blank">Download</a>')
        return "-"
