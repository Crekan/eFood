from django.urls import path

from .views import ProductsView, ProductRetrivUpdateDestroyView


urlpatterns = [
    path('products/', ProductsView.as_view(), name='products'),
    path('product/<int:pk>/', ProductRetrivUpdateDestroyView.as_view(), name='product_detail'),
]
