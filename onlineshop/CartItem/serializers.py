from rest_framework import serializers

from .models import CartItem


class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields=('id', 'cart','product','quantity','created_at','updated_at','price_at_purchase')
        read_only_fields=('id', 'created_at','updated_at')

    def get_total_price(self, obj):
        return obj.price_at_purchase*obj.quantity

