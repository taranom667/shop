from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from rest_framework import generics, request
from User.models import CustomUser
from Product.models import Product
from Wishlist.models import Wishlist
from .serializer import WishlistSerializer

class CreateWishlist(generics.CreateAPIView):
    serializer_class = WishlistSerializer


class WishlistItems(generics.ListAPIView):
    def get_queryset(self):
        wishlist = Wishlist.objects.get(user=self.request.user)
        return wishlist.products.all()
    permission_classes = [IsAuthenticated]


class WishlistDelete(generics.DestroyAPIView):
    def get_queryset(self):
        wishlist = Wishlist.objects.get(user=self.request.user)
        return wishlist.products.all()
    permission_classes = [IsAuthenticated]

@csrf_exempt
@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist = Wishlist.objects.get(user=request.user)
    wishlist.products.add(product)
    wishlist.save()

@csrf_exempt
@login_required
def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist = Wishlist.objects.get(user=request.user)
    wishlist.products.remove(product)
    wishlist.save()