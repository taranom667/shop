from rest_framework import serializers
from rest_framework.response import Response

from onlineshop.Order.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields=('id','status','user','total_amount','created_at','updated_at','address')
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

    def create(self,validated_data):
        Order.objects.create(**validated_data)
        return Order.objects.get(id=validated_data['id'])



    def update(self,instance,validated_data):
        Order.objects.filter(id=instance.id).update(**validated_data)
        return Order.objects.get(id=instance.id)


    def list(self,request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders,many=True)
        return Response(serializer.data)

