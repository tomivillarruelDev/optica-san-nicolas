from django.shortcuts import render
from .forms import ImageForm
from django.shortcuts import render

# Create your views here.
def home(request):
     return render(request, 'home.html')

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ImageForm()
    return render(request, 'cargar_imagen.html', {'form': form})