from django.contrib import admin
from .models import User, Student, Parent
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.urls import reverse
from django.utils.html import format_html

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Extra Info', {'fields': ('name', 'role', 'phone_number')}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Extra Info', {'fields': ('name', 'phone_number')}),
    )
    list_display = ('name', 'phone_number')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'admission_number', 'parent', 'total_paid', 'balance')
    readonly_fields = ('total_paid', 'balance')

    def total_paid(self, obj):
        return obj.total_paid
    total_paid.short_description = 'Total Paid'

    def balance(self, obj):
        return obj.balance
    balance.short_description = 'Balance'

    def download_balance_pdf(self, obj):
        url = reverse('balance_pdf', args=[obj.id])
        return format_html(f'<a class="button" href="{url}" target="_blank" >Download Balance PDF</a>')
    download_balance_pdf.short_description = 'Download Balance PDF'
