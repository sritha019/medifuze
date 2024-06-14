from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, TestCategory, Test, Doctor, Appointment, Report

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'address', 'mobile_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('User Type', {'fields': ('user_type',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(TestCategory)
admin.site.register(Test)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Report)
