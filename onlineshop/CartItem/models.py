
from Cart.models import Cart
from django.db import models
from Product.models import Product

class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='cart_item')
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True,related_name='cart_item')
    quantity=models.IntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)
    price_at_purchase=models.DecimalField(max_digits=10,decimal_places=2,default=0)

    def __str__(self):
        return f'product_id: {self.product.id}  ,name: {self.product.name} *{self.quantity}  , customer:{self.cart.user.id}'

    @property
    def total_price(self):
        return self.quantity * self.product.price

    def increase_quantity(self,amount=1):
        if self.quantity + amount <= self.product.stock:
            self.quantity+=amount
            return True
        return  False


