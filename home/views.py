from django.shortcuts import render
from .forms import ImageForm

from django.shortcuts import render
from pathologies.models import Pathology   # Asegúrate de importar el modelo Pathology
from shopping_cart.models import Product



# Create your views here.

def home(request):
    products = Product.objects.all()
    pathologies = Pathology.objects.all() 
    return render(request, 'home.html', {
        'products': products,
        'pathologies': pathologies
    })

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirigir a una página de éxito o hacer lo que necesites
    else:
        form = ImageForm()
    return render(request, 'cargar_imagen.html', {'form': form})