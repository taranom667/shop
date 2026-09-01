from User.models import CustomUser
from django.db import models


class Address(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='address')
    receiver_name = models.CharField(max_length=100, null=True, blank=True)
    receiver_email = models.EmailField(max_length=100, null=True, blank=True)
    postal_code = models.CharField(max_length=12, )
    country = models.CharField(max_length=50, null=True, blank=True)
    province = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    street = models.CharField(max_length=100, null=True, blank=True)
    alley = models.CharField(max_length=100, null=True, blank=True)
    plate = models.CharField(max_length=100, null=True, blank=True)
    is_default = models.BooleanField(default=False,null=True, blank=True)

    def __str__(self):
        return self.user.username.__str__() + "   address" + self.id.__str__()
