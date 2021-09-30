from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView

)

from core.permissions import (
    IsOwnerOrIsAdminUser,
    HasMakeCocktailPermission,
)
from .serializers import (
    StyleCreateSerializer,
    StyleDetailSerializer,
    CocktailSerializer,
    CocktailCreateSerializer,
    CocktailDetailSerializer,
    ReviewCreateSerializer,
)
from core.models import Style, Cocktail, Review


class StyleCreateView(CreateAPIView):
    serializer_class = StyleCreateSerializer
    permission_classes = [IsAuthenticated, HasMakeCocktailPermission]

    def perform_create(self, serializer: StyleCreateSerializer):
        serializer.save(user=self.request.user)

style_create_view = StyleCreateView.as_view()


class StyleDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = StyleDetailSerializer
    permission_classes = [IsAuthenticated]
    queryset = Style.objects.all()
    lookup_field = 'title_s'

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE', 'PATCH']:
            return [IsOwnerOrIsAdminUser()]
        return []

    def get_authenticators(self):
        if self.request.method in ['PUT', 'DELETE', 'PATCH']:
            return [JWTAuthentication()]
        return []


style_detail_view = StyleDetailView.as_view()


class CocktailCreateView(CreateAPIView):
    serializer_class = CocktailCreateSerializer
    permission_classes = [IsAuthenticated, HasMakeCocktailPermission]

    def perform_create(self, serializer: CocktailCreateSerializer):
        serializer.save(user=self.request.user)


cocktail_create_view = CocktailCreateView.as_view()


class CocktailListView(ListAPIView):
    serializer_class = CocktailSerializer
    permission_classes = [AllowAny]
    queryset = Cocktail.objects.all()


cocktail_list_view = CocktailListView.as_view()


class CocktailDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CocktailDetailSerializer
    queryset = Cocktail.objects.all()
    lookup_field = 'slug'

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE', 'PATCH']:
            return [IsOwnerOrIsAdminUser()]
        return []

    def get_authenticators(self):
        if self.request.method in ['PUT', 'DELETE', 'PATCH']:
            return [JWTAuthentication()]
        return []

cocktail_detail_view = CocktailDetailView.as_view()


class ReviewCreateView(CreateAPIView):
    serializer_class = ReviewCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer: ReviewCreateSerializer):
        serializer.save(user=self.request.user)

review_create_view = ReviewCreateView.as_view()
