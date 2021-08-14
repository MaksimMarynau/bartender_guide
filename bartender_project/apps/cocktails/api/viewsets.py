from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import (
    StyleSerializer,
    CocktailSerializer,
    CocktailIngredientSerializer,
)
from cocktails.models import Style, Cocktail, CocktailIngredient


class StyleViewSet(viewsets.ModelViewSet):
    queryset = Style.objects.all()
    serializer_class = StyleSerializer
    permission_classes = [IsAuthenticated]


class CocktailViewSet(viewsets.ModelViewSet):
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer
    permission_classes = [IsAuthenticated]


class CocktailIngredientViewSet(viewsets.ModelViewSet):
    queryset = CocktailIngredient.objects.all()
    serializer_class = CocktailIngredientSerializer
    permission_classes = [IsAuthenticated]
