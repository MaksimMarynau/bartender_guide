from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import CustomUser, AccountType


class AccountTypeAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'make_cocktail',
        'add_ingredient',
        'generate_temp_link',
    ]


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'account_type',]
    readonly_fields = ['date_joined','last_login']
    fieldsets = (
        (None, {'fields': ('username', 'password', 'account_type')}),
        (_('Personal info'), {'classes': ('collapse',), 'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'classes': ('collapse',),
                            'fields': ('is_admin','is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'classes': ('collapse',), 'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(CustomUser, UserAdmin)
admin.site.register(AccountType, AccountTypeAdmin)
