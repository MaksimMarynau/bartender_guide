from rest_framework import serializers

from core.models import Style, Cocktail
from ingredients.api.serializers import IngredientCreateSerializer

class StyleCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Style
        fields = ('title_s',)


class StyleSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='style_detail',
        lookup_field='title_s',
    )

    class Meta:
        model = Style
        fields = ('url','title_s')


class StyleDetailSerializer(serializers.ModelSerializer):

    cocktails = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True,
        many=True
    )

    class Meta:
        model = Style
        fields = ('title_s','cocktails')


class CocktailCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cocktail
        exclude = ('user',)


class CocktailSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='cocktail_detail',
        lookup_field='slug',
    )
    style = StyleSerializer(many=True)
    user = serializers.StringRelatedField()

    class Meta:
        model = Cocktail
        fields = ('url','name','style','user',)
        ordering = ('name',)


class CocktailDetailSerializer(serializers.ModelSerializer):

    style = StyleSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField()
    cocktail_item = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Cocktail
        fields = ('name','slug','serve_in','garnish','how_to_make','review','history','nutrition','style','user','draft','cocktail_item')
