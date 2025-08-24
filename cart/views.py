from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem, Order, OrderItem
from catalogue.models import Product


# Get or create cart for user
def get_user_cart(user):
    cart, created = Cart.objects.get_or_create(user=user)
    return cart


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = get_user_cart(request.user)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect("cart:cart_detail")


@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    item.delete()
    return redirect("cart:cart_detail")


@login_required
def update_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    if request.method == "POST":
        quantity = int(request.POST.get("quantity", 1))
        if quantity > 0:
            item.quantity = quantity
            item.save()
        else:
            item.delete()
    return redirect("cart:cart_detail")


@login_required
def cart_detail(request):
    cart = get_user_cart(request.user)
    return render(request, "cart/cart_detail.html", {"cart": cart})


@login_required
def checkout(request):
    cart = get_user_cart(request.user)
    if request.method == "POST":
        order = Order.objects.create(user=request.user, total=cart.total_price())
        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price,
            )
        cart.items.all().delete()  # Clear cart after order
        return render(request, "cart/order_success.html", {"order": order})

    return render(request, "cart/checkout.html", {"cart": cart})
