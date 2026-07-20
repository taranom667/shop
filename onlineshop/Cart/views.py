from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Cart
from .serializers import CartSerializer


#yekari kon be mahz sakht user enam sakhte she va kolan yek doonas

#cart creation

# def total_price




@login_required
def clear_cart(request):
    if request.method == 'POST':
        Cart.objects.get(user=request.user).delete()
        messages.success(request, "Your cart has been cleared.")
    return redirect('cart:cart_detail')


class GetCartApi(generics.RetrieveAPIView):
    def get_queryset(self):
        return Cart.objects.get(user=self.request.user)
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]


#GET/CART/SUMMERY



