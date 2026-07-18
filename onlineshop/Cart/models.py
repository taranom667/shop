from django.db import models
from User.models import CustomUser
from django.template.context_processors import request


# Create your models here.
class Cart(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE,null=True,blank=True,related_name='cart')

    def __str__(self):
        return self.user.username + "'s cart"

'''
caculate total

add item to cart
delete item from cart


'''
