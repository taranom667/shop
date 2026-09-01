from django.db import models
from User.models import CustomUser
from Address.models import Address
from django.db.models import Sum


class Order(models.Model):
    status_choices = TYPE_CHOICES = (
        ('OP', 'Order_Placed'),
        ('OC', 'Order_Confirmed'),
        ('OP', 'Order_Processing'),
        ('IT', 'In_Transit'),
        ('OFD', 'Out_for_Delivery'),
        ('D', 'Delivered'),
        ('OFD', 'Out_for_Delivery'),)

    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=10, choices=status_choices, default='pending')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='Order')
    total_amount = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='Order')


def __str__(self):
    return f'id:{self.id},  Order status: {self.status}, user: {self.user.username}'


def total_amount(self):
    self.Order.CartItem.objects.all().aggregate(total_amount=Sum('price_at_purchase'))
