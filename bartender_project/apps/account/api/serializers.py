from rest_framework import serializers

from account.models import CustomUser

class CustomUserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('url','pk','username','bartender_cocktails','bartender_ingredients')
