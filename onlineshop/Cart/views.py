from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Cart
from .serializers import CartSerializer
from CartItem.models import CartItem

class CreateCartApi(generics.CreateAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)




class GetCartApi(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    def get_object(self):
        return Cart.objects.get(user=self.request.user)

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

#Empty the cart
class DeleteCartItemsApi(generics.DestroyAPIView):
    def get_queryset(self):
        user = self.request.user
        return user.Cart.CartItem.objects.all()

    def perform_destroy(self, instance):
        instance.delete()

    permission_classes = [IsAuthenticated]


