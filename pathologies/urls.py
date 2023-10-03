from django.urls import path
from . import views

urlpatterns = [
    path('', views.pathologies, name='pathologies'),
    path('pathology/<int:pathology_id>', views.pathology, name='pathology'),
    
]