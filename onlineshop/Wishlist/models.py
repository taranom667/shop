from django.db import models
from User.models import CustomUser

# Create your models here.

class Wishlist(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)