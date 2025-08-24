from django.contrib import admin

# Register your models here.
admin.site.site_header = "Rice Vandar Admin"
admin.site.site_title = "Rice Vandar Admin Portal"
admin.site.index_title = "Welcome to Rice Vandar Admin"
from .models import Cart, CartItem, Order, OrderItem
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)