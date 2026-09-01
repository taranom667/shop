from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'category'
        ordering = ['-created_at']
    def __str__(self):
        return self.name

