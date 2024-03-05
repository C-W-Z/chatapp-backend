from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User, UserProfile

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('email', 'username', 'last_login', 'date_joined', 'is_staff', 'is_superuser')
    ordering = ('date_joined', 'last_login')
    search_fields = ('email', 'username')
    list_filter = ('is_staff', 'is_superuser')
    readonly_fields = ('date_joined', 'last_login')
    fieldsets = (
        ('Login Info', {'fields': (
            'email',
            'password'
        )}),
        ('Personal info', {'fields': (
            'username',
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
    add_fieldsets = (
        (None,{
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone')
    search_fields = ('user__email', 'user__username', 'phone')
    list_filter = ('user__is_active',)

admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
