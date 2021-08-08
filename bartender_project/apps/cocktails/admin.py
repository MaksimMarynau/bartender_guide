from django.contrib import admin

from .models import Style, Cocktail, CocktailIngredient


class StyleAdmin(admin.ModelAdmin):
    list_display = ['title_s',]

class CocktailAdmin(admin.ModelAdmin):
    list_display = ['name','slug','created','updated','draft',]
    filter_horizontal = ('cocktail_ingredients','style')

class CocktailIngredientAdmin(admin.ModelAdmin):
    list_display = ['how_many','ingredients']


admin.site.register(Style, StyleAdmin)
admin.site.register(Cocktail, CocktailAdmin)
admin.site.register(CocktailIngredient, CocktailIngredientAdmin)
