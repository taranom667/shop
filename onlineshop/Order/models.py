from django.db import models

from   User.models import CustomUser


# Create your models here.
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.BooleanField(default=False)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True,blank=True,related_name='Order')

    def __str__(self):
        return f'id:{self.id},  Order status: {self.status}, user: {self.user.username}'
