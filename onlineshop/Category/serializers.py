from rest_framework import serializers

from onlineshop.Category.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ( 'name','products')
