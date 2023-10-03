def cart_total(request):
    total = 0
    if 'cart' in request.session:
        for key, value in request.session['cart'].items():
            total += float(value['accumulated'])

    return {'cart_total': total}