from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem, Order
from catalogue.models import Product
from django.contrib.auth.decorators import login_required

@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, "cart/cart_detail.html", {"cart": cart})


@login_required
def add_to_cart(request, product_id):
    cart, created = Cart.objects.get_or_create(user=request.user)
    product = get_object_or_404(Product, id=product_id)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()

    return redirect("cart:view_cart")
@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.all()  # ধরে নিচ্ছি related_name="items" আছে

    total = sum(item.product.price * item.quantity for item in cart_items)

    return render(request, 'cart/view_cart.html', {
        'cart_items': cart_items,
        'total': total
    })

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect("cart:cart_detail")


@login_required
def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)
    order = Order.objects.create(
        user=request.user,
        cart=cart,
        total_price=cart.total_price()
    )
    return render(request, "cart/order_confirm.html", {"order": order})
