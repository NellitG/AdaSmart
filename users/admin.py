from django.contrib import admin
from .models import User, Student, Parent
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

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

    def balance(self, obj):
        return obj.balance
