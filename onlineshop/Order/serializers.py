from rest_framework import serializers

from onlineshop.Order.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
