from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView

)

from core.permissions import (
    IsOwner,
    HasMakeCocktailPermission,
)
from .api.serializers import (
    StyleCreateSerializer,
    StyleDetailSerializer,
    CocktailSerializer,
    CocktailCreateSerializer,
    CocktailDetailSerializer,
)
from core.models import Style, Cocktail


class StyleCreateView(CreateAPIView):
    serializer_class = StyleCreateSerializer
    permission_classes = [IsAuthenticated, HasMakeCocktailPermission]


style_create_view = StyleCreateView.as_view()


class StyleDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = StyleDetailSerializer
    permission_classes = [IsAuthenticated]
    queryset = Style.objects.all()
    lookup_field = 'title_s'


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
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = Cocktail.objects.all()
    lookup_field = 'slug'


cocktail_detail_view = CocktailDetailView.as_view()
