from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .cart import Cart

# Create your views here.
def cart(request):
    cart = Cart(request)
    cart_content = request.session.get('cart')
    return render(request, "cart.html", {"cart": cart})

def shopping_cart(request):
    cart = Cart(request)
    cart_content = request.session.get('cart')
    return render(request, "shopping_cart.html", {"cart": cart})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart = Cart(request)
    cart.add(product)
    return redirect('cart')

def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart = Cart(request)
    cart.remove(product)
    return redirect('cart')

def decrement_from_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart = Cart(request)
    cart.decrement(product)
    return redirect('cart')

def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart')

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, "product_detail.html", {'product': product})