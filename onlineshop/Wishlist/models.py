from django.db import models
from User.models import CustomUser

from Product.models import Product


# Create your models here.

class Wishlist(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True,related_name='wishlist')
    products = models.ManyToManyField(Product, related_name='wishlist')
