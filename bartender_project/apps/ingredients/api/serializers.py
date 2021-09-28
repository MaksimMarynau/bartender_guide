from rest_framework import serializers

from core.models import Category, Ingredient, IngredientItem


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

    ingredient_in_category = serializers.StringRelatedField(
        read_only=True,
        many=True
    )

    class Meta:
        model = Category
        fields = ('title_c','ingredient_in_category')


class IngredientItemCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = IngredientItem
        exclude = ('user',)


class IngredientCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = '__all__'


class IngredientItemSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='ingredient_detail',
        lookup_field='title_i',
    )
    category = CategorySerializer(many=True)

    class Meta:
        model = IngredientItem
        fields = ('url','title_i','category')


class IngredientItemDetailSerializer(serializers.ModelSerializer):

    category = CategorySerializer(many=True,read_only=True)
    user = serializers.StringRelatedField(read_only=True)
    cocktails = serializers.StringRelatedField(many=True,read_only=True)

    class Meta:
        model = IngredientItem
        fields = '__all__'
