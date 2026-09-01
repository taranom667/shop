
from django.urls import path
from .views import *

urlpatterns = [
    path('', GetCartItemsAPI.as_view(), name='cart-items-list'),
    path('add/', AddToCartAPI.as_view(), name='add-to-cart'),
    path('<int:id>/', UpdateCartItemAPI.as_view(), name='update-cart-item'),
    path('<int:id>/',RemoveFromCartAPI.as_view(), name='remove-from-cart'),
]