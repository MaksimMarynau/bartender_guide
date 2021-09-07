from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView

)

from account.permissions import (
    IsOwner,
    HasMakeCocktailPermission,
)
from .api.serializers import (
    StyleSerializer,
    CocktailSerializer,
    CocktailIngredientSerializer,
)
from cocktails.models import Style, Cocktail, CocktailIngredient


class StyleCreateView(CreateAPIView):
    serializer_class = StyleSerializer
    permission_classes = [IsAuthenticated, HasMakeCocktailPermission]

style_create_view = StyleCreateView.as_view()


class StyleDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = StyleSerializer
    permission_classes = [IsAuthenticated]
    queryset = Style.objects.all()
    lookup_field = 'title_s'

style_detail_view = StyleDetailView.as_view()


class CocktailIngredientCreateView(CreateAPIView):
    serializer_class = CocktailIngredientSerializer
    permission_classes = [IsAuthenticated, HasMakeCocktailPermission]


cocktailingredient_create_view = CocktailIngredientCreateView.as_view()


class CocktailIngredientListView(ListAPIView):
    serializer_class = CocktailIngredientSerializer
    permission_classes = [AllowAny]
    queryset = CocktailIngredient.objects.all()

cocktailingredient_list_view = CocktailIngredientListView.as_view()


class CocktailIngredientDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CocktailIngredientSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = CocktailIngredient.objects.all()
    lookup_field = 'ingredients.title_i'

cocktailingredient_detail_view = CocktailIngredientDetailView.as_view()


class CocktailCreateView(CreateAPIView):
    serializer_class = CocktailSerializer
    permission_classes = [IsAuthenticated, HasMakeCocktailPermission]

    def perform_create(self, serializer: CocktailSerializer):
        serializer.save(bartender=self.request.user)

cocktail_create_view = CocktailCreateView.as_view()


class CocktailListView(ListAPIView):
    serializer_class = CocktailSerializer
    permission_classes = [AllowAny]
    queryset = Cocktail.objects.all()

cocktail_list_view = CocktailListView.as_view()


class CocktailDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CocktailSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = Cocktail.objects.all()
    lookup_field = 'slug'

cocktail_detail_view = CocktailDetailView.as_view()
