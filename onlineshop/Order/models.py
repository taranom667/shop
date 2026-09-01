from django.db import models
from User.models import CustomUser
from Address.models import Address
from django.db.models import Sum

class Order(models.Model):
    status_choices = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('processing', 'Processing'),
        ('in_transit', 'In Transit'),
        ('out_for_delivery', 'Out for Delivery'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    )

    id = models.AutoField(primary_key=True)
    status = models.CharField( choices=status_choices, default='pending')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='Order',null=True,blank=True)
    total_amount = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='Order')


    def __str__(self):
        return f'id:{self.id},  Order status: {self.status}, user: {self.user.username}'



    def calculate_total(self):
        """Calculate total from order items"""
        return self.OrderItem.objects.filter(Order=self).aggregate(
            total=Sum(models.F('price_at_time') * models.F('quantity'), output_field=models.DecimalField())
        )['total'] or 0