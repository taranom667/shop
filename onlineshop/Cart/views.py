from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Cart
from .serializers import CartSerializer
from CartItem.models import CartItem


class GetCartApi(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        user = request.user
        return self.retrieve(request, *args, **kwargs)
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.get(user=self.request.user)

#Empty the cart
class DeleteCartItemsApi(generics.DestroyAPIView):
    def get_queryset(self):
        user = self.request.user
        return user.Cart.CartItem.objects.all()

    def perform_destroy(self, instance):
        instance.delete()

    permission_classes = [IsAuthenticated]