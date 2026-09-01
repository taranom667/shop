from django.urls import path
from .views import *
from CartItem.models import CartItem

urlpatterns = [
    path('GET/',WishlistItems.as_view()),
    path('Delete/<int:id>/',WishlistDelete.as_view()),
    path('Add/<int:id>/',add_to_wishlist.as_view()),
    path('Remove/<int:id>/',remove_from_wishlist.as_view()),



]