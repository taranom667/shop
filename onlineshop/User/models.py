from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.CharField(max_length=128, null=True, blank=True)
    phone_number = models.CharField(max_length=13, null=True, blank=True)


    class Meta:
        db_table = 'user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'