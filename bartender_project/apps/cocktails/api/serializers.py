from rest_framework import serializers

from cocktails.models import Style, Cocktail, CocktailIngredient


class StyleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Style
        fields = ('url','title_s','cocktails')


class CocktailSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Cocktail
        fields = ('url','name','slug','serve_in','garnish','how_to_make','cocktail_ingredients','review','history','nutrition','style','draft',)

class CocktailIngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CocktailIngredient
        fields = ('url','how_many','ingredients','cocktails_list')
