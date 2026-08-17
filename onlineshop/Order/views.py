from rest_framework import generics, request
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
        return Order.objects.filter(user=self.request.user)
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

class CreateOrderApi(request):
    #check in ke pardakht anjam shode
    if request.method == 'POST':
        serializer = OrderSerializer(request.POST)
        if serializer.is_valid():
            cart=Cart(request)
            user=cart.user
            Order.objects.create(
                status = "payed",
                user=user)



    


    

