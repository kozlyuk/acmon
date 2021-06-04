from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.accounts.forms import CustomUserCreationForm, CustomUserChangeForm
from apps.accounts.models import User


class UserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('last_name', 'first_name', 'mobile_number', 'email', 'is_staff', 'is_active',)
    list_filter = ('mobile_number', 'email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'email', 'birth_date', 'avatar')}),
        ('Permissions', {'fields': ('groups', 'is_staff', 'is_active', 'is_registered', 'password')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('mobile_number', 'password1', 'password2')
        }),
    )
    search_fields = ('mobile_number', 'email',)
    ordering = ('last_name', 'first_name',)


# class OperatorAdmin(admin.ModelAdmin):
#     list_display = ['user']
#     readonly_fields = []


# class DriverAdmin(admin.ModelAdmin):
#     list_display = ['user']
#     readonly_fields = []


admin.site.register(User, UserAdmin)
# admin.site.register(Operator, OperatorAdmin)
# admin.site.register(Driver, DriverAdmin)
