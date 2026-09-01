from django.db import models
from Product.models import Product
from CartItem.models import CartItem
from Order.models import Order


class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200,null=True, blank=True)
    price_at_time = models.DecimalField(max_digits=20, decimal_places=2,null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    Order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='OrderItem',default=None,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return f'name: {self.name} *{self.quantity} '
