from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from .models import User

# Register your models here.

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User

class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    list_display = ('email', 'username', 'is_staff', 'is_superuser')
    search_fields = ('email', 'username')
    list_filter = ('is_staff', 'is_superuser')
    fieldsets = (
        ('Login Info', {'fields': (
            'email',
            'password'
        )}),
        ('Personal info', {'fields': (
            'username',
            'phone',
            'description'
        )}),
        ('Permissions', {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions'
        )}),
        ('Important Dates', {'fields': (
            'date_joined',
            'last_login'
        )}),
    )

admin.site.register(User, CustomUserAdmin)
