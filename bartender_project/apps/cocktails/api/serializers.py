from rest_framework import serializers

from cocktails.models import Style, Cocktail, CocktailIngredient


class StyleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Style
        fields = ('title_s',)


class CocktailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cocktail
        fields = ('name','slug','serve_in','garnish','how_to_make','cocktail_ingredients','review','history','nutrition','style','bartender','draft',)

class CocktailIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = CocktailIngredient
        fields = ('how_many','ingredients')
