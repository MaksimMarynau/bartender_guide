from rest_framework import serializers

from account.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('id','username','bartender_cocktails','bartender_ingredients')
