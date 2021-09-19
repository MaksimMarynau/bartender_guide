# from django.contrib import admin
#
# from .models import Category, Ingredient
#
#
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['id','title_c',]
#
#
# class IngredientAdmin(admin.ModelAdmin):
#     list_display = [
#         'title_i',
#         'bartender',
#         'created',
#         'updated',
#         'draft',
#     ]
#     filter_horizontal = ('category',)
#     prepopulated_fields = {'slug':('title_i',)}
#
#
# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Ingredient, IngredientAdmin)
