from rest_framework import serializers

from ingredients.models import Category, Ingredient
from cocktails.api.serializers import CocktailIngredientSerializer


class CategoryCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('title_c',)


class CategorySerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='category_detail',
        lookup_field='title_c',
    )

    class Meta:
        model = Category
        fields = ('url','title_c',)


class CategoryDetailSerializer(serializers.ModelSerializer):

    ingredients = serializers.SlugRelatedField(
        slug_field='title_i',
        read_only=True,
        many=True
    )

    class Meta:
        model = Category
        fields = ('title_c','ingredients')


class IngredientCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        exclude = ('bartender',)


class IngredientSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='ingredient_detail',
        lookup_field='slug',
    )
    category = CategorySerializer(many=True)

    class Meta:
        model = Ingredient
        fields = ('url','title_i','category')


class IngredientDetailSerializer(serializers.ModelSerializer):

    category = CategorySerializer(many=True,read_only=True)
    cocktail_ingredient = CocktailIngredientSerializer(read_only=True, many=True)

    class Meta:
        model = Ingredient
        fields = ('title_i','slug','alc_product_of','aroma','taste','description','size','draft','category','cocktail_ingredient')
