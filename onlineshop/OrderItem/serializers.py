from rest_framework import serializers

from .models import OrderItem


class orderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
        read_only_fields = ('id',)
