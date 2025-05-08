
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'phone_number', 'is_staff']
    list_filter = ['is_staff', 'is_active']
    search_fields = ['username', 'email', 'phone_number']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('اطلاعات شخصی', {'fields': ('first_name', 'last_name', 'email', 'phone_number')}),
        ('مجوزها', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('تاریخ‌های مهم', {'fields': ('last_login', 'date_joined')}),
    )