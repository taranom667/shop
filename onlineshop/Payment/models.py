from django.db import models
from Order.models import Order
# Create your models here.
class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    Order= models.OneToOneField(Order,on_delete=models.CASCADE,null=True,blank=True,related_name='Payment')
