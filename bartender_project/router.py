from rest_framework import routers

from cocktails.api.viewsets import StyleViewSet, CocktailViewSet, CocktailIngredientViewSet
from ingredients.api.viewsets import CategoryViewSet, IngredientViewSet
from account.api.viewsets import CustomUserViewSet

router = routers.DefaultRouter()

router.register('users', CustomUserViewSet, basename='customuser')
router.register('styles', StyleViewSet, basename='style')
router.register('cocktails', CocktailViewSet, basename='cocktail')
router.register('cocktail_ingredients', CocktailIngredientViewSet,
                basename='cocktailingredient')
router.register('categories', CategoryViewSet, basename='category')
router.register('ingredients', IngredientViewSet, basename='ingredient')
