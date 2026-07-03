from django.db import models

# Create your models here.
class Shipment(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.BooleanField(default=False)
    date = models.DateField()