from rest_framework import serializers

from ingredients.models import Category, Ingredient


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('title_c',)


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ('title_i','alc_product_of','aroma','taste','description','size','draft','category','bartender')
