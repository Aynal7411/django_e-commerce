from .models import Cart

def cart_item_count(request):
    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(user=request.user)
            count = cart.items.count()
        except Cart.DoesNotExist:
            count = 0
    else:
        count = 0  # guest user জন্য 0 দেখানো হবে
    return {'cart_count': count}
