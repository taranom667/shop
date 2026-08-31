from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=20, decimal_places=2,
                                validators=[MinValueValidator(Decimal('0.01'))]
                                )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField()
    stock = models.IntegerField(default=0)

    # category = models.ForeignKey(Category,max_length=128,on_delete=models.DO_NOTHING ,related_name='category',null=True,blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    @property
    def is_available(self):
        return self.stock > 0
