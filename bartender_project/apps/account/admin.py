from django.contrib import admin

from .models import CustomUser, AccountType


class AccountTypeAdmin(admin.ModelAdmin):
    pass

class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(CustomUser, UserAdmin)
admin.site.register(AccountType)
