from rest_framework import serializers

from ingredients.models import Category, Ingredient

class CategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Category
        fields = ('url','pk','title_c','ingredients')

class IngredientSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Ingredient
        fields = ('url','title_i','slug','alc_product_of','aroma','taste','description','size','draft','category','cocktail_ingredients')
