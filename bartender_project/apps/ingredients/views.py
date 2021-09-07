from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView

)

from account.permissions import (
    IsOwner,
    HasAddIngredientPermission,
)
from ingredients.models import (
    Category,
    Ingredient
)
from .api.serializers import (
    CategorySerializer,
    IngredientSerializer,
)


class CategoryCreateView(CreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, HasAddIngredientPermission]

category_create_view = CategoryCreateView.as_view()


class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    lookup_field = 'title_c'

category_detail_view = CategoryDetailView.as_view()


class IngredientCreateView(CreateAPIView):
    serializer_class = IngredientSerializer
    permission_classes = [IsAuthenticated, HasAddIngredientPermission]

    def perform_create(self, serializer: IngredientSerializer):
        serializer.save(bartender=self.request.user)

ingredient_create_view = IngredientCreateView.as_view()


class IngredientListView(ListAPIView):
    serializer_class = IngredientSerializer
    permission_classes = [AllowAny]
    queryset = Ingredient.objects.all()

ingredient_list_view = IngredientListView.as_view()


class IngredientDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = IngredientSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = Ingredient.objects.all()
    lookup_field = 'slug'

ingredient_detail_view = IngredientDetailView.as_view()
