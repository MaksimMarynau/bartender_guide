from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import (
    CategorySerializer,
    IngredientSerializer,
)
from ingredients.models import Category, Ingredient


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [IsAuthenticated]
