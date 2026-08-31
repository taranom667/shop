from django.contrib.admin.utils import lookup_field
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializers import OrderSerializer
from Cart.models import Cart

class GetOrdersApi(generics.ListAPIView):
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

class GetOrderApi(generics.RetrieveAPIView):
    lookup_field = 'id'
    def get_queryset(self):
        return Order.objects.get(user=self.request.user,id=lookup_field)
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

class CreateOrderApi(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]




    


    

