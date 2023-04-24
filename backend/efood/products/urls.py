from django.urls import path

from .views import ProductsView, ProductRetrivUpdateDestroyView, ProductCreateView


urlpatterns = [
    path('products/', ProductsView.as_view(), name='products'),
    path('product/<int:pk>/', ProductRetrivUpdateDestroyView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
]
