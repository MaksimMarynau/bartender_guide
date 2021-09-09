from rest_framework import serializers

from ingredients.models import Category, Ingredient
from cocktails.api.serializers import CocktailIngredientSerializer


class CategorySerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='category_detail',
        lookup_field='title_c',
    )
    ingredients = serializers.SlugRelatedField(
        slug_field='title_i',
        read_only=True,
        many=True
    )

    class Meta:
        model = Category
        fields = ('url','title_c','ingredients')


class IngredientSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='ingredient_detail',
        lookup_field='slug',
    )
    category = CategorySerializer(many=True)
    cocktail_ingredient = CocktailIngredientSerializer(read_only=True, many=True)

    class Meta:
        model = Ingredient
        fields = ('url','title_i','slug','alc_product_of','aroma','taste','description','size','draft','category','cocktail_ingredient')
