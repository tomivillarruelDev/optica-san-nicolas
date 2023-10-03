class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = {}
        self.cart = cart

    def add(self, product):
        product_id = str(product.id)
        if product_id not in self.cart.keys():
            self.cart[product_id] = {
                "product_id": product_id,
                "name": product.name,
                "accumulated": str(product.price),
                "quantity": 1,
                "image": product.image.url 
            }
        else:
            self.cart[product_id]['quantity'] += 1
            self.cart[product_id]['accumulated'] = str(float(self.cart[product_id]['accumulated']) + float(product.price))
        self.save()

    def save(self):
        self.session['cart'] = self.cart
        self.session.modified = True
    
    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart.keys():
            del self.cart[product_id]
            self.save()
            
    def decrement(self, product):
        product_id = str(product.id)
        if product_id in self.cart.keys():
            self.cart[product_id]['quantity'] -= 1
            self.cart[product_id]['accumulated'] = str(float(self.cart[product_id]['accumulated']) - float(product.price))
            if self.cart[product_id]['quantity'] < 1:
                self.remove(product)
            else:
                self.save()

    def clear(self):
        self.session['cart'] = {}
        self.session.modified = True