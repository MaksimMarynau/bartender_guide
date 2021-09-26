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
    Ingredient,
    IngredientItem
)
from .serializers import (
    CategoryCreateSerializer,
    CategoryDetailSerializer,
    IngredientItemSerializer,
    IngredientItemCreateSerializer,
    IngredientItemDetailSerializer,
    IngredientCreateSerializer,
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


class IngredientItemCreateView(CreateAPIView):
    serializer_class = IngredientItemCreateSerializer
    permission_classes = [IsAuthenticated, HasAddIngredientPermission]

    def perform_create(self, serializer: IngredientItemCreateSerializer):
        serializer.save(user=self.request.user)

ingredient_create_view = IngredientItemCreateView.as_view()


class IngredientCreateView(CreateAPIView):
    serializer_class = IngredientCreateSerializer
    permission_classes = [IsAuthenticated, HasAddIngredientPermission]

add_ingredient_create_view = IngredientCreateView.as_view()


class IngredientItemListView(ListAPIView):
    serializer_class = IngredientItemSerializer
    permission_classes = [AllowAny]
    queryset = IngredientItem.objects.all()

ingredient_list_view = IngredientItemListView.as_view()


class IngredientItemDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = IngredientItemDetailSerializer
    queryset = IngredientItem.objects.all()
    lookup_field = 'title_i'

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE', 'PATCH']:
            return [IsOwnerOrIsAdminUser()]
        return [IsAuthenticated()]

ingredient_detail_view = IngredientItemDetailView.as_view()
