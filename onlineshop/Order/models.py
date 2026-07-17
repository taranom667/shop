from django.db import models

from   User.models import CustomUser


# Create your models here.
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.BooleanField(default=False)
    quantity = models.IntegerField()
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True,related_name='Order')


