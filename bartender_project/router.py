from rest_framework import routers

from cocktails.api.viewsets import StyleViewSet, CocktailViewSet, CocktailIngredientViewSet
from ingredients.api.viewsets import CategoryViewSet, IngredientViewSet


router = routers.DefaultRouter()
router.register('styles', StyleViewSet, basename='styles')
router.register('cocktails', CocktailViewSet, basename='cocktails')
router.register('cocktail_ingredients', CocktailIngredientViewSet, basename='cocktail_ingredients')
router.register('categories', CategoryViewSet, basename='categories')
router.register('ingredients', IngredientViewSet, basename='ingredients')
