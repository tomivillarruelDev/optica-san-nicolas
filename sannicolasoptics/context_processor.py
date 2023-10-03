from pathologies.models import Pathology
from shopping_cart.models import Product

def products(request):
    products = Product.objects.all()
    return {'products': products}

def pathologies(request):
    pathologies = Pathology.objects.all()
    return {'pathologies': pathologies}

def cart_total(request):
    total = 0
    if 'cart' in request.session:
        for key, value in request.session['cart'].items():
            total += float(value['accumulated'])

    return {'cart_total': total}