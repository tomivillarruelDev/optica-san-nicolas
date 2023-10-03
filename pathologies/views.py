from django.shortcuts import render
from .models import Pathology
from django.shortcuts import get_object_or_404


# Create your views here.

def pathologies(request):
    return render(request, 'pathologies.html')

def pathology(request, pathology_id):
    pathology = get_object_or_404(Pathology, pk=pathology_id)
    return render(request, 'pathology.html', {
        'pathology': pathology,
    })