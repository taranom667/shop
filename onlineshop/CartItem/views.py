from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .models import CartItem
from Product.models import Product
from django.shortcuts import render, redirect, get_object_or_404

from .serializers import CartItemSerializer


@csrf_exempt
@login_required
def increase_cartItem_quantity_api(request,product_id):
    product = get_object_or_404(Product, id=product_id)
    user=request.user
    if request.method == "POST":
         cart_item = user.cart.CarItem.Product.objects.get(id=product.id)
         if  int(cart_item.product.stock) >=1:
             cart_item.update(quantity=F('quantity') + 1)
             cart_item.save()
             messages.success(request,"Cart updated successfully.")

         else: messages.error(request, "Invalid quantity.")

    return redirect('cart:cart_detail')

@csrf_exempt
@login_required
def create_cartItem_api(request,product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user

    if product in user.cart.CarItem.Product.objects.all() :
        increase_cartItem_quantity_api(request, product.id)
    else:

        if not product.is_available:
            messages.error(request, f"{product.name} is out of stock.")
        else:    return redirect('products:product_detail', product_id=product.id)

        cart_item ,created= CartItem.objects.create(
            user=request.user,
            product=product,
            defaults={'quantity':1},
            Cart=request.user.Cart
        )

        if not created:
            if cart_item.increase_quantity():
                cart_item.save()
                messages.success(request, f"Increased {product.name} quantity to {cart_item.quantity}.")
            else:
                messages.warning(request, f"Cannot add more. Only {product.stock} in stock.")
        else:
            cart_item.Cart=request.user.Cart
            messages.success(request, f"{product.name} added to your cart.")

        return redirect('cart:cart_detail')



@csrf_exempt
@login_required
def decrease_cartItem_quantity_api(request,product_id):
    product = get_object_or_404(Product, id=product_id)
    user=request.user
    cart_item = user.cart.CarItem.Product.objects.get(id=product.id)

    if request.method == "POST":
        if cart_item.quantity>=1:
         cart_item.update(quantity=F('quantity') - 1)
         cart_item.save()
         messages.success(request,"CartItem quantity decreased successfully.")
        else:
            user.cart.CarItem.delete()
    return redirect('cart:cart_detail')

@csrf_exempt
@login_required
def cartitem_detail(request,cartitem_id):
    user = request.user
    cart_item= user.cart.CarItem.objects.get(id=cartitem_id)
    total_price = sum(item.total_price for item in cart_item)
    total_items = sum(item.quantity for item in cart_item)

    context = {
        'cart_items': cart_item,
        'total_price': total_price,
        'total_items': total_items,
    }

    return render(request, 'cart/cart_detail.html', context)

class DeleteCartItemApi(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CartItemSerializer
    def get_queryset(self,product_id):
        user=self.request.user
        return CartItem.objects.get(id=product_id,user=user)

