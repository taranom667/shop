from django.db import models
from User.models import CustomUser


class Cart(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name='cart')

    def __str__(self):
        return self.user.username + "'s cart"
'''
    def total_price(self):
        CartItems = self.CartItem.all()
        for meals in CartItems:

            total_price = 0
            for i in CartItems:
                 total_price += i.total_price
            return total_price'''