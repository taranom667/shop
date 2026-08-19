from django.contrib.auth.models import User
from rest_framework import generics,request
from rest_framework.permissions import IsAuthenticated
from .models import Cart
from .serializers import CartSerializer
from CartItem.models import CartItem

# yekari kon be mahz sakht user enam sakhte she va kolan yek doonas

'''class DeleteCartApi(request):
    Cart = request.user.Cart
    Cart.CartItem.objects.all().delete()


class CreateCartApi(generics.CreateAPIView):
    user =request.user
    serializer_class = CartSerializer'''


class GetCartApi(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.get(user=self.request.user)
