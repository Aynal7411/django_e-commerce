from django.shortcuts import render, get_object_or_404
from .models import Product, RiceCategory

# All products
def product_list(request):
    products = Product.objects.all().order_by('-created_at')
    categories = RiceCategory.objects.all()
    return render(request, 'catalogue/product_list.html', {'products': products, 'categories': categories})

# Single product detail
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    categories = RiceCategory.objects.all()
    return render(request, 'catalogue/product_detail.html', {'product': product, 'categories': categories})

# Products by category
def category_products(request, category_id):
    category = get_object_or_404(RiceCategory, pk=category_id)
    products = category.products.all()
    categories = RiceCategory.objects.all()
    return render(request, 'catalogue/product_list.html', {'products': products, 'categories': categories})
