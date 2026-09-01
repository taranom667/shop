from rest_framework import request
from CartItem.models import CartItem
from .models import OrderItem
from .serializers import OrderItemSerializer


class CreateOrderItemApi(request):
    if request.method == 'POST':
        serializer = OrderItemSerializer(request.POST)
        if serializer.is_valid():
            cart_item = CartItem(request)
            user = cart_item.Cart.user
            OrderItem.objects.create(
                name=cart_item.product.name,
                price=cart_item.product.price,
                quantity=cart_item.quantity
            )
