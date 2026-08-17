from django.apps import AppConfig
from django.shortcuts import render
from django.template.context_processors import request
from rest_framework.generics import get_object_or_404
from User.models import CustomUser
from Product.models import Product
from


# Create your views here.
# add to wishlist
# hazf as wish list
# see all the items in your wish list
# delete all items from your wish list

class AddToWishlist(request):
    object = get_object_or_404(Product, id=Product.id)
    wishlist = request.user.wishlist
    wishlist.product = object
    wishlist.save()
