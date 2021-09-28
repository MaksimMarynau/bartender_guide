from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        min_length=4,
        max_length=16,
        help_text='Passwords must match.'
    )
    account_type = serializers.StringRelatedField(read_only=True)
    user_cocktails = serializers.StringRelatedField(many=True, read_only=True)
    user_ingredients = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id','username','email','first_name','last_name','password','password2','user_cocktails','user_ingredients','account_type')

        extra_kwargs = {
            'password': {
                'write_only': True,
                'min_length': 4,
                'max_length': 16,
                'style' : {'input_type': 'password'},
                'help_text': 'Create password min 4 and max 16 characters.'
            },
        }

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        validated_data.pop('password2')
        
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update a user, setting the password correctly and return it"""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user
