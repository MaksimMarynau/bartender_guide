from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView

)

from core.permissions import (
    IsOwnerOrIsAdminUser,
    HasAddIngredientPermission,
)
from core.models import (
    Category,
    Ingredient
)
from .serializers import (
    CategoryCreateSerializer,
    CategoryDetailSerializer,
    IngredientSerializer,
    IngredientCreateSerializer,
    IngredientDetailSerializer,

)


class CategoryCreateView(CreateAPIView):
    serializer_class = CategoryCreateSerializer
    permission_classes = [IsAuthenticated, HasAddIngredientPermission]

category_create_view = CategoryCreateView.as_view()


class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategoryDetailSerializer
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    lookup_field = 'title_c'

category_detail_view = CategoryDetailView.as_view()


class IngredientCreateView(CreateAPIView):
    serializer_class = IngredientCreateSerializer
    permission_classes = [IsAuthenticated, HasAddIngredientPermission]

    def perform_create(self, serializer: IngredientCreateSerializer):
        serializer.save(user=self.request.user)

ingredient_create_view = IngredientCreateView.as_view()


class IngredientListView(ListAPIView):
    serializer_class = IngredientSerializer
    permission_classes = [AllowAny]
    queryset = Ingredient.objects.all()

ingredient_list_view = IngredientListView.as_view()


class IngredientDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = IngredientDetailSerializer
    queryset = Ingredient.objects.all()
    lookup_field = 'title_i'

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE', 'PATCH']:
            return [IsOwnerOrIsAdminUser()]
        return [IsAuthenticated()]

ingredient_detail_view = IngredientDetailView.as_view()
