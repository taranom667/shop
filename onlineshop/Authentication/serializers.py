from django.contrib.auth.models import User
from rest_framework import serializers
from User.models import CustomUser
from Cart.models import Cart
from Wishlist.models import Wishlist


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('first_name','last_name','email','phone_number','username' ,'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(**validated_data)
        user.set_password(validated_data['password'])
        created=user.save()
        if created:
            Cart.objects.create(user=user)
            Wishlist.objects.create(user=user)

        return user
