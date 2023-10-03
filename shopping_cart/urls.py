from django.urls import path
from . import views

urlpatterns = [
    path('shop/', views.shopping_cart, name='shopping_cart'),
    path('cart/', views.cart, name='cart'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('decrement/<int:product_id>/', views.decrement_from_cart, name='decrement_from_cart'),
    path('clear/', views.clear_cart, name='clear_cart')

    
]

