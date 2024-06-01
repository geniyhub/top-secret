from django.shortcuts import render
from .models import Product


def products(request):
    all_products = Product.objects.all()
    return render(request, 'shopapp/products.html', context={'products':all_products})
