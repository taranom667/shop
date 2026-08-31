from rest_framework import serializers

from .models import CartItem


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields=('cart','product','quantity','created_at','updated_at','price_at_purchase')