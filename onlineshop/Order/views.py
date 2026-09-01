from django.contrib.admin.utils import lookup_field
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializers import OrderSerializer
from Cart.models import Cart
from CartItem.models import CartItem
from Address.models import Address
from OrderItem.models import OrderItem


class GetOrdersApi(generics.ListAPIView):
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-created_at')
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
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user

        try:
            cart = Cart.objects.get(user=user)
            cart_items = CartItem.objects.filter(cart=cart)

            if not cart_items.exists():
                raise Exception("Cart is empty")

            # Calculate total
            total = sum(item.total_price for item in cart_items)

            # Get address from request
            address_id = self.request.data.get('address_id')

            address = Address.objects.get(id=address_id, user=user)

            # Create order
            order = serializer.save(user=user, total_amount=total, address=address)

            # Create order items from cart items

            for item in cart_items:
                OrderItem.objects.create(
                    Order=order,
                    name=item.product.name,
                    price_at_time=item.product.price,
                    quantity=item.quantity
                )

            # Clear cart
            cart_items.delete()

        except Cart.DoesNotExist:
            raise Exception("Cart not found")



    


    

