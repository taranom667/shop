from django.urls import path
from .views import *



urlpatterns = [
    #path(' ', cartitem_detail),
    path('add/<int:product_id>/',create_cartItem_api),
    #path('increase/<int:cart_item_id>/',increase_cartItem_quantity_api),
    #path('remove/<int:cart_item_id>/',decrease_cartItem_quantity_api),

]