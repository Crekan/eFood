from django.urls import path

from .views import ProductsView, ProductDetailView, ProductCreateView


urlpatterns = [
    path('products/', ProductsView.as_view(), name='products'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
]
