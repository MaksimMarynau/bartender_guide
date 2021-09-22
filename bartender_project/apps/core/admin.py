from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import CustomUser, AccountType
from .models import Style, Cocktail, Review
from .models import Category, Ingredient


class AccountTypeAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'make_cocktail',
        'add_ingredient',
        'generate_temp_link',
    ]


class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'account_type',]
    readonly_fields = ['date_joined', 'last_login']
    fieldsets = (
        (None, {'fields': ('username', 'password', 'account_type')}),
        (_('Personal info'), {'classes': ('collapse',),
                              'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'classes': ('collapse',),
                            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'classes': ('collapse',),
                                'fields': ('last_login', 'date_joined')}),
    )


class StyleAdmin(admin.ModelAdmin):
    list_display = ['title_s',]


class CocktailAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'updated', 'draft', ]
    filter_horizontal = ('ingredients', 'style')
    prepopulated_fields = {'slug': ('name',)}


# class CocktailIngredientAdmin(admin.ModelAdmin):
#     list_display = ['how_many', 'ingredient']


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('text', 'parent', 'cocktail', 'id')
    readonly_fields = ('user',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title_c',]


class IngredientAdmin(admin.ModelAdmin):
    list_display = [
        'title_i',
        'amount',
        'user',
    ]
    filter_horizontal = ('category',)



admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(AccountType, AccountTypeAdmin)
admin.site.register(Style, StyleAdmin)
admin.site.register(Cocktail, CocktailAdmin)
# admin.site.register(CocktailIngredient, CocktailIngredientAdmin)
admin.site.register(Review, ReviewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Ingredient, IngredientAdmin)
