# from django.contrib import admin
#
# from .models import Style, Cocktail, CocktailIngredient, Review
#
#
# class StyleAdmin(admin.ModelAdmin):
#     list_display = ['title_s',]
#
#
# class CocktailAdmin(admin.ModelAdmin):
#     list_display = ['name','slug','created','updated','draft',]
#     filter_horizontal = ('cocktail_ingredients','style')
#     prepopulated_fields = {'slug':('name',)}
#
#
# class CocktailIngredientAdmin(admin.ModelAdmin):
#     list_display = ['how_many','ingredient']
#
#
# class ReviewsAdmin(admin.ModelAdmin):
# 	list_display = ('text','parent','cocktail','id')
# 	readonly_fields = ('user',)
#
#
#
# admin.site.register(Style, StyleAdmin)
# admin.site.register(Cocktail, CocktailAdmin)
# admin.site.register(CocktailIngredient, CocktailIngredientAdmin)
# admin.site.register(Review, ReviewsAdmin)
