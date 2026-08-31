from rest_framework import serializers

from .models import OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields =('id','name','order','price_at_time','quantity','created_at','updated_at')
        read_only_fields = ('id',)
