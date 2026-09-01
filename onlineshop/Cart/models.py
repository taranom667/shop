from django.db import models
from User.models import CustomUser


class Cart(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name='cart',null=True,blank=True)

    def __str__(self):
        return self.user.username + "'s cart"

