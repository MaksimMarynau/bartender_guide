from rest_framework import serializers

from cocktails.models import Style, Cocktail, CocktailIngredient


class StyleSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='style_detail',
        lookup_field='title_s',
    )
    cocktails = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True,
        many=True
    )

    class Meta:
        model = Style
        fields = ('url','title_s','cocktails')


class CocktailSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='cocktail_detail',
        lookup_field='slug',
    )
    cocktail_ingredients = serializers.StringRelatedField(many=True)
    style = StyleSerializer(many=True)
    bartender = serializers.StringRelatedField()

    class Meta:
        model = Cocktail
        fields = ('url','name','slug','serve_in','garnish','how_to_make','cocktail_ingredients','review','history','nutrition','style','bartender','draft',)


class CocktailIngredientSerializer(serializers.ModelSerializer):

    cocktails_list = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True,
        many=True
    )
    ingredient = serializers.SlugRelatedField(
        slug_field='title_i',
        read_only=True,
    )

    class Meta:
        model = CocktailIngredient
        fields = ('how_many','ingredient','cocktails_list')
