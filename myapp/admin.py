from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

class CustomUserAdmin(UserAdmin):
    # Add the role field to the user list display
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_superuser', 'is_active', 'groups')

    # Add the role field to the form fieldsets (edit user page)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('role', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    # Add the role field to the fields displayed when creating a user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'role', 'is_staff', 'is_active'),
        }),
    )

    # Enable searching by role, username, or email
    search_fields = ('username', 'email', 'role')
    ordering = ('username',)

admin.site.register(User, CustomUserAdmin)
