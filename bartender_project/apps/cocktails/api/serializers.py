from rest_framework import serializers

from core.models import Style, Cocktail, CocktailIngredient


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


class CocktailIngredientCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CocktailIngredient
        fields = '__all__'



class CocktailIngredientSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='ci_detail',
        lookup_field='pk',
    )
    ingredient = serializers.SlugRelatedField(
        slug_field='title_i',
        read_only=True,
    )

    class Meta:
        model = CocktailIngredient
        fields = ('url','ingredient',)


class CocktailIngredientDetailSerializer(serializers.ModelSerializer):

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


class CocktailCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cocktail
        exclude = ('bartender',)


class CocktailSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='cocktail_detail',
        lookup_field='slug',
    )
    style = StyleSerializer(many=True)
    bartender = serializers.StringRelatedField()

    class Meta:
        model = Cocktail
        fields = ('url','name','style','bartender',)


class CocktailDetailSerializer(serializers.ModelSerializer):

    cocktail_ingredients = CocktailIngredientSerializer(many=True) #required=False, allow_null=True
    style = StyleSerializer(many=True, read_only=True)
    bartender = serializers.StringRelatedField()

    class Meta:
        model = Cocktail
        fields = ('name','slug','serve_in','garnish','how_to_make','cocktail_ingredients','review','history','nutrition','style','bartender','draft',)
