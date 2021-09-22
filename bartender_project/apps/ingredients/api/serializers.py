from rest_framework import serializers

from core.models import Category, Ingredient


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

    ingredients = serializers.StringRelatedField(
        read_only=True,
        many=True
    )

    class Meta:
        model = Category
        fields = ('title_c','ingredients')


class IngredientCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        exclude = ('user',)


class IngredientSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='ingredient_detail',
        lookup_field='title_i',
    )
    category = CategorySerializer(many=True)

    class Meta:
        model = Ingredient
        fields = ('url','title_i','category')


class IngredientDetailSerializer(serializers.ModelSerializer):

    category = CategorySerializer(many=True,read_only=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Ingredient
        fields = ('title_i','amount','category','user')
