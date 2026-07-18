from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from rest_framework import generics

from .models import Cart


#yekari kon be mahz sakht user enam sakhte she va kolan yek doonas

#cart creation
#cart details
# def total_price




@login_required
def clear_cart(request):
    if request.method == 'Delete':
        Cart.objects.filter(user=request.user).delete()
        messages.success(request, "Your cart has been cleared.")
    return redirect('cart:cart_detail')
