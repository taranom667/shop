from django.contrib.auth.models import User
from rest_framework import serializers
from User.models import CustomUser



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"
        extra_kwargs = {'password': {'write_only': True}}





class Serializer(serializers.ModelSerializer):
    pass